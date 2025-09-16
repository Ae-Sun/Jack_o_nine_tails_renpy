init python:
    class night_rules_mini_fuctions:
        def sleep_text(girl):
            return girl["name"] + " " + dic_idle[random.randint(0, 4)]
        def sleep_room(girl):
            return dic_slave_room_to_text[girl["sleep_room"]]
        def cook_text(girl):
            return dic_cook[food_meat_info["quality"]]
        def cook_room(girl):
            return "Kitchen"
        def cook_extra():
            return {"display_meat": True}
        def maid_text(girl):
            return dic_maid[girl["maid_slave_skill_performance"]]
        def maid_room(girl):
            return "Hall"
        def bath_text(girl):
            return dic_bath_master[2]
        def bath_room(girl):
            return "Bath"
        def bath_self_text(girl):
            return bathing_slave_alone[girl["psy_status"]]
        def bath_self_room(girl):
            return "Bath"
        def alarm_text(girl):
            return girl["rules_explain"]["behave_alarm"]
        def alarm_room(girl):
            return "Master bedroom"
        def alarm_extra():
            return {"sex_picture": True}
        def masturbation_text(girl):
            return girl["rules_explain"]["no_masturbation"]
        def masturbation_extra():
            return {"sex_picture": True}
        def masturbation_room(girl):
            return "Slave bedroom"
        def deny_orgasm_text(girl):
            return girl["rules_explain"]["deny_orgasm"]
        def deny_orgasm_extra():
            return {"sex_picture": True}
        def deny_orgasm_room(girl):
            return "Slave bedroom"


    class rules_fuctions():
        # ACT AS COOK
        def act_as_cook_condition(girl):
            return girl["rules"]["act_as_cook"]

        def act_as_cook_extra():
            return home_estate["kitchen"]["storage_capacity"] == 0


        # ACT AS MAID
        def act_as_maid_condition(girl):
            return girl["rules"]["act_as_maid"]

        # BATH SLAVE
        def bath_slave_condition(girl):
            return girl["rules"]["bath_slave"]

        def bath_slave_extra():
            return home_estate["bathroom"]["type"] == ""

        # BEHAVE ALARM
        def behave_alarm_condition(girl):
            return girl["rules"]["behave_alarm"]


        # BEHAVE HUMILITY
        def behave_humility_condition(girl):
            return girl["rules"]["behave_humility"]

        # BEHAVE PET
        def behave_pet_condition(girl):
            return girl["rules"]["behave_pet"]


        # BEHAVE SILENCE
        def behave_silence_condition(girl):
            return girl["rules"]["behave_silence"]


        # BEHAVE TOILET
        def behave_toilet_condition(girl):
            return girl["rules"]["behave_toilet"]


        # BEHAVE URINAL
        def behave_urinal_condition(girl):
            return girl["rules"]["behave_urinal"]


        # DENY ORGASM
        def deny_orgasm_condition(girl):
            return girl["rules"]["deny_orgasm"]


        # DENY TOILETING
        def deny_toileting_condition(girl):
            return girl["rules"]["deny_toileting"]

        # MILK THE FIEND
        def milk_the_fiend_condition(girl):
            return girl["rules"]["milk_the_fiend"]

        def milk_the_fiend_extra():
            return not tentacle["active"]

        # NO MASTURBATION
        def no_masturbation_condition(girl):
            return girl["rules"]["no_masturbation"] 

        # USE VAGINAL BEADS
        def use_vaginal_beads_condition(girl):
            return girl["rules"]["use_vaginal_beads"]



        # ENFORCE RULES
        def enforce_rules_condition(girl):
            return girl["rules"]["enforce_rules"]
    class night_rules_fuctions():
        
        def auto_slave_cook_meal():
            global already_prepared, already_ate, food_meat_info, home_mess_value
            global all_girls_list, dic_foods_list, storage, dic_hygiene_value_rate
            global girl_index, target_skill, tutor_modifier
            girl = all_girls_list[girl_index]
            if home_estate["kitchen"]["storage_capacity"] <= 0:
                return
            if not girl["rules"]["act_as_cook"]:
                return
            
            target_skill = "cooking"
            required_obedience = (
                -6 
                - girl["attributes"]["pride"] // 2 + 2
                + girl["attributes"]["nature"] // 3 
                + girl["attributes"]["intelligence"] // 3
            )

            if (not already_prepared
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
                                    if dic_improvement_rooms["kitchen"][home_estate["kitchen"]["type"]]["modifier"] >= n + 1:
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

                                        # Check sub-par diligence
                                        if food_meat_info["quality"] < slave_skill: 
                                            tutor_modifier -= 5
                                else:
                                    return
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
                    interaction_willingness_check()
                    diligence333_check333()
                    girl_skills_rise_checkcheck()
                    target_skill = ""
                    girl["already_done"]["Servant"] += 1 #must go last
            else:
                girl["rules_broken"]["act_as_cook"] = True
                girl["rules_explain"]["act_as_cook"] = f"{girl["name"]} is disobedient and doesn't want to cook."
        def auto_slave_maid():  
            global home_hygiene_value, home_mess_value, target_skill
            girl = all_girls_list[girl_index]
            if home_hygiene_value >= 4:
                return
            if not girl["rules"]["act_as_maid"]:
                return
            target_skill = "maid"
            required_obedience = (
                -5 
                + girl["attributes"]["endurance"] // 2 - 1
                + girl["attributes"]["intelligence"] // 2 - 1
                - girl["attributes"]["pride"] // 2 + 2
                + girl["attributes"]["nature"] // 3
                + girl["attributes"]["intelligence"] // 2 - 1
            )

            if (girl["energy"] > 0
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
                interaction_willingness_check()
                diligence333_check333()
                girl_skills_rise_checkcheck()
                target_skill = ""
                girl["already_done"]["Servant"] += 1 #must go last
            else:
                target_skill = ""
                girl["rules_broken"]["act_as_maid"] = True 
                girl["rules_explain"]["act_as_maid"] = f"{girl["name"]} is disobedient and doesn't want to clean."
        def auto_bath_slave_help_master():
            global hygiene_value_9, shameful, interaction_repulse_difficulty
            global interaction_willingness, libido_value_4, hygiene_experience_value_9
            global girl_index, mood_value_10, home_mess_value, already_bath
            global did_bath_yesterday, target_skill, target_skill_sexual
            target_skill = "sex"
            target_skill_sexual = ["petting","rubbing"]

            if home_estate["bathroom"]["type"] == "":
                return
            if hygiene_value_9 > 4 or already_bath:
                return

            girl = all_girls_list[girl_index]
            if girl["rules"]["bath_slave"] and girl["energy"] > -1:
                if girl["aura"]["devotion"] == 0:
                    shameful = True
                interaction_repulse_difficulty = 0
                interaction_willingness_check()
                target_skill = ""
                if interaction_willingness < 0:
                    girl["rules_broken"]["bath_slave"] = True
                    girl["rules_explain"]["bath_slave"] = f"{girl["name"]} is disobedient and doesn't want to bath master."
                else:
                    girl["arousal_rate"] -= libido_value_4
                    did_bath_yesterday = True
                    master_mood_state["good_mood"]["pos_self_clean"]["active"] = True
                    mood_value_10 += (min(girl["sex_experience"]["petting"]["petting"], girl["sex_experience"]["oral_pleasure"]["oral_pleasure"])) / 10 
                    night_rules_fuctions.slave_bath_alone()
                    home_mess_value += 3
                    girl["slave_auto_bath"] = True
                    already_bath = True
                    hygiene_value_9 = 5 #this is necessary since hygiene update check is made only on home screen 
                    hygiene_experience_value_9 = 0 
        def slave_bath_alone():
            global girl_index, home_mess_value
            if home_estate["bathroom"]["type"] == "":
                return
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
            if home_estate["bathroom"]["type"] == "":
                return
            if girl["energy"] < 0 or girl["hygiene"] > 2 or girl["already_bath"]:
                return
            home_mess_value += 3
            slave_bath_alone()
            girl["slave_auto_bath_self"] = True
        def auto_alarm():
            global girl_index, stimulating, interaction_willingness
            global damage, brusing, excitement_value, penetration_value_23
            global target_skill, target_skill_sexual, interaction_repulse_difficulty
            girl = all_girls_list[girl_index]
            if not girl["rules"]["behave_alarm"]:
                return
            interaction_repulse_difficulty = 6
            target_skill = "sex"
            target_skill_sexual = ["oral_pleasure","blowjob"]

            stimulating = True
            interaction_willingness_check()
            if interaction_willingness < 0:
                # if girl["rules"]["enforce_rules"]: #and assistant TODO
                #     girl["mood_state"]["bad_mood"]["rules"]["active"] = True
                #     girl["num_rules_wanttobreak"] += 1
                #     # lack assistant code
                #     girl["rules_explain"]["behave_alarm"] += dic_girl_rules_special_text["behave_alarm"]["assistant_pass"]
                #     damage = 3
                #     brusing = 1
                #     slave_damage_calculation()
                #     girl["experience"]["aura"]["despair"] += girl["attributes"]["empathy"]*2
                # else:
                #     girl["rules_broken"]["behave_alarm"] = True
                #     #lack assistant code 
                #     girl["rules_explain"]["behave_alarm"] += dic_girl_rules_special_text["behave_alarm"]["assistant_fail"]P
                girl["rules_broken"]["behave_alarm"] = True
                girl["rules_explain"]["behave_alarm"] += "[all_girls_list[girl_index]['name']] doesn't enters your room in the morning."
                return
            else:
                girl["rules_explain"]["behave_alarm"] += "[all_girls_list[girl_index]['name']] enters your room in the morning and wakes you up with a blowjob."
            if not girl["rules_broken"]["behave_alarm"]:
                diligence333_check333()
                girl_skills_rise_checkcheck()
                
                girl["slave_auto_alarm"] = True
                a = (20
                + girl["attributes"]["temperament"] 
                + (5 - girl["attributes"]["pride"])
                + girl["attributes"]["nature"]
                + girl["aura"]["despair"]
                - girl["aura"]["devotion"] * 4
                - girl["sex_experience"]["oral_pleasure"]["blowjob"] * 2
                - girl["aura"]["taming"]
                - girl["aura"]["habit"]
                - girl["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["lust_driver"]["value"]*3
                - girl["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["sexual_openness"]["value"]*3)/10 # TODO I didn't add meekness, I not sure if add submissive/dominant as trait
                girl["mood"] -= a # look alot but this is taking in considerantion the 80 - 90% new day mood reduction. (Tested with the original game, pretty close)
                b = max(0, min(excitement_value + 1, girl["sex_experience"]["oral_pleasure"]["blowjob"] - penetration_value_23 // 2))
                if interaction_willingness < 0 or a > 0: #slave who is not willing but actually like it , will do it anyways
                    if b < 1:
                        girl["rules_explain"]["behave_alarm"] += dic_girl_rules_special_text["behave_alarm"]["poor_job"]
                    else:
                        girl["rules_explain"]["behave_alarm"] += dic_girl_rules_special_text["behave_alarm"]["disgust"]
                elif b > 0:
                    girl["rules_explain"]["behave_alarm"] += dic_girl_rules_special_text["behave_alarm"]["good_job"]
                elif excitement_value < -2:
                    girl["rules_explain"]["behave_alarm"] += dic_girl_rules_special_text["behave_alarm"]["not_enough_excitement"]
                else:
                    girl["rules_explain"]["behave_alarm"] += dic_girl_rules_special_text["behave_alarm"]["almost_enough_excitement"]
        def auto_slave_humility():
            global girl_index
            girl = all_girls_list[girl_index]
            if not girl["rules"]["behave_humility"]:
                return
            if girl["obedience"] < 1 + dic_girl_psy_status[girl["psy_status"]] - girl["aura"]["fear"]:
                if girl["rules"]["enforce_rules"] and girl["equipment"]["neck"] == "Shock Collar":
                    girl["mood_state"]["bad_mood"]["rules"]["active"] = True
                    girl["num_rules_wanttobreak"] += 1
                    girl["rules_explain"]["behave_humility"] += f"{all_girls_list[girl_index]['name']} calls you 'Master' as her collar inexorably enforces."
                else:
                    girl["rules_broken"]["behave_humility"] = True
                    girl["rules_explain"]["behave_humility"] += f"{all_girls_list[girl_index]['name']} refuses to call you 'Master'."
            else:
                girl["rules_explain"]["behave_humility"] += f"{all_girls_list[girl_index]['name']} calls you 'Master'."
            if not girl["rules_broken"]["behave_humility"]:
                a = girl["attributes"]["nature"] + girl["attributes"]["pride"] - girl["aura"]["devotion"]
                girl["mood"] -= a
                if a > 0 :
                    girl["rules_explain"]["behave_humility"] += " But she is clearly too willful or proud to enjoy it."
                else:
                    girl["rules_explain"]["behave_humility"] += " And she seems to derive some satisfaction from it."
        def auto_slave_pet():
            global girl_index, domini_dictum_active
            girl = all_girls_list[girl_index]
            if not girl["rules"]["behave_pet"]:
                return
            if girl["obedience"] < 0 - 5*girl["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"] + dic_girl_psy_status[girl["psy_status"]]:
                if girl["rules"]["enforce_rules"] and girl["equipment"]["clothes"] == "Petsuit":
                    girl["mood_state"]["bad_mood"]["rules"]["active"] = True
                    girl["num_rules_wanttobreak"] += 1
                    girl["rules_explain"]["behave_pet"] += f"{all_girls_list[girl_index]['name']} cannot break out of her pet suit, maintaining her on all fours all day long. "
                else:
                    girl["rules_broken"]["behave_pet"] = True
                    girl["rules_explain"]["behave_pet"] += f"{all_girls_list[girl_index]['name']} refuses to behave like a pet."
            else:
                girl["rules_explain"]["behave_pet"] += f"{all_girls_list[girl_index]['name']} is a good pet."
            if not girl["rules_broken"]["behave_pet"]:
                a = girl["attributes"]["nature"] + girl["attributes"]["pride"] - girl["aura"]["devotion"] - girl["traits"]["traits_hidden"]["traits_skills(1/8)"]["pettrait"]["value"]*4
                girl["mood"] -= a
                if a > 0 :
                    girl["rules_explain"]["behave_pet"] += " She seems to resent this."
                else:
                    girl["rules_explain"]["behave_pet"] += " She seems to enjoy it."
        def auto_slave_silence():
            global girl_index
            girl = all_girls_list[girl_index]
            if not girl["rules"]["behave_silence"]:
                return
            if girl["obedience"] < girl["attributes"]["temperament"] + dic_girl_psy_status[girl["psy_status"]]:
                if girl["rules"]["enforce_rules"] and storage["house"]["sex_items"]["Reliable Gag"] > 0:
                    girl["mood_state"]["bad_mood"]["rules"]["active"] = True
                    girl["num_rules_wanttobreak"] += 1
                    girl["rules_explain"]["behave_silence"] += f"{all_girls_list[girl_index]['name']} regulary moans behind her gag. "
                else:
                    girl["rules_broken"]["behave_silence"] = True
                    girl["rules_explain"]["behave_silence"] += f"{all_girls_list[girl_index]['name']} speaks as if she was allowed to."
            else:
                girl["rules_explain"]["behave_silence"] += f"{all_girls_list[girl_index]['name']} remains silent unless you ask her a question."
            if not girl["rules_broken"]["behave_silence"]:
                a = girl["attributes"]["temperament"] - girl["aura"]["devotion"]
                girl["mood"] -= a
                if a > 0 :
                    girl["rules_explain"]["behave_silence"] += " She is clearly unhappy with this suppression of her temperament."
                else:
                    girl["rules_explain"]["behave_silence"] += " She seems happy to attend to you without words."
        def auto_slave_behave_toilet():
            global girl_index, stimulating, disgusting, interaction_repulse_difficulty
            global interaction_willingness
            girl = all_girls_list[girl_index]
            if not girl["rules"]["behave_toilet"]:
                return
            stimulating = 1
            disgusting = 1
            interaction_repulse_difficulty = 26
            interaction_willingness_check()
            if interaction_willingness < 0:
                if girl["rules"]["enforce_rules"] and storage["house"]["sex_items"]["Toilet Seat"] > 0:
                    girl["mood_state"]["bad_mood"]["rules"]["active"] = True
                    girl["num_rules_wanttobreak"] += 1
                    girl["rules_explain"]["behave_toilet"] += f"{all_girls_list[girl_index]['name']} would keep her mouth sealed or run away if not for the gag that force-spreads her lips and the toilet rack to which she is steadily tied."
                    girl["experience"]["aura"]["despair"] -= interaction_willingness
                else:
                    girl["rules_broken"]["behave_toilet"] = True
                    girl["rules_explain"]["behave_toilet"] += f"{all_girls_list[girl_index]['name']} refuses to take your shit. Using a special toilet seat could solve the problem."
            else:
                girl["rules_explain"]["behave_toilet"] += f"{all_girls_list[girl_index]['name']} lies down and opens her mouth whenever you mention your need."
            if girl["rules_broken"]["behave_toilet"]:
                a = 6 + girl["attributes"]["nature"] + girl["attributes"]["pride"] - girl["aura"]["devotion"] - girl["sex_experience"]["fetishism"]["scat"]
                girl["mood"] -= a
                if a > 0 :
                    girl["rules_explain"]["behave_toilet"] += " Being befouled with your waste seems to upset her"
                else:
                    girl["rules_explain"]["behave_toilet"] += " She seems happy to receive your waste."
        def auto_slave_behave_urinal():
            global girl_index, stimulating, disgusting, interaction_repulse_difficulty
            global interaction_willingness
            girl = all_girls_list[girl_index]
            if not girl["rules"]["behave_urinal"]:
                return
            stimulating = 1
            disgusting = 1
            interaction_repulse_difficulty = 18
            interaction_willingness_check()
            if interaction_willingness < 0:
                if girl["rules"]["enforce_rules"] and storage["house"]["sex_items"]["Urinal Rack"] > 0:
                    girl["mood_state"]["bad_mood"]["rules"]["active"] = True
                    girl["num_rules_wanttobreak"] += 1
                    girl["rules_explain"]["behave_toilet"] += f"{all_girls_list[girl_index]['name']} rwould flee if not restrained on the urinal rack."
                    girl["experience"]["aura"]["despair"] -= interaction_willingness
                else:
                    girl["rules_broken"]["behave_toilet"] = True
                    girl["rules_explain"]["behave_toilet"] += f"{all_girls_list[girl_index]['name']} refuses to take your urine. Tying her with a urinal rack could solve the problem."
            else:
                girl["rules_explain"]["behave_toilet"] += f"{all_girls_list[girl_index]['name']} kneels and opens her mouth whenever you mention your need."
            if not girl["rules_broken"]["behave_toilet"]:
                a =  3 + girl["attributes"]["nature"] + girl["attributes"]["pride"] - girl["aura"]["devotion"] - girl["sex_experience"]["fetishism"]["golden_shower"]
                girl["mood"] -= a
                if a > 0 :
                    girl["rules_explain"]["behave_toilet"] += " Being befouled with your urine seems to upset her."
                else:
                    girl["rules_explain"]["behave_toilet"] += " She seems happy to receive your urine."
        def auto_slave_masturbation():
            global girl_index
            girl = all_girls_list[girl_index]
            if (girl["arousal"] > girl["attributes"]["pride"] 
            and girl["arousal"] > 2 
            and girl["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["lust_driver"]["value"] >= 0):
                if girl["rules"]["no_masturbation"]:
                    if girl["rules"]["enforce_rules"] and storage["house"]["sex_items"]["Chastity Belt"] > 0:
                        girl["mood_state"]["bad_mood"]["rules"]["active"] = True
                        girl["num_rules_wanttobreak"] += 1
                        girl["rules_explain"]["no_masturbation"] += f"{all_girls_list[girl_index]['name']} often tugs and paws at her chastity belt when she thinks you are not paying attention. It seems she desperately wants to touch what no longer belongs to her. "
                        girl["slave_auto_masturbation"] = False
                    elif girl["aura"]["taming"] > girl["arousal"] or girl["obedience"] > girl["arousal"]*3 or girl["aura"]["devotion"] >= girl["arousal"]:
                        girl["experience"]["aura"]["taming"] += 1
                        girl["slave_auto_masturbation"] = False
                    else:
                        girl["slave_auto_masturbation"] = True
                        girl["rules_broken"]["no_masturbation"] = True
                        girl["rules_explain"]["no_masturbation"] += f"{all_girls_list[girl_index]['name']} masturbates when she thinks you are not paying attention."
                else:
                    girl["slave_auto_masturbation"] = True

        def auto_slave_deny_orgasm():
            global girl_index, target_skill, target_skill_sexual
            girl = all_girls_list[girl_index]
            night_rules_fuctions.auto_slave_masturbation()
            if girl["slave_auto_masturbation"]:
                target_skill = "sex"
                target_skill_sexual = ["demostration","masturbation"]
                interaction_willingness_check()
                diligence333_check333()
                girl_skills_rise_checkcheck()
                girl["slave_deny_orgasm"] = True 
                if not girl["rules"]["deny_orgasm"]:
                    girl["rules_explain"]["deny_orgasm"] += f" You caught your slave during masturbation, but she does not stop it. Looking into your eyes, {all_girls_list[girl_index]['name']} fingers more fiercely, her movements sharp and jittery, and then she throws her head back and writhes in the orgasmic throes, uttering moans of pleasure."
                    girl["mood"] += girl["arousal"]
                    girl["arousal_rate"] -= (girl["sex_experience"]["demostration"]["masturbation"] + girl["arousal"])*3
                    girl["mood_state"]["good_mood"]["orgasm"]["active"] = True
                    girl["mood_state"]["good_mood"]["orgasm"]["duration"] = 2
                else:
                    if girl["arousal"] > girl["obedience"]:
                        girl["rules_explain"]["deny_orgasm"] += f" You caught your slave during masturbation, but she does not stop it. You let her continue, recalling however, that she cannot cum. Nevertheless, {all_girls_list[girl_index]['name']} can't or doesn't want to stop in time, and she can not hide her moan of orgasm. Well, you have to punish her now…"
                        girl["rules_broken"]["deny_orgasm"] = True
                        girl["arousal_rate"] -= (girl["sex_experience"]["demostration"]["masturbation"] + girl["arousal"])*3
                        girl["mood_state"]["good_mood"]["orgasm"]["active"] = True
                        girl["mood_state"]["good_mood"]["orgasm"]["duration"] = 2
                    else:
                        girl["rules_explain"]["deny_orgasm"] += f"  You caught your slave during masturbation, but she does not stop it. You let her continue, recalling however, that she cannot cum. Obeying your will {all_girls_list[girl_index]['name']} does not bring herself to climax, pausing at the end. Poor thing will exhaust herself…"
                        girl["arousal_rate"] += girl["sex_experience"]["demostration"]["masturbation"] + girl["arousal"]
                        girl["experience"]["aura"]["habit"] += 1
        def auto_slave_deny_toileting():
            global girl_index, master_supermacy
            girl = all_girls_list[girl_index]
            if not girl["rules"]["deny_toileting"]:
                return
            if girl["obedience"] < girl["attributes"]["nature"] + girl["attributes"]["pride"]//2 - (master_supermacy- girl["supermacy"])  + dic_girl_psy_status[girl["psy_status"]]:
                if girl["rules"]["enforce_rules"] and girl["equipment"]["anus"] == "Anal Pear":
                    girl["mood_state"]["bad_mood"]["rules"]["active"] = True
                    girl["num_rules_wanttobreak"] += 1
                    girl["rules_explain"]["deny_toileting"] += f"{all_girls_list[girl_index]['name']} regularly tries to remove her anal plug, unsuccessfully. "
                else:
                    girl["rules_broken"]["deny_toileting"] = True
                    girl["rules_explain"]["deny_toileting"] += f"{all_girls_list[girl_index]['name']} uses the toilet as if it was allowed. You recall one of the slaver maxims: an anal pear each day keeps the shitting at bay."
            else:
                girl["rules_explain"]["deny_toileting"] += f"{all_girls_list[girl_index]['name']} refrains from using the toilet unsupervised."
            if not girl["rules_broken"]["deny_toileting"]:
                a = girl["attributes"]["nature"] - girl["aura"]["devotion"]
                girl["mood"] -= a
                if a > 0 :
                    girl["rules_explain"]["deny_toileting"] += " She seems resentful."
                else:
                    girl["rules_explain"]["deny_toileting"] += " She seems pleased to have more time with you."
        #def auto_slave_tentacle(): #TODO CODE SKIPPED 
        def auto_slave_use_vaginal_beads():
            global girl_index
            girl = all_girls_list[girl_index]
            if not girl["rules"]["use_vaginal_beads"]:
                return
            if girl["obedience"] < 2 + girl["attributes"]["pride"] + girl["attributes"]["nature"] - girl["sex_experience"]["penetration"]["vaginal_sex"] - girl["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["lust_driver"]["value"]*3 - girl["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]["sexual_openness"]["value"]*2 + dic_girl_psy_status[girl["psy_status"]]:
                if girl["rules"]["enforce_rules"] and storage["house"]["sex_items"]["V-balls"] > 0 and storage["house"]["sex_items"]["Chastity Belt"] > 0:
                    girl["mood_state"]["bad_mood"]["rules"]["active"] = True
                    girl["num_rules_wanttobreak"] += 1
                    girl["rules_explain"]["use_vaginal_beads"] += f"{all_girls_list[girl_index]['name']} only uses the vaginal beads because the chastity belt prevents her from removing them. "
                else:
                    girl["rules_broken"]["use_vaginal_beads"] = True
                    girl["rules_explain"]["use_vaginal_beads"] += f"{all_girls_list[girl_index]['name']} refuses to use the vaginal beads."
            else:
                girl["rules_explain"]["use_vaginal_beads"] += f"{all_girls_list[girl_index]['name']} uses the vaginal beads all day long without you having to remind her."
            if not girl["rules_broken"]["use_vaginal_beads"]:
                a = 4 + girl["attributes"]["pride"] + girl["attributes"]["nature"] - girl["aura"]["devotion"] - girl["sex_experience"]["penetration"]["vaginal_sex"] 
                girl["mood"] -= a
                if a > 0:
                    girl["rules_explain"]["use_vaginal_beads"] += " Too much self-esteem or a lack of experience makes this painful to her."
                else:
                    girl["rules_explain"]["use_vaginal_beads"] += " She seems to enjoy the sensations."











    auto_list = [   night_rules_fuctions.auto_slave_cook_meal, 
                    night_rules_fuctions.auto_slave_maid, 
                    night_rules_fuctions.auto_bath_slave_help_master,
                    night_rules_fuctions.slave_bath_alone,
                    night_rules_fuctions.slave_bath_selfwash_auto,
                    night_rules_fuctions.auto_alarm,
                    night_rules_fuctions.auto_slave_humility, 
                    night_rules_fuctions.auto_slave_pet, 
                    night_rules_fuctions.auto_slave_silence, 
                    night_rules_fuctions.auto_slave_behave_toilet, 
                    night_rules_fuctions.auto_slave_behave_urinal,
                    night_rules_fuctions.auto_slave_deny_orgasm,
                    night_rules_fuctions.auto_slave_deny_toileting,
                    night_rules_fuctions.auto_slave_masturbation,
                    night_rules_fuctions.auto_slave_use_vaginal_beads   ]    
