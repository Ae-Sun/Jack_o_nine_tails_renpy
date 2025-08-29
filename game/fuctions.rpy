init python:
    import os, json, random 

    selected_json_data = None  # This will hold the content of the selected JSON

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
    next_id = 0 # Initialize counter

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
    
    
    #def sex_acceptance_check():
        
    def interaction_willingness1_check():
        global attribute_track_index, dictionary_track_index, dictionary_name
        global dic_traits_skills_descriptions, target_skill, interaction_willingness
        interaction_willingness = all_girls_list[girl_index]["obedience"] + interaction_sex_acceptance + interaction_repulse
        if target_skill != "sex":
            target_skill2 = target_skill + "trait"
            if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["revealed"] and not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] == 0:
                attribute_track_index = target_skill2
                dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] 
                dictionary_name = dic_traits_skills_descriptions
                all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["revealed"] = True
                renpy.show_screen("tutorial_attribute")
            interaction_willingness += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] * 4
        else:
            if interaction_willingness > 0:
                all_girls_list[girl_index]["daring"] = max(all_girls_list[girl_index]["daring"], interaction_repulse)
    

        #TODO need to code sex part - sex_acceptace_check
    def diligence333_check333():
        store.slave_diligence = all_girls_list[girl_index]["mood"] + all_girls_list[girl_index]["aura"]["devotion"] + all_girls_list[girl_index]["aura"]["fear"]*2 - all_girls_list[girl_index]["aura"]["despair"] // 2 - all_girls_list[girl_index]["aura"]["spoil"]
        # Aura -Based MOTIVATION
        # I don't think is needed to enforce the range, make master_style way more useless -rec3ks
        store.slave_diligence -= (1 + motivation_repulse // 2) # ! reduce initial diligence by [0,3] - ImperatorAugustus
        if all_girls_list[girl_index]["aura"]["devotion"] > motivation_repulse:
            store.slave_diligence += 1
        if all_girls_list[girl_index]["aura"]["taming"] > motivation_repulse:
            store.slave_diligence += 1
        if all_girls_list[girl_index]["aura"]["awareness"] > motivation_repulse:
            store.slave_diligence += 1
        store.slave_diligence += all_girls_list[girl_index]["learning_bonus"][target_skill]
        #TODO I Will ignore phobias for now WIP #rec3ks    
        store.slave_diligence += all_girls_list[girl_index]["daily_count"]["punishments"]
        if all_girls_list[girl_index]["energy"] < 0:
            store.slave_diligence += all_girls_list[girl_index]["energy"]*4
        store.slave_diligence -= all_girls_list[girl_index]["attributes"]["pride"] - max(0,all_girls_list[girl_index]["arousal"] -3 )
        if dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] < 0:
            store.slave_diligence += dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]]
        else:
            store.slave_diligence -= dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]]
        if store.interaction_willingness < 0:
            store.slave_diligence += store.interaction_willingness // 2
        # BONUSES FOR TEACHING ABILITY
        if interaction_teach:
            if interaction_teach_type == "master_teaches_slave":
                store.slave_diligence += max(0, master_tutor - 2)
            # elif interaction_teach_type = "assistant_teaches_slave" and assistant['intellect'] > 3:
            #     store.slave_diligence += (assistant['intellect'] - 3) 
            #TODO SKIPPED ASSISTANT CODE
            elif interaction_teach_type == "school_class":
                store.slave_diligence += 2
            elif interaction_teach_type == 'coach_teaches_slave':
                store.slave_diligence += 5
        # NORMAL DIFFICULTY OVERRIDING, I'm going to do something eazier, because I believe the original code is just complicating things -rec3ks
        if dic_custom_start_difficulty_selection_index_index == 0:
            store.slave_diligence += 2
        elif dic_custom_start_difficulty_selection_index_index == 1:
            store.slave_diligence += 1
        elif dic_custom_start_difficulty_selection_index_index == 2:
            store.slave_diligence += 0
        # SPECIAL CASES
        if domini_dictum_active and interaction_willingness < 0 or all_girls_list[girl_index]["psy_status"] == "broken":
            store.slave_diligence = 1
        # I will just lower capping diligence, because high capping is just more grid and less fun - rec3ks
        if store.target_skill != "sex":
            target_skill2 = store.target_skill + "trait"
            store.slave_diligence += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] * 5
        store.slave_diligence = max(store.slave_diligence, 1) # i think 0 is too heavy for the game -rec3ks





    def girl_skills_rise_checkcheck():
        target_skill2 = store.target_skill + "trait"
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
        skill_rise = ((max(1,store.tutor_modifier)) * store.slave_diligence) / 4    # need diligence_check TODO NEED TO CHECK WHY IS RASING ONLY 2 TO 2 
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
            store.house_items += storage["house"]["artistic_material"][values]
        for values in storage["house"]["sex_items"]:
            store.house_items += storage["house"]["sex_items"][values]

    def display_pic():
        # i just realice there's something call x_general.webp TODO need update the function to incluin it
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
                        if dic_girl_choosing_image_condition_short[store.choosing_image_condition] + "_" + x + "_" + y + "_" + z in f
                    ]
                    return "girls/normal_scenes/" + random.choice(rest_girl)
            else:
                return "WIP "
        return choose_image()
    def all_hygiene_calculation():
        # Define hygiene thresholds
        hygiene_thresholds = [(80, 0), (60, 1), (40, 2), (20, 3), (10, 4), (0, 5)]

        def calculate_hygiene(value):
            """Return hygiene level based on thresholds."""
            for threshold, hygiene_level in hygiene_thresholds:
                if value >= threshold:
                    return hygiene_level
            return 5  # default if none matched

        # Update home hygiene
        store.home_hygiene_value = calculate_hygiene(store.home_mess_value)
        # Update home condition
        store.home_condition = dic_home_condition[store.home_hygiene_value]
        
        # Update each girl's hygiene
        for girl_index in all_girls_list:
            all_girls_list[girl_index]["hygiene"] = calculate_hygiene(all_girls_list[girl_index]["hygiene_rate"])
        # Update master hygiene
        store.hygiene_value_9 = calculate_hygiene(store.hygiene_experience_value_9)
    import random

    def auto_cook_meal():
        global already_prepared, already_ate, food_meat_info, home_mess_value
        global cryostore_ingredients_max
        global all_girls_list, dic_foods_list, storage, dic_hygiene_value_rate
        global girl_index, target_skill, tutor_modifier

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
                            if food_meat_info["quality"] < n + 1:
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

                if girl["energy"] > 0:
                    girl["energy"] -= 2
                else:
                    girl["yesterday_exhaustion"] += 2
    def master_cook_meal():
        global already_prepared, already_ate, food_meat_info, home_mess_value
        global cryostore_ingredients_max
        global dic_foods_list, storage, dic_hygiene_value_rate
        global target_skill, hygiene_experience_value_9, energy_value
        global personality_value_2, stewardship_value_13, stewardship_experience_value_13
        global skill_adv_mul
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
                        if food_meat_info["quality"] < n + 1:
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
            # gain bad moodlet if bad at cooking
            #TODO
            master_mood_state["bad_mood"]["neg_cook"]["duration"] = max(0, 3 + personality_value_2 - stewardship_value_13)
            if master_mood_state["bad_mood"]["neg_cook"]["duration"] > 0:
                master_mood_state["bad_mood"]["neg_cook"]["active"] = True
            else:
                master_mood_state["bad_mood"]["neg_cook"]["active"] = False

            # Hygiene and energy changes
            home_mess_value += dic_hygiene_value_rate["cook"]
            hygiene_experience_value_9 += dic_hygiene_value_rate["cook"]
            if energy_value > 0:
                energy_value -= 2
            else:
                yesterday_exhaustion += 2
    def auto_maid():
        global home_hygiene_value, home_mess_value
        if home_hygiene_value >= 4:
            return
        girl = all_girls_list[girl_index]
        target_skill = "maid"
        # Required obedience
        required_obedience = (
            -5 
            + girl["attributes"]["endurance"] // 2 - 1
            + girl["attributes"]["intelligence"] // 2 - 1
            + girl["attributes"]["pride"] // 2 - 2
            - girl["attributes"]["nature"] // 3
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

            if girl["energy"] > 0:
                girl["energy"] -= 2
            else:
                girl["yesterday_exhaustion"] += 2
            girl["hygiene_rate"] += dic_hygiene_value_rate["maid"]
        