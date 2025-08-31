init python:
    import os, json, random 


    def load_random_json():
        mods_path = os.path.join(config.gamedir, "girl_packs")
        json_files = []
        # Folder(s) to exclude
        excluded_folders = {"original_premiun_slaves_pack"}

        for root, dirs, files in os.walk(mods_path):
            # Remove excluded folders from dirs to avoid walking into them
            dirs[:] = [d for d in dirs if d not in excluded_folders]

            for file in files:
                if file.lower().endswith(".json"):
                    json_path = os.path.join(root, file)
                    json_files.append(json_path)

        if json_files:
            chosen_path = random.choice(json_files)
            try:
                with open(chosen_path, "r", encoding="utf-8") as f:
                    global selected_json_data
                    selected_json_data = json.load(f)
                    renpy.log(f"Loaded JSON file: {chosen_path}")
            except Exception as e:
                renpy.log(f"Error loading JSON: {chosen_path} → {e}")
        else:
            renpy.log("No JSON files found.")
    load_random_json()
    def load_json(filename):
        try:
            with renpy.loader.load(filename) as f:
                return json.load(f)
        except Exception as e:
            renpy.log(f"Failed to load {filename}: {e}")
            return None
    def add_slave(slave):
        global next_id       # Tell Python we want to use the external variable
        all_girls_list[next_id] = slave
        next_id += 1         # Increase the counter
    def reduce_check(x,a):
        if all_girls_list[girl_index]["experience"][x][a] <= attributes_min_threshold[all_girls_list[girl_index][x][a]] and all_girls_list[girl_index][x][a] > 0:
            all_girls_list[girl_index]["experience"][x][a] -= attributes_min_threshold[all_girls_list[girl_index][x][a]]
            all_girls_list[girl_index][x][a] = all_girls_list[girl_index][x][a] - 1
    def increase_check(x,a):
        if all_girls_list[girl_index]["experience"][x][a] >= attributes_max_threshold[all_girls_list[girl_index][x][a]] and all_girls_list[girl_index][x][a] < 5:
            all_girls_list[girl_index]["experience"][x][a] -= attributes_max_threshold[all_girls_list[girl_index][x][a]]
            all_girls_list[girl_index][x][a] = all_girls_list[girl_index][x][a] + 1
    def msg(x):
        renpy.show_screen("msg", msg_text=x)
    def meat_evaluation():
        base_meat_gain = all_girls_list[girl_index]["attributes"]["physical"] + 2
        if all_girls_list[girl_index]["age"] == 0:
            base_meat_gain = base_meat_gain*2
        elif all_girls_list[girl_index]["age"] == 2:
            base_meat_gain = base_meat_gain*3
        mince_gain = all_girls_list[girl_index]["attributes"]["physical"] * all_girls_list[girl_index]["boobs"]
        meat_max = 1 + all_girls_list[girl_index]["attributes"]["endurance"]
        if all_girls_list[girl_index]["age"] == 0:
            meat_max = meat_max*2
        elif all_girls_list[girl_index]["age"] == 2:
            meat_max = meat_max*3
        if base_meat_gain > meat_max:
            meat_gain = meat_max
            mince_bonus = base_meat_gain - meat_max
        else:
            meat_gain = base_meat_gain
            mince_gain += mince_bonus
        if all_girls_list[girl_index]["age"] == 1 or ( all_girls_list[girl_index]["age"] == 0 and all_girls_list[girl_index]["vaginal_tightness"] == 0):
            virgin_meat_gain = meat_gain
            meat_gain = 0
        else:
            virgin_meat_gain = 0
        meat_price = mince_gain + meat_gain*2 + virgin_meat_gain*4
        return(meat_price)
    # sex_acceptance_check() is literally interaction_willingness1 but for sex.
    def sex_acceptance_check(): 
        global interaction_sex_acceptance, girl_index, rape
        global allure_value_3, sum_of_sex_skill_slave_value
        global shameful, painful, disgusting, homosexual
        interaction_sex_acceptance = 0 
        girl = all_girls_list[girl_index]
        if girl["psy_status"] == "broken":
            return
        if girl["aura"]["devotion"] < 5 and rape:
            # rape is opposed by nature ([-20, -4]) unless fully devoted - ImperatorAugustus
            # but I will add devotion to the equation to make it more interesting
            interaction_sex_acceptance -= girl["attributes"]["nature"] + girl["attributes"]["temperament"] + girl["attributes"]["pride"] + girl["attributes"]["intelligence"]
            interaction_sex_acceptance = interaction_sex_acceptance // girl["aura"]["devotion"] + 1
            rape = False
            return
        if stimulating or orgastic:
            interaction_sex_acceptance = (allure_value_3 -5) + girl["mood"] + girl["aura"]["devotion"] + girl["arousal"]*2 - (10 - girl["attributes"]["pride"]*2)
            # initial value ranges from +20 (alluring master, ecstatic, max devotion, max arousal, no pride) to -20 (repulsive master, depressed, no devotion, no arousal, max pride)
            if girl["psy_status"] in ["frightened", "docile"]:
                interaction_sex_acceptance += girl["aura"]["fear"]
            elif girl["psy_status"] == "horny":
                interaction_sex_acceptance += girl["arousal"]
            elif girl["psy_status"] == 'servile':
                interaction_sex_acceptance += girl["attributes"]["nature"]
            elif girl["psy_status"] == 'obedient':
                interaction_sex_acceptance += girl["attributes"]["intelligence"]
            elif girl["psy_status"] == 'hysteric':
                interaction_sex_acceptance -= girl["aura"]["devotion"]
            elif girl["psy_status"] == 'hateful':
                interaction_sex_acceptance -= girl["attributes"]["temperament"]
            elif girl["psy_status"] == 'resistant':
                interaction_sex_acceptance -= girl["attributes"]["nature"]
            elif girl["psy_status"] == 'arrogant':
                interaction_sex_acceptance -= girl["attributes"]["pride"]
            elif girl["psy_status"] in ["reluctant", "depresive", "lachrymose"]:
                interaction_sex_acceptance += girl["attributes"]["empathy"]
            # check lust_driver trait
            if girl["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["lust_driver"]["value"] > 0:
                interaction_sex_acceptance += girl["arousal"] * girl["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["lust_driver"]["value"]
            if girl["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["lust_driver"]["value"] < 0:
                interaction_sex_acceptance -= girl["attributes"]["empathy"] * girl["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["lust_driver"]["value"]
            #TODO next thing to do 
            sum_of_sex_skill_slave_value += (girl["sex_experience"]["petting"]["petting"] 
                                            + girl["sex_experience"]["oral_pleasure"]["oral_pleasure"] 
                                            + girl["sex_experience"]["penetration"]["penetration"]  
                                            + girl["sex_experience"]["group_sex"]["group_sex"] 
                                            + girl["sex_experience"]["demostration"]["demostration"]
                                            + girl["sex_experience"]["fetishism"]["fetishism"]
                                            + girl["sex_experience"]["xenophily"]["xenophily"])
            interaction_sex_acceptance += sum_of_sex_skill_slave_value // 2
            if shameful:
                interaction_sex_acceptance += girl["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"] * 4
            if painful:
                interaction_sex_acceptance += girl["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["value"] * 4
            if disgusting:
                interaction_sex_acceptance += girl["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["sexual_openness"]["value"] * 4
            if homosexual:
                interaction_sex_acceptance += girl["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["sexual_orientation"]["value"] * 4
            shameful = False
            painful = False
            disgusting = False
            homosexual = False





    
    def interaction_willingness_check(): # A.K.A $dyn_repulse_check
        global attribute_track_index, dictionary_track_index, dictionary_name
        global dic_traits_skills_descriptions, target_skill, interaction_willingness
        global domini_dictum_active, interaction_sex_acceptance, interaction_repulse_difficulty
        global testvariable1
        sex_acceptance_check()
        interaction_willingness = all_girls_list[girl_index]["obedience"] + interaction_sex_acceptance + interaction_repulse_difficulty
        testvariable1 = interaction_willingness
        
        if target_skill != "sex":
            target_skill2 = target_skill + "trait"
            if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["revealed"] and not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] == 0:
                attribute_track_index = target_skill2
                dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] 
                dictionary_name = dic_traits_skills_descriptions
                all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["revealed"] = True
                renpy.show_screen("tutorial_attribute")
            interaction_willingness += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] * 3
        else:
            if interaction_willingness > 0:
                all_girls_list[girl_index]["daring"] = max(all_girls_list[girl_index]["daring"], interaction_repulse_difficulty)
        if domini_dictum_active and interaction_willingness < 0:
            interaction_willingness = 0 

        #TODO need to code sex part - sex_acceptace_check
    def diligence333_check333():
        global slave_diligence, motivation_repulse, girl_index, target_skill
        global interaction_willingness, testvariable1,testvariable2, testvariable3
        slave_diligence = all_girls_list[girl_index]["mood"] + all_girls_list[girl_index]["aura"]["devotion"] + all_girls_list[girl_index]["aura"]["fear"]*2 - all_girls_list[girl_index]["aura"]["despair"] // 2 - all_girls_list[girl_index]["aura"]["spoil"]
        # Aura -Based MOTIVATION
        slave_diligence -= (1 + motivation_repulse // 2) # ! reduce initial diligence by [0,3] - ImperatorAugustus
        if all_girls_list[girl_index]["aura"]["devotion"] > motivation_repulse:
            slave_diligence += 1
        if all_girls_list[girl_index]["aura"]["taming"] > motivation_repulse:
            slave_diligence += 1
        if all_girls_list[girl_index]["aura"]["awareness"] > motivation_repulse:
            slave_diligence += 1
        slave_diligence += all_girls_list[girl_index]["learning_bonus"][target_skill]
        #TODO I Will ignore phobias for now WIP #rec3ks    
        slave_diligence += all_girls_list[girl_index]["daily_count"]["punishments"]
        if all_girls_list[girl_index]["energy"] < 0:
            slave_diligence += all_girls_list[girl_index]["energy"]*4
        slave_diligence -= 5 - all_girls_list[girl_index]["attributes"]["pride"] - max(0,all_girls_list[girl_index]["arousal"] -3 )
        if dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] < 0:
            slave_diligence += dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]]
        else:
            slave_diligence -= dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]]
        if interaction_willingness < 0:
            slave_diligence += interaction_willingness // 2
        # BONUSES FOR TEACHING ABILITY
        if interaction_teach:
            if interaction_teach_type == "master_teaches_slave":
                slave_diligence += max(0, master_tutor - 2)
            # elif interaction_teach_type = "assistant_teaches_slave" and assistant['intellect'] > 3:
            #     slave_diligence += (assistant['intellect'] - 3) 
            #TODO SKIPPED ASSISTANT CODE
            elif interaction_teach_type == "school_class":
                slave_diligence += 2
            elif interaction_teach_type == 'coach_teaches_slave':
                slave_diligence += 5
        # NORMAL DIFFICULTY OVERRIDING, I'm going to do something eazier, because I believe the original code is just complicating things -rec3ks
        if dic_custom_start_difficulty_selection_index_index == 0:
            slave_diligence += 2
        elif dic_custom_start_difficulty_selection_index_index == 1:
            slave_diligence += 1
        elif dic_custom_start_difficulty_selection_index_index == 2:
            slave_diligence += 0
        # SPECIAL CASES
        if domini_dictum_active and interaction_willingness < 0 or all_girls_list[girl_index]["psy_status"] == "broken":
            slave_diligence = 1
        # I will just lower capping diligence, because high capping is just more grid and less fun - rec3ks
        if store.target_skill != "sex":
            target_skill2 = store.target_skill + "trait"
            slave_diligence += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] * 5
        slave_diligence = max(slave_diligence, 1) # i think 0 is too heavy for the game -rec3ks
    def girl_skills_rise_checkcheck():
        global skill_adv_mul, target_skill, slave_diligence
        target_skill2 = target_skill + "trait"
        if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["revealed"] and not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] == 0: 
            store.attribute_track_index = target_skill2
            store.dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] 
            store.dictionary_name = dic_traits_skills_descriptions
            all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["revealed"] = True
            renpy.show_screen("tutorial_attribute")
        if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] > 0:
            all_girls_list[girl_index]["mood_state"]["good_mood"]["job"]["active"] = True
        else:
            all_girls_list[girl_index]["mood_state"]["bad_mood"]["job"]["active"] = True
        #MAY HAVE SOME PROBLEMS IF MORE THAN ONE TRAIT IS REVEALED AT THE SAME TIME, but for now is good enough -rec3ks
        #tutor modifier
        if all_girls_list[girl_index]["attributes"]["intelligence"] >= 5:
            store.tutor_modifier += 2
        elif all_girls_list[girl_index]["attributes"]["intelligence"] >= 4:
            store.tutor_modifier += 1
        elif all_girls_list[girl_index]["attributes"]["intelligence"] >= 3:
            store.tutor_modifier += 0
        elif all_girls_list[girl_index]["attributes"]["intelligence"] >= 2:
            store.tutor_modifier -= 1
        else:
            store.tutor_modifier -= 2
        skill_rise = ((max(1,store.tutor_modifier)) * slave_diligence) / 4   
        if target_skill == "athletics":
            skill_rise = skill_rise / 2
            if skill_rise > 3:
                skill_rise = 3
            if all_girls_list[girl_index]["exertion"] >= all_girls_list[girl_index]["attributes"]["endurance"]:
                skill_rise *= -1 
            all_girls_list[girl_index]["exertion"] += 1
            skill_rise = skill_rise // 1 #this is to avoid floating point numbers
            all_girls_list[girl_index]["experience"]["attributes"]["endurance"] += skill_rise * skill_adv_mul
        else:
            if target_skill != "cow":
                all_girls_list[girl_index]["experience"]["skills"]["cow"] -= 3
            elif all_girls_list[girl_index]["skills"]["cow"] == 5:
                skill_rise = max(1, skill_rise - all_girls_list[girl_index]["skills"]["cow"]) #! S+ cow skill greatly impedes training other skills - ImperatorAugustus
            if skill_rise < 1: 
                skill_rise = 1
            skill_rise = skill_rise // 1 #this is to avoid floating point numbers
            all_girls_list[girl_index]["experience"]["skills"][target_skill] += skill_rise * skill_adv_mul
    def cryo_ingredients_loss_calculation():        
        keys_list = list(storage["ingredients"].keys())
        keys_list_index = 0
        
        while store.cryostore_ingredients > store.cryostore_ingredients_max:
            if storage["ingredients"][keys_list[keys_list_index]] == 0:
                keys_list_index += 1
            else:
                storage["ingredients"][keys_list[keys_list_index]] -= 1
            
            # Recalculate cryostore_ingredients
            store.cryostore_ingredients = sum(storage["ingredients"].values())
    def cryo_amount_calculation():
        global house_items
        store.cryostore_ingredients = 0
        for values in storage["ingredients"]:
            store.cryostore_ingredients += storage["ingredients"][values]
        store.cryostore_ingredients_max = 0
        store.cryostore_ingredients_max += home_estate["kitchen"]["Deplorable kitchen"]*50
        store.cryostore_ingredients_max += home_estate["kitchen"]["Basic kitchen"]*50
        store.cryostore_ingredients_max += home_estate["kitchen"]["Well-equipped kitchen"]*50
        store.cryostore_ingredients_max += home_estate["kitchen"]["Gourmet kitchen"]*50
        store.laboratory_ingredients = 0
        for values in storage["laboratory"]["ingredients"]:
            store.laboratory_ingredients += storage["laboratory"]["ingredients"][values]
        for values in storage["laboratory"]["potion"]:
            store.laboratory_ingredients += storage["laboratory"]["potion"][values]
        house_items = 0
        for values in storage["house"]["artistic_material"]:
            house_items += storage["house"]["artistic_material"][values]
        for values in storage["house"]["sex_items"]:
            house_items += storage["house"]["sex_items"][values]
    def display_pic():
        if all_girls_list[girl_index]["hairlength"] == "":
            if "white" in all_girls_list[girl_index]["fullimage"]:
                all_girls_list[girl_index]["haircolor"] = "white"
            elif "red" in all_girls_list[girl_index]["fullimage"]:
                all_girls_list[girl_index]["haircolor"] = "red"
            elif "purple" in all_girls_list[girl_index]["fullimage"]:
                all_girls_list[girl_index]["haircolor"] = "purple"
            elif "pink" in all_girls_list[girl_index]["fullimage"]:
                all_girls_list[girl_index]["haircolor"] = "pink"
            elif "green" in all_girls_list[girl_index]["fullimage"]:
                all_girls_list[girl_index]["haircolor"] = "green"
            elif "brown" in all_girls_list[girl_index]["fullimage"]:
                all_girls_list[girl_index]["haircolor"] = "brown"
            elif "blue" in all_girls_list[girl_index]["fullimage"]:
                all_girls_list[girl_index]["haircolor"] = "blue"
            elif "blond" in all_girls_list[girl_index]["fullimage"]:
                all_girls_list[girl_index]["haircolor"] = "blond"
            elif "black" in all_girls_list[girl_index]["fullimage"]:
                all_girls_list[girl_index]["haircolor"] = "black"
            if "short" in all_girls_list[girl_index]["fullimage"]:
                all_girls_list[girl_index]["hairlength"] = "short"
            else:
                all_girls_list[girl_index]["hairlength"] = "long"

        x = all_girls_list[girl_index]["haircolor"]
        y = all_girls_list[girl_index]["hairlength"]
        z = dic_girl_age_text2[all_girls_list[girl_index]["age"]]
        def choose_image():
            choosing_image_condition2 = store.choosing_image_condition + "_folder"
            if all_girls_list[girl_index][store.choosing_image_condition]:
                if all_girls_list[girl_index][choosing_image_condition2]:
                    choosing_image_condition3 = store.choosing_image_condition + "_folder_localization"
                    path = os.path.join(config.gamedir, all_girls_list[girl_index][choosing_image_condition3]) # i'm not sure if this part works untested -rec3ks
                    rest_girl = [
                        f for f in os.listdir(path)
                    ]
                    return all_girls_list[girl_index][choosing_image_condition3] + random.choice(rest_girl) 
                else:
                    path = os.path.join(config.gamedir, "images", "girls", "normal_scenes")
                    rest_girl = [
                        f for f in os.listdir(path)
                        if (dic_girl_choosing_image_condition_short[store.choosing_image_condition] + "_" + x + "_" + y + "_" + z in f
                        or dic_girl_choosing_image_condition_short[store.choosing_image_condition] + "_" + "general" + "_" + z in f
                        )
                    ]
                    return "girls/normal_scenes/" + random.choice(rest_girl)
            else:
                return "WIP "
        return choose_image()
    def all_hygiene_calculation():
        global home_hygiene_value, home_mess_value, home_condition, girl_index, save_girl_index
        global hygiene_value_9, hygiene_experience_value_9
        # Define hygiene thresholds
        hygiene_thresholds = [(80, 0), (60, 1), (40, 2), (20, 3), (10, 4), (0, 5)]

        def calculate_hygiene(value):
            """Return hygiene level based on thresholds."""
            for threshold, hygiene_level in hygiene_thresholds:
                if value >= threshold:
                    return hygiene_level
            return 5  # default if none matched

        # Update home hygiene
        home_hygiene_value = calculate_hygiene(home_mess_value)
        # Update home condition
        home_condition = dic_home_condition[home_hygiene_value]
        
        # Update each girl's hygiene
        save_girl_index = girl_index
        for girl_index in all_girls_list:
            all_girls_list[girl_index]["hygiene"] = calculate_hygiene(all_girls_list[girl_index]["hygiene_rate"])
        
        girl_index = save_girl_index
        # Update master hygiene
        hygiene_value_9 = calculate_hygiene(hygiene_experience_value_9)
    def auto_cook_meal():
        global already_prepared, already_ate, food_meat_info, home_mess_value
        global cryostore_ingredients_max
        global all_girls_list, dic_foods_list, storage, dic_hygiene_value_rate
        global girl_index, target_skill, tutor_modifier
        all_girls_list[girl_index]["slave_auto_cook"] = False
        if cryostore_ingredients_max <= 0:
            return
        
        girl = all_girls_list[girl_index]
        target_skill = "cooking"
        # Required obedience
        required_obedience = (
            -6 
            - girl["attributes"]["pride"] // 2 + 2
            + girl["attributes"]["nature"] // 3 
            + girl["attributes"]["intelligence"] // 3
        )

        if (not already_prepared
            and girl["rules"]["act_as_cook"]
            and girl["energy"] > 0
            and girl["obedience"] >= required_obedience):

            if not already_ate or food_actions["eat_best_food"]:
                girl["slave_auto_cook"] = True
                tutor_modifier = 0
                # Cooking skill level
                slave_skill = min(
                    girl["skills"]["cooking"],
                    max(1, girl["mood"] // 1),
                    5
                )

                keys_list = ["D- quality", "C- quality", "B+ quality", "A+ quality", "S+ quality"]
                n = slave_skill - 1
                food_not_found = True
                roll = random.randint(0, 1000000)

                # Try recipes from highest to lowest skill tier
                while n >= 0 and food_not_found:
                    for i, entry in enumerate(dic_foods_list[keys_list[n]]):
                        i = (i + roll) % len(dic_foods_list[keys_list[n]])
                        missing = 0

                        # Check if ingredients are available
                        for slot in range(4):
                            ingredient = dic_foods_list[keys_list[n]][i][1][slot]
                            if ingredient != "none" and storage["ingredients"][ingredient] == 0:
                                missing += 1

                        if missing == 0:
                            #dont cook if cooking doesn't improve the quality
                            if food_meat_info["quality"] < n + 1:
                                #don't cook if kitchen isn't good enough. this actually CAP the cooking quality
                                if dic_improvement_rooms["kitchen"][best_kitchen]["modifier"] >= n + 1:
                                    already_prepared = True
                                    food_not_found = False

                                    # Deduct ingredients
                                    for slot in range(4):
                                        ingredient = dic_foods_list[keys_list[n]][i][1][slot]
                                        if ingredient != "none":
                                            storage["ingredients"][ingredient] -= 1

                                    already_ate = True
                                    food_meat_info["name"] = dic_foods_list[keys_list[n]][i][0]
                                    food_meat_info["quality"] = n + 1

                                    # Update last cooked level
                                    girl["last_cooked_meat_level"] = food_meat_info["quality"]
                    n -= 1

                # Default to canned food
                if food_not_found and food_meat_info["quality"] == 0:
                    already_ate = True
                    already_prepared = True
                    food_meat_info["quality"] = 0
                    food_meat_info["name"] = "Canned food"

                # Hygiene and energy changes
                home_mess_value += dic_hygiene_value_rate["cook"]
                girl["hygiene_rate"] += dic_hygiene_value_rate["cook"]

                slave_energy_drop_calculation()
        else:
            girl["rules_broken"]["slave_auto_cook"] = True
    def master_cook_meal():
        global already_prepared, already_ate, food_meat_info, home_mess_value
        global cryostore_ingredients_max
        global dic_foods_list, storage, dic_hygiene_value_rate
        global target_skill, hygiene_experience_value_9, energy_value
        global personality_value_2, stewardship_value_13, stewardship_experience_value_13
        global skill_adv_mul, best_kitchen
        global testvariable1, testvariable2, testvariable3, best_kitchen
        if cryostore_ingredients_max <= 0:
            return
        
        target_skill = "stewardship"

        if not already_ate or food_actions["eat_best_food"]:
            master_auto["cook"] = True

            # Cooking skill level
            master_skill = min(
                stewardship_value_13,
                max(1, (mood_value_10 + 2)// 1),
                5
            )
            keys_list = ["D- quality", "C- quality", "B+ quality", "A+ quality", "S+ quality"]
            n = master_skill - 1
            n = n // 1
            food_not_found = True
            roll = random.randint(0, 1000000)

            # Try recipes from highest to lowest skill tier
            while n >= 0 and food_not_found:
                for i, entry in enumerate(dic_foods_list[keys_list[n]]):
                    i = (i + roll) % len(dic_foods_list[keys_list[n]])
                    missing = 0

                    # Check if ingredients are available
                    for slot in range(4):
                        ingredient = dic_foods_list[keys_list[n]][i][1][slot]
                        if ingredient != "none" and storage["ingredients"][ingredient] == 0:
                            missing += 1

                    if missing == 0:
                        #dont cook if cooking doesn't improve the quality
                        if food_meat_info["quality"] < n + 1:
                            #don't cook if kitchen isn't good enough. this actually CAP the cooking quality
                            if dic_improvement_rooms["kitchen"][best_kitchen]["modifier"] >= n + 1:
                                already_prepared = True
                                food_not_found = False

                                # Deduct ingredients
                                for slot in range(4):
                                    ingredient = dic_foods_list[keys_list[n]][i][1][slot]
                                    if ingredient != "none":
                                        storage["ingredients"][ingredient] -= 1
                                already_ate = True
                                food_meat_info["name"] = dic_foods_list[keys_list[n]][i][0]
                                food_meat_info["quality"] = n + 1
                                stewardship_experience_value_13 += 1* skill_adv_mul
                n -= 1

            # Default to canned food
            if food_not_found and food_meat_info["quality"] == 0:
                already_ate = True
                already_prepared = True
                food_meat_info["quality"] = 0
                food_meat_info["name"] = "Canned food"
            master_mood_state["bad_mood"]["neg_cook"]["duration"] = max(0, 3 + personality_value_2 - stewardship_value_13)
            if master_mood_state["bad_mood"]["neg_cook"]["duration"] > 0:
                master_mood_state["bad_mood"]["neg_cook"]["active"] = True
            else:
                master_mood_state["bad_mood"]["neg_cook"]["active"] = False


            # Hygiene and energy changes
            home_mess_value += dic_hygiene_value_rate["cook"]
            hygiene_experience_value_9 += dic_hygiene_value_rate["cook"]
            master_energy_drop_calculation()
    def auto_maid():
        global home_hygiene_value, home_mess_value, target_skill
        if home_hygiene_value >= 4:
            return
        girl = all_girls_list[girl_index]
        target_skill = "maid"
        # Required obedience
        required_obedience = (
            -5 
            + girl["attributes"]["endurance"] // 2 - 1
            + girl["attributes"]["intelligence"] // 2 - 1
            - girl["attributes"]["pride"] // 2 + 2
            + girl["attributes"]["nature"] // 3
            + girl["attributes"]["intelligence"] // 2 - 1
        )

        if (girl["rules"]["act_as_maid"]
            and girl["energy"] > 0
            and girl["obedience"] >= required_obedience):
            girl["slave_auto_maid"] = True
            tutor_modifier = 0

            slave_skill = min(
                girl["skills"]["maid"],
                girl["mood"] + 2 // 1
            )
            slave_skill = max(slave_skill, 0)
            girl["maid_slave_skill_performance"] = int(slave_skill)

            home_mess_value -= max(8, slave_skill*16)
            home_mess_value = max(0, home_mess_value)
            if slave_skill < 3 and home_mess_value == 0: 
                home_mess_value = 10

            slave_energy_drop_calculation()
            girl["hygiene_rate"] += dic_hygiene_value_rate["maid"] + home_hygiene_value - 5
        else:
            girl["rules_broken"]["slave_auto_maid"] = True
        
    def master_clean():
        global home_hygiene_value, home_mess_value, energy_value , stewardship_experience_value_13
        global skill_adv_mul, personality_value_2, hygiene_experience_value_9
        if energy_value < 0 or home_hygiene_value >= 2 : 
            return
        master_auto["clean"] = True
        stewardship_experience_value_13 += 1 * skill_adv_mul

        master_mood_state["bad_mood"]["neg_cleaning"]["duration"] = 1 + personality_value_2 
        master_mood_state["bad_mood"]["neg_cleaning"]["active"] = True
        master_energy_drop_calculation()
        hygiene_experience_value_9 += dic_hygiene_value_rate["maid"] + home_hygiene_value - 5
        home_mess_value -= max(8,stewardship_value_13*16)
        home_mess_value = max(0, home_mess_value)
    def update_moodlet_new_day_slave():
        # TODO need to check permanent state of some moodlet 1/2 DONE
        for key in dic_slave_mood["good_mood"]:
            if all_girls_list[girl_index]["mood_state"]["good_mood"][key]["active"]:
                if not all_girls_list[girl_index]["mood_state"]["good_mood"][key]["permanent"]:
                    all_girls_list[girl_index]["mood_state"]["good_mood"][key]["duration"] -= 1
                    if all_girls_list[girl_index]["mood_state"]["good_mood"][key]["duration"] == 0:
                        all_girls_list[girl_index]["mood_state"]["good_mood"][key]["active"] = False
                        all_girls_list[girl_index]["mood_state"]["good_mood"][key]["duration"] = all_girls_list[girl_index]["mood_state"]["good_mood"][key]["default_duration"]
                if not all_girls_list[girl_index]["mood_state"]["good_mood"][key]["accustomed"]:
                    all_girls_list[girl_index]["mood_state"]["good_mood"][key]["accustomed_value"] -= 1
                    if all_girls_list[girl_index]["mood_state"]["good_mood"][key]["accustomed_value"] == 0:
                        all_girls_list[girl_index]["mood_state"]["good_mood"][key]["accustomed"] = True
        for key in dic_slave_mood["bad_mood"]:
            if all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["active"]:
                if not all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["permanent"]:
                    all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["duration"] -= 1
                    if all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["duration"] == 0:
                        all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["active"] = False
                        all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["duration"] = all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["default_duration"]
                if not all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["accustomed"]:
                    all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["accustomed_value"] -= 1
                    if all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["accustomed_value"] == 0:
                        all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["accustomed"] = True
    def slave_dead_for_low_endurance_code():
        global girl_index, all_girls_list, sparks_37
        if all_girls_list[girl_index]["attributes"]["endurance"] == 0 and all_girls_list[girl_index]["experience"]["attributes"]["endurance"] <= -10:
            roll = random.randint(1, 2)
            if roll == 1:
                temporal_value = meat_evaluation()
                key_to_delete = list(all_girls_list.keys())[girl_index]
                del all_girls_list[key_to_delete]                       
                sparks_37 += temporal_value
                msg("Your slave is dead, and you sale the meat to the butcher for [temporal_value]")
            if roll == 2:
                all_girls_list[girl_index]["experience"]["attributes"]["endurance"] = -10
    def slave_attack_escape_calculation():
        global slave_escape_type, slave_rebellion_fight, slave_rebellion_attack, slave_suicide, girl_index
        if all_girls_list[girl_index]["sleep"] != 0 and all_girls_list[girl_index]["psy_status"] != "broken":
            if all_girls_list[girl_index]["attributes"]["endurance"] > 0:
                if all_girls_list[girl_index]["mood"] < -1 and all_girls_list[girl_index]["attributes"]["temperament"] > all_girls_list[girl_index]["obedience"]:
                    n = 7 + personality_value_2 - all_girls_list[girl_index]["aura"]["despair"]
                    for girl_index in all_girls_list:
                        # this doble for is not a error -rec3ks 
                        if all_girls_list[girl_index]["conscience"]:
                            if all_girls_list[girl_index]["assistant"]:
                                n += all_girls_list[girl_index]["attributes"]["intelligence"] + all_girls_list[girl_index]["aura"]["devotion"]
                    ### need assistant supervision code  - TODO
                    roll = random.randint(1, n)
                    if roll == 1:
                        if all_girls_list[girl_index]["aura"]["despair"] > 0:
                            if all_girls_list[girl_index]["attributes"]["gladiatrix"] > 0 and all_girls_list[girl_index]["aura"]["despair"] > max(0, (master_supermacy - all_girls_list[girl_index]["supermacy"]) - 5 + allure_value_3): 
                                slave_rebellion_fight = True
                                slave_rebellion_attack = True
                        elif dic_girl_equipment_neck_mod[all_girls_list[girl_index]["equipment"]["neck"]]["escape"]:
                            if all_girls_list[girl_index]["brand"] == 5:
                                slave_escape_type = 2
                            else: 
                                slave_escape_type = 1
                        elif all_girls_list[girl_index]["brand"] in [1,4]:
                            slave_escape_type = 3
                        elif all_girls_list[girl_index]["brand"] == 3:
                            slave_escape_type = 4
                if all_girls_list[girl_index]["aura"]["despair"] > 2 and all_girls_list[girl_index]["attributes"]["endurance"] > 3 and all_girls_list[girl_index]["skills"]["gladiatrix"] > 0 and all_girls_list[girl_index]["aura"]["devotion"] == 0 and all_girls_list[girl_index]["mood"] < 0: #TODO and (master_supermacy - allure_value_3) < 2 and exam_in_progress = 0:
                    slave_rebellion_fight = True
                    slave_rebellion_attack = True
                    slave_escape_type = 0
                if all_girls_list[girl_index]["obedience"] > 7 or all_girls_list[girl_index]["aura"]["devotion"] > 1:
                    slave_rebellion_fight = False
                    slave_escape_type = 0
                if all_girls_list[girl_index]["mood"] <= -5 and all_girls_list[girl_index]["aura"]["despair"] > max(all_girls_list[girl_index]["attributes"]["nature"], all_girls_list[girl_index]["attributes"]["temperament"]):
                    roll = random.randint(1, 100)
                    roll += all_girls_list[girl_index]["suicide_rate"]
                    if roll >= 90:
                        slave_suicide = True
                    else:
                        all_girls_list[girl_index]["suicide_rate"] += 15
                else:
                    all_girls_list[girl_index]["suicide_rate"] = min(all_girls_list[girl_index]["suicide_rate"] - 3, 0)
    def well_rest_bonus_calculation():
        if all_girls_list[girl_index]["energy"] > 0:
            if all_girls_list[girl_index]["mood"] > -2:
                all_girls_list[girl_index]["mood"] += all_girls_list[girl_index]["energy"] / 20
                all_girls_list[girl_index]["mood_state"]["good_mood"]["well_rested"]["active"] = True # Thanks to the new system using true and false and weight this is too op
                all_girls_list[girl_index]["mood_state"]["good_mood"]["well_rested"]["weight"] = 0 
                all_girls_list[girl_index]["slave_auto_sleep"] = True
    def brand_effect_activation():
        if all_girls_list[girl_index]["brand"] != 0:
            all_girls_list[girl_index]["experience"]["aura"]["habit"] += 1
        if all_girls_list[girl_index]["brand"] == 5:
            all_girls_list[girl_index]["experience"]["aura"]["habit"] += 1
        increase_check("aura","habit")
    def spoiling_calculation():
        ### spoiling - increase
        if all_girls_list[girl_index]["daily_count"]["reward"] > 2:
            all_girls_list[girl_index]["experience"]["aura"]["spoil"] += all_girls_list[girl_index]["daily_count"]["reward"]*5
        if all_girls_list[girl_index]["aura"]["devotion"] <= 2 and all_girls_list[girl_index]["aura"]["fear"] == 0 and all_girls_list[girl_index]["days_without_food"] == 0 and all_girls_list[girl_index]["days_without_sleep"] == 0 and all_girls_list[girl_index]["rules"]["rules_count"] < dic_overnight_rules_count[dic_overnight_rules_count_index]:
            all_girls_list[girl_index]["experience"]["aura"]["spoil"] += 5 - all_girls_list[girl_index]["attributes"]["pride"] + all_girls_list[girl_index]["attributes"]["nature"] + all_girls_list[girl_index]["attributes"]["temperament"]
        increase_check("aura","spoil")
        if all_girls_list[girl_index]["aura"]["spoil"] > 0:
            all_girls_list[girl_index]["experience"]["aura"]["devotion"] -= all_girls_list[girl_index]["aura"]["spoil"]
            all_girls_list[girl_index]["experience"]["aura"]["awareness"] -= all_girls_list[girl_index]["aura"]["spoil"]
            all_girls_list[girl_index]["experience"]["aura"]["taming"] -= all_girls_list[girl_index]["aura"]["spoil"]
            all_girls_list[girl_index]["experience"]["aura"]["habit"] -= all_girls_list[girl_index]["aura"]["spoil"]
        reduce_check( "aura","devotion")
        reduce_check( "aura","awareness")
        reduce_check( "aura","taming")
        reduce_check( "aura","habit")
        if all_girls_list[girl_index]["aura"]["spoil"] > max(0, all_girls_list[girl_index]["mood"], all_girls_list[girl_index]["aura"]["fear"]) and all_girls_list[girl_index]["sleep"] in [2,3]:
            all_girls_list[girl_index]["neg_spoil"] = True
        all_girls_list[girl_index]["daily_count"]["reward"] == 0
        ### spoiling - reduce
        if all_girls_list[girl_index]["aura"]["spoil"] > 0 or all_girls_list[girl_index]["experience"]["aura"]["spoil"] > 0 and dic_overnight_rules_count[dic_overnight_rules_count_index] <= all_girls_list[girl_index]["rules"]["rules_count"] or all_girls_list[girl_index]["days_without_food"] != 0 or all_girls_list[girl_index]["days_without_sleep"] != 0 or all_girls_list[girl_index]["aura"]["fear"] > all_girls_list[girl_index]["aura"]["devotion"]:
            all_girls_list[girl_index]["experience"]["aura"]["spoil"] -= 1 + all_girls_list[girl_index]["aura"]["devotion"] + all_girls_list[girl_index]["aura"]["fear"] + all_girls_list[girl_index]["aura"]["despair"]*2 + max(0, all_girls_list[girl_index]["days_without_food"])*3 + max(0, all_girls_list[girl_index]["days_without_sleep"])*3
        if all_girls_list[girl_index]["mood"] < 0:
            all_girls_list[girl_index]["experience"]["aura"]["spoil"] -= all_girls_list[girl_index]["attributes"]["empathy"]
        reduce_check( "aura","spoil")
    def energy_and_sleep_calculation():
        global girl_index
        if all_girls_list[girl_index]["sleep"] != 4:
            # energy is capped to 10 if devotion is less than 3
            if all_girls_list[girl_index]["aura"]["devotion"] >= 3:
                all_girls_list[girl_index]["energy"] = all_girls_list[girl_index]["attributes"]["endurance"] * 2 + 4 - all_girls_list[girl_index]["yesterday_exhaustion"] + all_girls_list[girl_index]["stored_yesterday_energy"] + dic_improvement_rooms["slaves_rooms"][all_girls_list[girl_index]["sleep_room"]]["modifier"]
            else:
                all_girls_list[girl_index]["energy"] = min(10, all_girls_list[girl_index]["attributes"]["endurance"] * 2 + 2 - all_girls_list[girl_index]["yesterday_exhaustion"] + all_girls_list[girl_index]["stored_yesterday_energy"]) + dic_improvement_rooms["slaves_rooms"][all_girls_list[girl_index]["sleep_room"]]["modifier"]
            all_girls_list[girl_index]["stored_yesterday_energy"] = 0
            all_girls_list[girl_index]["days_without_sleep"] = 0
        else:
            all_girls_list[girl_index]["energy"] = min(10, (all_girls_list[girl_index]["attributes"]["endurance"] * 2 + 2) // 2 ) - all_girls_list[girl_index]["yesterday_exhaustion"] + dic_improvement_rooms["slaves_rooms"][all_girls_list[girl_index]["sleep_room"]]["modifier"]
            all_girls_list[girl_index]["days_without_sleep"] += 1
            all_girls_list[girl_index]["experience"]["attributes"]["endurance"] -= all_girls_list[girl_index]["days_without_sleep"] *3
            all_girls_list[girl_index]["experience"]["aura"]["taming"] += all_girls_list[girl_index]["days_without_sleep"]
            reduce_check("attributes","endurance")
            increase_check("aura","taming")
            all_girls_list[girl_index]["stored_yesterday_energy"] = 0
    def slave_energy_drop_calculation():
        global girl_index
        girl = all_girls_list[girl_index]
        if girl["energy"] > 0:
            girl["energy"] -= 2
        else:
            girl["yesterday_exhaustion"] += 2
        girl["calories"] -= 1
    def master_energy_drop_calculation():
        global energy_value, yesterday_exhaustion, strength_experience_value_1, strength_value_1
        global skill_adv_mul
        if energy_value > 0:
            energy_value -= 2
        else:
            yesterday_exhaustion += 2
        if strength_value_1 < 3:
            strength_experience_value_1 += 1 * skill_adv_mul
    def best_kitchen_calculation():
        global best_kitchen
        best_kitchen = "Deplorable kitchen"
        for kitchen in home_estate["kitchen"]:
            if home_estate["kitchen"][kitchen] > 0 and dic_improvement_rooms["kitchen"][kitchen]["modifier"] > dic_improvement_rooms["kitchen"][best_kitchen]["modifier"]:
                best_kitchen = kitchen
    def auto_bath_slave_help_master():
        global hygiene_value_9, shameful, interaction_repulse_difficulty
        global interaction_willingness, libido_value_4, hygiene_experience_value_9
        global girl_index, mood_value_10, home_mess_value, already_bath
        global did_bath_yesterday
        if not home_estate["bathroom"] or hygiene_value_9 > 4 or already_bath:
            return
        girl = all_girls_list[girl_index]
        if girl["rules"]["bath_slave"] and girl["energy"] > -1:
            if girl["aura"]["devotion"] == 0:
                shameful = True
            interaction_repulse_difficulty = 0
            interaction_willingness_check()
            if interaction_willingness < 0:
                girl["rules_broken"]["bath_slave"] = True
            else:
                girl["slave_auto_bath"] = True
                girl["arousal_rate"] -= libido_value_4
                did_bath_yesterday = True
                master_mood_state["good_mood"]["pos_self_clean"]["active"] = True
                mood_value_10 += (min(girl["sex_experience"]["petting"]["petting"], girl["sex_experience"]["oral_pleasure"]["oral_pleasure"])) / 10 
                slave_bath_alone()
                home_mess_value += 3
                already_bath = True
                girl["already_bath"] = True

    #TODO newloc_update_slave
    def slave_bath_alone():
        global girl_index, home_mess_value
        girl = all_girls_list[girl_index]
        girl["mood"] += (5 - girl["hygiene"]) / 5 # up to 1 mood, 2 is too op
        girl["did_bath_yesterday"] = True
        girl["mood_state"]["good_mood"]["slave_clean"]["active"] = True
        girl["mood_state"]["good_mood"]["slave_clean"]["weight"] = 0 #too op
        girl["make_up"] = 0
        girl["perfume"] = 0
        home_mess_value += 1
        girl["energy"] -= 1
    def slave_bath_selfwash():
        global girl_index, home_mess_value
        girl = all_girls_list[girl_index]
        if not home_estate["bathroom"] or girl["energy"] < 0 or girl["hygiene"] > 2 or girl["already_bath"]:
            return
        home_mess_value += 3
        slave_bath_alone()





        





      




    def sex_experience_average_update():
        global girl_index
        all_girls_list[girl_index]["sex_experience"]["petting"]["petting"] = (all_girls_list[girl_index]["sex_experience"]["petting"]["handjob"] + all_girls_list[girl_index]["sex_experience"]["petting"]["footjob"] + all_girls_list[girl_index]["sex_experience"]["petting"]["rubbing"] + all_girls_list[girl_index]["sex_experience"]["petting"]["titjob"]) // 4
        all_girls_list[girl_index]["sex_experience"]["oral_pleasure"]["oral_pleasure"] = (all_girls_list[girl_index]["sex_experience"]["oral_pleasure"]["kissing"] + all_girls_list[girl_index]["sex_experience"]["oral_pleasure"]["licking"] + all_girls_list[girl_index]["sex_experience"]["oral_pleasure"]["blowjob"] + all_girls_list[girl_index]["sex_experience"]["oral_pleasure"]["deep_throat"] + all_girls_list[girl_index]["sex_experience"]["oral_pleasure"]["rimming"]) // 5
        all_girls_list[girl_index]["sex_experience"]["penetration"]["penetration"] = (all_girls_list[girl_index]["sex_experience"]["penetration"]["vaginal_sex"] + all_girls_list[girl_index]["sex_experience"]["penetration"]["fisting"] + all_girls_list[girl_index]["sex_experience"]["penetration"]["anal_sex"] + all_girls_list[girl_index]["sex_experience"]["penetration"]["anal_fisting"]) // 4
        all_girls_list[girl_index]["sex_experience"]["group_sex"]["group_sex"] = (all_girls_list[girl_index]["sex_experience"]["group_sex"]["threesome"] + all_girls_list[girl_index]["sex_experience"]["group_sex"]["bukkake"] + all_girls_list[girl_index]["sex_experience"]["group_sex"]["doble_penetration"] + all_girls_list[girl_index]["sex_experience"]["group_sex"]["triple_penetration"] + all_girls_list[girl_index]["sex_experience"]["group_sex"]["gangbang"]) // 5
        all_girls_list[girl_index]["sex_experience"]["demostration"]["demostration"] = (all_girls_list[girl_index]["sex_experience"]["demostration"]["seduction"] + all_girls_list[girl_index]["sex_experience"]["demostration"]["masturbation"] + all_girls_list[girl_index]["sex_experience"]["demostration"]["dildo"] + all_girls_list[girl_index]["sex_experience"]["demostration"]["humiliation"] + all_girls_list[girl_index]["sex_experience"]["demostration"]["exhibitionism"]) // 5
        all_girls_list[girl_index]["sex_experience"]["fetishism"]["fetishism"] = (all_girls_list[girl_index]["sex_experience"]["fetishism"]["enema"] + all_girls_list[girl_index]["sex_experience"]["fetishism"]["masochism"] + all_girls_list[girl_index]["sex_experience"]["fetishism"]["self-torture"] + all_girls_list[girl_index]["sex_experience"]["fetishism"]["golden_shower"] + all_girls_list[girl_index]["sex_experience"]["fetishism"]["scat"]) // 5
        all_girls_list[girl_index]["sex_experience"]["xenophily"]["xenophily"] = (all_girls_list[girl_index]["sex_experience"]["xenophily"]["dog_mating"] + all_girls_list[girl_index]["sex_experience"]["xenophily"]["pig_mating"] + all_girls_list[girl_index]["sex_experience"]["xenophily"]["house_mating"] + all_girls_list[girl_index]["sex_experience"]["xenophily"]["spider_mating"] + all_girls_list[girl_index]["sex_experience"]["xenophily"]["sea_tentacle_mating"] + all_girls_list[girl_index]["sex_experience"]["xenophily"]["field_mating"]) // 6


