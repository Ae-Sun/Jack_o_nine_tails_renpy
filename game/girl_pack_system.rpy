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
        renpy.call_screen("msg", msg_text=x)
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
    def equipment_check2():
        #it's a little bit diferent that equipment_check label
        all_girls_list[girl_index]["worn_mood"] = 0
        all_girls_list[girl_index]["style_plus"] = 0
        all_girls_list[girl_index]["exotic_plus"] = 0
        all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = False
        all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = False
        all_girls_list[girl_index]["wig"] = False
        for keys in all_girls_list[girl_index]["learning_bonus"]:
            all_girls_list[girl_index]["learning_bonus"][keys] = 0
        for keys in all_girls_list[girl_index]["daily_bonus"]:
            all_girls_list[girl_index]["daily_bonus"][keys] = 0
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Naked":
            all_girls_list[girl_index]["learning_bonus"]["sex"] += 1 
            all_girls_list[girl_index]["learning_bonus"]["athletics"] += 1 
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["attributes"]["pride"]*3 - 15 
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"] != 0:
                if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"] < 0 and all_girls_list[girl_index]["psy_status"] != "horny":
                    all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"]*2
                elif all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"] > 0:
                    all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"]*2
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["revealed"]:
                    attribute_track_index = "exhibitionism"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"] 
                    dictionary_name = dic_traits_miscellaneous_description
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["revealed"] = True
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Frilly Apron":
            all_girls_list[girl_index]["learning_bonus"]["cooking"] += 2
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["cookingtrait"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Maid Outfit":
            all_girls_list[girl_index]["learning_bonus"]["maid"] += 2
            all_girls_list[girl_index]["style_plus"] += 1
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["maidtrait"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Nurse Outfit":
            all_girls_list[girl_index]["learning_bonus"]["nursing"] += 2
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["nursingtrait"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Athletic Leotard":
            all_girls_list[girl_index]["learning_bonus"]["athletics"] += 2
            all_girls_list[girl_index]["daily_bonus"]["endurance"] += 2
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["athleticstrait"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Chainmail Bikini":
            all_girls_list[girl_index]["learning_bonus"]["athletics"] += 1
            all_girls_list[girl_index]["learning_bonus"]["gladiatrix"] += 3
            all_girls_list[girl_index]["exotic_plus"] += 1
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["gladiatrixtrait"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Sorceress Robes":
            all_girls_list[girl_index]["learning_bonus"]["witchcraft"] += 3
            all_girls_list[girl_index]["learning_bonus"]["alchemy"] += 2
            all_girls_list[girl_index]["style_plus"] -= 1
            all_girls_list[girl_index]["exotic_plus"] += 2               
            if all_girls_list[girl_index]["attributes"]["pride"] <=2:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["witchcrafttrait"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Light Sundress":
            all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
            all_girls_list[girl_index]["style_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Lace Underwear":
            all_girls_list[girl_index]["learning_bonus"]["sex"] += 2
            all_girls_list[girl_index]["style_plus"] += 1            
            if all_girls_list[girl_index]["aura"]["devotion"] > 0 and master_style >= 3:
                all_girls_list[girl_index]["daily_bonus"]["arousal"] += 1
        if all_girls_list[girl_index]["equipment"]["clothes"] == "School Uniform":
            all_girls_list[girl_index]["learning_bonus"]["secretary"] += 2
            all_girls_list[girl_index]["learning_bonus"]["academy"] += 2
            all_girls_list[girl_index]["style_plus"] += 1
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["secretarytrait"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True                     
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Gown":
            all_girls_list[girl_index]["style_plus"] += 2
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Latex Dress":
            all_girls_list[girl_index]["learning_bonus"]["sex"] += 3
            all_girls_list[girl_index]["style_plus"] += 2
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Kimono-Yukata":
            all_girls_list[girl_index]["learning_bonus"]["elocution"] += 3
            all_girls_list[girl_index]["style_plus"] += 2
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["elocutiontrait"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Exotic Outfit":
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["athleticstrait"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True                            
            all_girls_list[girl_index]["learning_bonus"]["dance"] += 3
            all_girls_list[girl_index]["learning_bonus"]["sex"] += 1
            all_girls_list[girl_index]["exotic_plus"] += 3
            all_girls_list[girl_index]["style_plus"] += 2
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Leather Corset":
            all_girls_list[girl_index]["learning_bonus"]["sex"] += 4
            all_girls_list[girl_index]["style_plus"] += 2
            if all_girls_list[girl_index]["aura"]["devotion"] > 0 and master_style >= 3:
                all_girls_list[girl_index]["daily_bonus"]["arousal"] += 2
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Gorgeous Dress":
            all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
            all_girls_list[girl_index]["worn_mood"] -= 5
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Wedding Dress":
            all_girls_list[girl_index]["learning_bonus"]["sex"] += all_girls_list[girl_index]["aura"]["devotion"]
            all_girls_list[girl_index]["style_plus"] += 3
            if all_girls_list[girl_index]["attributes"]["pride"] >=3 and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] <= 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
            if min(all_girls_list[girl_index]["aura"]["devotion"],all_girls_list[girl_index]["mood"],master_style) >=3: 
                all_girls_list[girl_index]["daily_bonus"]["devotion"] += 1
                all_girls_list[girl_index]["daily_bonus"]["arousal"] += 1
                all_girls_list[girl_index]["worn_mood"] += 5
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Cow Gear":
            all_girls_list[girl_index]["learning_bonus"]["cow"] += 2
            if all_girls_list[girl_index]["attributes"]["pride"] < 4:
                all_girls_list[girl_index]["daily_bonus"]["pride"] += 1
            all_girls_list[girl_index]["style_plus"] -= 2
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["cowtrait"]["value"] < 0 and all_girls_list[girl_index]["skills"]["cow"] < 3 and all_girls_list[girl_index]["skills"]["pet"] < 3:
                if all_girls_list[girl_index]["conscience"] and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] > 0 and all_girls_list[girl_index]["obedience"] < 0 and not all_girls_list[girl_index]["beaten_ever"] and not all_girls_list[girl_index]["domini_dictum_ever"]:
                    slave_rebellion_fight = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["cowtrait"]["value"] != 0:
                all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["cowtrait"]["value"] * 3
                if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["cowtrait"]["value"] > 0:
                    all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
                elif all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["cowtrait"]["value"] < 0 and max(all_girls_list[girl_index]["skills"]["cow"],all_girls_list[girl_index]["skills"]["pet"]) < 3:
                    all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
                    all_girls_list[girl_index]["worn_mood"] -= 5
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Petsuit":
            all_girls_list[girl_index]["daily_bonus"]["pride"] += 1
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 2
            all_girls_list[girl_index]["learning_bonus"]["pet"] += 3
            all_girls_list[girl_index]["learning_bonus"]["maid"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["cooking"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["secretary"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["elocution"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["nursing"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["alchemy"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["witchcraft"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["dance"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["gladiatrix"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["music"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["painting"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["pony"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["cow"] -= 10
            all_girls_list[girl_index]["style_plus"] -= 2
            all_girls_list[girl_index]["exotic_plus"] += 1
            if all_girls_list[girl_index]["attributes"]["pride"] < 4 and all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"] <= 0 and all_girls_list[girl_index]["skills"]["pet"] < 3 and all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] <= 0:
                if all_girls_list[girl_index]["conscience"] and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] > 0 and all_girls_list[girl_index]["obedience"] < 0 and not all_girls_list[girl_index]["beaten_ever"] and not all_girls_list[girl_index]["domini_dictum_ever"]:
                    slave_rebellion_fight = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] != 0:
                all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] * 3
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["revealed"]:
                    attribute_track_index = "deprivation_attitude"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] 
                    dictionary_name = dic_traits_miscellaneous_description
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["revealed"] = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] <= 0:
                all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
                all_girls_list[girl_index]["worn_mood"] += -15 + all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"]
                all_girls_list[girl_index]["daily_bonus"]["nature"] -= 1
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] > 0:   
                all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"]                      
        if all_girls_list[girl_index]["equipment"]["clothes"] == "Deprivation Suit":
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 3
            all_girls_list[girl_index]["style_plus"] -= 4
            all_girls_list[girl_index]["exotic_plus"] += 2
            all_girls_list[girl_index]["learning_bonus"]["maid"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["cooking"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["secretary"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["elocution"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["nursing"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["alchemy"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["witchcraft"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["dance"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["gladiatrix"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["music"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["painting"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["pet"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["pony"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["cow"] -= 10
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] <= 0:
                if all_girls_list[girl_index]["conscience"] and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] > 0 and all_girls_list[girl_index]["obedience"] < 0 and not all_girls_list[girl_index]["beaten_ever"] and not all_girls_list[girl_index]["domini_dictum_ever"]:
                    slave_rebellion_fight = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] != 0:
                all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] * 5
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["revealed"]:
                    attribute_track_index = "deprivation_attitude"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] 
                    dictionary_name = dic_traits_miscellaneous_description
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["revealed"] = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] <= 0:
                all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
                all_girls_list[girl_index]["worn_mood"] += -20 + all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] 
                all_girls_list[girl_index]["daily_bonus"]["temperament"] -= 1
        if all_girls_list[girl_index]["equipment"]["hands"] == "Rubber Gloves":
            all_girls_list[girl_index]["learning_bonus"]["nurse"] += 1
            all_girls_list[girl_index]["learning_bonus"]["maid"] += 1
            all_girls_list[girl_index]["style_plus"] -= 2
        if all_girls_list[girl_index]["equipment"]["hands"] == "Lace Gloves":
            all_girls_list[girl_index]["style_plus"] += 2
        if all_girls_list[girl_index]["equipment"]["hands"] == "Leather Gloves":
            all_girls_list[girl_index]["learning_bonus"]["gladiatrix"] += 1
            all_girls_list[girl_index]["learning_bonus"]["alchemy"] += 1
            all_girls_list[girl_index]["style_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["hands"] == "Carbon Fiber Gloves":
            all_girls_list[girl_index]["learning_bonus"]["gladiatrix"] += 2
            all_girls_list[girl_index]["style_plus"] -= 1
        if all_girls_list[girl_index]["equipment"]["hands"] == "Fluffy Paws":
            all_girls_list[girl_index]["learning_bonus"]["pet"] += 1
            all_girls_list[girl_index]["learning_bonus"]["maid"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["cooking"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["secretary"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["elocution"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["nursing"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["alchemy"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["witchcraft"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["dance"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["gladiatrix"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["music"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["painting"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["pony"] -= 10
            all_girls_list[girl_index]["learning_bonus"]["cow"] -= 10
            all_girls_list[girl_index]["style_plus"] -= 1                
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
        if all_girls_list[girl_index]["equipment"]["hands"] == "Pony Harness":
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["learning_bonus"]["pony"] += 4
            all_girls_list[girl_index]["style_plus"] -= 2
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] <= 0:
                if all_girls_list[girl_index]["conscience"] and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] > 0 and all_girls_list[girl_index]["obedience"] < 0 and not all_girls_list[girl_index]["beaten_ever"] and not all_girls_list[girl_index]["domini_dictum_ever"]:
                    slave_rebellion_fight = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] != 0:
                all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] *3
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["revealed"]:
                    attribute_track_index = "ponytrait"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] 
                    dictionary_name = dic_traits_skills_descriptions
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["revealed"] = True
            elif all_girls_list[girl_index]["races_won"] < 4 or all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] <= 0:
                all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
                all_girls_list[girl_index]["worn_mood"] += -2
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] != 0:
                all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"]
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["revealed"]:
                    attribute_track_index = "deprivation_attitude"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] 
                    dictionary_name = dic_traits_miscellaneous_description
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["revealed"] = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"] != 0:
                all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"]
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["revealed"]:
                    attribute_track_index = "exhibitionism"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"] 
                    dictionary_name = dic_traits_miscellaneous_description
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["revealed"] = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"] <= 0:
                all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
        if all_girls_list[girl_index]["equipment"]["hands"] == "Leather Shackles":
            all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] * 3
            all_girls_list[girl_index]["daily_bonus"]["arousal"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"]
            all_girls_list[girl_index]["learning_bonus"]["sex"] +=1
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["style_plus"] -= 1
            
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] < 0:
                if all_girls_list[girl_index]["conscience"] and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] > 0 and all_girls_list[girl_index]["obedience"] < 0 and not all_girls_list[girl_index]["beaten_ever"] and not all_girls_list[girl_index]["domini_dictum_ever"]:
                    slave_rebellion_fight = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] != 0:
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["revealed"]:
                    attribute_track_index = "deprivation_attitude"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] 
                    dictionary_name = dic_traits_miscellaneous_description
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["revealed"] = True         
        if all_girls_list[girl_index]["equipment"]["feet"] == "Leather Shackles":
            all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] * 3
            all_girls_list[girl_index]["daily_bonus"]["arousal"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"]
            all_girls_list[girl_index]["learning_bonus"]["sex"] +=1
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["style_plus"] -= 1
            
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] < 0:
                if all_girls_list[girl_index]["conscience"] and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] > 0 and all_girls_list[girl_index]["obedience"] < 0 and not all_girls_list[girl_index]["beaten_ever"] and not all_girls_list[girl_index]["domini_dictum_ever"]:
                    slave_rebellion_fight = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] != 0:
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["revealed"]:
                    attribute_track_index = "deprivation_attitude"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["value"] 
                    dictionary_name = dic_traits_miscellaneous_description
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["deprivation_attitude"]["revealed"] = True         
        if all_girls_list[girl_index]["equipment"]["feet"] == "Soft Slippers":
            all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
            all_girls_list[girl_index]["style_plus"] -= 1
            all_girls_list[girl_index]["exotic_plus"] -= 1
        if all_girls_list[girl_index]["equipment"]["feet"] == "Pointes":
            if all_girls_list[girl_index]["skills"]["dance"] > 2 or all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["dancetrait"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
                all_girls_list[girl_index]["learning_bonus"]["dance"] += 2
        if all_girls_list[girl_index]["equipment"]["feet"] == "Sneakers":
            all_girls_list[girl_index]["learning_bonus"]["athletics"] += 3
            all_girls_list[girl_index]["learning_bonus"]["dance"] += 1
            all_girls_list[girl_index]["learning_bonus"]["gladiatrix"] += 1
            all_girls_list[girl_index]["style_plus"] -= 1
            all_girls_list[girl_index]["exotic_plus"] -= 1
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["athleticstrait"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
        if all_girls_list[girl_index]["equipment"]["feet"] == "Heels":
            if all_girls_list[girl_index]["skills"]["dance"] < 3:
                all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
                all_girls_list[girl_index]["worn_mood"] -= 3
            all_girls_list[girl_index]["style_plus"] += 2
        if all_girls_list[girl_index]["equipment"]["feet"] == "High Boots":
            all_girls_list[girl_index]["learning_bonus"]["sex"] += 2
            all_girls_list[girl_index]["style_plus"] += 2 
            if all_girls_list[girl_index]["skills"]["dance"] < 3:
                all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
                all_girls_list[girl_index]["worn_mood"] -= 3
            if all_girls_list[girl_index]["attributes"]["temperament"] > 2:
                all_girls_list[girl_index]["daily_bonus"]["temperament"] += 1
        if all_girls_list[girl_index]["equipment"]["feet"] == "Hooved Boots":
            all_girls_list[girl_index]["learning_bonus"]["pony"] += 5
            if all_girls_list[girl_index]["attributes"]["temperament"] > 2:
                all_girls_list[girl_index]["daily_bonus"]["temperament"] += 1
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] != 0:
                all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] * 3
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["revealed"]:
                    attribute_track_index = "ponytrait"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] 
                    dictionary_name = dic_traits_skills_descriptions
                    customboxcheck = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] <= 0 and all_girls_list[girl_index]["races_won"] < 4:
                all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
                all_girls_list[girl_index]["worn_mood"] += -15
        if all_girls_list[girl_index]["equipment"]["ring1"] == "Elegant Ring":
            all_girls_list[girl_index]["style_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["ring1"] == "Gemstone Ring":
            all_girls_list[girl_index]["style_plus"] += 2
        if all_girls_list[girl_index]["equipment"]["ring2"] == "Elegant Ring":
            all_girls_list[girl_index]["style_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["ring2"] == "Gemstone Ring":
            all_girls_list[girl_index]["style_plus"] += 2
        if all_girls_list[girl_index]["equipment"]["earrings"]["type"] == "Small Hoop":
            all_girls_list[girl_index]["style_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["earrings"]["type"] == "Gemstone Stud":
            all_girls_list[girl_index]["style_plus"] += 2
            all_girls_list[girl_index]["exotic_plus"] += 2
        if all_girls_list[girl_index]["equipment"]["earrings"]["type"] == "Thick Steel Ring":
            all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
            all_girls_list[girl_index]["style_plus"] -= 1
            all_girls_list[girl_index]["exotic_plus"] += 2
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["worn_mood"] -= 3
        if all_girls_list[girl_index]["equipment"]["nipples"]["type"] == "Barbell":
            all_girls_list[girl_index]["daily_bonus"]["arousal"] += 1
            all_girls_list[girl_index]["style_plus"] += 1
            all_girls_list[girl_index]["exotic_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["nipples"]["type"] == "Nipple Chain":
            all_girls_list[girl_index]["daily_bonus"]["arousal"] += 2
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["exotic_plus"] += 1
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["value"] != 0:
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["revealed"]:
                    attribute_track_index = "masochism"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["value"] 
                    dictionary_name = dic_traits_miscellaneous_description
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["revealed"] = True
            if all_girls_list[girl_index]["attributes"]["pride"] <= 4 or all_girls_list[girl_index]["arousal"] == 0 and all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["value"] <= 0:
                if all_girls_list[girl_index]["conscience"] and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] > 0 and all_girls_list[girl_index]["obedience"] < 0 and not all_girls_list[girl_index]["beaten_ever"] and not all_girls_list[girl_index]["domini_dictum_ever"]:
                    slave_rebellion_fight = True
            if all_girls_list[girl_index]["arousal"] == 0 and all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["value"] < 0:
                all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
                all_girls_list[girl_index]["worn_mood"] += 3 * all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["value"]
            elif all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
                all_girls_list[girl_index]["worn_mood"] += 3 * all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["value"]
        if all_girls_list[girl_index]["equipment"]["nipples"]["type"] == "Thick Steel Ring":
            all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
            all_girls_list[girl_index]["style_plus"] -= 1
            all_girls_list[girl_index]["exotic_plus"] += 2
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["worn_mood"] -= 3
        if all_girls_list[girl_index]["equipment"]["nipples"]["type"] == "Small Hoop":
            all_girls_list[girl_index]["style_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["tongue"]["type"] == "Barbell":
            all_girls_list[girl_index]["daily_bonus"]["arousal"] += 1
            all_girls_list[girl_index]["style_plus"] += 1
            all_girls_list[girl_index]["exotic_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["tongue"]["type"] == "Thick Steel Ring":
            all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
            all_girls_list[girl_index]["style_plus"] -= 1
            all_girls_list[girl_index]["exotic_plus"] += 2
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["worn_mood"] -= 3
        if all_girls_list[girl_index]["equipment"]["tongue"]["type"] == "Small Hoop":
            all_girls_list[girl_index]["style_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["navel"]["type"] == "Barbell":
            all_girls_list[girl_index]["daily_bonus"]["arousal"] += 1
            all_girls_list[girl_index]["style_plus"] += 1
            all_girls_list[girl_index]["exotic_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["navel"]["type"] == "Thick Steel Ring":
            all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
            all_girls_list[girl_index]["style_plus"] -= 1
            all_girls_list[girl_index]["exotic_plus"] += 2
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["worn_mood"] -= 3
        if all_girls_list[girl_index]["equipment"]["navel"]["type"] == "Small Hoop":
            all_girls_list[girl_index]["style_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["navel"]["type"] == "Gemstone Stud":
            all_girls_list[girl_index]["style_plus"] += 2
            all_girls_list[girl_index]["exotic_plus"] += 2
        if all_girls_list[girl_index]["equipment"]["clitoris"]["type"] == "Barbell":
            all_girls_list[girl_index]["daily_bonus"]["arousal"] += 1
            all_girls_list[girl_index]["style_plus"] += 1
            all_girls_list[girl_index]["exotic_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["clitoris"]["type"] == "Thick Steel Ring":
            all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
            all_girls_list[girl_index]["style_plus"] -= 1
            all_girls_list[girl_index]["exotic_plus"] += 2
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["worn_mood"] -= 3
        if all_girls_list[girl_index]["equipment"]["clitoris"]["type"] == "Small Hoop":
            all_girls_list[girl_index]["style_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["clitoris"]["type"] == "Gemstone Stud":
            all_girls_list[girl_index]["style_plus"] += 2
            all_girls_list[girl_index]["exotic_plus"] += 2
        if all_girls_list[girl_index]["equipment"]["headgear"] == "Headband":
            all_girls_list[girl_index]["wig"] = True
            all_girls_list[girl_index]["learning_bonus"]["cooking"] += 1
        if all_girls_list[girl_index]["equipment"]["headgear"] == "Hijab":
            all_girls_list[girl_index]["learning_bonus"]["maid"] += 1
            all_girls_list[girl_index]["learning_bonus"]["cooking"] += 1
            all_girls_list[girl_index]["style_plus"] -= 1
        if all_girls_list[girl_index]["equipment"]["headgear"] == "Crown of Thorns":
            all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["value"]*3 -3
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 2
            all_girls_list[girl_index]["style_plus"] -= 2
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["value"] <= 0:
                if all_girls_list[girl_index]["conscience"] and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] > 0 and all_girls_list[girl_index]["obedience"] < 0 and not all_girls_list[girl_index]["beaten_ever"] and not all_girls_list[girl_index]["domini_dictum_ever"]:
                    slave_rebellion_fight = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["value"] != 0:
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["revealed"]:
                    attribute_track_index = "masochism"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["value"] 
                    dictionary_name = dic_traits_miscellaneous_description
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["revealed"] = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["masochism"]["value"] != 2:
                all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
        if all_girls_list[girl_index]["equipment"]["headgear"] == "Ornamented Diadem":
            all_girls_list[girl_index]["style_plus"] += 2
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["value"] != 0:
                all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["value"] *3
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["revealed"]:
                    attribute_track_index = "passion_luxury"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["value"] 
                    dictionary_name = dic_traits_miscellaneous_description
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["revealed"] = True
        if all_girls_list[girl_index]["equipment"]["headgear"] == "Hairnet":
            all_girls_list[girl_index]["wig"] = True
            all_girls_list[girl_index]["style_plus"] += 2
        if all_girls_list[girl_index]["equipment"]["headgear"] == "Stylish Glasses":
            all_girls_list[girl_index]["learning_bonus"]["secretary"] += 1
            all_girls_list[girl_index]["style_plus"] += 2 
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["secretarytrait"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
        if all_girls_list[girl_index]["equipment"]["headgear"] == "Cat Ears":
            all_girls_list[girl_index]["style_plus"] -= 1
            all_girls_list[girl_index]["exotic_plus"] += 1
            all_girls_list[girl_index]["learning_bonus"]["pet"] += 1
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"] > 0:
                all_girls_list[girl_index]["mood_state"]["good_mood"]["clothes"]["active"] = True
        if all_girls_list[girl_index]["equipment"]["headgear"] == "Precious Tiara":
            all_girls_list[girl_index]["style_plus"] += 3
            all_girls_list[girl_index]["exotic_plus"] += 1
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["value"] != 0:
                all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["value"] *3
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["revealed"]:
                    attribute_track_index = "passion_luxury"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["value"] 
                    dictionary_name = dic_traits_miscellaneous_description
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["revealed"] = True
        if all_girls_list[girl_index]["equipment"]["headgear"] == "Exotic Wig":
            all_girls_list[girl_index]["wig"] = True
            all_girls_list[girl_index]["style_plus"] += 1
            all_girls_list[girl_index]["exotic_plus"] += 2
        if all_girls_list[girl_index]["equipment"]["headgear"] == "Plumed Bridle":
            all_girls_list[girl_index]["style_plus"] += 1
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["learning_bonus"]["pony"] += 3
            if all_girls_list[girl_index]["attributes"]["pride"] < 4:
                all_girls_list[girl_index]["daily_bonus"]["pride"] += 1
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] <= 0:
                if all_girls_list[girl_index]["conscience"] and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] > 0 and all_girls_list[girl_index]["obedience"] < 0 and not all_girls_list[girl_index]["beaten_ever"] and not all_girls_list[girl_index]["domini_dictum_ever"]:
                    slave_rebellion_fight = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] != 0:
                all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] *3
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["revealed"]:
                    attribute_track_index = "ponytrait"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] 
                    dictionary_name = dic_traits_skills_descriptions
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["revealed"] = True
            elif all_girls_list[girl_index]["races_won"] < 4 or all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] <= 0:
                all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
                all_girls_list[girl_index]["worn_mood"] += -2
        if all_girls_list[girl_index]["equipment"]["neck"] == "Chain with Pendant":
            all_girls_list[girl_index]["style_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["neck"] == "Gemstone Necklace":
            all_girls_list[girl_index]["style_plus"] += 2
        if all_girls_list[girl_index]["equipment"]["neck"] == "Collar and Leash":
            all_girls_list[girl_index]["learning_bonus"]["pet"] += 2
            all_girls_list[girl_index]["style_plus"] -= 1
            if all_girls_list[girl_index]["skills"]["pet"] < 3 and all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"] < 0:
                if all_girls_list[girl_index]["conscience"] and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] > 0 and all_girls_list[girl_index]["obedience"] < 0 and not all_girls_list[girl_index]["beaten_ever"] and not all_girls_list[girl_index]["domini_dictum_ever"]:
                    slave_rebellion_fight = True
            if all_girls_list[girl_index]["skills"]["pet"] > 2 and all_girls_list[girl_index]["attributes"]["pride"] > 2 or all_girls_list[girl_index]["aura"]["devotion"] > 1:
                if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"] > 0:
                    all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"] *3
        if all_girls_list[girl_index]["equipment"]["neck"] == "Leather Collar":
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["learning_bonus"]["pet"] += 1
            all_girls_list[girl_index]["style_plus"] -= 1
            if all_girls_list[girl_index]["conscience"] and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] > 0 and all_girls_list[girl_index]["obedience"] < 0 and not all_girls_list[girl_index]["beaten_ever"] and not all_girls_list[girl_index]["domini_dictum_ever"]:
                slave_rebellion_fight = True
        if all_girls_list[girl_index]["equipment"]["neck"] == "Steel Collar":
            all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 2
            all_girls_list[girl_index]["style_plus"] -= 2
            if all_girls_list[girl_index]["attributes"]["pride"] < 2:
                all_girls_list[girl_index]["daily_bonus"]["pride"] += 1
            if all_girls_list[girl_index]["conscience"] and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] > 0 and all_girls_list[girl_index]["obedience"] < 0 and not all_girls_list[girl_index]["beaten_ever"] and not all_girls_list[girl_index]["domini_dictum_ever"]:
                slave_rebellion_fight = True
        if all_girls_list[girl_index]["equipment"]["neck"] == "Spiked Collar":
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["daily_bonus"]["empathy"] += 1
            all_girls_list[girl_index]["learning_bonus"]["gladiatrix"] += 1
            all_girls_list[girl_index]["style_plus"] -= 1
            if all_girls_list[girl_index]["skills"]["gladiatrix"] < 3 and all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["gladiatrixtrait"]["value"] < 0:
                if all_girls_list[girl_index]["conscience"] and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] > 0 and all_girls_list[girl_index]["obedience"] < 0 and not all_girls_list[girl_index]["beaten_ever"] and not all_girls_list[girl_index]["domini_dictum_ever"]:
                    slave_rebellion_fight = True
            if all_girls_list[girl_index]["skills"]["gladiatrix"] > 2 and all_girls_list[girl_index]["attributes"]["pride"] <3 and all_girls_list[girl_index]["attributes"]["temperament"] > 2:
                all_girls_list[girl_index]["worn_mood"] += 5
            else:
                all_girls_list[girl_index]["worn_mood"] -= 1
                all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
        if all_girls_list[girl_index]["equipment"]["neck"] == "Shock Collar":
            all_girls_list[girl_index]["worn_mood"] -= 1
            all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["style_plus"] += 2
            all_girls_list[girl_index]["exotic_plus"] += 1
        if all_girls_list[girl_index]["equipment"]["neck"] == "Ornamented Collar":
            all_girls_list[girl_index]["daily_bonus"]["taming"] += 1
            all_girls_list[girl_index]["style_plus"] += 2
            all_girls_list[girl_index]["exotic_plus"] += 2
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["value"] != 0:
                all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["value"] *3
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["revealed"]:
                    attribute_track_index = "passion_luxury"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["value"] 
                    dictionary_name = dic_traits_miscellaneous_description
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["passion_luxury"]["revealed"] = True
        if all_girls_list[girl_index]["equipment"]["anus"] == "Anal tail":
            all_girls_list[girl_index]["learning_bonus"]["pet"] += 2
            all_girls_list[girl_index]["learning_bonus"]["pony"] += 1
            all_girls_list[girl_index]["daily_bonus"]["arousal"] += 2
            all_girls_list[girl_index]["style_plus"] -= 2
            if all_girls_list[girl_index]["attributes"]["pride"] < 4:   
                all_girls_list[girl_index]["daily_bonus"]["pride"] += 1
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] <= 0 and all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"] <= 0:
                if all_girls_list[girl_index]["conscience"] and dic_girl_psy_status[all_girls_list[girl_index]["psy_status"]] > 0 and all_girls_list[girl_index]["obedience"] < 0 and not all_girls_list[girl_index]["beaten_ever"] and not all_girls_list[girl_index]["domini_dictum_ever"]:
                    slave_rebellion_fight = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] <= 0 and all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"] <= 0 and all_girls_list[girl_index]["races_won"] <= 7 and all_girls_list[girl_index]["psy_status"] != "horny":
                all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
                all_girls_list[girl_index]["worn_mood"] += -25 + all_girls_list[girl_index]["attributes"]["pride"] * 5
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] != 0:
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["revealed"]:
                    attribute_track_index = "ponytrait"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] 
                    dictionary_name = dic_traits_skills_descriptions
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["revealed"] = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"] != 0:
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["revealed"]:
                    attribute_track_index = "pettrait"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"] 
                    dictionary_name = dic_traits_skills_descriptions
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["revealed"] = True
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] > 0 or all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"] > 0:
                if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] > all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"]:
                    all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["ponytrait"]["value"] *3
                else:
                    all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"] *3
        if all_girls_list[girl_index]["equipment"]["anus"] == "Anal Pear":
            all_girls_list[girl_index]["daily_bonus"]["arousal"] += 1
            all_girls_list[girl_index]["daily_bonus"]["pride"] += 1
            all_girls_list[girl_index]["style_plus"] -= 1            
        if all_girls_list[girl_index]["equipment"]["clothes"] in ["Frilly Apron","Maid Outfit","Athletic Leotard","Chainmail Bikini","Lace Underwear","Latex Dress","Exotic Outfit","Leather Corset"]:
            all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["attributes"]["pride"]*2 - 10
            if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"] != 0:
                if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"] < 0 and all_girls_list[girl_index]["psy_status"] != "horny":
                    all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"]
                    all_girls_list[girl_index]["mood_state"]["bad_mood"]["clothes"]["active"] = True
                elif all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"] > 0:
                    all_girls_list[girl_index]["worn_mood"] += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"]
                if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["revealed"]:
                    attribute_track_index = "exhibitionism"
                    dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["value"] 
                    dictionary_name = dic_traits_miscellaneous_description
                    customboxcheck = True
                    all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["exhibitionism"]["revealed"] = True
                    # show exhibition text -rec3ks
        all_girls_list[girl_index]["worn_mood"] = all_girls_list[girl_index]["worn_mood"]/10           
    #def sex_acceptance_check():
        
    def interaction_willingness_check():
        store.interaction_willingness = all_girls_list[girl_index]["obedience"] + interaction_sex_acceptance + interaction_repulse
        if target_skill != "sex":
            target_skill2 = target_skill + "trait"
            if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["revealed"]:
                store.attribute_track_index = target_skill2
                store.dictionary_track_index = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] 
                store.dictionary_name = dic_traits_skills_descriptions
                all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["revealed"] = True
                renpy.show_screen("tutorial_attribute")
            store.interaction_willingness += all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] * 3
        else:
            if interaction_willingness > 0:
                all_girls_list[girl_index]["daring"] = max(all_girls_list[girl_index]["daring"], interaction_repulse)
                

        #TODO need to code sex part - sex_acceptace_check
    def diligence_check():
        # called from interaction_result after $dyn_repulse_check
        # sets slave_diligence in range [0,5], zero reflects inadequate/lackluster effort, positive reflects praise-worthy effort
        # interaction_repulse can be set by caller in [0,5] range as a malus to overcome (motivation_repulse affects only diligence, not obedience)
        # this function adjusts diligence to account for $target_affinity, if set by caller (affinities have strong influence)
        # this function also imposes a range of [0, diligence] on the sex_quality global (which represents the slave applying skills to improve sex for partner)
        # expects to be called with dynamic $replace($dyn_diligence, 'dyn'+'slave', 'a slave instance variable')
        store.slave_diligence = all_girls_list[girl_index]["mood"] + all_girls_list[girl_index]["aura"]["devotion"] + all_girls_list[girl_index]["aura"]["fear"]*2 - all_girls_list[girl_index]["aura"]["despair"] // 2 - all_girls_list[girl_index]["aura"]["spoil"]
        # Aura -Based MOTIVATION
        # I don't think is needed to enforce the range, make master_style way more useless -rec3ks
        #interaction_dynslave['motivation_repulse'] = max(0, min(5, interaction_dynslave['motivation_repulse'])) &! enforce [0,5] range (default 0)
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
        if interaction_willingness < 0:
            store.slave_diligence += interaction_willingness // 2
        # BONUSES FOR TEACHING ABILITY
        if interaction_teach:
            if interaction_teach_type == "master_teaches_slave":
                store.slave_diligence += max(0, master_tutor - 2)
            # elif interaction_teach_type = "assistant_teaches_slave" and assistant['intellect'] > 3:
            #     store.slave_diligence += (assistant['intellect'] - 3) 
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
        store.slave_diligence = max(store.slave_diligence, 0)





    def girl_skills_rise_check():
        # target_affinity - check if the girl have the trait and reveal if true -rec3ks
        target_skill2 = target_skill + "trait"
        if all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["value"] != 0:
            if not all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"][target_skill2]["revealed"]:
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
            skill_rise = ((max(1,store.tutor_modifier)) * store.slave_diligence) // 4  # need diligence_check TODO NEED TO CHECK WHY IS RASING ONLY 2 TO 2 
            if target_skill == "athletics":
                skill_rise = skill_rise // 2
                if skill_rise > 3:
                    skill_rise = 3
                if all_girls_list[girl_index]["exertion"] >= all_girls_list[girl_index]["attributes"]["endurance"]:
                    skill_rise *= -1 
                all_girls_list[girl_index]["exertion"] += 1
                all_girls_list[girl_index]["experience"]["attributes"]["endurance"] += skill_rise * skill_adv_mul
            else:
                if target_skill != "cow":
                    all_girls_list[girl_index]["experience"]["skills"]["cow"] -= 3
                elif all_girls_list[girl_index]["skills"]["cow"] == 5:
                    skill_rise = max(1, skill_rise - all_girls_list[girl_index]["skills"]["cow"]) #! S+ cow skill greatly impedes training other skills - ImperatorAugustus
                if skill_rise < 1 or slave_diligence == 0: 
                    skill_rise = 1
                all_girls_list[girl_index]["experience"]["skills"][target_skill] += skill_rise * skill_adv_mul
        

                