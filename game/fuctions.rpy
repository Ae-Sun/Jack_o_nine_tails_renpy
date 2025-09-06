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
    def load_json(filename):
        try:
            with renpy.loader.load(filename) as f:
                return json.load(f)
        except Exception as e:
            renpy.log(f"Failed to load {filename}: {e}")
            return None
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
    def sex_acceptance_check():  # sex_acceptance_check() is literally interaction_willingness1 but for sex.
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
        sex_acceptance_check()
        interaction_willingness = all_girls_list[girl_index]["obedience"] + interaction_sex_acceptance + interaction_repulse_difficulty
        interaction_repulse_difficulty = 0
        if target_skill != "":
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
        global attribute_track_index, dictionary_track_index, dictionary_name
        target_skill2 = target_skill + "trait"
        if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["revealed"] and not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] == 0: 
            attribute_track_index = target_skill2
            dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] 
            dictionary_name = dic_traits_skills_descriptions
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
            target_skill = ""
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
        global girl_index, choosing_image_condition
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
            choosing_image_condition2 = choosing_image_condition + "_folder"
            if all_girls_list[girl_index][choosing_image_condition2]:
                choosing_image_condition3 = choosing_image_condition + "_folder_localization"
                path = os.path.join(config.gamedir, all_girls_list[girl_index][choosing_image_condition3]) # i'm not sure if this part works untested -rec3ks
                rest_girl = [
                    f for f in os.listdir(path)
                ]
                return all_girls_list[girl_index][choosing_image_condition3] + random.choice(rest_girl) 
            else:
                path = os.path.join(config.gamedir, "images", "girls", "normal_scenes")
                rest_girl = [
                    f for f in os.listdir(path)
                    if (f.startswith(dic_girl_choosing_image_condition_short[choosing_image_condition] + "_" + x + "_" + y + "_" + z)
                    or f.startswith(dic_girl_choosing_image_condition_short[choosing_image_condition] + "_" + "general" + "_" + z)
                    )
                ]
                return "girls/normal_scenes/" + random.choice(rest_girl)
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
                girl["already_done"]["Servant"] += 1
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
            girl["hygiene_rate"] += dic_hygiene_value_rate["maid"] - home_hygiene_value + 5
            girl["already_done"]["Servant"] += 1
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
        hygiene_experience_value_9 += dic_hygiene_value_rate["maid"] - home_hygiene_value + 5
        home_mess_value -= max(8,stewardship_value_13*16)
        home_mess_value = max(0, home_mess_value)
    def update_moodlet_new_day_slave():
        global girl_index
        girl = all_girls_list[girl_index]
        # TODO need to check permanent state of some moodlet 1/2 DONE
        for key in dic_slave_mood["good_mood"]:
            if girl["mood_state"]["good_mood"][key]["active"]:
                if not girl["mood_state"]["good_mood"][key]["permanent"]:
                    girl["mood_state"]["good_mood"][key]["duration"] -= 1
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
        all_girls_list[girl_index]["affection_needs"] = (max(0,all_girls_list[girl_index]["affection_needs"] 
        - (
            all_girls_list[girl_index]["attributes"]["empathy"] 
            + all_girls_list[girl_index]["attributes"]["temperament"] 
            + all_girls_list[girl_index]["attributes"]["nature"] 
            + all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["lust_driver"]["value"]*3)
        * all_girls_list[girl_index]["arousal"]))
        if girl["portion_size"] == 0 or girl["days_without_food"] > 0:
            girl["mood_state"]["bad_mood"]["hungry"]["active"] = True
            girl["mood_state"]["bad_mood"]["hungry"]["weight"] = min(0.2*girl["days_without_food"],1)
        else:
            girl["mood_state"]["bad_mood"]["hungry"]["active"] = False
        if girl["days_without_food"] > 0:
            girl["mood_state"]["bad_mood"]["starvation"]["active"] = True
        else:
            girl["mood_state"]["bad_mood"]["starvation"]["active"] = False  
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
        global did_bath_yesterday, target_skill
        target_skill = ""
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
                girl["arousal_rate"] -= libido_value_4
                did_bath_yesterday = True
                master_mood_state["good_mood"]["pos_self_clean"]["active"] = True
                mood_value_10 += (min(girl["sex_experience"]["petting"]["petting"], girl["sex_experience"]["oral_pleasure"]["oral_pleasure"])) / 10 
                slave_bath_alone()
                home_mess_value += 3
                girl["slave_auto_bath"] = True
                already_bath = True
                hygiene_value_9 = 5 #this is necessary since hygiene update check is made only on home screen 
                hygiene_experience_value_9 = 0 
    def update_beauty_style_exoticism_slave():
        global girl_index
        girl = all_girls_list[girl_index]
        def update_slave_beauty():
            global attribute_track_index, dictionary_track_index, dictionary_name, customboxcheck
            girl["attributes"]["beauty"] = girl["attributes"]["natural_beauty"] - (girl["injuries"] + girl["scars"])/2
            if girl["attributes"]["physical"] == 5:
                girl["attributes"]["beauty"] -= 1
            else:
                girl["attributes"]["beauty"] -= max(1 - girl["attributes"]["physical"]*0.5, 0)
            if girl["neoplasty"]:
                girl["attributes"]["beauty"] += 1
            if girl["attributes"]["beauty"] > 5:
                girl["attributes"]["beauty"] = 5
            if (girl["attributes"]["beauty"] == 5 
            and girl["aura"]["devotion"] >= 5 #maybe change this for S+
            and girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["beautytrait"]["value"] == 2
            or girl["attributes"]["beauty"] == 5
            and girl["aura"]["devotion"] >= 5 #maybe change this for S+
            and girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["beautytrait"]["value"] == 1
            and girl["neoplasty"]):
                girl["attributes"]["beauty"] += 1
            girl["attributes"]["beauty"] = int(girl["attributes"]["beauty"])
            if girl["injuries"] + girl["scars"] == 0 and girl["attributes"]["physical"] == 4:
                if girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["beautytrait"]["value"] != 0:
                    if not girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["beautytrait"]["revealed"]:
                        girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["beautytrait"]["revealed"] = True
                        attribute_track_index = "beautytrait"
                        dictionary_track_index = girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["beautytrait"]["value"] 
                        dictionary_name = dic_traits_attributes_description
                        customboxcheck = True
        def update_slave_style():
            global natural_grace_color
            global attribute_track_index, dictionary_track_index, dictionary_name, customboxcheck

            girl["attributes"]["style"] = (girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["styletrait"]["value"] 
            + (girl["hygiene"] - 4)/2
            + girl["hairstyle"] / 2)
            for value in ["perfume","manicure","epilation","make_up"]:
                if girl[value] > 0:
                    girl["attributes"]["style"] += 0.5        
            n = [1,3,5,7,9,11,13]     
            for i in n:
                if girl["style_plus"] >= i:
                    girl["attributes"]["style"] += 0.5
            # IN TOTAL 7 POINTS for normal slaves
            girl["attributes"]["style"] = int(girl["attributes"]["style"])
            girl["attributes"]["style"] = max(girl["attributes"]["style"], 0)
            if girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["styletrait"]["value"] == 2:
                girl["attributes"]["style"] = min(girl["attributes"]["style"], 6)
            else:
                girl["attributes"]["style"] = min(girl["attributes"]["style"], 5)
            m = [(2,"#009900"),(1,"#0000D8"),(0,"#000000"),(-1,"#812000"),(-2,"#320000")]
            for values, color in m:
                if girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["styletrait"]["value"] == values:
                    natural_grace_color = color
                    break 
            if girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["styletrait"]["value"] != 0:
                if not girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["styletrait"]["revealed"]:
                    girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["styletrait"]["revealed"] = True
                    attribute_track_index = "styletrait"
                    dictionary_track_index = girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["styletrait"]["value"] 
                    dictionary_name = dic_traits_attributes_description
                    customboxcheck = True
        def update_slave_exoticism():
            global natural_exoticism_color
            girl["attributes"]["exoticism"] = girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["exoticismtrait"]["value"]
            a = [1,3,5,7,9]
            for i in a:
                if girl["piercings"] >= i:
                    girl["attributes"]["exoticism"] += 0.3
                if girl["exotic_plus"] >= 1:
                    girl["attributes"]["exoticism"] += 0.3
            e = [11,13]
            for i in e:
                if girl["exotic_plus"] >= i:
                    girl["attributes"]["exoticism"] += 0.5
            b = [(1,0.2),(2,0.4),(3,0.6),(4,0.8),(5,1)]
            for values, value in b:
                if girl["tattoo"] >= values:
                    girl["attributes"]["exoticism"] += value
            # IN TOTAL 7 POINTS for normal slaves
            girl["attributes"]["exoticism"] = int(girl["attributes"]["exoticism"])
            girl["attributes"]["exoticism"] = max(girl["attributes"]["exoticism"], 0)
            if girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["exoticismtrait"]["value"] == 2:
                girl["attributes"]["exoticism"] = min(girl["attributes"]["exoticism"], 6)
            else:
                girl["attributes"]["exoticism"] = min(girl["attributes"]["exoticism"], 5)
            m = [(2,"#009900"),(1,"#0000D8"),(0,"#000000"),(-1,"#812000"),(-2,"#320000")]
            for values, color in m:
                if girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["exoticismtrait"]["value"] == values:
                    natural_exoticism_color = color
                    break 
            if girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["exoticismtrait"]["value"] != 0:
                if not girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["exoticismtrait"]["revealed"]:
                    girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["exoticismtrait"]["revealed"] = True
                    attribute_track_index = "exoticismtrait"
                    dictionary_track_index = girl["traits"]["traits_hidden"]["traits_attributes(1/20)"]["exoticismtrait"]["value"] 
                    dictionary_name = dic_traits_attributes_description
                    customboxcheck = True
        if girl["age"] == 1:
            girl["epilation"] = 100
        update_slave_beauty()
        update_slave_style()
        update_slave_exoticism()
    def slave_rank_update():
        global rating_help_text, rating_text_display
        girl = all_girls_list[girl_index]
        girl["skills_sum"] = 0
        girl["skills_max"] = 0
        girl["sex_skills_sum"] = 0
        girl["sex_skill_max"] = 0
        girl["attributes_sum"] = (
            girl["attributes"]["endurance"]
            + girl["attributes"]["empathy"]
            + girl["attributes"]["temperament"]
            + girl["attributes"]["intelligence"]
            + girl["attributes"]["nature"]
            - (5 - girl["attributes"]["pride"]))
        for skills in girl["skills"]:
            girl["skills_sum"] += girl["skills"][skills]
            if girl["skills"][skills] >= 5:
                girl["skills_max"] += 1
        for sex_skills in girl["sex_experience"]:
            for values in girl["sex_experience"][sex_skills]:
                if values == sex_skills:
                    girl["sex_skills_sum"] += girl["sex_experience"][sex_skills][values]
                    if girl["sex_experience"][sex_skills][values] >= 5:
                        girl["sex_skill_max"] += 1
        a = max(girl["attributes"]["beauty"], girl["attributes"]["fame"])
        b =[(6,5,0),(8,10,0),(10,15,2),(12,18,4),(13,20,8),(14,24,10),(15,28,15),(16,30,18),(18,35,20),(20,40,25),(26,76,36),(999,999,999)]
        for i in range (12):
            if (a < i/2 
            or girl["attributes_sum"] < b[i][0]
            or girl["skills_sum"] < b[i][1]
            or girl["sex_skills_sum"] < b[i][2]):
                girl["rating"] = i
                break
            if i >= 3:
                if girl["aura"]["devotion"] < 1:
                    girl["rating"] = i
                    break
            if i >= 4:
                if (girl["skills_max"] < 2
                or girl["sex_skill_max"] < 1
                or girl["aura"]["devotion"] < 2):
                    girl["rating"] = i
                    break
            if i >= 5:
                if girl["aura"]["devotion"] < 3:
                    girl["rating"] = i
                    break
            if i >= 6:
                if (girl["skills_max"] < 3
                or girl["sex_skill_max"] < 2
                or girl["aura"]["devotion"] < 4):
                    girl["rating"] = i
                    break
            if i >= 8:
                if (girl["skills_max"] < 4
                or girl["sex_skill_max"] < 3
                or girl["aura"]["devotion"] < 5):
                    girl["rating"] = i
                    break
            if i >= 9:
                if (girl["skills_max"] < 5
                or girl["sex_skill_max"] < 4):
                    girl["rating"] = i
                    break
        a = max(girl["attributes"]["beauty"], girl["attributes"]["fame"])
        rating = girl["rating"]
        rating_help_text = ""
        if rating == 0:
            if a < 0.0:
                rating_help_text += f"- {girl['name']} is either not beautiful enough or famous enough to rank higher\n"
            if girl["obedience"] < 1:
                rating_help_text += f"- {girl['name']} needs to learn obedience\n"
            if girl["skills_sum"] < 5:
                rating_help_text += "- Teach this slave some common skills\n"
            if girl["attributes_sum"] < 6:
                rating_help_text += "- Develop this slave’s basic attributes\n"
            if girl["attributes"]["stamina"] < 2:
                rating_help_text += f"- {girl['name']} has low stamina and cannot rank higher or be sold to many customers\n"

        elif rating == 1:
            if a < 0.5:
                rating_help_text += f"- {girl['name']} is either not beautiful enough or famous enough to rank higher\n"
            if girl["obedience"] < 5:
                rating_help_text += f"- {girl['name']} needs to be more obedient\n"
            if girl["skills_sum"] < 10:
                rating_help_text += "- Teach this slave some common skills\n"
            if girl["attributes_sum"] < 8:
                rating_help_text += "- Further develop this slave’s basic attributes\n"

        elif rating == 2:
            if a < 1.0:
                rating_help_text += f"- {girl['name']} is either not beautiful enough or famous enough to rank higher\n"
            if girl["obedience"] < 6:
                rating_help_text += f"- {girl['name']} needs to be more obedient\n"
            if girl["sex_skills_sum"] < 2:
                rating_help_text += "- Improve this slave’s sexual skills\n"
            if girl["skills_sum"] < 15:
                rating_help_text += "- Improve this slave’s common skills\n"
            if girl["attributes_sum"] < 10:
                rating_help_text += "- Further develop this slave’s basic attributes\n"

        elif rating == 3:
            if girl["attributes"]["endurance"] < 3:
                rating_help_text += f"- {girl['name']} has low stamina and cannot rank higher or be sold to many customers\n"
            if girl["sex_skills_sum"] < 4:
                rating_help_text += "- Further improve this slave’s sexual skills\n"
            if girl["skills_sum"] < 18:
                rating_help_text += "- Further improve this slave’s common skills\n"
            if girl["attributes_sum"] < 12:
                rating_help_text += "- Further develop this slave’s basic attributes\n"
            if girl["aura"]["devotion"] < 1:
                rating_help_text += "- Encourage a strong sense of loyalty in this slave\n"

        elif rating == 4:
            if a < 2.0:
                rating_help_text += f"- {girl['name']} is either not beautiful enough or famous enough to rank higher\n"
            if girl["sex_skills_sum"] < 8:
                rating_help_text += "- Further improve this slave’s sexual skills\n"
            if girl["skills_sum"] < 20:
                rating_help_text += "- Further improve this slave’s common skills\n"
            if girl["attributes_sum"] < 13:
                rating_help_text += "- Further develop this slave’s basic attributes\n"
            if girl["aura"]["devotion"] < 2:
                rating_help_text += "- Encourage a stronger sense of loyalty in this slave\n"
            if girl["skills_max"] < 2:
                rating_help_text += f"- {girl['name']} should master a total of 2 common skills\n"
            if girl["sex_skill_max"] < 1:
                rating_help_text += f"- {girl['name']} should master 1 sexual skill\n"

        elif rating == 5:
            if girl["sex_skills_sum"] < 10:
                rating_help_text += "- Further improve this slave’s sexual skills\n"
            if girl["skills_sum"] < 22:
                rating_help_text += "- Further improve this slave’s common skills\n"
            if girl["attributes_sum"] < 14:
                rating_help_text += "- Further develop this slave’s basic attributes\n"
            if girl["aura"]["devotion"] < 3:
                rating_help_text += "- Encourage a stronger sense of loyalty in this slave\n"

        elif rating == 6:
            if a < 3.0:
                rating_help_text += f"- {girl['name']} is either not beautiful enough or famous enough to rank higher\n"
            if girl["sex_skills_sum"] < 15:
                rating_help_text += "- Further improve this slave’s sexual skills\n"
            if girl["skills_sum"] < 24:
                rating_help_text += "- Further improve this slave’s common skills\n"
            if girl["attributes_sum"] < 15:
                rating_help_text += "- Further develop this slave’s basic attributes\n"
            if girl["aura"]["devotion"] < 4:
                rating_help_text += "- Encourage a stronger sense of loyalty in this slave\n"
            if girl["skills_max"] < 3:
                rating_help_text += f"- {girl['name']} should master a total of 3 common skills\n"
            if girl["sex_skill_max"] < 2:
                rating_help_text += f"- {girl['name']} should master a total of 2 sexual skills\n"

        elif rating == 7:
            if girl["attributes_sum"] < 16:
                rating_help_text += "- Further develop this slave’s basic attributes\n"
            if girl["sex_skills_sum"] < 18:
                rating_help_text += "- Further improve this slave’s sexual skills\n"
            if girl["skills_sum"] < 26:
                rating_help_text += "- Further improve this slave’s common skills\n"

        elif rating == 8:
            if a < 4.0:
                rating_help_text += f"- {girl['name']} is either not beautiful enough or famous enough to rank higher\n"
            if girl["sex_skills_sum"] < 20:
                rating_help_text += "- Further improve this slave’s sexual skills\n"
            if girl["skills_sum"] < 28:
                rating_help_text += "- Further improve this slave’s common skills\n"
            if girl["attributes_sum"] < 18:
                rating_help_text += "- Further develop this slave’s basic attributes\n"
            if girl["aura"]["devotion"] < 5:
                rating_help_text += "- Develop absolute loyalty in this slave\n"
            if girl["skills_max"] < 4:
                rating_help_text += f"- {girl['name']} should master a total of 4 common skills\n"
            if girl["sex_skill_max"] < 3:
                rating_help_text += f"- {girl['name']} should master a total of 3 sexual skills\n"

        elif rating == 9:
            if girl["sex_skills_sum"] < 25:
                rating_help_text += "- Perfect this slave’s sexual skills\n"
            if girl["skills_sum"] < 30:
                rating_help_text += "- Perfect this slave’s common skills\n"
            if girl["attributes_sum"] < 20:
                rating_help_text += "- Fully develop this slave’s basic attributes\n"
            if girl["skills_max"] < 5:
                rating_help_text += f"- {girl['name']} should master a total of 5 common skills\n"
            if girl["sex_skill_max"] < 4:
                rating_help_text += f"- {girl['name']} should master a total of 4 sexual skills\n"
        rating_text_display = dic_rating_colored[all_girls_list[girl_index]["rating"]]
    def slave_specialization_check():
        global girl_index, client_slave_requierement_tier
        girl = all_girls_list[girl_index]
        for key in girl["specialization"]:
            n = len(dic_specializations[key])
            missing = 0
            for i in range(n):
                if girl["skills"][dic_specializations[key][i]] < max(client_slave_requierement_tier,3):
                    missing += 1
            if missing == 0:
                girl["specialization"][key] = True
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
        girl["already_bath"] = True
        girl["hygiene"] = 5
        girl["hygiene_rate"] = 0
    def slave_bath_selfwash_auto():
        global girl_index, home_mess_value
        girl = all_girls_list[girl_index]
        if not home_estate["bathroom"] or girl["energy"] < 0 or girl["hygiene"] > 2 or girl["already_bath"]:
            return
        home_mess_value += 3
        slave_bath_alone()
        girl["slave_auto_bath_self"] = True
    def slave_bath_selfwash_ask():
        global girl_index, home_mess_value
        girl = all_girls_list[girl_index]
        home_mess_value += 3
        slave_bath_alone()
    def setup_interaction_screen():
        # Hide the screens
        renpy.hide_screen("homehome_attributes_menu")
        renpy.hide_screen("goguild")
        renpy.hide_screen("sparks_menu")
        # Show the screens
        renpy.show_screen("interaction_screen")
        renpy.show_screen("information_for_consideration_screen")
    def master_bath():
        global hygiene_experience_value_9, home_mess_value
        global hygiene_value_9, energy_value, pic_displayed
        global already_bath
        roll = random.randint(1, 3)
        if roll == 1:
            pic_displayed = "scene/master_bathing.webp"
        elif roll == 2:
            pic_displayed = "scene/master_bathing_2.webp"
        elif roll == 3:
            pic_displayed = "scene/master_bathing_3.webp"
        hygiene_value_9 = 5
        hygiene_experience_value_9 = 0
        home_mess_value += 4 # because slave bath is also 4 (3 + 1)
        energy_value -= 1
        master_mood_state["good_mood"]["pos_self_clean"]["active"] = True
        already_bath = True
    def sex_experience_average_update():
        global girl_index
        all_girls_list[girl_index]["sex_experience"]["petting"]["petting"] = (all_girls_list[girl_index]["sex_experience"]["petting"]["handjob"] + all_girls_list[girl_index]["sex_experience"]["petting"]["footjob"] + all_girls_list[girl_index]["sex_experience"]["petting"]["rubbing"] + all_girls_list[girl_index]["sex_experience"]["petting"]["titjob"]) // 4
        all_girls_list[girl_index]["sex_experience"]["oral_pleasure"]["oral_pleasure"] = (all_girls_list[girl_index]["sex_experience"]["oral_pleasure"]["kissing"] + all_girls_list[girl_index]["sex_experience"]["oral_pleasure"]["licking"] + all_girls_list[girl_index]["sex_experience"]["oral_pleasure"]["blowjob"] + all_girls_list[girl_index]["sex_experience"]["oral_pleasure"]["deep_throat"] + all_girls_list[girl_index]["sex_experience"]["oral_pleasure"]["rimming"]) // 5
        all_girls_list[girl_index]["sex_experience"]["penetration"]["penetration"] = (all_girls_list[girl_index]["sex_experience"]["penetration"]["vaginal_sex"] + all_girls_list[girl_index]["sex_experience"]["penetration"]["fisting"] + all_girls_list[girl_index]["sex_experience"]["penetration"]["anal_sex"] + all_girls_list[girl_index]["sex_experience"]["penetration"]["anal_fisting"]) // 4
        all_girls_list[girl_index]["sex_experience"]["group_sex"]["group_sex"] = (all_girls_list[girl_index]["sex_experience"]["group_sex"]["threesome"] + all_girls_list[girl_index]["sex_experience"]["group_sex"]["bukkake"] + all_girls_list[girl_index]["sex_experience"]["group_sex"]["doble_penetration"] + all_girls_list[girl_index]["sex_experience"]["group_sex"]["triple_penetration"] + all_girls_list[girl_index]["sex_experience"]["group_sex"]["gangbang"]) // 5
        all_girls_list[girl_index]["sex_experience"]["demostration"]["demostration"] = (all_girls_list[girl_index]["sex_experience"]["demostration"]["seduction"] + all_girls_list[girl_index]["sex_experience"]["demostration"]["masturbation"] + all_girls_list[girl_index]["sex_experience"]["demostration"]["dildo"] + all_girls_list[girl_index]["sex_experience"]["demostration"]["humiliation"] + all_girls_list[girl_index]["sex_experience"]["demostration"]["exhibitionism"]) // 5
        all_girls_list[girl_index]["sex_experience"]["fetishism"]["fetishism"] = (all_girls_list[girl_index]["sex_experience"]["fetishism"]["enema"] + all_girls_list[girl_index]["sex_experience"]["fetishism"]["masochism"] + all_girls_list[girl_index]["sex_experience"]["fetishism"]["self-torture"] + all_girls_list[girl_index]["sex_experience"]["fetishism"]["golden_shower"] + all_girls_list[girl_index]["sex_experience"]["fetishism"]["scat"]) // 5
        all_girls_list[girl_index]["sex_experience"]["xenophily"]["xenophily"] = (all_girls_list[girl_index]["sex_experience"]["xenophily"]["dog_mating"] + all_girls_list[girl_index]["sex_experience"]["xenophily"]["pig_mating"] + all_girls_list[girl_index]["sex_experience"]["xenophily"]["house_mating"] + all_girls_list[girl_index]["sex_experience"]["xenophily"]["spider_mating"] + all_girls_list[girl_index]["sex_experience"]["xenophily"]["sea_tentacle_mating"] + all_girls_list[girl_index]["sex_experience"]["xenophily"]["field_mating"]) // 6
    def generation_slave():
        global girl_index, traits_skills, traits_sexual, traits_miscellaneous, traits_aura, traits_attributes
        all_girls_list[girl_index].setdefault("obedience",0)
        all_girls_list[girl_index].setdefault("aura",{
        "fear": 0,
        "despair": 0,
        "awareness": 0,
        "taming": 0,
        "habit": 0,
        "spoil": 0,
        "devotion": 0,
        })
        all_girls_list[girl_index]["aura"].setdefault("obedience_bonus",0)
        all_girls_list[girl_index].setdefault("experience", {})
        roll = random.randint(1,4)
        a = ""
        if roll == 1:
            a = "reluctant"
        if roll == 2:
            a = "soft"
        if roll == 3:
            a = "optimistic"
        if roll == 4:
            a = "depresive"
        all_girls_list[girl_index].setdefault("attributes_sum",0)
        all_girls_list[girl_index].setdefault("skills_sum",0)
        all_girls_list[girl_index].setdefault("skills_max",0)
        all_girls_list[girl_index].setdefault("sex_skills_sum",0)
        all_girls_list[girl_index].setdefault("sex_skills_max",0)
        all_girls_list[girl_index].setdefault("rating",0)
        all_girls_list[girl_index].setdefault("neoplasty",0)
        all_girls_list[girl_index].setdefault("psy_status",a)
        all_girls_list[girl_index].setdefault("ill",0)
        all_girls_list[girl_index].setdefault("rehabilitation",0)
        all_girls_list[girl_index].setdefault("injuries",0)
        all_girls_list[girl_index].setdefault("scars",0)
        all_girls_list[girl_index].setdefault("piercings",0)
        all_girls_list[girl_index].setdefault("tattoo",0)
        all_girls_list[girl_index].setdefault("affection_needs",100)
        all_girls_list[girl_index].setdefault("name", "WIP")
        all_girls_list[girl_index].setdefault("hygiene",5)
        all_girls_list[girl_index].setdefault("hygiene_rate",0)
        all_girls_list[girl_index].setdefault("style_plus",0)
        all_girls_list[girl_index].setdefault("exotic_plus",0)
        all_girls_list[girl_index].setdefault("mood",0)
        all_girls_list[girl_index].setdefault("mood_temporal",0)
        all_girls_list[girl_index].setdefault("past_mood",0)
        all_girls_list[girl_index].setdefault("worn_mood",0)
        all_girls_list[girl_index].setdefault("mood_state",{})
        all_girls_list[girl_index].setdefault("beaten_ever",False)
        all_girls_list[girl_index].setdefault("domini_dictum_ever",False)
        all_girls_list[girl_index].setdefault("calories",0)
        all_girls_list[girl_index].setdefault("wig",False)
        all_girls_list[girl_index].setdefault("assistant",False)
        all_girls_list[girl_index].setdefault("races_won",0)
        all_girls_list[girl_index].setdefault("supermacy",0)
        all_girls_list[girl_index].setdefault("bonus_fear",0)
        all_girls_list[girl_index].setdefault("make_up",0)
        all_girls_list[girl_index].setdefault("epilation",0)
        all_girls_list[girl_index].setdefault("manicure",0)
        all_girls_list[girl_index].setdefault("hairstyle",0)
        all_girls_list[girl_index].setdefault("perfume",0)
        all_girls_list[girl_index].setdefault("caught_masturbating",0)
        all_girls_list[girl_index].setdefault("daring",0)
        all_girls_list[girl_index].setdefault("energised",0)
        all_girls_list[girl_index].setdefault("suicide_rate",0)
        all_girls_list[girl_index].setdefault("mood_label","{color=#009FEF}Euphoric{/color}")
        all_girls_list[girl_index].setdefault("exertion","")
        all_girls_list[girl_index].setdefault("yesterday_exhaustion",0)
        all_girls_list[girl_index].setdefault("haircolor","")
        all_girls_list[girl_index].setdefault("hairlength","")
        all_girls_list[girl_index]["mood_state"].setdefault("good_mood",{})
        all_girls_list[girl_index]["mood_state"].setdefault("bad_mood",{})
        
        for key in dic_slave_mood["good_mood"]:
            all_girls_list[girl_index]["mood_state"]["good_mood"].setdefault(key, {"permanent": False , "accustomed": False, "accustomed_value": 20, "active": False, "weight": 1, "duration": 1, "default_duration": 1})
        for key in dic_slave_mood["bad_mood"]:
            all_girls_list[girl_index]["mood_state"]["bad_mood"].setdefault(key, {"permanent": False , "accustomed": False, "accustomed_value": 20, "active": False, "weight": 1, "duration": 1, "default_duration": 1})
        all_girls_list[girl_index].setdefault("already_done",{})
        for key in dic_specializations:
            all_girls_list[girl_index]["already_done"].setdefault(key, 0)
        all_girls_list[girl_index]["already_done"].setdefault("sex", 0)
        all_girls_list[girl_index]["experience"].setdefault("aura", {})
        all_girls_list[girl_index]["experience"]["aura"].setdefault("fear", 0)
        all_girls_list[girl_index]["experience"]["aura"].setdefault("despair", 0)
        all_girls_list[girl_index]["experience"]["aura"].setdefault("awareness", 0)
        all_girls_list[girl_index]["experience"]["aura"].setdefault("taming", 0)
        all_girls_list[girl_index]["experience"]["aura"].setdefault("habit", 0)
        all_girls_list[girl_index]["experience"]["aura"].setdefault("spoil", 0)
        all_girls_list[girl_index]["experience"]["aura"].setdefault("devotion", 0)
        all_girls_list[girl_index]["experience"].setdefault("attributes", {})
        all_girls_list[girl_index]["experience"].setdefault("skills", {})
        all_girls_list[girl_index]["experience"].setdefault("traits", {})
        all_girls_list[girl_index]["experience"].setdefault("sex_experience", {})
        all_girls_list[girl_index]["experience"].setdefault("traits_skills", {})
        all_girls_list[girl_index]["experience"].setdefault("traits_sexual", {})
        all_girls_list[girl_index]["experience"].setdefault("traits_miscellaneous", {})
        all_girls_list[girl_index]["experience"].setdefault("traits_aura", {})
        all_girls_list[girl_index]["experience"].setdefault("traits_attributes", {})
        all_girls_list[girl_index].setdefault("energy", all_girls_list[girl_index]["attributes"]["endurance"] * 2 + 2)
        all_girls_list[girl_index].setdefault("stored_yesterday_energy", 0)
        all_girls_list[girl_index].setdefault("attributes", {})
        all_girls_list[girl_index].setdefault("skills", {})
        all_girls_list[girl_index].setdefault("traits", {})
        all_girls_list[girl_index].setdefault("lactation", False)
        all_girls_list[girl_index].setdefault("breast_modification", 0)
        all_girls_list[girl_index].setdefault("vagina_modification", 0)
        all_girls_list[girl_index].setdefault("vaginal_tightness",0)
        all_girls_list[girl_index].setdefault("anal_tightness",0)
        all_girls_list[girl_index].setdefault("brand",2)
        all_girls_list[girl_index].setdefault("equipment",{})
        all_girls_list[girl_index].setdefault("conscience",True)
        all_girls_list[girl_index].setdefault("days_without_food",0)
        all_girls_list[girl_index].setdefault("days_without_sleep",0)
        all_girls_list[girl_index].setdefault("daily_count",{})
        all_girls_list[girl_index].setdefault("arousal",0)
        all_girls_list[girl_index].setdefault("arousal_rate",0)
        all_girls_list[girl_index].setdefault("status_met",False)
        all_girls_list[girl_index].setdefault("last_cooked_meat_level",0)
        all_girls_list[girl_index].setdefault("slave_auto_sleep",False)
        all_girls_list[girl_index].setdefault("slave_auto_cook",False)
        all_girls_list[girl_index].setdefault("slave_auto_maid",False)
        all_girls_list[girl_index].setdefault("slave_auto_bath",False)
        all_girls_list[girl_index].setdefault("slave_auto_bath_self",False)
        all_girls_list[girl_index].setdefault("did_bath_yesterday",False)
        all_girls_list[girl_index].setdefault("already_bath",False)

        
        

        # variables need for screen logic
        all_girls_list[girl_index].setdefault("maid_slave_skill_performance",0)

        # custom images
        all_girls_list[girl_index].setdefault("slave_auto_sleep_folder",False)
        all_girls_list[girl_index].setdefault("slave_auto_cook_folder",False)
        all_girls_list[girl_index].setdefault("slave_auto_maid_folder",False)
        all_girls_list[girl_index].setdefault("slave_auto_bath_folder",False)
        all_girls_list[girl_index].setdefault("slave_auto_bath_self_folder",False)



        #all_girls_list[girl_index].setdefault("max_daily_reward_level",0)
        #all_girls_list[girl_index].setdefault("max_daily_punishment_level",0)

        all_girls_list[girl_index]["day_bought"] = day_tracker
        all_girls_list[girl_index]["daily_count"].setdefault("reward",0)
        all_girls_list[girl_index]["daily_count"].setdefault("punishments",0)
        all_girls_list[girl_index]["equipment"].setdefault("armour","Without armour")
        all_girls_list[girl_index]["equipment"].setdefault("weapon","Fist")
        all_girls_list[girl_index]["equipment"].setdefault("weapon2","Fist")
        all_girls_list[girl_index]["equipment"].setdefault("amulet","")
        all_girls_list[girl_index]["equipment"].setdefault("ring","")
        all_girls_list[girl_index]["equipment"].setdefault("clothes","Naked")
        all_girls_list[girl_index]["equipment"].setdefault("headgear","")
        all_girls_list[girl_index]["equipment"].setdefault("neck","")
        all_girls_list[girl_index]["equipment"].setdefault("hands","")
        all_girls_list[girl_index]["equipment"].setdefault("feet","")
        all_girls_list[girl_index]["equipment"].setdefault("ring1","")
        all_girls_list[girl_index]["equipment"].setdefault("ring2","")
        all_girls_list[girl_index]["equipment"].setdefault("earrings",{"pierced":True,"type":""})
        all_girls_list[girl_index]["equipment"].setdefault("tongue",{"pierced":True,"type":""})
        all_girls_list[girl_index]["equipment"].setdefault("nipples",{"pierced":True,"type":""})
        all_girls_list[girl_index]["equipment"].setdefault("clitoris",{"pierced":False,"type":""})
        all_girls_list[girl_index]["equipment"].setdefault("navel",{"pierced":False,"type":""})
        all_girls_list[girl_index]["equipment"].setdefault("anus","")
        all_girls_list[girl_index]["equipment"].setdefault("aura_bound",{})
        for key in dic_girl_clothing_full:
            all_girls_list[girl_index]["equipment"]["aura_bound"].setdefault(key, False)
        all_girls_list[girl_index].setdefault("learning_bonus",{})
        for key in dic_slave_skills:
            all_girls_list[girl_index]["learning_bonus"].setdefault(key,0)
        all_girls_list[girl_index]["learning_bonus"].setdefault("sex",0)
        all_girls_list[girl_index]["learning_bonus"].setdefault("academy",0)
        all_girls_list[girl_index].setdefault("specialization",{})
        for key in dic_specializations:
            all_girls_list[girl_index]["specialization"].setdefault(key,False)
        all_girls_list[girl_index].setdefault("daily_bonus",{})
        all_girls_list[girl_index]["daily_bonus"].setdefault("devotion",0)
        all_girls_list[girl_index]["daily_bonus"].setdefault("taming",0)
        all_girls_list[girl_index]["daily_bonus"].setdefault("arousal",0)
        all_girls_list[girl_index]["daily_bonus"].setdefault("endurance",0)
        all_girls_list[girl_index]["daily_bonus"].setdefault("empathy",0)
        all_girls_list[girl_index]["daily_bonus"].setdefault("temperament",0)
        all_girls_list[girl_index]["daily_bonus"].setdefault("nature",0)
        all_girls_list[girl_index]["daily_bonus"].setdefault("pride",0)
        all_girls_list[girl_index]["traits"].setdefault("traits_open", {})
        all_girls_list[girl_index]["traits"]["traits_open"].setdefault("traits_always", {})
        all_girls_list[girl_index]["traits"]["traits_open"].setdefault("traits_especial", {})
        all_girls_list[girl_index]["traits"].setdefault("traits_hidden", {})
        all_girls_list[girl_index]["traits"]["traits_hidden"].setdefault("traits_skills(1/8)", {})
        all_girls_list[girl_index]["traits"]["traits_hidden"].setdefault("traits_sexual(1/10)", {})       
        all_girls_list[girl_index]["traits"]["traits_hidden"].setdefault("traits_miscellaneous(1/12)", {})       
        all_girls_list[girl_index]["traits"]["traits_hidden"].setdefault("traits_aura(1/16)", {})     
        all_girls_list[girl_index]["traits"]["traits_hidden"].setdefault("traits_attributes(1/20)", {})
        all_girls_list[girl_index].setdefault("sex_experience", {})
        all_girls_list[girl_index]["sex_experience"].setdefault("petting", {})
        all_girls_list[girl_index]["sex_experience"].setdefault("oral_pleasure", {})
        all_girls_list[girl_index]["sex_experience"].setdefault("penetration", {})
        all_girls_list[girl_index]["sex_experience"].setdefault("group_sex", {})
        all_girls_list[girl_index]["sex_experience"].setdefault("demostration", {})
        all_girls_list[girl_index]["sex_experience"].setdefault("fetishism", {})
        all_girls_list[girl_index]["sex_experience"].setdefault("xenophily", {})
        all_girls_list[girl_index].setdefault("sleep", 2)
        all_girls_list[girl_index].setdefault("diet", 0)
        all_girls_list[girl_index].setdefault("portion_size", 1)
        all_girls_list[girl_index].setdefault("your_leftovers",False)
        all_girls_list[girl_index].setdefault("supplements",False)
        all_girls_list[girl_index].setdefault("rules", {})
        all_girls_list[girl_index]["rules"].setdefault("rules_count",0)
        all_girls_list[girl_index]["rules"].setdefault("act_as_cook",False)
        all_girls_list[girl_index]["rules"].setdefault("act_as_maid",False)
        all_girls_list[girl_index]["rules"].setdefault("bath_slave",False)
        all_girls_list[girl_index]["rules"].setdefault("behave_alarm",False)
        all_girls_list[girl_index]["rules"].setdefault("behave_humility",False)
        all_girls_list[girl_index]["rules"].setdefault("behave_pet",False)
        all_girls_list[girl_index]["rules"].setdefault("behave_silence",False)
        all_girls_list[girl_index]["rules"].setdefault("behave_toilet",False)
        all_girls_list[girl_index]["rules"].setdefault("behave_urinal",False)
        all_girls_list[girl_index]["rules"].setdefault("deny_orgasm",False)
        all_girls_list[girl_index]["rules"].setdefault("deny_toileting",False)
        all_girls_list[girl_index]["rules"].setdefault("milk_the_fiend",False)
        all_girls_list[girl_index]["rules"].setdefault("no_masturbation",False)   
        all_girls_list[girl_index]["rules"].setdefault("use_vaginal_beads",False)
        all_girls_list[girl_index]["rules"].setdefault("enforce_rules",False)
        ###########################################
        all_girls_list[girl_index].setdefault("rules_broken", {})
        all_girls_list[girl_index]["rules_broken"].setdefault("act_as_cook",False)
        all_girls_list[girl_index]["rules_broken"].setdefault("act_as_maid",False)
        all_girls_list[girl_index]["rules_broken"].setdefault("bath_slave",False)
        all_girls_list[girl_index]["rules_broken"].setdefault("behave_alarm",False)
        all_girls_list[girl_index]["rules_broken"].setdefault("behave_humility",False)
        all_girls_list[girl_index]["rules_broken"].setdefault("behave_pet",False)
        all_girls_list[girl_index]["rules_broken"].setdefault("behave_silence",False)
        all_girls_list[girl_index]["rules_broken"].setdefault("behave_toilet",False)
        all_girls_list[girl_index]["rules_broken"].setdefault("behave_urinal",False)
        all_girls_list[girl_index]["rules_broken"].setdefault("deny_orgasm",False)
        all_girls_list[girl_index]["rules_broken"].setdefault("deny_toileting",False)
        all_girls_list[girl_index]["rules_broken"].setdefault("milk_the_fiend",False)
        all_girls_list[girl_index]["rules_broken"].setdefault("no_masturbation",False)   
        all_girls_list[girl_index]["rules_broken"].setdefault("use_vaginal_beads",False)
        all_girls_list[girl_index]["rules_broken"].setdefault("enforce_rules",False)


        traits_skills = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]
        traits_sexual = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_sexual(1/10)"]
        traits_miscellaneous = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]
        traits_aura = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_aura(1/16)"]
        traits_attributes = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_attributes(1/20)"]

        for key, values in dic_slave_skills.items():
            all_girls_list[girl_index]["experience"]["skills"].setdefault(key,0)
            if key not in all_girls_list[girl_index]["skills"]:
                roll = random.randint(1, 3)
                if roll == 1:
                    roll2 = random.randint(1, 5)
                    val = 2 if roll2 == 1 else 1
                else:
                    val = 0
                all_girls_list[girl_index]["skills"][key] = val
        for key, values in dic_traits_skills.items():
            all_girls_list[girl_index]["experience"]["traits_skills"].setdefault(key,0)
            if key not in traits_skills:
                roll = random.randint(1, 16)
                if roll == 1:
                    roll2 = random.randint(1, 5)
                    val = 2 if roll2 == 1 else 1
                elif roll == 16:
                    roll2 = random.randint(1, 5)
                    val = -2 if roll2 == 1 else -1
                else:
                    val = 0
                traits_skills[key] = {"value": val, "revealed": False}    
        for key, values in dic_traits_sexual.items():
            all_girls_list[girl_index]["experience"]["traits_sexual"].setdefault(key,0)
            if key not in traits_sexual:
                roll = random.randint(1, 20)
                if roll == 1:
                    roll2 = random.randint(1, 5)
                    val = 2 if roll2 == 1 else 1
                elif roll == 20:
                    roll2 = random.randint(1, 5)
                    val = -2 if roll2 == 1 else -1
                else:
                    val = 0
                traits_sexual[key] = {"value": val, "revealed": False}
        for key, values in dic_traits_miscellaneous.items():
            all_girls_list[girl_index]["experience"]["traits_miscellaneous"].setdefault(key,0)
            if key not in traits_miscellaneous:
                roll = random.randint(1, 24)
                if roll == 1:
                    roll2 = random.randint(1, 5)
                    val = 2 if roll2 == 1 else 1
                elif roll == 24:
                    roll2 = random.randint(1, 5)
                    val = -2 if roll2 == 1 else -1
                else:
                    val = 0
                traits_miscellaneous[key] = {"value": val, "revealed": False}
        for key, values in dic_traits_aura.items():
            all_girls_list[girl_index]["experience"]["traits_aura"].setdefault(key,0)
            if key not in traits_aura:
                roll = random.randint(1, 32)
                if roll == 1:
                    roll2 = random.randint(1, 5)
                    val = 2 if roll2 == 1 else 1
                elif roll == 32:
                    roll2 = random.randint(1, 5)
                    val = -2 if roll2 == 1 else -1
                else:
                    val = 0
                traits_aura[key] = {"value": val, "revealed": False}
        for key, values in dic_traits_attributes.items():
            all_girls_list[girl_index]["experience"]["traits_attributes"].setdefault(key,0)
            if key not in traits_attributes:
                roll = random.randint(1, 40)
                if roll == 1:
                    roll2 = random.randint(1, 5)
                    val = 2 if roll2 == 1 else 1
                elif roll == 40:
                    roll2 = random.randint(1, 5)
                    val = -2 if roll2 == 1 else -1
                else:
                    val = 0
                traits_attributes[key] = {"value": val, "revealed": False}
        for key, values in dic_sex_experience.items():
            all_girls_list[girl_index]["experience"]["sex_experience"].setdefault(key, {})
            for key2, values2 in dic_sex_experience[key].items():
                if key2 not in all_girls_list[girl_index]["sex_experience"][key]:
                    roll = random.randint(1, 3)
                    if roll == 1:
                        roll2 = random.randint(1, 2)
                        val = 2 if roll2 == 1 else 1
                    else:
                        val = 0
                    all_girls_list[girl_index]["sex_experience"][key][key2] = val
                all_girls_list[girl_index]["experience"]["sex_experience"][key].setdefault(key2,0)
        for key, values in dic_slave_attributes.items():
            all_girls_list[girl_index]["experience"]["attributes"].setdefault(key,0)
            if key not in all_girls_list[girl_index]["attributes"]:
                if key == "beauty":
                    roll = random.randint(1, 5)
                elif key in ["exoticism", "style", "fame"]:
                    roll = 0
                else:
                    roll = random.randint(0, 5)
                all_girls_list[girl_index]["attributes"].setdefault(key, roll)
        if not "world_description" in all_girls_list[girl_index]:
            roll = random.randint(0,13)
            all_girls_list[girl_index]["world"] = world[roll][name]
            roll = random.randint(0, len(shared_families[all_girls_list[girl_index]["world"]])-1)
            all_girls_list[girl_index]["family"] = shared_families[all_girls_list[girl_index]["world"]][roll]
            roll = random.randint(0, len(occupation[all_girls_list[girl_index]["family"]])-1)
            all_girls_list[girl_index]["ocupation"] = ocupation[all_girls_list[girl_index]["family"]][roll]
            if all_girls_list[girl_index]["world"] == "prehistoric":
                all_girls_list[girl_index]["attributes"]["exotic"] += 1
                if all_girls_list[girl_index]["attributes"]["endurance"] < 5:
                    all_girls_list[girl_index]["attributes"]["endurance"] += 1
                if all_girls_list[girl_index]["attributes"]["temperament"] < 5:
                    all_girls_list[girl_index]["attributes"]["temperament"] += 1
                if all_girls_list[girl_index]["attributes"]["nature"] > 0:
                    all_girls_list[girl_index]["attributes"]["nature"] -= 1
                if all_girls_list[girl_index]["attributes"]["intelligence"] > 0:
                    all_girls_list[girl_index]["attributes"]["intelligence"] -= 1
            elif all_girls_list[girl_index]["world"] == "barbarian":
                if all_girls_list[girl_index]["attributes"]["endurance"] < 5:
                    all_girls_list[girl_index]["attributes"]["endurance"] += 1
                if all_girls_list[girl_index]["attributes"]["temperament"] < 5:
                    all_girls_list[girl_index]["attributes"]["temperament"] += 1
                if all_girls_list[girl_index]["attributes"]["nature"] > 0:
                    all_girls_list[girl_index]["attributes"]["nature"] -= 1
                if all_girls_list[girl_index]["attributes"]["intelligence"] > 0:
                    all_girls_list[girl_index]["attributes"]["intelligence"] -= 1
            elif all_girls_list[girl_index]["world"] == "sns":
                if all_girls_list[girl_index]["attributes"]["endurance"] < 5:
                    all_girls_list[girl_index]["attributes"]["endurance"] += 1
                if all_girls_list[girl_index]["attributes"]["nature"] > 0:
                    all_girls_list[girl_index]["attributes"]["nature"] -= 1 
                if all_girls_list[girl_index]["attributes"]["intelligence"] > 0:
                    all_girls_list[girl_index]["attributes"]["intelligence"] -= 1
            elif all_girls_list[girl_index]["world"] == "medieval":
                if all_girls_list[girl_index]["attributes"]["temperament"] > 0:
                    all_girls_list[girl_index]["attributes"]["temperament"] -= 1
                if all_girls_list[girl_index]["attributes"]["nature"] > 0:
                    all_girls_list[girl_index]["attributes"]["nature"] -= 1
                if all_girls_list[girl_index]["attributes"]["intelligence"] > 0:
                    all_girls_list[girl_index]["attributes"]["intelligence"] -= 1
                all_girls_list[girl_index]["aura"]["habit"] += 1
            elif all_girls_list[girl_index]["world"] == "highfantasy":
                all_girls_list[girl_index]["attributes"]["exotic"] += 1
                if all_girls_list[girl_index]["attributes"]["empathy"] < 5:
                    all_girls_list[girl_index]["attributes"]["empathy"] += 1
            elif all_girls_list[girl_index]["world"] == "darkfantasy":
                all_girls_list[girl_index]["attributes"]["exotic"] += 1
                all_girls_list[girl_index]["aura"]["habit"] += 2
                if all_girls_list[girl_index]["attributes"]["endurance"] > 0:
                    all_girls_list[girl_index]["attributes"]["endurance"] -= 1
                if all_girls_list[girl_index]["attributes"]["temperament"] > 0:
                    all_girls_list[girl_index]["attributes"]["temperament"] -= 1
                if all_girls_list[girl_index]["attributes"]["nature"] > 0:
                    all_girls_list[girl_index]["attributes"]["nature"] -= 1
                if all_girls_list[girl_index]["attributes"]["empathy"] > 0:
                    all_girls_list[girl_index]["attributes"]["empathy"] -= 1
                if all_girls_list[girl_index]["attributes"]["intelligence"] > 0:
                    all_girls_list[girl_index]["attributes"]["intelligence"] -= 1
                if all_girls_list[girl_index]["attributes"]["pride"] < 5:
                    all_girls_list[girl_index]["attributes"]["pride"] += 1
            elif all_girls_list[girl_index]["world"] == "steampunk":
                all_girls_list[girl_index]["aura"]["habit"] += 1
            elif all_girls_list[girl_index]["world"] == "industrial":
                all_girls_list[girl_index]["aura"]["habit"] += 1
            elif all_girls_list[girl_index]["world"] == "modern":
                if all_girls_list[girl_index]["attributes"]["nature"] < 5:
                    all_girls_list[girl_index]["attributes"]["nature"] += 1
                if all_girls_list[girl_index]["attributes"]["pride"] > 0:
                    all_girls_list[girl_index]["attributes"]["pride"] -= 1
                if all_girls_list[girl_index]["attributes"]["intelligence"] < 5:
                    all_girls_list[girl_index]["attributes"]["intelligence"] += 1
                if all_girls_list[girl_index]["attributes"]["endurance"] > 0:
                    all_girls_list[girl_index]["attributes"]["endurance"] -= 1
            elif all_girls_list[girl_index]["world"] == "cyberpunk":
                if all_girls_list[girl_index]["attributes"]["pride"] > 0:
                    all_girls_list[girl_index]["attributes"]["pride"] -= 1                                
                if all_girls_list[girl_index]["attributes"]["intelligence"] < 5:
                    all_girls_list[girl_index]["attributes"]["intelligence"] += 1
                if all_girls_list[girl_index]["attributes"]["temperament"] > 0:
                    all_girls_list[girl_index]["attributes"]["temperament"] -= 1      
                if all_girls_list[girl_index]["attributes"]["endurance"] > 0:
                    all_girls_list[girl_index]["attributes"]["endurance"] -= 1
            elif all_girls_list[girl_index]["world"] == "utopia":
                all_girls_list[girl_index]["attributes"]["exotic"] += 1
                all_girls_list[girl_index]["aura"]["spoil"] += 1
                if all_girls_list[girl_index]["attributes"]["intelligence"] < 5:
                    all_girls_list[girl_index]["attributes"]["intelligence"] += 1
                all_girls_list[girl_index]["attributes"]["empathy"] = min(all_girls_list[girl_index]["attributes"]["empathy"]+2,5)
                if all_girls_list[girl_index]["attributes"]["pride"] > 0:
                    all_girls_list[girl_index]["attributes"]["pride"] -= 1        
            elif all_girls_list[girl_index]["world"] == "darkfuture":
                all_girls_list[girl_index]["aura"]["habit"] += 2
                all_girls_list[girl_index]["attributes"]["temperament"] = max(all_girls_list[girl_index]["attributes"]["temperament"]-2,0)
                all_girls_list[girl_index]["attributes"]["nature"] = max(all_girls_list[girl_index]["attributes"]["nature"]-2,0)
                if all_girls_list[girl_index]["attributes"]["endurance"] > 0:
                    all_girls_list[girl_index]["attributes"]["endurance"] -= 1        
                if all_girls_list[girl_index]["attributes"]["temperament"] > 0:
                    all_girls_list[girl_index]["attributes"]["temperament"] -= 1  
                if all_girls_list[girl_index]["attributes"]["intelligence"] < 5:
                    all_girls_list[girl_index]["attributes"]["intelligence"] += 1
                if all_girls_list[girl_index]["attributes"]["empathy"] > 0:
                    all_girls_list[girl_index]["attributes"]["empathy"] -= 1
                if all_girls_list[girl_index]["attributes"]["pride"] > 0:
                    all_girls_list[girl_index]["attributes"]["pride"] -= 1 
                if all_girls_list[girl_index]["attributes"]["physical"] < 5:
                    all_girls_list[girl_index]["attributes"]["physical"] += 1 
            elif all_girls_list[girl_index]["world"] == "space":
                all_girls_list[girl_index]["attributes"]["exotic"] += 1
                if all_girls_list[girl_index]["attributes"]["endurance"] > 0:
                    all_girls_list[girl_index]["attributes"]["endurance"] -= 1                
                if all_girls_list[girl_index]["attributes"]["intelligence"] < 5:
                    all_girls_list[girl_index]["attributes"]["intelligence"] += 1
                if all_girls_list[girl_index]["attributes"]["pride"] > 0:
                    all_girls_list[girl_index]["attributes"]["pride"] -= 1         
                if all_girls_list[girl_index]["attributes"]["nature"] < 5:
                    all_girls_list[girl_index]["attributes"]["nature"] += 1    
        # TODO TRIBU AND OCUPATION
        
        
        all_girls_list[girl_index]["attributes"]["natural_beauty"] = all_girls_list[girl_index]["attributes"]["beauty"]
        all_girls_list[girl_index]["attributes"]["natural_exoticism"] = all_girls_list[girl_index]["attributes"]["exoticism"] #TODO WIP
        if all_girls_list[girl_index]["sex_experience"]["penetration"]["vaginal_sex"] >= 1:
            all_girls_list[girl_index]["vaginal_tightness"] = 2
        elif all_girls_list[girl_index]["sex_experience"]["penetration"]["fisting"] >= 4:
            all_girls_list[girl_index]["vaginal_tightness"] = 3
        if all_girls_list[girl_index]["sex_experience"]["penetration"]["anal_sex"] >= 1:
            all_girls_list[girl_index]["anal_tightness"] = 2
        elif all_girls_list[girl_index]["sex_experience"]["penetration"]["anal_fisting"] >= 4:
            all_girls_list[girl_index]["anal_tightness"] = 3
        
        # Extra code for beauty trait
        if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_attributes(1/20)"]["beautytrait"]["value"] < 0:
            all_girls_list[girl_index]["attributes"]["beauty"] = 0
            all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_attributes(1/20)"]["beautytrait"]["value"] = 0
        if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_attributes(1/20)"]["beautytrait"]["value"] > 0:
            all_girls_list[girl_index]["attributes"]["beauty"] = 5
    def master_moodlet_calculation():
        global wealth_quality_modifier, standard_of_living_value_8, brand_reputation_value_6
        global estate_quality, estate_quality_modifier, brand_reputation_value_6
        global personality_value_2, home_hygiene_value, hygiene_value_9
        global after_sex_effects, excitement_value, libido_value_4
        global blazing_counter, injuries_value_11,energy_value, strength_value_1
        global pos_show_counter, alone_count, girl_index, save_girl_index
        wealth_quality_modifier = standard_of_living_value_8 - brand_reputation_value_6 - 1
        if wealth_quality_modifier > 0: 
            master_mood_state["good_mood"]['pos_wealth']["active"] = True
            master_mood_state["bad_mood"]['neg_wealth']["active"] = False
        if wealth_quality_modifier == 0: 
            master_mood_state["good_mood"]['pos_wealth']["active"] = False
            master_mood_state["bad_mood"]['neg_wealth']["active"] = False
        if wealth_quality_modifier < 0: 
            master_mood_state["good_mood"]['pos_wealth']["active"] = False
            master_mood_state["bad_mood"]['neg_wealth']["active"] = True
        estate_quality = 0
        estate_quality += home_estate["kitchen"]["Deplorable kitchen"]*1
        estate_quality += home_estate["kitchen"]["Basic kitchen"]*2
        estate_quality += home_estate["kitchen"]["Well-equipped kitchen"]*3
        estate_quality += home_estate["kitchen"]["Gourmet kitchen"]*4
        estate_quality += home_estate["barn"]["Collapsing barn"]*1
        estate_quality += home_estate["barn"]["Worn barn"]*2
        estate_quality += home_estate["barn"]["Sturdy barn"]*3
        estate_quality += home_estate["barn"]["Masterwork barn"]*4
        estate_quality += home_estate["laboratory"]["Makeshift lab"]*1
        estate_quality += home_estate["laboratory"]["Crude lab"]*2
        estate_quality += home_estate["laboratory"]["Proper lab"]*3
        estate_quality += home_estate["laboratory"]["Advanced laboratory"]*4
        estate_quality += home_estate["slaves_rooms"]["squalid_room"]*1
        estate_quality += home_estate["slaves_rooms"]["cramped_room"]*2
        estate_quality += home_estate["slaves_rooms"]["comfortable_room"]*3
        estate_quality += home_estate["slaves_rooms"]["luxurios_room"]*4
        estate_quality += dic_home_state2[master_house_reputation["home_estate"]]["prestige"]*20
        estate_quality_modifier = (estate_quality //20) - brand_reputation_value_6
        if estate_quality_modifier > personality_value_2 - home_hygiene_value + 5: 
            master_mood_state["good_mood"]["pos_housing"]["active"] = True
            master_mood_state["bad_mood"]["neg_housing"]["active"] = False
        else: 
            master_mood_state["good_mood"]["pos_housing"]["active"] = False
            master_mood_state["bad_mood"]["neg_housing"]["active"] = False
        if personality_value_2 > standard_of_living_value_8 - 1 :
            master_mood_state["good_mood"]["pos_housing"]["active"] = False
            master_mood_state["bad_mood"]["neg_housing"]["active"] = True
        if personality_value_2 > estate_quality_modifier :
            master_mood_state["good_mood"]["pos_wealth"]["active"] = False
            master_mood_state["bad_mood"]["neg_wealth"]["active"] = True
        if home_hygiene_value == 5:
            master_mood_state["good_mood"]["pos_house_clean"]["active"] = True
            master_mood_state["bad_mood"]["neg_home_hygiene_value"]["active"] = False
        elif home_hygiene_value >= 3:
            master_mood_state["good_mood"]["pos_house_clean"]["active"] = False
            master_mood_state["bad_mood"]["neg_home_hygiene_value"]["active"] = False
        else:
            master_mood_state["good_mood"]["pos_house_clean"]["active"] = False
            master_mood_state["bad_mood"]["neg_home_hygiene_value"]["active"] = True
        if hygiene_value_9 >= 4:
            master_mood_state["good_mood"]["pos_self_clean"]["active"] = True
            master_mood_state["bad_mood"]["neg_dirty"]["active"] = False
        elif hygiene_value_9 < 2:
            master_mood_state["good_mood"]["pos_self_clean"]["active"] = False
            master_mood_state["bad_mood"]["neg_dirty"]["active"] = True
        else:
            master_mood_state["good_mood"]["pos_self_clean"]["active"] = False
            master_mood_state["bad_mood"]["neg_dirty"]["active"] = False
        if after_sex_effects < 0:
            after_sex_effects = 0
            master_mood_state["good_mood"]["pos_satisfied"]["active"] = False
        if excitement_value > after_sex_effects:
            master_mood_state["bad_mood"]["neg_boner"]["active"] = True
        if after_sex_effects > 2:
            master_mood_state["bad_mood"]["neg_boner"]["active"] = False
        if excitement_value < after_sex_effects:
            master_mood_state["bad_mood"]["neg_boner"]["active"] = False
        if excitement_value < -2 and libido_value_4 > 0:
            master_mood_state["bad_mood"]["neg_softcore"]["active"] = True
        if excitement_value > 3 or libido_value_4 == 0:
            master_mood_state["bad_mood"]["neg_softcore"]["active"] = False
        if excitement_value >= 5 and blazing_counter >= 3:
            master_mood_state["bad_mood"]["neg_blazing"]["active"] = True
        else:
            master_mood_state["bad_mood"]["neg_blazing"]["active"] = False
        if injuries_value_11 >= 5:
            master_mood_state["bad_mood"]["neg_wounded"]["active"] = False
        else:
            master_mood_state["bad_mood"]["neg_wounded"]["active"] = True
        if energy_value < 0:
            master_mood_state["good_mood"]["pos_energy"]["active"] = False
            master_mood_state["bad_mood"]["neg_tired"]["active"] = True
        elif energy_value >= strength_value_1:
            for values in ["neg_drunk","neg_wounded","neg_no_koffe","neg_no_meth","neg_no_opium","neg_master_ill"]:
                n = 0
                if master_mood_state["bad_mood"][values]["active"]:
                    n += 1
            if n == 0:
                master_mood_state["good_mood"]["pos_energy"]["active"] = True
                master_mood_state["bad_mood"]["neg_tired"]["active"] = False
        else: 
            master_mood_state["good_mood"]["pos_energy"]["active"] = False
            master_mood_state["bad_mood"]["neg_tired"]["active"] = False
        if pos_show_counter > 0:
            master_mood_state["bad_mood"]["neg_boring"]["active"] = False
        if alone_count > 2: 
            master_mood_state["bad_mood"]["neg_alone"]["active"] = True
        else:
            master_mood_state["bad_mood"]["neg_alone"]["active"] = False
        save_girl_index = girl_index
        # this pos_optimism is higher when more slave are horny, servile or obedient
        master_mood_state["good_mood"]["pos_optimism"]["weight"] = 0.5
        for girl_index in all_girls_list:
            if all_girls_list[girl_index]["psy_status"] in ["horny","servile","obedient"]:
                all_girls_list[girl_index]["status_met"] = True
            else:
                all_girls_list[girl_index]["status_met"] = False
            if all_girls_list[girl_index]["attributes"]["beauty"] > 2 and all_girls_list[girl_index]["skills"]["elocution"] > 3 and all_girls_list[girl_index]["status_met"]:
                master_mood_state["good_mood"]["pos_optimism"]["active"] = True
                master_mood_state["good_mood"]["pos_optimism"]["weight"] += 0.5
            if all_girls_list[girl_index]["psy_status"] == "broken":
                master_mood_state["good_mood"]["pos_optimism"]["active"] = False
                master_mood_state["bad_mood"]["neg_grumpy"]["active"] = True
        girl_index = save_girl_index
    def master_mood_calculation():
        global mood_value_10, master_past_mood, master_worn_bonus, master_temporal_mood
        global mood_textvalue_10
        mood_value_10 = 0
        mood_value_10 += master_worn_bonus
        mood_value_10 += master_temporal_mood
        if master_past_mood > 0:
            mood_value_10 += master_past_mood/10
        else:
            mood_value_10 += master_past_mood/4
        for key in dic_master_mood["good_mood"]:
            if master_mood_state["good_mood"][key]["active"]:
                mood_value_10 += master_mood_state["good_mood"][key]["weight"]
        for key in dic_master_mood["bad_mood"]:
            if master_mood_state["bad_mood"][key]["active"]:
                mood_value_10 -= master_mood_state["bad_mood"][key]["weight"]
        if mood_value_10 <= -5:
            mood_textvalue_10 = dic_slave_moodlevel[0]
        elif mood_value_10 <= -4:
            mood_textvalue_10 = dic_slave_moodlevel[1]
        elif mood_value_10 <= -3:
            mood_textvalue_10 = dic_slave_moodlevel[2]
        elif mood_value_10 <= -2:
            mood_textvalue_10 = dic_slave_moodlevel[3]
        elif mood_value_10 <= -1:
            mood_textvalue_10 = dic_slave_moodlevel[4]
        elif mood_value_10 < 1:
            mood_textvalue_10 = dic_slave_moodlevel[5]
        elif mood_value_10 < 2:
            mood_textvalue_10 = dic_slave_moodlevel[6]
        elif mood_value_10 < 3:
            mood_textvalue_10 = dic_slave_moodlevel[7]
        elif mood_value_10 < 4:
            mood_textvalue_10 = dic_slave_moodlevel[8]
        elif mood_value_10 < 5:
            mood_textvalue_10 = dic_slave_moodlevel[9]
        elif mood_value_10 >= 5:
            mood_textvalue_10 = dic_slave_moodlevel[10]
        if mood_value_10 >= 5 and reputation_value_1 >= 5:
            mood_textvalue_10 = dic_slave_moodlevel[11]
    def obedience_difficulty_adjustment():
        global slave_difficulty, slave_obedience_bonus, dic_overnight_rules_count_index
        global dic_custom_start_difficulty_selection_index_index
        if dic_custom_start_difficulty_selection_index_index == 0:
            slave_obedience_bonus = 4
            slave_difficulty = 2
            dic_overnight_rules_count_index = 0
        elif dic_custom_start_difficulty_selection_index_index == 1:
            slave_obedience_bonus = 0
            slave_difficulty = 4
            dic_overnight_rules_count_index = 1
        elif dic_custom_start_difficulty_selection_index_index == 2:
            slave_obedience_bonus = 0
            slave_difficulty = 14 - min(8, 4*all_girls_list[girl_index]["aura"]["devotion"])
            dic_overnight_rules_count_index =2
    def supermacy_calculation():
        global master_supermacy, girl_index, personality_value_2, allure_value_3, dominance_value_5, strength_value_1, magna_magnifika

        master_supermacy = personality_value_2 + allure_value_3 + dominance_value_5 + strength_value_1 + magna_magnifika
        all_girls_list[girl_index]["supermacy"] = (
        all_girls_list[girl_index]["attributes"]["temperament"] 
        + all_girls_list[girl_index]["attributes"]["nature"] 
        + 5 - all_girls_list[girl_index]["attributes"]["pride"] 
        + all_girls_list[girl_index]["attributes"]["endurance"] 
        + all_girls_list[girl_index]["attributes"]["intelligence"] - 3
        )
        if all_girls_list[girl_index]["beaten_ever"]:
            all_girls_list[girl_index]["supermacy"] -= 1
        if all_girls_list[girl_index]["domini_dictum_ever"]:
            all_girls_list[girl_index]["supermacy"] -= 1
    def cap_slave_values():
        global girl_index
        # Cap aura values
        for aura in ["fear","despair","awareness","taming","habit","spoil","devotion"]:
            if all_girls_list[girl_index]["aura"][aura] == 0 and all_girls_list[girl_index]["experience"]["aura"][aura] < -10:
                all_girls_list[girl_index]["experience"]["aura"][aura] = -10
            if all_girls_list[girl_index]["aura"][aura] == 5 and all_girls_list[girl_index]["experience"]["aura"][aura] > 10:
                all_girls_list[girl_index]["experience"]["aura"][aura] = 10
        # Cap attributes values
        for attributes in ["endurance","nature","temperament","exoticism","style","fame","intelligence"]:
            if all_girls_list[girl_index]["attributes"][attributes] == 0 and all_girls_list[girl_index]["experience"]["attributes"][attributes] < -10:
                all_girls_list[girl_index]["experience"]["attributes"][attributes] = -10
            if all_girls_list[girl_index]["attributes"][attributes] == 5 and all_girls_list[girl_index]["experience"]["attributes"][attributes] > 10:
                all_girls_list[girl_index]["experience"]["attributes"][attributes] = 10
        # Cap attributes for especial values
        for attributes in ["pride","physical"]:
            if all_girls_list[girl_index]["attributes"][attributes] == 0 and all_girls_list[girl_index]["experience"]["attributes"][attributes] < -10:
                all_girls_list[girl_index]["experience"]["attributes"][attributes] = 10
            if all_girls_list[girl_index]["attributes"][attributes] == 5 and all_girls_list[girl_index]["experience"]["attributes"][attributes] > 10:
                all_girls_list[girl_index]["experience"]["attributes"][attributes] = -10
        # Cap skills
        for skill in all_girls_list[girl_index]["skills"]:
            if all_girls_list[girl_index]["skills"][skill] == 0 and all_girls_list[girl_index]["experience"]["skills"][skill] < -10:
                all_girls_list[girl_index]["experience"]["skills"][skill] = -10
            if all_girls_list[girl_index]["skills"][skill] == 5 and all_girls_list[girl_index]["experience"]["skills"][skill] > 10:
                all_girls_list[girl_index]["experience"]["skills"][skill] = 10
        # Cap sexual experience
        for sex_experience in all_girls_list[girl_index]["sex_experience"]:
            for type in all_girls_list[girl_index]["sex_experience"][sex_experience]:
                if type != sex_experience:
                    if all_girls_list[girl_index]["sex_experience"][sex_experience][type] == 0 and all_girls_list[girl_index]["experience"]["sex_experience"][sex_experience][type] < -10:
                        all_girls_list[girl_index]["experience"]["sex_experience"][sex_experience][type] = -10
                    if all_girls_list[girl_index]["sex_experience"][sex_experience][type] == 5 and all_girls_list[girl_index]["experience"]["sex_experience"][sex_experience][type] > 10:
                        all_girls_list[girl_index]["experience"]["sex_experience"][sex_experience][type] = 10
    def slave_fainted():
        global is_slave_nearly_fainted
        if all_girls_list[girl_index]["energy"] <= -5 and all_girls_list[girl_index]["conscience"]:
            all_girls_list[girl_index]["conscience"] = False
            msg("Your slave fainted due to extreme exhaustion.")
        elif all_girls_list[girl_index]["attributes"]["endurance"] == 0 and all_girls_list[girl_index]["conscience"]:
            all_girls_list[girl_index]["conscience"] = False
            msg("Your slave fainted due to having no stamina.")
        elif all_girls_list[girl_index]["attributes"]["endurance"] == 1 and all_girls_list[girl_index]["experience"]["attributes"]["endurance"] <= 0:
            if not is_slave_nearly_fainted:
                is_slave_nearly_fainted = True
                msg("Be careful, your slave nearly fainted due to a lack of stamina.")
    def dead_slave_check():
        global sparks_37
        if (all_girls_list[girl_index]["attributes"]["endurance"] == 0 
        and all_girls_list[girl_index]["attributes"]["physical"] == 5 
        and max(all_girls_list[girl_index]["experience"]["attributes"]["endurance"], all_girls_list[girl_index]["experience"]["attributes"]["physical"]) <= -10):    
            temporal_value = meat_evaluation()
            del all_girls_list[girl_index]
            sparks_37 += temporal_value
            msg("Your slave is dead, and you sale the meat to the butcher for [temporal_value]")
    def broken_slave_check():
        if all_girls_list[girl_index]["attributes"]["nature"] + all_girls_list[girl_index]["attributes"]["temperament"] + 5 - all_girls_list[girl_index]["attributes"]["pride"] < 3:
            all_girls_list[girl_index]["psy_status"] = "broken"
            all_girls_list[girl_index]["experience"]["attributes"]["pride"] = 0
            all_girls_list[girl_index]["experience"]["attributes"]["temperament"] = 0
            all_girls_list[girl_index]["experience"]["aura"]["fear"] = 0
            all_girls_list[girl_index]["experience"]["aura"]["despair"] = 0
            all_girls_list[girl_index]["experience"]["aura"]["devotion"] = 0
            all_girls_list[girl_index]["experience"]["aura"]["spoil"] = 0
            all_girls_list[girl_index]["experience"]["aura"]["habit"] = 0
            all_girls_list[girl_index]["experience"]["aura"]["taming"] = 0
            all_girls_list[girl_index]["experience"]["aura"]["awareness"] = 0
            all_girls_list[girl_index]["arousal"] = 0
    def obedience_calculation():
        slave_nature = (5 - all_girls_list[girl_index]["attributes"]["pride"] 
        + all_girls_list[girl_index]["attributes"]["temperament"] 
        + all_girls_list[girl_index]["attributes"]["nature"] 
        + all_girls_list[girl_index]["attributes"]["intelligence"])
        if all_girls_list[girl_index]["aura"]["fear"] > 0:    
            if slave_nature < 11:
                all_girls_list[girl_index]["bonus_fear"] = all_girls_list[girl_index]["aura"]["fear"] *2
            elif slave_nature == 11:
                all_girls_list[girl_index]["bonus_fear"] = all_girls_list[girl_index]["aura"]["fear"] *2 + 1
            elif slave_nature == 12:
                all_girls_list[girl_index]["bonus_fear"] = all_girls_list[girl_index]["aura"]["fear"] *2 + 2
            elif slave_nature == 13:
                all_girls_list[girl_index]["bonus_fear"] = all_girls_list[girl_index]["aura"]["fear"] *2 + 3
            elif slave_nature == 14:
                all_girls_list[girl_index]["bonus_fear"] = all_girls_list[girl_index]["aura"]["fear"] *2 + 4
            elif slave_nature > 14:
                all_girls_list[girl_index]["bonus_fear"] = all_girls_list[girl_index]["aura"]["fear"] *2 + 5
        else:
            all_girls_list[girl_index]["bonus_fear"] = 0
        all_girls_list[girl_index]["obedience"] = (slave_obedience_bonus 
        + all_girls_list[girl_index]["mood"] 
        + all_girls_list[girl_index]["bonus_fear"] 
        + all_girls_list[girl_index]["aura"]["devotion"]*4 
        + all_girls_list[girl_index]["aura"]["taming"] * 2 
        + int((1+all_girls_list[girl_index]["aura"]["despair"]) // 2) 
        + all_girls_list[girl_index]["aura"]["awareness"] 
        + all_girls_list[girl_index]["aura"]["habit"] 
        - all_girls_list[girl_index]["aura"]["spoil"]*2 
        - int(slave_difficulty/2) 
        - slave_nature +100)
        # set obedience to 100 if broken
        if all_girls_list[girl_index]["psy_status"] == "broken":
            all_girls_list[girl_index]["obedience"] = 100
    def slave_mood_giga_calculation():
        def slave_moodlet_update():
            global home_hygiene_value
            girl = all_girls_list[girl_index]
            if girl["attributes"]["beauty"] == 0:
                girl["mood_state"]["bad_mood"]["ugly"]["active"] = True
            else:
                girl["mood_state"]["bad_mood"]["ugly"]["active"] = False
            if home_hygiene_value < 2:
                girl["mood_state"]["bad_mood"]["slave_mess"]["active"] = True
                girl["mood_state"]["bad_mood"]["slave_mess"]["weight"] = 0.5 # I think 1 is too heavy
            else:
                girl["mood_state"]["bad_mood"]["slave_mess"]["active"] = False
            if girl["hygiene"] >= 4:
                girl["mood_state"]["good_mood"]["slave_clean"]["active"] = True
                girl["mood_state"]["bad_mood"]["slave_dirty"]["active"] = False
            elif girl["hygiene"] < 2:
                girl["mood_state"]["good_mood"]["slave_clean"]["active"] = False
                girl["mood_state"]["bad_mood"]["slave_dirty"]["active"] = True
            else:
                girl["mood_state"]["good_mood"]["slave_clean"]["active"] = False
                girl["mood_state"]["bad_mood"]["slave_dirty"]["active"] = False
            if girl["affection_needs"] == 0:
                girl["mood_state"]["bad_mood"]["horny"]["active"] = True
            else:
                girl["mood_state"]["bad_mood"]["horny"]["active"] = False
            if girl["injuries"] > 0:
                girl["mood_state"]["bad_mood"]["wounded"]["active"] = True
                girl["mood_state"]["bad_mood"]["wounded"]["weight"] = 0.2*girl["injuries"]
            else:
                girl["mood_state"]["bad_mood"]["wounded"]["active"] = False
            if girl["ill"] > 0:
                girl["mood_state"]["bad_mood"]["slave_ill"]["active"] = True
                girl["mood_state"]["bad_mood"]["slave_ill"]["weight"] = 0.2*girl["ill"]
            else:
                girl["mood_state"]["bad_mood"]["slave_ill"]["active"] = False
            if girl["aura"]["despair"] > 0:
                girl["mood_state"]["bad_mood"]["angst"]["active"] = True
                girl["mood_state"]["bad_mood"]["angst"]["weight"] = 0.2*girl["aura"]["despair"]
            else:
                girl["mood_state"]["bad_mood"]["angst"]["active"] = False
            if girl["aura"]["fear"] == 0 and girl["aura"]["despair"] == 0:
                girl["mood_state"]["good_mood"]["moral"]["active"] = True
                girl["mood_state"]["good_mood"]["moral"]["weight"] = girl["aura"]["devotion"]*0.2
            else:
                girl["mood_state"]["good_mood"]["moral"]["active"] = False
            if girl["aura"]["devotion"] == 0:
                girl["mood_state"]["bad_mood"]["slave"]["active"] = True
            else:
                girl["mood_state"]["bad_mood"]["slave"]["active"] = False


        def slave_mood_calculation():
            global girl_index, all_girls_list
            all_girls_list[girl_index]["mood"] = 0
            # + clothes mood 
            all_girls_list[girl_index]["mood"] += all_girls_list[girl_index]["worn_mood"]
            # + all temporal mood
            all_girls_list[girl_index]["mood"] += all_girls_list[girl_index]["mood_temporal"]
            # + past mood, a slave that yesterday is depressing, will start more sad that one that was happy yesterday
            # more negative that positive because sadness stick longer that hapiness, like IRL
            if all_girls_list[girl_index]["past_mood"] > 0:
                all_girls_list[girl_index]["mood"] += all_girls_list[girl_index]["past_mood"]/10 # this number is arbitrary and can be balance change
            else:
                all_girls_list[girl_index]["mood"] += all_girls_list[girl_index]["past_mood"]/4 # this number is arbitrary and can be balance change
            for key in dic_slave_mood["good_mood"]:
                if all_girls_list[girl_index]["mood_state"]["good_mood"][key]["active"]:
                    all_girls_list[girl_index]["mood"] += all_girls_list[girl_index]["mood_state"]["good_mood"][key]["weight"]
            for key in dic_slave_mood["bad_mood"]:
                if all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["active"]:
                    all_girls_list[girl_index]["mood"] -= all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["weight"]           
            all_girls_list[girl_index]["mood"] +=  (all_girls_list[girl_index]["aura"]["devotion"] + all_girls_list[girl_index]["attributes"]["endurance"] - 3 - all_girls_list[girl_index]["aura"]["fear"] - all_girls_list[girl_index]["aura"]["spoil"] - all_girls_list[girl_index]["aura"]["despair"]*2 + all_girls_list[girl_index]["hygiene"] - 5 + (home_hygiene_value - 4))/5 
        def slave_mood_adjustment():
            global slave_psy_hardness, girl_index, all_girls_list
            if all_girls_list[girl_index]["mood"] >= 1 and all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"]:
                all_girls_list[girl_index]["mood"] -= 1
                if all_girls_list[girl_index]["mood"] < 1:
                    all_girls_list[girl_index]["mood"] = 1
            if all_girls_list[girl_index]["aura"]["despair"] > all_girls_list[girl_index]["attributes"]["temperament"]:
                if all_girls_list[girl_index]["mood"] > 0:
                    all_girls_list[girl_index]["mood"] = 0
            elif all_girls_list[girl_index]["aura"]["despair"] > 0:
                all_girls_list[girl_index]["mood"] = min(all_girls_list[girl_index]["mood"], (2 - (all_girls_list[girl_index]["aura"]["despair"]/2)))
            elif all_girls_list[girl_index]["obedience"] < slave_psy_hardness:
                if all_girls_list[girl_index]["mood"] > 2:
                    all_girls_list[girl_index]["mood"] = 2
            elif all_girls_list[girl_index]["aura"]["fear"] >= all_girls_list[girl_index]["aura"]["devotion"]:
                if all_girls_list[girl_index]["mood"] > 3:
                    all_girls_list[girl_index]["mood"] = 3
            all_girls_list[girl_index]["mood"] = round(all_girls_list[girl_index]["mood"], 4) # I dont like too much decimals

        def slave_mood_apply():
            global girl_index, all_girls_list
            if all_girls_list[girl_index]["mood"] <= -5:
                all_girls_list[girl_index]["mood_label"] = dic_slave_moodlevel[0]
            elif all_girls_list[girl_index]["mood"] <= -4:
                all_girls_list[girl_index]["mood_label"] = dic_slave_moodlevel[1]
            elif all_girls_list[girl_index]["mood"] <= -3:
                all_girls_list[girl_index]["mood_label"] = dic_slave_moodlevel[2]
            elif all_girls_list[girl_index]["mood"] <= -2:
                all_girls_list[girl_index]["mood_label"] = dic_slave_moodlevel[3]
            elif all_girls_list[girl_index]["mood"] <= -1:
                all_girls_list[girl_index]["mood_label"] = dic_slave_moodlevel[4]
            elif all_girls_list[girl_index]["mood"] < 1:
                all_girls_list[girl_index]["mood_label"] = dic_slave_moodlevel[5]
            elif all_girls_list[girl_index]["mood"] < 2:
                all_girls_list[girl_index]["mood_label"] = dic_slave_moodlevel[6]
            elif all_girls_list[girl_index]["mood"] < 3:
                all_girls_list[girl_index]["mood_label"] = dic_slave_moodlevel[7]
            elif all_girls_list[girl_index]["mood"] < 4:
                all_girls_list[girl_index]["mood_label"] = dic_slave_moodlevel[8]
            elif all_girls_list[girl_index]["mood"] < 5:
                all_girls_list[girl_index]["mood_label"] = dic_slave_moodlevel[9]
            elif all_girls_list[girl_index]["mood"] >= 5:
                all_girls_list[girl_index]["mood_label"] = dic_slave_moodlevel[10]
            if all_girls_list[girl_index]["mood"] >= 5 and all_girls_list[girl_index]["aura"]["devotion"] >= 5:
                all_girls_list[girl_index]["mood_label"] = dic_slave_moodlevel[11]
        if all_girls_list[girl_index]["psy_status"] != "broken": # only calculated if not broken
            slave_moodlet_update()
            slave_mood_calculation()                                       
            slave_mood_adjustment()
            slave_mood_apply()              
        else:
            all_girls_list[girl_index]["mood"] = 0
            all_girls_list[girl_index]["mood_label"] = dic_slave_moodlevel[0]
    def slave_psy_status_calculation():
        global maxmotivation, slave_difficulty, slave_obedience_bonus, slave_psy_hardness
        if all_girls_list[girl_index]["psy_status"] != "broken":
            ### Slaves psy status calculation
            if all_girls_list[girl_index]["psy_status"] == "lachrymose" and all_girls_list[girl_index]["aura"]["devotion"] > 0:
                all_girls_list[girl_index]["psy_status"] = "soft"
            # if mood is positive - better psy status for slaves
            if all_girls_list[girl_index]["mood"] < 0:
                if all_girls_list[girl_index]["aura"]["devotion"] < 2:
                    if all_girls_list[girl_index]["attributes"]["temperament"] >= max(4, maxmotivation):
                        all_girls_list[girl_index]["psy_status"] = "hateful"
                    if all_girls_list[girl_index]["attributes"]["nature"] >= max(4, maxmotivation):
                        all_girls_list[girl_index]["psy_status"] = "resistant"
                    if all_girls_list[girl_index]["attributes"]["pride"] >= max(4, maxmotivation):
                        all_girls_list[girl_index]["psy_status"] = "arrogant"
                else:
                    if all_girls_list[girl_index]["attributes"]["temperament"] >= max(4, maxmotivation):
                        all_girls_list[girl_index]["psy_status"] = "hysteric"
                    if all_girls_list[girl_index]["attributes"]["nature"] >= max(4, maxmotivation):
                        all_girls_list[girl_index]["psy_status"] = "docile"
                    if all_girls_list[girl_index]["attributes"]["pride"] >= max(4, maxmotivation):
                        all_girls_list[girl_index]["psy_status"] = "soft"
            if all_girls_list[girl_index]["aura"]["fear"] == maxmotivation and all_girls_list[girl_index]["aura"]["fear"] > all_girls_list[girl_index]["attributes"]["nature"]:
                all_girls_list[girl_index]["psy_status"] = "frightened"
            elif all_girls_list[girl_index]["mood"] < 2 and all_girls_list[girl_index]["aura"]["despair"] > 1 or all_girls_list[girl_index]["mood"] <= -5:
                all_girls_list[girl_index]["psy_status"] = "depresive"
                if all_girls_list[girl_index]["attributes"]["empathy"] > 3 and all_girls_list[girl_index]["mood"] < 2:
                    all_girls_list[girl_index]["psy_status"] = "lachrymose"
            elif all_girls_list[girl_index]["obedience"] > slave_psy_hardness/2:
                if all_girls_list[girl_index]["aura"]["spoil"] > max(1, all_girls_list[girl_index]["aura"]["fear"], (all_girls_list[girl_index]["aura"]["devotion"]+1)/2):
                    all_girls_list[girl_index]["psy_status"] = "hysteric"
                elif all_girls_list[girl_index]["mood"] >= 0:
                    if maxmotivation != 0:
                        if maxmotivation == all_girls_list[girl_index]["aura"]["fear"]:
                            all_girls_list[girl_index]["psy_status"] = "docile"
                        if maxmotivation == all_girls_list[girl_index]["aura"]["taming"] or all_girls_list[girl_index]["aura"]["devotion"] > 1:
                            all_girls_list[girl_index]["psy_status"] = "obedient"
                        if maxmotivation == all_girls_list[girl_index]["aura"]["devotion"] or all_girls_list[girl_index]["aura"]["devotion"] > 3:
                            all_girls_list[girl_index]["psy_status"] = "servile"
                        if all_girls_list[girl_index]["aura"]["spoil"] >= (all_girls_list[girl_index]["aura"]["devotion"]+1)/2:
                            all_girls_list[girl_index]["psy_status"] = "docile"
                        if maxmotivation == all_girls_list[girl_index]["arousal"] and all_girls_list[girl_index]["aura"]["devotion"] > 0:
                            all_girls_list[girl_index]["psy_status"] = "horny"
    def handle_menu():
        global current_menu, show_main_slave
        # Handle home menu case
        if current_menu == 0:
            show_main_slave = False
            renpy.hide_screen("main_slave_image")
            renpy.hide_screen("screen_attributes_skills_sexual_slave")
            renpy.show_screen("homehome_attributes_menu")
            renpy.call_screen("home_menu")
        else:
            renpy.hide_screen("home_menu")

        # Slave menus
        if current_menu == 1:
            renpy.call_screen("slave_activities_menu")
        elif current_menu == 2:
            renpy.call_screen("slave_assignments_menu")
        elif current_menu == 3:
            renpy.call_screen("domestic_issues_menu")
        elif current_menu == 4:
            renpy.call_screen("cast_spell_menu")
        elif current_menu == 41:
            renpy.call_screen("spellbook_info")
        elif current_menu == 42:
            renpy.call_screen("home_menu_auspex")
        elif current_menu in [100, 101, 102, 103]:
            renpy.hide_screen("sparks_menu")
            renpy.hide_screen("homehome_attributes_menu")
            renpy.show_screen("screen_attributes_skills_sexual_slave")
            screens = {
                100: "slave_rules_menu",
                101: "slave_anatomy_menu",
                102: "slave_equipment_menu",
                103: "slave_aura_menu"
            }
            renpy.call_screen(screens[current_menu])

        # Master menus
        elif current_menu in [200, 201, 202, 203]:
            renpy.hide_screen("sparks_menu")
            renpy.hide_screen("homehome_attributes_menu")
            renpy.show_screen("master_attributes_screen")
            screens = {
                200: "master_storage",
                201: "master_objectives",
                202: "master_equipment_menu",
                203: "master_diary_menu"
            }
            renpy.call_screen(screens[current_menu])
    def hidden_trait_discover_text_display_check():
        global customboxcheck, attribute_checkbox, attributeisphysical
        if customboxcheck:
            renpy.hide_screen("tutorial_description")
            renpy.hide_screen("tutorial_description2")
            renpy.hide_screen("tutorial_descriptionphysical")
            renpy.show_screen("tutorial_attribute")
        if attribute_checkbox:
            renpy.hide_screen("tutorial_attribute")
            if attributeisphysical:
                renpy.show_screen("tutorial_descriptionphysical")
                renpy.hide_screen("tutorial_description")
            else:
                renpy.show_screen("tutorial_description")
                renpy.hide_screen("tutorial_descriptionphysical")
    def master_libido_update():
        global libido_value_4, mood_value_10, strength_value_1, excitement_value, energy_value
        global libido_experience_value_4, master_ill
        if (mood_value_10 > 0 
        and strength_value_1 > 2
        and excitement_value > -5
        and excitement_value < 5
        and energy_value >= 0):
            libido_experience_value_4 += (1 + libido_value_4)/2
        if energy_value < 0:
            libido_experience_value_4 -= 3
        if mood_value_10 < 0:
            libido_experience_value_4 -= 3
        if master_ill > 6:
            libido_experience_value_4 -= 5
        libido_experience_value_4 -= injuries_value_11
        if excitement_value == 5: #TODO need add chimera_gem_on
            libido_experience_value_4 -= 3
    def girl_already_done_check():
        global girl_index
        n = []
        for key in all_girls_list[girl_index]["already_done"]:
            n.append(all_girls_list[girl_index]["already_done"][key])

        all_girls_list[girl_index]["mood_state"]["bad_mood"]["boring"]["weight"] = max(min(max(n)*0.2-0.6, 1), 0)
        all_girls_list[girl_index]["mood_state"]["bad_mood"]["boring"]["active"] = False
        if max(n) >= 3:
            all_girls_list[girl_index]["mood_state"]["bad_mood"]["boring"]["active"] = True
    def girl_already_done_update():
        global girl_index
        a = sorted(all_girls_list[girl_index]["already_done"].items(), key=lambda x: x[1])
        for i in range(5):
            key, value = a[i]
            all_girls_list[girl_index]["already_done"][key] = max(value - 2, 0)
    def all_rise_excitement_update():
        global girl_index
        global excitement_experience_value, libido_value_4, mood_textvalue_10
        excitement_experience_value += libido_value_4*10 + max(0,mood_value_10*10)
        if excitement_value >= 5 and master_equipment["earrings"] != "chimera_earring":
            blazing_counter += 1
        else:
            blazing_counter = 0
        save_girl_index = girl_index
        for girl_index in all_girls_list:
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["lust_driver"]["value"] > 0:
                all_girls_list[girl_index]["arousal_rate"] += (all_girls_list[girl_index]["attributes"]["temperament"] + all_girls_list[girl_index]["attributes"]["empathy"] + all_girls_list[girl_index]["mood"])/2
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["lust_driver"]["value"] < 0:
                all_girls_list[girl_index]["arousal_rate"] -= (all_girls_list[girl_index]["attributes"]["temperament"])/2
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["lust_driver"]["value"] >= 0:
                all_girls_list[girl_index]["arousal_rate"] += all_girls_list[girl_index]["attributes"]["endurance"] + all_girls_list[girl_index]["attributes"]["empathy"] + all_girls_list[girl_index]["mood"] + all_girls_list[girl_index]["aura"]["devotion"]
            all_girls_list[girl_index]["arousal_rate"] -= (6 
            + all_girls_list[girl_index]["aura"]["despair"]
            + ( 5 - all_girls_list[girl_index]["attributes"]["pride"])
            + all_girls_list[girl_index]["aura"]["fear"]
            + all_girls_list[girl_index]["aura"]["spoil"])
        girl_index = save_girl_index
    def slave_daily_bonus_update():
        global girl_index
        girl = all_girls_list[girl_index]
        girl["experience"]["aura"]["devotion"] += girl["daily_bonus"]["devotion"]
        girl["experience"]["aura"]["taming"] += girl["daily_bonus"]["taming"]
        girl["arousal_rate"] += girl["daily_bonus"]["arousal"]
        girl["experience"]["attributes"]["endurance"] += girl["daily_bonus"]["endurance"]
        girl["experience"]["attributes"]["empathy"] += girl["daily_bonus"]["empathy"]
        girl["experience"]["attributes"]["temperament"] += girl["daily_bonus"]["temperament"]
        girl["experience"]["attributes"]["nature"] += girl["daily_bonus"]["nature"]
        girl["experience"]["attributes"]["pride"] += girl["daily_bonus"]["pride"]
    def master_excitement_check():
        global excitement_value, excitement_experience_value
        excitement_experience_value = max(-160,excitement_experience_value)
        excitement_experience_value = min(160,excitement_experience_value)
        a = [(-5,-160),(-4,-80),(-3,-40),(-2,-20),(-1,-10),(0,0),(1,10),(2,20),(3,40),(4,80),(5,160)]
        for i in a:
            if excitement_experience_value >= i[1]:
                excitement_value = i[0]
        
            

                

        
