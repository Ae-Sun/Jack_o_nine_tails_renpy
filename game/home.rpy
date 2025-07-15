default bgstyle = "bg_main_old.webp"
default bgstyle2 = "bg_old.webp"
default bgstyle3 = "bg_stat_old.webp"
default home_decoration = "bg/interiors/slum_study_large.webp"
default home_decoration_mini = "bg/interiors/slum_study.webp"
default home_menu_image1 = "ui overhaul/activity.webp"
default home_menu_image2 = "ui overhaul/slave_assignments.webp"
default home_menu_image3 = "ui overhaul/domestic_issues.webp"
default home_menu_image4 = "ui overhaul/cast_spell.webp"
default home_menu_image5 = "ui overhaul/assistant_assignments.webp"
default home_menu_image6 = "ui overhaul/end_day.webp"
default energy_image1 = "ui overhaul/energy/energy_green.webp"
default energy_image2 = "ui overhaul/energy/energy_green_half.webp"
default dic_spellbook_info_index = "default"
default mc_image = ""
default mc_image2 = ""
default text_slave_conditions_index = "default"
default is_main_slave = False
default show_main_slave = False
default is_assistant_assigned = False
default energy_value = 0
default current_menu = 0
default mood_value = 0
default day_tracker = 1
default is_auspex_active = False
default slave_suicide = False
default boobs1 =" marshmallowy tits"
default boobs2 =" motherly breasts"
default boobs3 =" empty breast-sacks"
default boobs4 =" round tits"
default boobs5 =" firm melons"
default boobs6 =" shapely balloons"
default dic_overnight_rules_count_index = 1
default slave_rebellion_fight = False
default slave_rebellion_attack = False
default description_slave_attributes_track_value = "default"
default available_options = 0
default equipment_choice = "clothes"
default equipment_choice_image = "scene/item/clear_small"
default equipment_choice_image_text = "You can navigate up and down in the clothing equipment menu pressing the 1 and 2 keys."
default aura_is_hover = False
default aura_check_hover = ""
default inventory_track =""
default inventory_track_weapon = ""
default inventory_track_weapon2 = ""
default is_slave_nearly_fainted = False
default doblecheck_equipment = False
default slave_obedience_bonus = 0
default slave_difficulty = 0
default debt_tracker = 0
default debt = 0
default gameover = False
default pony_count = 0
default slave_escape_type = 0
default home_estate ={
    "kitchen": 0,
    "barn": 0,
    "laboratory": 0,
}
default inventory = {
    "remove": "-",
    "Without armour": "-",
    "Aramid Suit": 0,
    "Leather Armor": 0,
    "Adaptive Suit": 0,
    "Phantom Aegis Suit": 0,
    "Elven Chainmail": 0,
    "Combined Armor": 0,
    "Adaptive armor": 0,
    "Semi-perfect armor": 0,
    "Iron Armor": 0,
    "Obsidian Bulwark": 0,
    "Gothic plate": 0,
    "Mithril Mail": 0,
    "Fist": "-",
    "Baton": 0,
    "Rapier": 0,
    "Koncerz": 0,
    "Whip": 0,
    "Epee": 0,
    "Gladius": 0,
    "katana": 0,
    "Blowgun Darts": 0,
    "shuriken": 0,
    "Buckler": 0,
    "Adarga": 0,
    "Huge mace": 0,
    "Baseball Bat": 0,
    "Gattle Prod": 0,
    "Naginata": 0,
    "magic_protection": 0,
    "physical_protection": 0,
    "stamina_restore": 0,
    "penetration": 0,
    "Lucky": 0,
    "speed": 0,
    "bleeding_ring": 0,
    "stun_ring": 0,
    "confusion_ring": 0,
    "injured_ring": 0,
    "sleep_ring": 0,
    "pain_ring": 0,
    "naked": "-",
    "common_apron": 0,
    "maid_dress": 0,
    "nurse_dress": 0,
    "leotard": 0,
    "chainmail_bikini": 0,
    "enchanter_robe": 0,
    "sun_dress": 0,
    "laced_underwear": 0,
    "sailor_foku": 0,
    "cocktail_dress": 0,
    "rubber_dress": 0,
    "ukata": 0,
    "bellydance": 0,
    "leather_corset": 0,
    "rich_dress": 0,
    "wedding_dress": 0,
    "petsuit": 0,
    "deprivation_suit": 0,
    "cow_gear": 0,
    "pony_plume": 0,
    "plain_headband": 0,
    "hijab": 0,
    "crown_of_thorns": 0,
    "plain_tiara": 0,
    "hairnet": 0,
    "glasses": 0,
    "nekomimi": 0,
    "incrusted_tiara": 0,
    "exotic_wig": 0,
    "plain_pendant": 0,
    "incrusted_necklace": 0,
    "dog_collar": 0,
    "leather_collar": 0,
    "steel_collar": 0,
    "spiked_collar": 0,
    "shock_collar": 0,
    "golden_collar": 0,
    "rubber_gloves": 0,
    "laced_gloves": 0,
    "leather_gloves": 0,
    "plastic_bracers": 0,
    "fluffy_gloves": 0,
    "ponygirl_harness": 0,
    "leather_straps": 0,
    "tabi": 0,
    "fluffy_stepins": 0,
    "pointes": 0,
    "sneakers": 0,
    "high_heels": 0,
    "high_boots": 0,
    "hoofed_boots": 0,
    "plain_ring": 0,
    "incrusted_ring": 0,
    "plain_earrings": 0,
    "incrusted_earrings": 0,
    "heavy_gauge_rings": 0,
    "barbells": 0,
    "nipple_chain": 0,
    "anal_plug": 0,
    "anal_tail": 0,
    "":0 # this is necessary -rec3ks
}
default magna_magnifika = 0
default item_supermacy_bonus = 0
label iniciation_label:
    $ mc_image2 = mc_image.replace(".webp", "_hover.webp")
    $ energy_value = 10
    if is_tutorial:
        python:
            mc_image = "master/master_noble.webp"

            for key, value in inventory.items():
                if value != "-":
                    inventory[key] = 1
        jump equipment_check
    else:
        if is_normal_start == True:
            $mc_image = dic_custom_character_selection[mc][0]
        else:
            $mc_image = dic_custom_character_selection[dic_charactersOnlyName[characterOnlyNameIndex]][0]
    jump Home
label next_day_label:
    python:
        is_auspex_active = False
        is_slave_nearly_fainted = False
        energy_value += strength_value_1 *2 + 2
        energy_value = min(10, energy_value)
        day_tracker += 1
        save_girl_index = girl_index
        for girl_index in all_girls_list:
            # save pass mood
            all_girls_list[girl_index]["past_mood"] = all_girls_list[girl_index]["mood"]
            # reset temporal mood always
            all_girls_list[girl_index]["mood_temporal"] = 0
            if all_girls_list[girl_index]["conscience"]:
                all_girls_list[girl_index]["epilation"] = max(all_girls_list[girl_index]["epilation"]-1,0)
                all_girls_list[girl_index]["manicure"] = max(all_girls_list[girl_index]["manicure"]-1,0)
                all_girls_list[girl_index]["hairstyle"] = max(all_girls_list[girl_index]["hairstyle"]-1,0)
                all_girls_list[girl_index]["perfume"] = max(all_girls_list[girl_index]["perfume"]-1,0)
                all_girls_list[girl_index]["caught_masturbating"] = max(all_girls_list[girl_index]["caught_masturbating"]-1,0)
                all_girls_list[girl_index]["daring"] = max(all_girls_list[girl_index]["daring"]- random.randint(0, 3),0)
                if all_girls_list[girl_index]["energised"] > 5:
                    all_girls_list[girl_index]["energised"] = max(all_girls_list[girl_index]["energised"]- random.randint(0, 7),0)
                for key in dic_slave_mood["good_mood"]:
                    if not all_girls_list[girl_index]["mood_state"]["good_mood"][key]["permanent"]:
                        if not all_girls_list[girl_index]["mood_state"]["good_mood"][key]["accustomed"]:
                            all_girls_list[girl_index]["mood_state"]["good_mood"][key]["accustomed_value"] -= 1
                            if all_girls_list[girl_index]["mood_state"]["good_mood"][key]["accustomed_value"] == 0:
                                all_girls_list[girl_index]["mood_state"]["good_mood"][key]["accustomed"] = True
                for key in dic_slave_mood["bad_mood"]:
                    if not all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["permanent"]:
                        if not all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["accustomed"]:
                            all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["accustomed_value"] -= 1
                            if all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["accustomed_value"] == 0:
                                all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["accustomed"] = True
                if debt_tracker > 0:
                    debt_tracker -= 1
                    if debt_tracker == 0 and debt > 0:
                        msg("As in any other city, in the Eternal Rome it is reckless to forget to repay money you have borrowed. You died a disgraceful death at the hand of the moneylender’s henchmen…")
                        gameover = True
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
                if all_girls_list[girl_index]["sleep"] != 0 and all_girls_list[girl_index]["psy_status"] != "broken":
                    if all_girls_list[girl_index]["attributes"]["endurance"] > 0:
                        if all_girls_list[girl_index]["mood"] < -1 and all_girls_list[girl_index]["attributes"]["temperament"] > all_girls_list[girl_index]["obedience"]:
                            n = 7 + personality_value_2 - all_girls_list[girl_index]["aura"]["despair"]
                            for girl_index in all_girls_list:
                                if all_girls_list[girl_index]["conscience"]:
                                    if all_girls_list[girl_index]["assistant"]:
                                        n += all_girls_list[girl_index]["attributes"]["intelligence"] + all_girls_list[girl_index]["aura"]["devotion"]
                            ### need assistant supervision code  - WIP
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
                        if all_girls_list[girl_index]["aura"]["despair"] > 2 and all_girls_list[girl_index]["attributes"]["endurance"] > 3 and all_girls_list[girl_index]["skills"]["gladiatrix"] > 0 and all_girls_list[girl_index]["aura"]["devotion"] == 0 and all_girls_list[girl_index]["mood"] < 0: #and (master_supermacy - master_style) < 2 and exam_in_progress = 0:
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
                #if not all_girls_list[girl_index]["assistant"]:
                    # WIP Cooking rule
                    #if home_estate["kitchen"] != 0: 

                                    
                
                
                
                if all_girls_list[girl_index]["assistant"]:
                    if all_girls_list[girl_index]["attributes"]["nature"] < 3:
                        all_girls_list[girl_index]["experience"]["attributes"]["nature"] +=1
                        increase_check("attributes","nature")
                if all_girls_list[girl_index]["brand"] != 0:
                    all_girls_list[girl_index]["experience"]["aura"]["habit"] += 1
                if all_girls_list[girl_index]["brand"] == 5:
                    all_girls_list[girl_index]["experience"]["aura"]["habit"] += 1
                increase_check("aura","habit")
            ### energy and sleep condition -half done
                if all_girls_list[girl_index]["sleep"] != 4:
                    if all_girls_list[girl_index]["aura"]["devotion"] >= 3:
                        all_girls_list[girl_index]["energy"] = min(12, all_girls_list[girl_index]["energy"]//2 + all_girls_list[girl_index]["attributes"]["endurance"] * 2 + 2)
                    else:
                        all_girls_list[girl_index]["energy"] = min(10, all_girls_list[girl_index]["energy"]//2 + all_girls_list[girl_index]["attributes"]["endurance"] * 2 + 2)
                    all_girls_list[girl_index]["days_without_sleep"] = 0
                else:
                    all_girls_list[girl_index]["energy"] = min(12,all_girls_list[girl_index]["energy"]//2 + (all_girls_list[girl_index]["attributes"]["endurance"] * 2 + 2)/2)
                    all_girls_list[girl_index]["days_without_sleep"] += 1
                    all_girls_list[girl_index]["experience"]["attributes"]["endurance"] -= all_girls_list[girl_index]["days_without_sleep"] *3
                    all_girls_list[girl_index]["experience"]["aura"]["taming"] += all_girls_list[girl_index]["days_without_sleep"]
                    reduce_check("attributes","endurance")
                    increase_check("aura","taming")

                #### SPOILING SECTION - Done
                ### spoiling - increase
                if all_girls_list[girl_index]["daily_count"]["reward"] > 2:
                    all_girls_list[girl_index]["experience"]["aura"]["spoil"] += all_girls_list[girl_index]["daily_count"]["reward"]*5
                if all_girls_list[girl_index]["aura"]["devotion"] <= 2 and all_girls_list[girl_index]["aura"]["fear"] == 0 and all_girls_list[girl_index]["days_without_food"] == 0 and all_girls_list[girl_index]["days_without_sleep"] == 0 and all_girls_list[girl_index]["rules"]["rules_count"] < dic_overnight_rules_count[dic_overnight_rules_count_index]:
                    all_girls_list[girl_index]["experience"]["aura"]["spoil"] += all_girls_list[girl_index]["attributes"]["pride"] + all_girls_list[girl_index]["attributes"]["nature"] + all_girls_list[girl_index]["attributes"]["temperament"]
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

        slave_nearly_fainted = False
        girl_index = save_girl_index
    show screen home_menu
    $ msg("New day [day_tracker]")
    jump Home
label Home: 
    show screen bg_home()
    show screen home_attributes_menu()
    show screen sparks_menu()
    hide screen description_slave_attributes
    hide screen screen_rules
    python:
        equipment_check2()
        doblecheck_equipment = True
        infobox_jump = "Home"
        # supermacy calculation
        master_supermacy = personality_value_2 + allure_value_3 + dominance_value_5 + strength_value_1 + magna_magnifika
        all_girls_list[girl_index]["supermacy"] = all_girls_list[girl_index]["attributes"]["temperament"] + all_girls_list[girl_index]["attributes"]["nature"] + 5 - all_girls_list[girl_index]["attributes"]["pride"] + all_girls_list[girl_index]["attributes"]["endurance"] + all_girls_list[girl_index]["attributes"]["intelligence"] - 3
        # obedience difficulty ajustment
        if all_girls_list[girl_index]["beaten_ever"]:
            all_girls_list[girl_index]["supermacy"] -= 1
        if all_girls_list[girl_index]["domini_dictum_ever"]:
            all_girls_list[girl_index]["supermacy"] -= 1
        if dic_custom_start_difficulty_selection_index_index == 0:
            slave_obedience_bonus = 4
            slave_difficulty = 2
        elif dic_custom_start_difficulty_selection_index_index == 1:
            slave_obedience_bonus = 0
            slave_difficulty = 4
        elif dic_custom_start_difficulty_selection_index_index == 2:
            slave_obedience_bonus = 0
            slave_difficulty = 14 - min(8, 4*all_girls_list[girl_index]["aura"]["devotion"])
        girl_index_save = girl_index
        for girl_index in all_girls_list:
            # Obedience re-calculation
            slave_nature = 5 - all_girls_list[girl_index]["attributes"]["pride"] + all_girls_list[girl_index]["attributes"]["temperament"] + all_girls_list[girl_index]["attributes"]["nature"] + all_girls_list[girl_index]["attributes"]["intelligence"]
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
            all_girls_list[girl_index]["obedience"] = slave_obedience_bonus + all_girls_list[girl_index]["mood"] + all_girls_list[girl_index]["bonus_fear"] + all_girls_list[girl_index]["aura"]["devotion"]*4 + all_girls_list[girl_index]["aura"]["taming"] * 2 \
            + int((1+all_girls_list[girl_index]["aura"]["despair"]) // 2) + all_girls_list[girl_index]["aura"]["awareness"] + all_girls_list[girl_index]["aura"]["habit"] - all_girls_list[girl_index]["aura"]["spoil"]*2 - int(slave_difficulty/2) - slave_nature
            # set obedience to 100 if broken
            if all_girls_list[girl_index]["psy_status"] == "broken":
                all_girls_list[girl_index]["obedience"] = 100
            # Cap aura values
            for aura in ["fear","despair","awareness","taming","habit","spoil","devotion"]:
                if all_girls_list[girl_index]["aura"][aura] == 0 and all_girls_list[girl_index]["experience"]["aura"][aura] < -10:
                    all_girls_list[girl_index]["experience"]["aura"][aura] = -10
                if all_girls_list[girl_index]["aura"][aura] == 5 and all_girls_list[girl_index]["experience"]["aura"][aura] > 10:
                    all_girls_list[girl_index]["experience"]["aura"][aura] = 10
            for attributes in ["endurance"]:
                if all_girls_list[girl_index]["attributes"][attributes] == 0 and all_girls_list[girl_index]["experience"]["attributes"][attributes] < -10:
                    all_girls_list[girl_index]["experience"]["attributes"][attributes] = -10
                if all_girls_list[girl_index]["attributes"][attributes] == 5 and all_girls_list[girl_index]["experience"]["attributes"][attributes] > 10:
                    all_girls_list[girl_index]["experience"]["attributes"][attributes] = 10
            ### fainted code
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
            ### slave dead code
            if all_girls_list[girl_index]["attributes"]["endurance"] == 0 and all_girls_list[girl_index]["attributes"]["physical"] == 5 and max(all_girls_list[girl_index]["experience"]["attributes"]["endurance"] ,all_girls_list[girl_index]["experience"]["attributes"]["physical"]) <= -10:    
                temporal_value = meat_evaluation()
                del all_girls_list[girl_index]
                sparks_37 += temporal_value
                msg("Your slave is dead, and you sale the meat to the butcher for [temporal_value]")
            ### check slave broken
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
            ### define maxmotivation
            maxmotivation = max(all_girls_list[girl_index]["aura"]["fear"],all_girls_list[girl_index]["aura"]["devotion"],all_girls_list[girl_index]["aura"]["spoil"],all_girls_list[girl_index]["aura"]["habit"],all_girls_list[girl_index]["aura"]["awareness"],all_girls_list[girl_index]["aura"]["taming"],all_girls_list[girl_index]["arousal"])
            slave_psy_hardness = max(all_girls_list[girl_index]["attributes"]["temperament"],all_girls_list[girl_index]["attributes"]["nature"],(5 - all_girls_list[girl_index]["attributes"]["pride"]),all_girls_list[girl_index]["attributes"]["intelligence"])
            ### Slaves psy status calculation
            if all_girls_list[girl_index]["psy_status"] != "broken":
                if all_girls_list[girl_index]["psy_status"] == "lachrymose" and all_girls_list[girl_index]["aura"]["devotion"] > 0:
                    all_girls_list[girl_index]["psy_status"] = "soft"
                # if mood is positive - better psy status for slaves
                if all_girls_list[girl_index]["mood"] < 0:
                    if all_girls_list[girl_index]["aura"]["devotion"] < 2:
                        if all_girls_list[girl_index]["attributes"]["temperament"] >= min(4, maxmotivation):
                            all_girls_list[girl_index]["psy_status"] = "hateful"
                        if all_girls_list[girl_index]["attributes"]["nature"] >= min(4, maxmotivation):
                            all_girls_list[girl_index]["psy_status"] = "resistant"
                        if all_girls_list[girl_index]["attributes"]["pride"] >= min(4, maxmotivation):
                            all_girls_list[girl_index]["psy_status"] = "arrogant"
                    else:
                        if all_girls_list[girl_index]["attributes"]["temperament"] >= min(4, maxmotivation):
                            all_girls_list[girl_index]["psy_status"] = "hysteric"
                        if all_girls_list[girl_index]["attributes"]["nature"] >= min(4, maxmotivation):
                            all_girls_list[girl_index]["psy_status"] = "docile"
                        if all_girls_list[girl_index]["attributes"]["pride"] >= min(4, maxmotivation):
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
            #### Mood define
            # set mood to default 
            all_girls_list[girl_index]["mood"] = 0
            if all_girls_list[girl_index]["psy_status"] != "broken":
                # + clothes mood 
                all_girls_list[girl_index]["mood"] += all_girls_list[girl_index]["worn_mood"]
                # + all temporal mood
                all_girls_list[girl_index]["mood"] += all_girls_list[girl_index]["mood_temporal"]
                # + past mood, a slave that yesterday is depressing, will start more sad that one that was happy yesterday
                # + 1/2 if negative + 1/3 if positive because sadness stick longer that hapiness, like IRL
                if all_girls_list[girl_index]["past_mood"] > 0:
                    all_girls_list[girl_index]["mood"] += all_girls_list[girl_index]["past_mood"]/3
                else:
                    all_girls_list[girl_index]["mood"] += all_girls_list[girl_index]["past_mood"]/2
                for key in dic_slave_mood["good_mood"]:
                    if all_girls_list[girl_index]["mood_state"]["good_mood"][key]["active"]:
                        all_girls_list[girl_index]["mood"] += 1
                for key in dic_slave_mood["bad_mood"]:
                    if all_girls_list[girl_index]["mood_state"]["bad_mood"][key]["active"]:
                        all_girls_list[girl_index]["mood"] -= 1
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
                # WIP            
                # if dynslave_state = CONST_INT['slave_exist']:
                # 	! state check is conscious only - ImperatorAugustus
                # 	! carry over +0.2 mood for each level of previous day mood that was above -5 (+0.2 at Dysphoric, +0.4 at Sullen, +0.6 at Melancholic, +0.8 at Pessimistic, +1 at Calm, +2 at Ecstatic)
                # 	dynslave_rate['mood'] += 10 + dynslave['mood']*2 + dynslave['moral'] + (dynslave['stamina'] - 3) + _
                # 		- dynslave['arousal'] - dynslave['fear'] - dynslave['spoil'] - dynslave['angst']*2 _
                # 		- dynslave['hygiene'] - (house_mess - 1) &! removed energy from this formula (handled elsewhere), doubled angst impact, adjusted carry over to reduce mood swings by applying a bonus representing half of the previous day mood (counting anything above depressed as positive) - ImperatorAugustus

                        
                
                        





                
                    

            






        girl_index = girl_index_save
    if slave_rebellion_fight:
        jump slave_rebellion_fight_label
    if is_tutorial == True and current_menu == 0:
        show screen goguild()
    else:
        hide screen goguild
    if show_main_slave:
        show screen main_slave_image() 

    if customboxcheck:
        hide screen tutorial_description
        hide screen tutorial_description2
        hide screen tutorial_descriptionphysical
        show screen tutorial_attribute()
    if attribute_checkbox:
        if attributeisphysical:
            show screen tutorial_descriptionphysical()
            hide screen tutorial_description
        else:
            show screen tutorial_description()
            hide screen tutorial_descriptionphysical
        hide screen tutorial_attribute
    ### this may look stupid, but it's not. Think how back feature works in renpy. -rec3ks
    if current_menu == 0:
        $ show_main_slave = False
        hide screen main_slave_image
        hide screen screen_rules
        call screen home_menu()
    elif current_menu == 1:
        call screen slave_activities_menu()
    elif current_menu == 2:
        call screen slave_assignments_menu()
    elif current_menu == 3:
        call screen domestic_issues_menu()
    elif current_menu == 4:
        call screen cast_spell_menu()
    elif current_menu == 41:
        call screen spellbook_info()
    elif current_menu == 42:
        call screen home_menu_auspex()
    elif current_menu == 100:
        hide screen sparks_menu
        hide screen home_attributes_menu
        show screen screen_rules
        call screen slave_rules_menu()
    elif current_menu == 101:
        hide screen sparks_menu
        hide screen home_attributes_menu
        show screen screen_rules
        call screen slave_anatomy_menu()
    elif current_menu == 102:
        hide screen sparks_menu
        hide screen home_attributes_menu
        show screen screen_rules
        call screen slave_equipment_menu()
    elif current_menu == 103:
        hide screen sparks_menu
        hide screen home_attributes_menu
        show screen screen_rules
        call screen slave_aura_menu()
label slave_rebellion_fight_label:
    if slave_rebellion_attack:
        $ slave_rebellion_attack = False
        "You wake feeling threatened and instinctively roll off the bed. Where you had just laid is stuck a knife! Looks like [all_girls_list[girl_index]['name']]stole it from the kitchen and decided to kill you!"
    else:
        "[all_girls_list[girl_index]['name']] refuses to wear the [all_girls_list[girl_index]['equipment'][equipment_choice]]. Use force to make her wear it anyway"
    "WIP"
    "Please use the Ren'Py rollback function to return to a previous game state."
    "{color=#ff0000}Returning to the main menu in... 3{/color}"
    "{color=#ff0000}Returning to the main menu in... 2{/color}"
    "{color=#ff0000}Returning to the main menu in... 1{/color}"

    return 
label equipment_check:
    python:
        girl_index_save = girl_index
        for girl_index in all_girls_list:
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
        girl_index = girl_index_save

    jump Home
screen main_slave_image():
    add all_girls_list[girl_index]["fullimage"] + ".webp" xalign 0.2 yalign 0.9999 size(795,535)
screen goguild():
    zorder 10
    textbutton "Go to Guild" xalign 0.10 yalign 0.76:
        style "home_button"
        action SetVariable("angelika_speech_text_count", 4),Hide("home_attributes_menu"),Jump("Tutorial")
    add "ui overhaul/guild.webp" xalign 0.05 yalign 0.755 size(50,50)
screen spellbook_info():
    key "K_SPACE" action SetVariable("current_menu", 4),Jump("Home")
    add bgstyle2 xsize 1280 ysize 720
    add home_decoration_mini pos(0.004,0.007111) anchor (0.0, 0.0) xsize 795 ysize 535
    text dic_spellbook_info[dic_spellbook_info_index] pos (0.02, 0.78) size 20 color "#000000" font "consolas.ttf" xmaximum 750 
    vbox:
        yalign 0.3
        xalign 0.10
        textbutton "Basics":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "basics"),Jump("Home")
        textbutton "Auspex":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "auspex"),Jump("Home")
        textbutton "Magna Magnifika":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "magna"),Jump("Home")
        textbutton "Sententia Veritas":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "sententia"),Jump("Home")
        textbutton "Back":
            style "home_button"
            action SetVariable("current_menu", 4),Jump("Home")
    vbox:
        yalign 0.3
        xalign 0.4
        textbutton "Tremendio":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "tremendio"),Jump("Home")
        textbutton "Cruciato":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "cruciato"),Jump("Home")
        textbutton "Delikacia":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "delikacia"),Jump("Home")
        textbutton "Domini Dictum":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "domini"),Jump("Home")
        textbutton "Adverto Servili":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "adverto"),Jump("Home")
    vbox:
        yalign 0.29
        xalign 0.05
        add "ui overhaul/basics.webp" size(50,50)
        add "ui overhaul/auspex spellbook.webp" size(50,50)
        add "ui overhaul/cruciato spellbook.webp" size(50,50)
        add "ui overhaul/domini dictum spellbook.webp" size(50,50)
        add "ui overhaul/back_city_use.webp" size(50,50)
    vbox:
        yalign 0.29
        xalign 0.3132
        add "ui overhaul/tremendio spellbook.webp" size(50,50)
        add "ui overhaul/cruciato spellbook.webp" size(50,50)
        add "ui overhaul/delikacia spellbook.webp" size(50,50)
        add "ui overhaul/domini dictum spellbook.webp" size(50,50)
        add "ui overhaul/adverto servili spellbook.webp" size(50,50)
screen cast_spell_menu():
    key "K_SPACE" action SetVariable("current_menu", 0),Jump("Home")
    imagebutton pos(0.02,0.4):
        idle "ui overhaul/back.webp"
        hover "ui overhaul/back_hover.webp"
        action SetVariable("current_menu", 0),Jump("Home")
    vbox:
        yalign 0.5
        xalign 0.10
        textbutton "Spellbook":
            style "home_button"
            action SetVariable("current_menu", 41),SetVariable("dic_spellbook_info_index", "default"),Jump("Home")
        if is_auspex_active:
            textbutton "Auspex":
                style "home_button"
                action NullAction()
        else:
            textbutton "Auspex":
                style "home_button"
                action SetVariable("current_menu", 42),SetVariable("sparks_37",sparks_37 -2),Jump("Home")
        textbutton "Magna Magnifika":
            style "home_button"
            action NullAction()
        textbutton "Sententia Veritas":
            style "home_button"
            action NullAction()
        textbutton "Tremendio":
            style "home_button"
            action NullAction()
        textbutton "Cruciato":
            style "home_button"
            action NullAction()
        textbutton "Delikacia":
            style "home_button"
            action NullAction()
        textbutton "Domini Dictum":
            style "home_button"
            action NullAction()
        textbutton "Adverto Servili":
            style "home_button"
            action NullAction()
    vbox:
        yalign 0.48
        xalign 0.05
        add "ui overhaul/spellbook.webp" size(50,50)
        if is_auspex_active:
            add "ui overhaul/auspex_gray.webp" size(50,50)
        else:
            add "ui overhaul/auspex.webp" size(50,50)
        add "ui overhaul/magna magnifika.webp" size(50,50)
        add "ui overhaul/sententia veritas.webp" size(50,50)
        add "ui overhaul/tremendio.webp" size(50,50)
        add "ui overhaul/cruciato.webp" size(50,50)
        add "ui overhaul/delikacia.webp" size(50,50)
        add "ui overhaul/domini dictum.webp" size(50,50)
        add "ui overhaul/adverto servili.webp" size(50,50)
screen domestic_issues_menu():
    key "K_SPACE" action SetVariable("current_menu", 0),Jump("Home")
    imagebutton pos(0.02,0.4):
        idle "ui overhaul/back.webp"
        hover "ui overhaul/back_hover.webp"
        action SetVariable("current_menu", 0),Jump("Home")
    vbox:
        yalign 0.5
        xalign 0.10
        textbutton "Take a bath":
            style "home_button"
            action NullAction()
        textbutton "Prepare a meal":
            style "home_button"
            action NullAction()
        textbutton "Tidy up the house":
            style "home_button"
            action NullAction()
        textbutton "Take a drug":
            style "home_button"
            action NullAction()
        textbutton "Drink a potion":
            style "home_button"
            action NullAction()
        textbutton "Accounting":
            style "home_button"
            action NullAction()
        textbutton "Business":
            style "home_button"
            action NullAction()
    vbox:
        yalign 0.49
        xalign 0.05
        add "ui overhaul/take_bath.webp" size(50,50)
        add "ui overhaul/prepare_a_meal.webp" size(50,50)
        add "ui overhaul/tidy_up_the_house.webp" size(50,50)
        add "ui overhaul/take a drug.webp" size(50,50)
        add "ui overhaul/drink a potion.webp" size(50,50)
        add "ui overhaul/accounting.webp" size(50,50)
        add "ui overhaul/business.webp" size(50,50)
screen home_menu_auspex():
    key "K_SPACE" action SetVariable("current_menu", 103),Hide("home_menu_auspex"),SetVariable("is_auspex_active", True),Jump("Home")
    add bgstyle2 xsize 1280 ysize 720
    add home_decoration_mini pos(0.004,0.007111) anchor (0.0, 0.0) xsize 795 ysize 535
    if magic_value_17 > 0:
        add "magic.webp"  pos(0.004,0.007111) anchor (0.0, 0.0) xsize 795 ysize 535
        text spells_books_description["Auspex"]["cast"] size 18 color "#000000" font "fonts/Consolas.ttf" pos(0.02, 0.78) xmaximum 750
        vbox:
            xalign 0.655
            yalign 0.96
            imagebutton:
                idle "buttons/demo_noback_button_hover.webp" anchor (0.5, 0.5)
                hover "buttons/demo_noback_button_hover.webp"
                action NullAction()
            imagebutton:
                idle "buttons/auk_fwrd.webp" anchor (0.5, 0.5)
                hover "buttons/auk_fwrd_hover.webp"
                action SetVariable("is_auspex_active", True),Hide("home_menu_auspex")
    else:
        text spells_books_description["Auspex"]["fail"] size 18 color "#000000" font "fonts/Consolas.ttf" pos(0.02, 0.78) xmaximum 750  
        vbox:
            xalign 0.655
            yalign 0.96
            imagebutton:
                idle "buttons/demo_noback_button_hover.webp" anchor (0.5, 0.5)
                hover "buttons/demo_noback_button_hover.webp"
                action NullAction()
            imagebutton:
                idle "buttons/auk_fwrd.webp" anchor (0.5, 0.5)
                hover "buttons/auk_fwrd_hover.webp"
                action Hide("home_menu_auspex")
screen home_menu():
    vbox:
        yalign 0.5
        xalign 0.10
        if is_main_slave:
            $ home_menu_image1 = "ui overhaul/activity.webp"
            textbutton "Slave activities":
                style "home_button"
                action SetVariable("current_menu", 1),SetVariable("show_main_slave", True), Jump("Home")
        else:
            $ home_menu_image1 = "ui overhaul/activity_gray.webp"
            textbutton "Slave activities":
                style "home_button_grey"
                action NullAction()
        if is_main_slave:
            $ home_menu_image2 = "ui overhaul/slave_assignments.webp"
            textbutton "Slaves assignments":
                style "home_button"
                action SetVariable("current_menu", 2),SetVariable("show_main_slave", True), Jump("Home")
        elif is_assistant_assigned:
            $ home_menu_image2 = "ui overhaul/assistant_assignments.webp"
            textbutton "Train assistant":
                style "home_button"
                action NullAction()
        else:
            $ home_menu_image2 = "ui overhaul/slave_assignments_gray.webp"
            textbutton "Slave assignments":
                style "home_button_grey"
                action NullAction()
        textbutton "Domestic issues":   
            style "home_button"
            action SetVariable("current_menu", 3), Jump("Home")
        textbutton "Cast a spell":
            style "home_button"
            action SetVariable("current_menu", 4), Jump("Home")
        if is_assistant_assigned:
            $ home_menu_image5 = "ui overhaul/assistant_assignments.webp"
            textbutton "Assistant assignments":
                style "home_button"
                action NullAction()
        else:
            $ home_menu_image5 = "ui overhaul/appoint_assignments_gray.webp"
            textbutton "Appoint assistant":
                style "home_button_grey"
                action NullAction()
        textbutton "End of the day":
            style "home_button"
            action SetVariable("current_menu", 0), Jump("next_day_label")
    vbox:
        yalign 0.49
        xalign 0.05
        add home_menu_image1 size(50,50)
        add home_menu_image2 size(50,50)
        add home_menu_image3 size(50,50)
        add home_menu_image4 size(50,50)
        add home_menu_image5 size(50,50)
        add home_menu_image6 size(50,50)
    vbox:

        if is_tutorial:
            yalign 0.08
            xalign 0.74
            if girl_index == 0:
                textbutton "change girl":   
                    style "home_button"
                    action SetVariable("girl_index", 1),Jump("Home")
            if girl_index == 1:
                textbutton "change girl":
                    style "home_button"
                    action SetVariable("girl_index", 2),Jump("Home")
            if girl_index == 2:
                textbutton "change girl":
                    style "home_button"
                    action SetVariable("girl_index", 0),Jump("Home")
screen slave_activities_menu():
    key "K_SPACE" action SetVariable("current_menu", 0),Jump("Home")
    imagebutton pos(0.02,0.4):
        idle "ui overhaul/back.webp"
        hover "ui overhaul/back_hover.webp"
        action SetVariable("current_menu", 0),Jump("Home")
    vbox:
        yalign 0.5
        xalign 0.10
        textbutton "Talk":
            style "home_button"
            action NullAction()
        textbutton "Sex":
            style "home_button"
            action NullAction()
        textbutton "conduct a lesson":
            style "home_button"
            action NullAction()
        textbutton "Sex education":
            style "home_button"
            action NullAction()
        textbutton "Invite a tutor (5-25$)":
            style "home_button"
            action NullAction()
        textbutton "Reward":   
            style "home_button"
            action NullAction()
        textbutton "Punish":
            style "home_button"
            action NullAction()
        textbutton "Get rid of her":
            style "home_button"
            action NullAction()
    vbox:
        yalign 0.49
        xalign 0.05
        add "ui overhaul/talk.webp" size(50,50)
        add "ui overhaul/sex.webp" size(50,50)
        add "ui overhaul/conduct a lesson.webp" size(50,50)
        add "ui overhaul/sex education.webp" size(50,50)
        add "ui overhaul/invite a tutor.webp" size(50,50)
        add "ui overhaul/reward.webp" size(50,50)
        add "ui overhaul/punish.webp" size(50,50)
        add "ui overhaul/get rid of her.webp" size(50,50)
screen slave_assignments_menu():
    key "K_SPACE" action SetVariable("current_menu", 0),Jump("Home")
    imagebutton pos(0.02,0.4):
        idle "ui overhaul/back.webp"
        hover "ui overhaul/back_hover.webp"
        action SetVariable("current_menu", 0),Jump("Home")
    vbox:
        yalign 0.5
        xalign 0.10
        textbutton "Attend classes (2-12$)":
            style "home_button"
            action NullAction()
        textbutton "Gymnastics":
            style "home_button"
            action NullAction()
        textbutton "Tidy up the house":
            style "home_button"
            action NullAction()
        textbutton "Prepare dinner":
            style "home_button"
            action NullAction()
        textbutton "Take a bath":
            style "home_button"
            action NullAction()
        textbutton "Milk the Fiend":
            style "home_button"
            action NullAction()
        textbutton "Serve me":
            style "home_button"
            action NullAction()
        textbutton "Take a drug":
            style "home_button"
            action NullAction()
        textbutton "Drink a potion":
            style "home_button"
            action NullAction()
    vbox:
        yalign 0.48
        xalign 0.05
        add "ui overhaul/attend classes_s.webp" size(50,50)
        add "ui overhaul/gymnastics_s.webp" size(50,50)
        add "ui overhaul/tidy up the house_s.webp" size(50,50)
        add "ui overhaul/prepare dinner_s.webp" size(50,50)
        add "ui overhaul/take a bath_s.webp" size(50,50)
        add "ui overhaul/milk the fiend_s.webp" size(50,50)
        add "ui overhaul/serve me_s.webp" size(50,50)
        add "ui overhaul/take a drug.webp" size(50,50)
        add "ui overhaul/drink a potion.webp" size(50,50)
screen sparks_menu():
    zorder 10
    hbox:
        xalign 0.01
        yalign 0.01
        textbutton "Day: " + str(day_tracker) :
            style "day_tracker_button"
            action NullAction()
        add "spacer" size(4,0) 
        text "(" + str(sparks_37) + "$)":
            style "day_tracker_button_text"
screen slave_anatomy_menu():
    add "bg/page_blank.webp" xsize 795 ysize 535 pos(0.5028,0.42) anchor (0.5,0.5)
    key "K_SPACE" action SetVariable("current_menu", 0),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
    if all_girls_list[girl_index]["lactation"]:
        $boobs1 = "milk-swollen breasts"
        $boobs2 = "milk-swollen breasts"
        $boobs3 = "milk-distended breasts"
        $boobs4 = "milk-swollen breasts"
        $boobs5 = "milk-swollen breasts"
        $boobs6 = "milk-swollen breasts"
    else:
        $boobs1 =" marshmallowy tits"
        $boobs2 =" motherly breasts"
        $boobs3 =" empty breast-sacks"
        $boobs4 =" round tits"
        $boobs5 =" firm melons"
        $boobs6 =" shapely balloons"
    hbox:
        pos(0.205,0.07)
        add "girls/body/" + all_girls_list[girl_index]["boobs_img"] + ".webp" size(372,250)
        add "spacer" size(20,0)
        add "girls/body/" + all_girls_list[girl_index]["pussy_img"] + ".webp" size(372,250)  
    vbox:
        pos(0.21,0.42)

        if all_girls_list[girl_index]["age"]==0:
            text dic_girl_boobs_text["young"][all_girls_list[girl_index]["boobs"]] size 16 color "#000000" font "fonts/Segoe Print.ttf"
        elif all_girls_list[girl_index]["age"]==1:
            text dic_girl_boobs_text["loli"][all_girls_list[girl_index]["boobs"]] size 16 color "#000000" font "fonts/Segoe Print.ttf"
        elif all_girls_list[girl_index]["age"]==2:
            text dic_girl_boobs_text["mature"][all_girls_list[girl_index]["boobs"]] size 16 color "#000000" font "fonts/Segoe Print.ttf"
        if all_girls_list[girl_index]["lactation"]:
            text "Lactating" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        else:
            text "Not lactating" size 16 color "#000000" font "fonts/Segoe Print.ttf" 
        if all_girls_list[girl_index]["equipment"]["nipples"]["pierced"]:
            text "Nipples pierced" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        else:
            text "Nipples not pierced" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        text dic_girl_breast_modification[all_girls_list[girl_index]["breast_modification"]] size 16 color "#000000" font "fonts/Segoe Print.ttf"
        text dic_girl_age_text[all_girls_list[girl_index]["age"]] size 16 color "#000000" font "fonts/Segoe Print.ttf"
    vbox:
        pos(0.64,0.42)
        text dic_girl_vaginal_tightness[all_girls_list[girl_index]["vaginal_tightness"]] size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        text dic_girl_anal_tightness[all_girls_list[girl_index]["anal_tightness"]] size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        if all_girls_list[girl_index]["equipment"]["clitoris"]["pierced"]:
            text "Clitoris pierced" size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        else:
            text "Clitoris not pierced" size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        text dic_girl_vagina_modification[all_girls_list[girl_index]["vagina_modification"]] size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        text dic_girl_brand[all_girls_list[girl_index]["brand"]] size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
    vbox:
        pos(0.215,0.62)

        text "{color=#" + dic_color_level[all_girls_list[girl_index]["attributes"]["beauty"]] + "}Beauty{/color}{color=#0000D8} ={/color} {color=#" + dic_color_level[all_girls_list[girl_index]["attributes"]["natural_beauty"]] + "} Natural Beauty{/color}{color=#0000D8} +{/color} Neoplasty{color=#0000D8} - ({/color} No Scars{color=#0000D8} +{/color} Bruises{color=#0000D8} +{/color} Physique{color=#0000D8}){/color}" xalign 0.5 size 14 color "#000000" font "fonts/Segoe Print.ttf" 
        text "{color=#" + dic_color_level[all_girls_list[girl_index]["attributes"]["style"]] + "}Style{/color} {color=#0000D8}={/color} Clothes{color=#0000D8} +{/color} {color=#" + dic_color_level[all_girls_list[girl_index]["attributes"]["natural_beauty"]] + "} Natural Beauty{/color}{color=#0000D8} +{/color} Tangled Hair{color=#0000D8} +{/color} Scent, Nails & Pelage{color=#0000D8} +{/color} Natural Grace{color=#0000D8} -{/color} Hygiene" xalign 0.5 size 14 color "#000000" font "fonts/Segoe Print.ttf" 
        text "{color=#" + dic_color_level[all_girls_list[girl_index]["attributes"]["exoticism"]] + "}Exoticism{/color} {color=#0000D8}={/color} Natural Exoticism{color=#0000D8} +{/color} No Tattoos{color=#0000D8} +{/color} No Piercings{color=#0000D8} +{/color} Clothes" xalign 0.5 size 14 color "#000000" font "fonts/Segoe Print.ttf"
        add "spacer" size(0,2)
        if is_auspex_active:
            spacing(-2)
            text "Aura {color=#0000D8}={/color} No Devotion {color=#0000D8}-{/color} (No Despair {color=#0000D8}+{/color} Not Spoiled)" xalign 0.5 size 14 color "#000000" font "fonts/Segoe Print.ttf" 
            text "Charm    {color=#0000D8}={/color} Unknown{color=#0000D8} +{/color} Unknown{color=#0000D8} +{/color}{color=#" + dic_color_level[all_girls_list[girl_index]["attributes"]["style"]] + "} Style{/color}{color=#0000D8} +{/color} {color=#" + dic_color_level[all_girls_list[girl_index]["attributes"]["exoticism"]] + "}Exoticism{/color}{color=#0000D8} +{/color} Aura{color=#0000D8} +{/color} Weight{color=#0000D8} -{/color} No Scars{color=#0000D8} -{/color} No Bruises" xalign 0.5 size 14 color "#000000" font "fonts/Segoe Print.ttf" 
        else:
            text "You must cast Auspex to view the aura and charm rating of your slave" xalign 0.5 size 14 color "#000000" font "fonts/Segoe Print.ttf" 
screen slave_equipment_menu():
    add "bg/page_blank.webp" xsize 795 ysize 535 pos(0.5028,0.42) anchor (0.5,0.5)
    add equipment_choice_image + ".webp" xsize 160 ysize 120 pos(0.24,0.815)
    text equipment_choice_image_text size 15 color "#000000" font "fonts/Consolas.ttf" pos(0.40,0.82) xmaximum 500
    key "K_SPACE" action SetVariable("current_menu", 0),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
    if available_options != 2:
        key "K_1" action SetVariable("equipment_choice", dic_inventory_move_down[(dic_inventory_move_up[equipment_choice]+1) % 13]),Jump("Home")
        key "K_2" action SetVariable("equipment_choice", dic_inventory_move_down[(dic_inventory_move_up[equipment_choice]-1) % 13]),Jump("Home")
    if available_options == 2:
        key "K_1" action SetVariable("equipment_choice", dic_combat_move_down[(dic_combat_move_up[equipment_choice]+1) % 5]),Jump("Home")
        key "K_2" action SetVariable("equipment_choice", dic_combat_move_down[(dic_combat_move_up[equipment_choice]-1) % 5]),Jump("Home")
    vbox:
        pos(0.24,0.068)
        text "{u}SLAVE EQUIPMENT{/u}" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        if equipment_choice == "armour":
            textbutton "{u}Armour:{/u} [all_girls_list[girl_index]['equipment']['armour']]":
                style "slave_equipment_menu_button4" 
                action SetVariable("available_options", 2),SetVariable("equipment_choice", "armour")
        else:
            textbutton "{u}Armour:{/u} [all_girls_list[girl_index]['equipment']['armour']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 2),SetVariable("equipment_choice", "armour")
        if equipment_choice == "weapon":
            textbutton "{u}Left Hand:{/u} [all_girls_list[girl_index]['equipment']['weapon']]":
                style "slave_equipment_menu_button4"
                action SetVariable("available_options", 2),SetVariable("equipment_choice", "weapon")
        else:
            textbutton "{u}Left Hand:{/u} [all_girls_list[girl_index]['equipment']['weapon']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 2),SetVariable("equipment_choice", "weapon")
        if equipment_choice == "weapon2":
            textbutton "{u}Right Hand:{/u} [all_girls_list[girl_index]['equipment']['weapon2']]":
                style "slave_equipment_menu_button4"
                action SetVariable("available_options", 2),SetVariable("equipment_choice", "weapon2")
        else:
            textbutton "{u}Right Hand:{/u} [all_girls_list[girl_index]['equipment']['weapon2']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 2),SetVariable("equipment_choice", "weapon2")
        if equipment_choice == "amulet":
            textbutton "{u}Amulet:{/u} [all_girls_list[girl_index]['equipment']['amulet']]":
                style "slave_equipment_menu_button4"
                action SetVariable("available_options", 2),SetVariable("equipment_choice", "amulet")
        else:
            textbutton "{u}Amulet:{/u} [all_girls_list[girl_index]['equipment']['amulet']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 2),SetVariable("equipment_choice", "amulet")
        if equipment_choice == "ring":
            textbutton "{u}Ring:{/u} [all_girls_list[girl_index]['equipment']['ring']]":
                style "slave_equipment_menu_button4"
                action SetVariable("available_options", 2),SetVariable("equipment_choice", "ring")
        else:
            textbutton "{u}Ring:{/u} [all_girls_list[girl_index]['equipment']['ring']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 2),SetVariable("equipment_choice", "ring")
        add "spacer" size(0,20)
        if available_options != 1:
            textbutton "{u}Clothes:{/u} [all_girls_list[girl_index]['equipment']['clothes']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 1),SetVariable("equipment_choice", "clothes"), Jump("Home")

            textbutton "{u}Headgear:{/u} [all_girls_list[girl_index]['equipment']['headgear']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 1),SetVariable("equipment_choice", "headgear"), Jump("Home")

            textbutton "{u}Neck:{/u} [all_girls_list[girl_index]['equipment']['neck']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 1),SetVariable("equipment_choice", "neck"), Jump("Home")

            textbutton "{u}Hands:{/u} [all_girls_list[girl_index]['equipment']['hands']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 1),SetVariable("equipment_choice", "hands"), Jump("Home")

            textbutton "{u}Feet:{/u} [all_girls_list[girl_index]['equipment']['feet']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 1),SetVariable("equipment_choice", "feet"), Jump("Home")

            textbutton "{u}Ring 1:{/u} [all_girls_list[girl_index]['equipment']['ring1']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 1),SetVariable("equipment_choice", "ring1"), Jump("Home")

            textbutton "{u}Ring 2:{/u} [all_girls_list[girl_index]['equipment']['ring2']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 1),SetVariable("equipment_choice", "ring2"), Jump("Home")

            textbutton "{u}Earrings:{/u} [all_girls_list[girl_index]['equipment']['earrings']['type']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 1),SetVariable("equipment_choice", "earrings"), Jump("Home")

            textbutton "{u}Tongue:{/u} [all_girls_list[girl_index]['equipment']['tongue']['type']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 1),SetVariable("equipment_choice", "tongue"), Jump("Home")

            textbutton "{u}Nipples:{/u} [all_girls_list[girl_index]['equipment']['nipples']['type']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 1),SetVariable("equipment_choice", "nipples"), Jump("Home")

            textbutton "{u}Navel:{/u} [all_girls_list[girl_index]['equipment']['navel']['type']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 1),SetVariable("equipment_choice", "navel"), Jump("Home")

            textbutton "{u}Clitoris:{/u} [all_girls_list[girl_index]['equipment']['clitoris']['type']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 1),SetVariable("equipment_choice", "clitoris"), Jump("Home")

            textbutton "{u}Anus:{/u} [all_girls_list[girl_index]['equipment']['anus']]":
                style "slave_equipment_menu_button"
                action SetVariable("available_options", 1),SetVariable("equipment_choice", "anus"), Jump("Home")
        if available_options == 1:
            if equipment_choice == "clothes":
                textbutton "{u}Clothes:{/u} [all_girls_list[girl_index]['equipment']['clothes']]":
                    style "slave_equipment_menu_button4"
                    action SetVariable("available_options", 0),SetVariable("equipment_choice", "clothes"), Jump("Home")
            else:
                textbutton "{u}Clothes:{/u} [all_girls_list[girl_index]['equipment']['clothes']]":
                    style "slave_equipment_menu_button"
                    action SetVariable("equipment_choice", "clothes"), Jump("Home")
            if equipment_choice == "headgear":
                textbutton "{u}Headgear:{/u} [all_girls_list[girl_index]['equipment']['headgear']]":
                    style "slave_equipment_menu_button4"
                    action SetVariable("available_options", 0),SetVariable("equipment_choice", "headgear"), Jump("Home")
            else:
                textbutton "{u}Headgear:{/u} [all_girls_list[girl_index]['equipment']['headgear']]":
                    style "slave_equipment_menu_button"
                    action SetVariable("equipment_choice", "headgear"), Jump("Home")
            if equipment_choice == "neck":
                textbutton "{u}Neck:{/u} [all_girls_list[girl_index]['equipment']['neck']]":
                    style "slave_equipment_menu_button4"
                    action SetVariable("available_options", 0),SetVariable("equipment_choice", "neck"), Jump("Home")
            else:
                textbutton "{u}Neck:{/u} [all_girls_list[girl_index]['equipment']['neck']]":
                    style "slave_equipment_menu_button"
                    action SetVariable("equipment_choice", "neck"), Jump("Home")
            if equipment_choice == "hands":
                textbutton "{u}Hands:{/u} [all_girls_list[girl_index]['equipment']['hands']]":
                    style "slave_equipment_menu_button4"
                    action SetVariable("available_options", 0),SetVariable("equipment_choice", "hands"), Jump("Home")
            else:
                textbutton "{u}Hands:{/u} [all_girls_list[girl_index]['equipment']['hands']]":
                    style "slave_equipment_menu_button"
                    action SetVariable("equipment_choice", "hands"), Jump("Home")
            if equipment_choice == "feet":
                textbutton "{u}Feet:{/u} [all_girls_list[girl_index]['equipment']['feet']]":
                    style "slave_equipment_menu_button4"
                    action SetVariable("available_options", 0),SetVariable("equipment_choice", "feet"), Jump("Home")
            else:
                textbutton "{u}Feet:{/u} [all_girls_list[girl_index]['equipment']['feet']]":
                    style "slave_equipment_menu_button"
                    action SetVariable("equipment_choice", "feet"), Jump("Home")
            if equipment_choice == "ring1":
                textbutton "{u}Ring 1:{/u} [all_girls_list[girl_index]['equipment']['ring1']]":
                    style "slave_equipment_menu_button4"
                    action SetVariable("available_options", 0),SetVariable("equipment_choice", "ring1"), Jump("Home")
            else:
                textbutton "{u}Ring 1:{/u} [all_girls_list[girl_index]['equipment']['ring1']]":
                    style "slave_equipment_menu_button"
                    action SetVariable("equipment_choice", "ring1"), Jump("Home")
            if equipment_choice == "ring2":
                textbutton "{u}Ring 2:{/u} [all_girls_list[girl_index]['equipment']['ring2']]":
                    style "slave_equipment_menu_button4"
                    action SetVariable("available_options", 0),SetVariable("equipment_choice", "ring2"), Jump("Home")
            else:
                textbutton "{u}Ring 2:{/u} [all_girls_list[girl_index]['equipment']['ring2']]":
                    style "slave_equipment_menu_button"
                    action SetVariable("equipment_choice", "ring2"), Jump("Home")
            if equipment_choice == "earrings":
                textbutton "{u}Earrings:{/u} [all_girls_list[girl_index]['equipment']['earrings']['type']]":
                    style "slave_equipment_menu_button4"
                    action SetVariable("available_options", 0),SetVariable("equipment_choice", "earrings"), Jump("Home")
            else:
                textbutton "{u}Earrings:{/u} [all_girls_list[girl_index]['equipment']['earrings']['type']]":
                    style "slave_equipment_menu_button"
                    action SetVariable("equipment_choice", "earrings"), Jump("Home")
            if equipment_choice == "tongue":
                textbutton "{u}Tongue:{/u} [all_girls_list[girl_index]['equipment']['tongue']['type']]":
                    style "slave_equipment_menu_button4"
                    action SetVariable("available_options", 0),SetVariable("equipment_choice", "tongue"), Jump("Home")
            else:
                textbutton "{u}Tongue:{/u} [all_girls_list[girl_index]['equipment']['tongue']['type']]":
                    style "slave_equipment_menu_button"
                    action SetVariable("equipment_choice", "tongue"), Jump("Home")
            if equipment_choice == "nipples":
                textbutton "{u}Nipples:{/u} [all_girls_list[girl_index]['equipment']['nipples']['type']]":
                    style "slave_equipment_menu_button4"
                    action SetVariable("available_options", 0),SetVariable("equipment_choice", "nipples"), Jump("Home")
            else:
                textbutton "{u}Nipples:{/u} [all_girls_list[girl_index]['equipment']['nipples']['type']]":
                    style "slave_equipment_menu_button"
                    action SetVariable("equipment_choice", "nipples"), Jump("Home")
            if equipment_choice == "navel":
                textbutton "{u}Navel:{/u} [all_girls_list[girl_index]['equipment']['navel']['type']]":
                    style "slave_equipment_menu_button4"
                    action SetVariable("available_options", 0),SetVariable("equipment_choice", "navel"), Jump("Home")
            else:
                textbutton "{u}Navel:{/u} [all_girls_list[girl_index]['equipment']['navel']['type']]":
                    style "slave_equipment_menu_button"
                    action SetVariable("equipment_choice", "navel"), Jump("Home")
            if equipment_choice == "clitoris":
                textbutton "{u}Clitoris:{/u} [all_girls_list[girl_index]['equipment']['clitoris']['type']]":
                    style "slave_equipment_menu_button4"
                    action SetVariable("available_options", 0),SetVariable("equipment_choice", "clitoris"), Jump("Home")
            else:
                textbutton "{u}Clitoris:{/u} [all_girls_list[girl_index]['equipment']['clitoris']['type']]":
                    style "slave_equipment_menu_button"
                    action SetVariable("equipment_choice", "clitoris"), Jump("Home")
            if equipment_choice == "anus":
                textbutton "{u}Anus:{/u} [all_girls_list[girl_index]['equipment']['anus']]":
                    style "slave_equipment_menu_button4"
                    action SetVariable("available_options", 0),SetVariable("equipment_choice", "anus"), Jump("Home")
            else:
                textbutton "{u}Anus:{/u} [all_girls_list[girl_index]['equipment']['anus']]":
                    style "slave_equipment_menu_button"
                    action SetVariable("equipment_choice", "anus"), Jump("Home")
    if available_options == 0:
        button:
            xpos(0.62)
            ypos(0.1)
            xsize 200
            ysize 515
            action SetVariable("available_options", 1),Jump("Home")
    if available_options == 2:
        vbox:
            pos(0.76,0.068)
            anchor(1.0,0.0)
            spacing -2
            text "" size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
            for values in range(0,len(inventory_type[equipment_choice])):
                if all_girls_list[girl_index]["equipment"][equipment_choice] != dic_combat_full[inventory_type[equipment_choice][values]]:
                    if equipment_choice == "armour":
                        if values == 0:
                            textbutton "- Remove -" xalign 1.0: 
                                style "slave_equipment_menu_button2"
                                action SetDict(all_girls_list[girl_index]["equipment"], equipment_choice,"Without armour"),SetDict(inventory, inventory_track, inventory[inventory_track]+1),SetVariable("inventory_track", ""), Jump("Home")
                        elif inventory[inventory_type[equipment_choice][values]] > 0:
                            textbutton dic_combat_full[inventory_type[equipment_choice][values]] xalign 1.0:
                                style "slave_equipment_menu_button2"
                                action SetDict(all_girls_list[girl_index]["equipment"], equipment_choice, dic_combat_full[inventory_type[equipment_choice][values]]),SetDict(inventory, inventory_type[equipment_choice][values], inventory[inventory_type[equipment_choice][values]]-1),SetVariable("inventory_track", inventory_type[equipment_choice][values]),SetDict(inventory, inventory_track, inventory[inventory_track]+1), Jump("Home")
                        else:
                            textbutton dic_combat_full[inventory_type[equipment_choice][values]] xalign 1.0:
                                style "slave_equipment_menu_button"
                                action NullAction()
                    elif equipment_choice in ["amulet","ring"]:
                        if values == 0:
                            if all_girls_list[girl_index]["equipment"][equipment_choice] != "":
                                textbutton "- Remove -" xalign 1.0: 
                                    style "slave_equipment_menu_button2"
                                    action SetDict(all_girls_list[girl_index]["equipment"], equipment_choice,""),SetDict(inventory, inventory_track, inventory[inventory_track]+1),SetVariable("inventory_track", ""),Jump("Home")
                        elif inventory[inventory_type[equipment_choice][values]] > 0:
                            textbutton dic_combat_full[inventory_type[equipment_choice][values]] xalign 1.0:
                                style "slave_equipment_menu_button2"
                                action SetDict(all_girls_list[girl_index]["equipment"], equipment_choice, dic_combat_full[inventory_type[equipment_choice][values]]),SetDict(inventory, inventory_type[equipment_choice][values], inventory[inventory_type[equipment_choice][values]]-1),SetVariable("inventory_track", inventory_type[equipment_choice][values]),SetDict(inventory, inventory_track, inventory[inventory_track]+1), Jump("Home")
                        else:
                            textbutton dic_combat_full[inventory_type[equipment_choice][values]] xalign 1.0:
                                style "slave_equipment_menu_button"
                                action NullAction()
                    elif equipment_choice == "weapon":
                        python:
                            if all_girls_list[girl_index]["equipment"]["weapon"] != "Fist":
                                inventory_track_weapon = dic_combat_full_inv[all_girls_list[girl_index]["equipment"]["weapon"]]
                            else:
                                inventory_track_weapon = ""
                        if all_girls_list[girl_index]["equipment"]["weapon2"] != dic_combat_full[inventory_type[equipment_choice][values]] or all_girls_list[girl_index]["equipment"]["weapon2"] == "Fist":
                                if values == 0:
                                    textbutton "- Remove -" xalign 1.0: 
                                        style "slave_equipment_menu_button2"
                                        action SetDict(all_girls_list[girl_index]["equipment"], equipment_choice,"Fist"),SetDict(inventory, inventory_track_weapon, inventory[inventory_track_weapon]+1),SetVariable("inventory_track_weapon", ""),Jump("Home")
                                elif inventory[inventory_type[equipment_choice][values]] > 0:
                                    textbutton dic_combat_full[inventory_type[equipment_choice][values]] xalign 1.0:
                                        style "slave_equipment_menu_button2"
                                        action SetDict(all_girls_list[girl_index]["equipment"], equipment_choice, dic_combat_full[inventory_type[equipment_choice][values]]),SetDict(inventory, inventory_type[equipment_choice][values], inventory[inventory_type[equipment_choice][values]]-1),SetVariable("inventory_track_weapon", inventory_type[equipment_choice][values]),SetDict(inventory, inventory_track_weapon, inventory[inventory_track_weapon]+1), Jump("Home")
                                else:
                                    textbutton dic_combat_full[inventory_type[equipment_choice][values]] xalign 1.0:
                                        style "slave_equipment_menu_button"
                                        action NullAction()
                    elif equipment_choice == "weapon2":
                        python:
                            if all_girls_list[girl_index]["equipment"]["weapon2"] != "Fist":
                                inventory_track_weapon2 = dic_combat_full_inv[all_girls_list[girl_index]["equipment"]["weapon2"]]
                            else:
                                inventory_track_weapon2 = ""
                        if all_girls_list[girl_index]["equipment"]["weapon"] != dic_combat_full[inventory_type[equipment_choice][values]] or all_girls_list[girl_index]["equipment"]["weapon"] == "Fist":
                            if values == 0:
                                textbutton "- Remove -" xalign 1.0: 
                                    style "slave_equipment_menu_button2"
                                    action SetDict(all_girls_list[girl_index]["equipment"], equipment_choice,"Fist"),SetDict(inventory, inventory_track_weapon2, inventory[inventory_track_weapon2]+1),SetVariable("inventory_track_weapon2", ""),Jump("Home")
                            elif inventory[inventory_type[equipment_choice][values]] > 0:
                                textbutton dic_combat_full[inventory_type[equipment_choice][values]] xalign 1.0:
                                    style "slave_equipment_menu_button2"
                                    action SetDict(all_girls_list[girl_index]["equipment"], equipment_choice, dic_combat_full[inventory_type[equipment_choice][values]]),SetDict(inventory, inventory_type[equipment_choice][values], inventory[inventory_type[equipment_choice][values]]-1),SetVariable("inventory_track_weapon2", inventory_type[equipment_choice][values]),SetDict(inventory, inventory_track_weapon2, inventory[inventory_track_weapon2]+1), Jump("Home")
                            else:
                                textbutton dic_combat_full[inventory_type[equipment_choice][values]] xalign 1.0:
                                        style "slave_equipment_menu_button"
                                        action NullAction()


       
        vbox:   
            pos(0.62,0.068)
            spacing -2
            text "" size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
            if available_options == 2:
                for values in range(0,len(inventory_type[equipment_choice])):
                    if all_girls_list[girl_index]["equipment"][equipment_choice] != dic_combat_full[inventory_type[equipment_choice][values]]:
                        if (all_girls_list[girl_index]["equipment"]["weapon2"] != dic_combat_full[inventory_type[equipment_choice][values]] or all_girls_list[girl_index]["equipment"]["weapon2"] == "Fist") and (all_girls_list[girl_index]["equipment"]["weapon"] != dic_combat_full[inventory_type[equipment_choice][values]] or all_girls_list[girl_index]["equipment"]["weapon"] == "Fist"):
                            if inventory[inventory_type[equipment_choice][values]] == "-":
                                if all_girls_list[girl_index]["equipment"][equipment_choice] != "":
                                    text str(inventory[inventory_type[equipment_choice][values]]) xalign 0.5:
                                        style "slave_equipment_menu_button2_text"
                            elif inventory[inventory_type[equipment_choice][values]] > 0:
                                text str(inventory[inventory_type[equipment_choice][values]]) xalign 0.5:
                                    style "slave_equipment_menu_button2_text"
                            else:
                                text str(inventory[inventory_type[equipment_choice][values]]) xalign 0.5:
                                    style "slave_equipment_menu_button_text"

    vbox:
        pos(0.62,0.068)
        spacing -2  
        text "{u}AVAILABLE OPTIONS{/u}" size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        if available_options == 0:
            text "{u}Active effects:{/u}" size 14 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
            for key, values in all_girls_list[girl_index]["learning_bonus"].items(): 
                text "{color=009FEF}{u}Learning bonus{/u}{/color}: " + "{color=#0000D8}" + str(key) + "{/color}" + " " + str(values) xalign 1.0 size 10 color "#000000" font "fonts/Segoe Print.ttf"
            for key, values in all_girls_list[girl_index]["daily_bonus"].items():
                text "{color=009900}{u}Daily bonus{/u}{/color}: " + "{color=#0000D8}" + str(key) + "{/color}" + " " + str(values) xalign 1.0 size 10 color "#000000" font "fonts/Segoe Print.ttf"
            text "{color=6B0084}{u}Style bonus{/u}{/color}: " + str(all_girls_list[girl_index]["style_plus"]) xalign 1.0 size 10 color "#000000" font "fonts/Segoe Print.ttf"
            text "{color=6B0084}{u}Exotic bonus{/u}{/color}: " + str(all_girls_list[girl_index]["exotic_plus"]) xalign 1.0 size 10 color "#000000" font "fonts/Segoe Print.ttf"
            text "{color=6B0084}{u}Mood bonus for clothes{/u}{/color}: " + str(all_girls_list[girl_index]["worn_mood"]) xalign 1.0 size 10 color "#000000" font "fonts/Segoe Print.ttf"

        elif available_options == 1:
            for values in inventory_type[equipment_choice]:
                if all_girls_list[girl_index]["equipment"][equipment_choice] != dic_girl_clothing_full[values]["name"]:
                    if equipment_choice not in ["tongue","nipples","navel","clitoris","earrings"]:
                        if dic_girl_clothing_full[values]["name"] == "Naked":
                            textbutton "- Strip -" xalign 1.0:
                                style "slave_equipment_menu_button2"
                                action SetDict(all_girls_list[girl_index]["equipment"], equipment_choice, dic_girl_clothing_full[values]["name"]),SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]),SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"]),SetVariable("available_options", 0), Jump("equipment_check")
                        elif dic_girl_clothing_full[values]["name"] == "":
                            textbutton "- Remove -" xalign 1.0:
                                style "slave_equipment_menu_button2"
                                action SetDict(all_girls_list[girl_index]["equipment"], equipment_choice,""),SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]),SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"]),SetVariable("available_options", 0), Jump("equipment_check")
                        elif all_girls_list[girl_index]["equipment"]["aura_bound"][values] == True:
                            hbox:
                                xalign 1.0
                                textbutton dic_girl_clothing_full[values]["name"] xalign 1.0:
                                    style "slave_equipment_menu_button3"
                                    action SetDict(all_girls_list[girl_index]["equipment"], equipment_choice, dic_girl_clothing_full[values]["name"]),SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]),SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"]),SetVariable("available_options", 0), Jump("equipment_check")
                                    hovered SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]),SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"])
                                add "aurabound.webp" size(15,15) xalign 1.0 yalign 0.5
                        elif inventory[values] > 0:
                            textbutton dic_girl_clothing_full[values]["name"] xalign 1.0:
                                style "slave_equipment_menu_button2"
                                action SetDict(all_girls_list[girl_index]["equipment"], equipment_choice, dic_girl_clothing_full[values]["name"]), SetDict(inventory, values, inventory[values] - 1), SetDict(all_girls_list[girl_index]["equipment"]["aura_bound"], values, True),SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]),SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"]),SetVariable("available_options", 0), Jump("equipment_check")
                                hovered SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]),SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"])

                        else:
                            textbutton dic_girl_clothing_full[values]["name"] xalign 1.0:
                                style "slave_equipment_menu_button"
                                action SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]), SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"])
                                hovered SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]),SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"])

                    else:
                        if all_girls_list[girl_index]["equipment"][equipment_choice]["pierced"]:
                            if all_girls_list[girl_index]["equipment"][equipment_choice]["type"] != dic_girl_clothing_full[values]["name"]:
                                if all_girls_list[girl_index]["equipment"]["aura_bound"][values] == True:
                                    hbox:
                                        xalign 1.0
                                        textbutton dic_girl_clothing_full[values]["name"] xalign 1.0:
                                            style "slave_equipment_menu_button3"
                                            action SetDict(all_girls_list[girl_index]["equipment"][equipment_choice], "type", dic_girl_clothing_full[values]["name"]),SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]),SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"]),SetVariable("available_options", 0), Jump("equipment_check")
                                            hovered SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]),SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"])
                                        add "aurabound.webp" size(15,15) xalign 1.0 yalign 0.5
                                elif dic_girl_clothing_full[values]["name"] == "":
                                    textbutton "- Remove -" xalign 1.0:
                                        style "slave_equipment_menu_button2"
                                        action SetDict(all_girls_list[girl_index]["equipment"][equipment_choice], "type", ""),SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]),SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"]),SetVariable("available_options", 0), Jump("equipment_check")
                                elif inventory[values] > 0:
                                    textbutton dic_girl_clothing_full[values]["name"] xalign 1.0:
                                        style "slave_equipment_menu_button2"
                                        action SetDict(all_girls_list[girl_index]["equipment"][equipment_choice], "type", dic_girl_clothing_full[values]["name"]), SetDict(inventory, values, inventory[values] - 1), SetDict(all_girls_list[girl_index]["equipment"]["aura_bound"], values, True),SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]),SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"]),SetVariable("available_options", 0), Jump("equipment_check")
                                        hovered SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]),SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"])
                                else:
                                    textbutton dic_girl_clothing_full[values]["name"] xalign 1.0:
                                        style "slave_equipment_menu_button"
                                        action SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]), SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"])
                                        hovered SetVariable("equipment_choice_image", dic_girl_clothing_full[values]["icon"]),SetVariable("equipment_choice_image_text", dic_girl_clothing_full[values]["desc"])
            if equipment_choice in ["tongue","nipples","navel","clitoris","earrings"]:          
                if all_girls_list[girl_index]["equipment"][equipment_choice]["pierced"] == False:
                    textbutton equipment_choice + " (Not pierced)" xalign 1.0:
                        style "slave_equipment_menu_button"
                        action NullAction()
    vbox:   
        pos(0.62,0.068)
        spacing -2
        text "" size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        if available_options == 1:
            for values in inventory_type[equipment_choice]:
                if all_girls_list[girl_index]["equipment"][equipment_choice] != dic_girl_clothing_full[values]["name"]:
                    if equipment_choice not in ["tongue","nipples","navel","clitoris","earrings"]:
                        if inventory[values] == "-":
                            text str(inventory[values]) xalign 0.5:
                                style "slave_equipment_menu_button2_text"
                        elif inventory[values] > 0:
                            text str(inventory[values]) xalign 0.5:
                                style "slave_equipment_menu_button2_text"
                        else:
                            text str(inventory[values]) xalign 0.5:
                                style "slave_equipment_menu_button_text"
                    else:
                        if all_girls_list[girl_index]["equipment"][equipment_choice]["pierced"]:
                            if all_girls_list[girl_index]["equipment"][equipment_choice]["type"] != dic_girl_clothing_full[values]["name"]:
                                if dic_girl_clothing_full[values]["name"] == "":
                                    text "-" xalign 0.5:
                                        style "slave_equipment_menu_button2_text"
                                elif inventory[values] > 0:
                                    text str(inventory[values]) xalign 0.5:
                                        style "slave_equipment_menu_button2_text"
                                else:
                                    text str(inventory[values]) xalign 0.5:
                                        style "slave_equipment_menu_button_text"
screen slave_aura_menu():
    add "page_aura.webp" xsize 795 ysize 535 pos(0.5028,0.42) anchor (0.5,0.5)
    key "K_SPACE" action SetVariable("current_menu", 0),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
    if not is_auspex_active:
        text dic_slave_aura_conditions["nocast"] size 18 color "#000000" font "fonts/Consolas.ttf" pos(0.21,0.82) xmaximum 750  
        textbutton "Cast auspex ( 2 sparks)" pos(0.40,0.92):
            style "slave_aura_button"
            action Show("home_menu_auspex") ,SetVariable("sparks_37",sparks_37 -2)
    else:
        text dic_slave_aura_conditions["casted"] size 18 color "#000000" font "fonts/Consolas.ttf" pos(0.21,0.82) xmaximum 750  
    if is_auspex_active:
        vbox: 
            pos (0.22,0.08)
            spacing(20)
            if aura_is_hover and "obedience" == aura_check_hover:
                if all_girls_list[girl_index]["obedience"] >= 0 and all_girls_list[girl_index]["obedience"] < 10:
                    textbutton aura_descriptions_no_color["obedience"][all_girls_list[girl_index]["obedience"]] xmaximum 750:
                        style "aura_description_button"
                        action NullAction()
                        hovered SetVariable("aura_is_hover", True), SetVariable("aura_check_hover", "obedience"), Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", "obedience")
                        unhovered SetVariable("aura_is_hover", False), Hide("description_slave_attributes")
                elif all_girls_list[girl_index]["obedience"] > 9:
                    textbutton aura_descriptions_no_color["obedience"][10] xmaximum 750:
                        style "aura_description_button"
                        action NullAction()
                        hovered SetVariable("aura_is_hover", True), SetVariable("aura_check_hover", "obedience"), Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", "obedience")
                        unhovered SetVariable("aura_is_hover", False), Hide("description_slave_attributes")
                elif all_girls_list[girl_index]["obedience"] < 0 and all_girls_list[girl_index]["obedience"] > -10:
                    textbutton aura_descriptions_no_color["obedience"][(all_girls_list[girl_index]["obedience"])*-1 + 10] xmaximum 750:
                        style "aura_description_button"
                        action NullAction()
                        hovered SetVariable("aura_is_hover", True), SetVariable("aura_check_hover", "obedience"), Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", "obedience")
                        unhovered SetVariable("aura_is_hover", False), Hide("description_slave_attributes")
                elif all_girls_list[girl_index]["obedience"] < -9:
                    textbutton aura_descriptions_no_color["obedience"][-1] xmaximum 750:
                        style "aura_description_button"
                        action NullAction()
                        hovered SetVariable("aura_is_hover", True), SetVariable("aura_check_hover", "obedience"), Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", "obedience")
                        unhovered SetVariable("aura_is_hover", False), Hide("description_slave_attributes")
            else:
                if all_girls_list[girl_index]["obedience"] >= 0 and all_girls_list[girl_index]["obedience"] < 10:
                    textbutton aura_descriptions["obedience"][all_girls_list[girl_index]["obedience"]] xmaximum 750:
                        style "aura_description_button"
                        action NullAction()
                        hovered SetVariable("aura_is_hover", True), SetVariable("aura_check_hover", "obedience"), Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", "obedience")
                        unhovered SetVariable("aura_is_hover", False), Hide("description_slave_attributes")
                elif all_girls_list[girl_index]["obedience"] > 9:
                    textbutton aura_descriptions_no_color["obedience"][10] xmaximum 750:
                        style "aura_description_button"
                        action NullAction()
                        hovered SetVariable("aura_is_hover", True), SetVariable("aura_check_hover", "obedience"), Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", "obedience")
                        unhovered SetVariable("aura_is_hover", False), Hide("description_slave_attributes")
                elif all_girls_list[girl_index]["obedience"] < 0 and all_girls_list[girl_index]["obedience"] > -10:
                    textbutton aura_descriptions["obedience"][(all_girls_list[girl_index]["obedience"])*-1 + 10] xmaximum 750:
                        style "aura_description_button"
                        action NullAction()
                        hovered SetVariable("aura_is_hover", True), SetVariable("aura_check_hover", "obedience"), Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", "obedience")
                        unhovered SetVariable("aura_is_hover", False), Hide("description_slave_attributes")
                elif all_girls_list[girl_index]["obedience"] < -9:
                    textbutton aura_descriptions["obedience"][-1] xmaximum 750:
                        style "aura_description_button"
                        action NullAction()
                        hovered SetVariable("aura_is_hover", True), SetVariable("aura_check_hover", "obedience"), Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", "obedience")
                        unhovered SetVariable("aura_is_hover", False), Hide("description_slave_attributes")
            if aura_is_hover and "supermacy" == aura_check_hover:
                python:
                    supermacy_text = ""
                    if master_supermacy - all_girls_list[girl_index]["supermacy"] > 2:
                        supermacy_text = aura_descriptions_no_color["supermacy"][4]
                    if master_supermacy > all_girls_list[girl_index]["supermacy"]:
                        supermacy_text = aura_descriptions_no_color["supermacy"][3]
                    if master_supermacy == all_girls_list[girl_index]["supermacy"]:
                        supermacy_text = aura_descriptions_no_color["supermacy"][2]
                    if master_supermacy < all_girls_list[girl_index]["supermacy"]:
                        supermacy_text = aura_descriptions_no_color["supermacy"][1]
                    if master_supermacy - all_girls_list[girl_index]["supermacy"] < -2:
                        supermacy_text = aura_descriptions_no_color["supermacy"][0]
                textbutton supermacy_text xmaximum 750:
                    style "aura_description_button"
                    action NullAction()
                    hovered SetVariable("aura_is_hover", True), SetVariable("aura_check_hover", "supermacy")
                    unhovered SetVariable("aura_is_hover", False)      
                
            else:
                python:
                    supermacy_text = ""
                    if master_supermacy - all_girls_list[girl_index]["supermacy"] > 2:
                        supermacy_text = aura_descriptions["supermacy"][4]
                    if master_supermacy > all_girls_list[girl_index]["supermacy"]:
                        supermacy_text = aura_descriptions["supermacy"][3]
                    if master_supermacy == all_girls_list[girl_index]["supermacy"]:
                        supermacy_text = aura_descriptions["supermacy"][2]
                    if master_supermacy < all_girls_list[girl_index]["supermacy"]:
                        supermacy_text = aura_descriptions["supermacy"][1]
                    if master_supermacy - all_girls_list[girl_index]["supermacy"] < -2:
                        supermacy_text = aura_descriptions["supermacy"][0]                
                textbutton supermacy_text xmaximum 750:
                    style "aura_description_button"
                    action NullAction()
                    hovered SetVariable("aura_is_hover", True), SetVariable("aura_check_hover", "supermacy")
                    unhovered SetVariable("aura_is_hover", False)

            if aura_is_hover and "arousal" == aura_check_hover: 
                textbutton aura_descriptions2_no_color["arousal"][all_girls_list[girl_index]["arousal"]] xmaximum 750:
                    style "aura_description_button"
                    action NullAction()
                    hovered SetVariable("aura_is_hover", True), SetVariable("aura_check_hover", "arousal")
                    unhovered SetVariable("aura_is_hover", False)
            else:
                textbutton aura_descriptions2["arousal"][all_girls_list[girl_index]["arousal"]] xmaximum 750:
                    style "aura_description_button"
                    action NullAction()
                    hovered SetVariable("aura_is_hover", True), SetVariable("aura_check_hover", "arousal")
                    unhovered SetVariable("aura_is_hover", False)

            # Display aura description buttons in a loop
            for aura_key in ["fear", "despair", "awareness", "taming", "habit", "spoil", "devotion"]:
                if aura_is_hover and aura_key == aura_check_hover: 
                    textbutton aura_descriptions2_no_color[aura_key][all_girls_list[girl_index]["aura"][aura_key]] xmaximum 750:
                        style "aura_description_button"
                        action NullAction()
                        hovered SetVariable("aura_is_hover", True), SetVariable("aura_check_hover", aura_key),Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", aura_key)
                        unhovered SetVariable("aura_is_hover", False),Hide("description_slave_attributes")
                else:
                    textbutton aura_descriptions2[aura_key][all_girls_list[girl_index]["aura"][aura_key]] xmaximum 750:
                        style "aura_description_button"
                        action NullAction()
                        hovered SetVariable("aura_is_hover", True), SetVariable("aura_check_hover", aura_key),Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", aura_key)
                        unhovered SetVariable("aura_is_hover", False)
screen slave_rules_menu():
    add all_girls_list[girl_index]["fullimage"] + ".webp" xalign 0.5 yalign 0.1838 size(795,535)  
    add "padding.webp" xsize 230 ysize 535 pos(0.2835,0.42) anchor (0.5,0.5)
    add "padding.webp" xsize 230 ysize 535 pos(0.724,0.42) anchor (0.5,0.5)
    key "K_SPACE" action SetVariable("current_menu", 0),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
    text dic_slave_conditions[text_slave_conditions_index] size 18 color "#000000" font "fonts/Consolas.ttf" pos(0.21,0.82) xmaximum 750
    vbox:
        pos(0.20,0.05)
        anchor (0.0,0.0)
        text "SLEEP:" size 16 color "#FFD700" font "fonts/Segoe Print.ttf"
        add "spacer" size(0,138)
        text "DIET:" size 16 color "#FFD700" font "fonts/Segoe Print.ttf"  
        add "spacer" size(0,138)
        text "PORTION SIZE:" size 16 color "#FFD700" font "fonts/Segoe Print.ttf"
        add "spacer" size(0,110)
        text "CALORIES REMAINING:" size 16 color "#FFD700" font "fonts/Segoe Print.ttf"
    vbox:
        pos(0.205,0.095)
        anchor (0.0,0.0)
        spacing 6
        for i in range(5):
            if all_girls_list[girl_index]["sleep"] == i:
                imagebutton:
                    idle "buttons/sel_button.webp"
                    hover "buttons/sel_button_hover.webp"
                    action NullAction()
            else:
                imagebutton:
                    idle "buttons/unsel_button.webp"
                    hover "buttons/unsel_button_hover.webp"
                    action SetDict(all_girls_list[girl_index], "sleep", i),SetVariable("text_slave_conditions_index",dic_slave_conditions_sleep[i]), Jump("Home")
        add "spacer" size(0,19.5)
        for i in range(3):
            if all_girls_list[girl_index]["diet"] == i:
                imagebutton:
                    idle "buttons/sel_button.webp"
                    hover "buttons/sel_button_hover.webp"
                    action SetDict(all_girls_list[girl_index], "diet", 3),SetVariable("text_slave_conditions_index", dic_slave_conditions_food[3]), Jump("Home")
            else:
                imagebutton:
                    idle "buttons/unsel_button.webp"
                    hover "buttons/unsel_button_hover.webp"
                    action SetDict(all_girls_list[girl_index], "diet", i),SetVariable("text_slave_conditions_index", dic_slave_conditions_food[i]), Jump("Home")
        if all_girls_list[girl_index]["your_leftovers"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index], "your_leftovers", False), SetVariable("text_slave_conditions_index","No_leftovers"), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index], "your_leftovers", True), SetVariable("text_slave_conditions_index","Eats_leftovers"), Jump("Home")
        if all_girls_list[girl_index]["supplements"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index], "supplements", False), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index], "supplements", True),SetVariable("text_slave_conditions_index","supplements"), Jump("Home")
        add "spacer" size(0,19.5)
       
        if all_girls_list[girl_index]["diet"] != 3:
            for i in range(4):
                if all_girls_list[girl_index]["portion_size"] == i:
                    imagebutton:
                        idle "buttons/sel_button.webp"
                        hover "buttons/sel_button_hover.webp"
                        action NullAction()
                else:
                    imagebutton:
                        idle "buttons/unsel_button.webp"
                        hover "buttons/unsel_button_hover.webp"
                        action SetDict(all_girls_list[girl_index], "portion_size", i),SetVariable("text_slave_conditions_index",dic_slave_conditions_portion[i]), Jump("Home")
        else:
            for i in range(4):
                imagebutton:
                    idle "buttons/unactive_button.webp"
                    hover "buttons/unactive_button_hover.webp"
                    action SetDict(all_girls_list[girl_index], "diet", 0),SetDict(all_girls_list[girl_index], "portion_size", i),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[0]), Jump("Home")
    vbox:
        pos(0.225,0.09)
        anchor (0.0,0.0)
        textbutton "- In the cells": 
            style "slave_screen_order_button"
            action SetDict(all_girls_list[girl_index], "sleep", 0),SetVariable("text_slave_conditions_index","in_the_cells"), Jump("Home")
        textbutton "- On the floor": 
            style "slave_screen_order_button"
            action SetDict(all_girls_list[girl_index], "sleep", 1),SetVariable("text_slave_conditions_index","On_the_floor"), Jump("Home")
        textbutton "- On a bedroll": 
            style "slave_screen_order_button"
            action SetDict(all_girls_list[girl_index], "sleep", 2),SetVariable("text_slave_conditions_index","On_a_bedroll"), Jump("Home")
        textbutton "- In my bed": 
            style "slave_screen_order_button"
            action SetDict(all_girls_list[girl_index], "sleep", 3),SetVariable("text_slave_conditions_index","In_my_bed"), Jump("Home")
        textbutton "- Do not sleep": 
            style "slave_screen_order_button"
            action SetDict(all_girls_list[girl_index], "sleep", 4),SetVariable("text_slave_conditions_index","Do_not_sleep"), Jump("Home")
        add "spacer" size(0,25)
        if all_girls_list[girl_index]["diet"] == 0:
            textbutton "- Dehydrated food": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 3),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[3]), Jump("Home")
        else:
            textbutton "- Dehydrated food": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 0),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[0]), Jump("Home")
        if all_girls_list[girl_index]["diet"] == 1:
            textbutton "- Canned food": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 3),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[3]), Jump("Home")
        else:
            textbutton "- Canned food": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 1),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[1]), Jump("Home")
        if all_girls_list[girl_index]["diet"] == 2:
            textbutton "- Fiend's cum": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 3),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[3]), Jump("Home")
        else:
            textbutton "- Fiend's cum": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 2),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[2]), Jump("Home")
        if all_girls_list[girl_index]["your_leftovers"]:
            textbutton "- Your leftovers": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "your_leftovers", False), SetVariable("text_slave_conditions_index","No_leftovers"), Jump("Home")
        else:
            textbutton "- Your leftovers": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "your_leftovers", True), SetVariable("text_slave_conditions_index","Eats_leftovers"), Jump("Home")
        if all_girls_list[girl_index]["supplements"]:
            textbutton "- Supplements": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "supplements", False), Jump("Home")
        else:
            textbutton "- Supplements": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "supplements", True),SetVariable("text_slave_conditions_index","supplements"), Jump("Home")
        add "spacer" size(0,25)
        if all_girls_list[girl_index]["diet"] != 3:
            textbutton "- Restricted":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "portion_size", 0),SetVariable("text_slave_conditions_index",dic_slave_conditions_portion[0]), Jump("Home")
            textbutton "- Moderate":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "portion_size", 1),SetVariable("text_slave_conditions_index",dic_slave_conditions_portion[1]), Jump("Home")
            textbutton "- Generous":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "portion_size", 2),SetVariable("text_slave_conditions_index",dic_slave_conditions_portion[2]), Jump("Home")
            textbutton "- Calculated":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "portion_size", 3),SetVariable("text_slave_conditions_index",dic_slave_conditions_portion[3]), Jump("Home")
        else:
            textbutton "- Restricted":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 0),SetDict(all_girls_list[girl_index], "portion_size", 0),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[0]), Jump("Home")
            textbutton "- Moderate":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 0),SetDict(all_girls_list[girl_index], "portion_size", 1),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[0]), Jump("Home")
            textbutton "- Generous":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 0),SetDict(all_girls_list[girl_index], "portion_size", 2),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[0]), Jump("Home")
            textbutton "- Calculated":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 0),SetDict(all_girls_list[girl_index], "portion_size", 3),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[0]), Jump("Home")
                
        add "spacer" size(0,25)
        textbutton "  2000":
            style "slave_screen_order_button"
            action NullAction()
    vbox:
        pos(0.807,0.05)
        anchor (1.0,0.0)
        if all_girls_list[girl_index]["rules"]["rules_count"] >= dic_overnight_rules_count[dic_overnight_rules_count_index]:
            text "{color=#FFD700}RULES: ([str(all_girls_list[girl_index]['rules']['rules_count'])]){/color}" size 16 font "fonts/Segoe Print.ttf"
        else:
            text "{color=#FFD700}RULES: ({/color}{color=#CD0000}[str(all_girls_list[girl_index]['rules']['rules_count'])]{/color}{color=#FFD700}){/color}" size 16 font "fonts/Segoe Print.ttf"
    vbox:
        pos(0.802,0.095)
        anchor (1.0,0.0)
        spacing 6
        if all_girls_list[girl_index]["rules"]["act_as_cook"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_cook", False),SetVariable("text_slave_conditions_index","cook_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_cook", True),SetVariable("text_slave_conditions_index","cook_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")

        if all_girls_list[girl_index]["rules"]["act_as_maid"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_maid", False),SetVariable("text_slave_conditions_index","maid_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_maid", True),SetVariable("text_slave_conditions_index","maid_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["bath_slave"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "bath_slave", False),SetVariable("text_slave_conditions_index","bath_slave_abort_rule"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "bath_slave", True),SetVariable("text_slave_conditions_index","bath_slave_rule"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_alarm"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_alarm", False),SetVariable("text_slave_conditions_index","behave_alarm_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_alarm", True),SetVariable("text_slave_conditions_index","behave_alarm_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_humility"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_humility", False),SetVariable("text_slave_conditions_index","behave_humility_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_humility", True),SetVariable("text_slave_conditions_index","behave_humility_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_pet"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_pet", False),SetVariable("text_slave_conditions_index","behave_pet_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_pet", True),SetVariable("text_slave_conditions_index","behave_pet_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_silence"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_silence", False),SetVariable("text_slave_conditions_index","behave_silence_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_silence", True),SetVariable("text_slave_conditions_index","behave_silence_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_toilet"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_toilet", False),SetVariable("text_slave_conditions_index","behave_toilet_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_toilet", True),SetVariable("text_slave_conditions_index","behave_toilet_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_urinal"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_urinal", False),SetVariable("text_slave_conditions_index","behave_urinal_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_urinal", True),SetVariable("text_slave_conditions_index","behave_urinal_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["deny_orgasm"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_orgasm", False),SetVariable("text_slave_conditions_index","deny_orgasm_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_orgasm", True),SetVariable("text_slave_conditions_index","deny_orgasm_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["deny_toileting"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_toileting", False),SetVariable("text_slave_conditions_index","deny_toileting_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_toileting", True),SetVariable("text_slave_conditions_index","deny_toileting_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["milk_the_fiend"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "milk_the_fiend", False),SetVariable("text_slave_conditions_index","slave_tentacle_rule_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "milk_the_fiend", True),SetVariable("text_slave_conditions_index","slave_tentacle_rule"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["no_masturbation"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "no_masturbation", False),SetVariable("text_slave_conditions_index","no_masturbation_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "no_masturbation", True),SetVariable("text_slave_conditions_index","no_masturbation_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["use_vaginal_beads"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "use_vaginal_beads", False),SetVariable("text_slave_conditions_index","use_vaginal_beads_rule_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "use_vaginal_beads", True),SetVariable("text_slave_conditions_index","use_vaginal_beads_rule"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["enforce_rules"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "enforce_rules", False),SetVariable("text_slave_conditions_index","enforce_rules_abort"), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "enforce_rules", True),SetVariable("text_slave_conditions_index","enforce_rules"), Jump("Home")
    vbox:
        pos(0.65,0.09)
        anchor (0.0,0.0)
        if all_girls_list[girl_index]["rules"]["act_as_cook"]:
            textbutton "Act as cook -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_cook", False),SetVariable("text_slave_conditions_index","cook_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            textbutton "Act as cook -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_cook", True),SetVariable("text_slave_conditions_index","cook_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["act_as_maid"]:
            textbutton "Act as maid -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_maid", False),SetVariable("text_slave_conditions_index","maid_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            textbutton "Act as maid -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_maid", True),SetVariable("text_slave_conditions_index","maid_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["bath_slave"]:
            textbutton "Bath slave -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "bath_slave", False),SetVariable("text_slave_conditions_index","bath_slave_rule"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            textbutton "Bath slave -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "bath_slave", True),SetVariable("text_slave_conditions_index","bath_slave_abort_rule"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_alarm"]:
            textbutton "Behave: alarm -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_alarm", False),SetVariable("text_slave_conditions_index","behave_alarm_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            textbutton "Behave: alarm -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_alarm", True),SetVariable("text_slave_conditions_index","behave_alarm_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_humility"]:
            textbutton "Behave: humility -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_humility", False),SetVariable("text_slave_conditions_index","behave_humility_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            textbutton "Behave: humility -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_humility", True),SetVariable("text_slave_conditions_index","behave_humility_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_pet"]:
            textbutton "Behave: pet -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_pet", False),SetVariable("text_slave_conditions_index","behave_pet_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            textbutton "Behave: pet -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_pet", True),SetVariable("text_slave_conditions_index","behave_pet_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        
        if all_girls_list[girl_index]["rules"]["behave_silence"]:
            textbutton "Behave: silence -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_silence", False),SetVariable("text_slave_conditions_index","behave_silence_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            textbutton "Behave: silence -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_silence", True),SetVariable("text_slave_conditions_index","behave_silence_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_toilet"]:
            textbutton "Behave: toilet -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_toilet", False),SetVariable("text_slave_conditions_index","behave_toilet_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            textbutton "Behave: toilet -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_toilet", True),SetVariable("text_slave_conditions_index","behave_toilet_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_urinal"]:
            textbutton "Behave: urinal -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_urinal", False),SetVariable("text_slave_conditions_index","behave_urinal_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            textbutton "Behave: urinal -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_urinal", True),SetVariable("text_slave_conditions_index","behave_urinal_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["deny_orgasm"]:
            textbutton "Deny orgasm -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_orgasm", False),SetVariable("text_slave_conditions_index","deny_orgasm_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            textbutton "Deny orgasm -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_orgasm", True),SetVariable("text_slave_conditions_index","deny_orgasm_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["deny_toileting"]:
            textbutton "Deny toileting -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_toileting", False),SetVariable("text_slave_conditions_index","deny_toileting_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            textbutton "Deny toileting -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_toileting", True),SetVariable("text_slave_conditions_index","deny_toileting_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["milk_the_fiend"]:
            textbutton "Milk the fiend -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "milk_the_fiend", False),SetVariable("text_slave_conditions_index","slave_tentacle_rule"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            textbutton "Milk the fiend -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "milk_the_fiend", True),SetVariable("text_slave_conditions_index","slave_tentacle_rule_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["no_masturbation"]:
            textbutton "No masturbation -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "no_masturbation", False),SetVariable("text_slave_conditions_index","no_masturbation_rules"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            textbutton "No masturbation -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "no_masturbation", True),SetVariable("text_slave_conditions_index","no_masturbation_rules_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["use_vaginal_beads"]:
            textbutton "Use vaginal beads -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "use_vaginal_beads", False),SetVariable("text_slave_conditions_index","use_vaginal_beads_rule"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] - 1), Jump("Home")
        else:
            textbutton "Use vaginal beads -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "use_vaginal_beads", True),SetVariable("text_slave_conditions_index","use_vaginal_beads_rule_abort"),SetDict(all_girls_list[girl_index]["rules"],"rules_count",all_girls_list[girl_index]["rules"]["rules_count"] + 1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["enforce_rules"]:
            textbutton "Enforce rules -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "enforce_rules", False),SetVariable("text_slave_conditions_index","enforce_rules_abort"), Jump("Home")
        else:
            textbutton "Enforce rules -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "enforce_rules", True),SetVariable("text_slave_conditions_index","enforce_rules"), Jump("Home")
screen screen_rules():   
    add bgstyle3 xsize 1280 ysize 720
    add home_decoration_mini xsize 795 ysize 535 pos(0.5028,0.42) anchor (0.5,0.5)
    imagebutton:
        idle "buttons/close_button.webp" pos (1004,1)
        hover "buttons/close_button_hover.webp"
        action SetVariable("current_menu", 0),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
    hbox:
        pos(0.475,0.01)
        anchor (0.5,0.0)
        spacing 0
        button:
            xsize 185
            ysize 40
            style "slave_screen_button"
            action SetVariable("current_menu", 100),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
        button:
            xsize 185
            ysize 40
            style "slave_screen_button"
            action SetVariable("current_menu", 101),Jump("Home")
        button:
            xsize 185
            ysize 40
            style "slave_screen_button"
            action SetVariable("current_menu", 102),Jump("Home")
        button:
            xsize 185
            ysize 40
            style "slave_screen_button"
            action SetVariable("current_menu", 103),Jump("Home")
    
    
    hbox: 
        pos(0.475,0.01)
        anchor (0.5,0.0)
        spacing 122
        textbutton "Rules":
            style "slave_screen_button"
            action SetVariable("current_menu", 100),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
        textbutton "Anatomy":
            style "slave_screen_button"
            action SetVariable("current_menu", 101),Jump("Home")
        textbutton "Equipment":
            style "slave_screen_button"
            action SetVariable("current_menu", 102),Jump("Home")
        textbutton "Aura":
            style "slave_screen_button"
            action SetVariable("current_menu", 103),Jump("Home")   



    
    hbox: 
        pos(0.525,0.005)
        anchor (0.50,0.0)
        spacing 162 
        if current_menu == 100:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action NullAction()
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetVariable("current_menu", 100),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
        if current_menu == 101:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action NullAction()
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetVariable("current_menu", 101),Jump("Home")
        if current_menu == 102:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action NullAction()
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetVariable("current_menu", 102),Jump("Home")
        if current_menu == 103:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action NullAction()
        else:
            imagebutton:
                idle "buttons/unsel_button.webp" 
                hover "buttons/unsel_button_hover.webp"
                action SetVariable("current_menu", 103),Jump("Home")
    vbox:
        pos(0.01,0.02)
        text "Name: " + all_girls_list[girl_index]["name"] size 16 color "#000000" font "fonts/Segoe Print.ttf"
        text "Age: " + dic_girl_age_text[all_girls_list[girl_index]["age"]] size 16 color "#000000" font "fonts/Segoe Print.ttf"
        text "Owned for: " + str(day_tracker - all_girls_list[girl_index]["day_bought"]) + " days" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        text "Rank:" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        text "{u}ATTRIBUTES{/u}" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        for key, values in dic_slave_attributes.items():
            if key != "physical":
                textbutton values[all_girls_list[girl_index]["attributes"][key]]:
                    style "attribute_custom_slave" + str(all_girls_list[girl_index]["attributes"][key])
                    action SetVariable("attribute_track_index",key),SetVariable("attribute_track_basic",key),SetVariable("dictionary_track_index",7),SetVariable("dictionary_name",dic_slave_attributes),SetVariable("attribute_checkbox",True),SetVariable("attributeisphysical",False),Jump("Home")
                    hovered Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", key)
                    unhovered Hide("description_slave_attributes")
            else:
                textbutton values[all_girls_list[girl_index]["attributes"][key]]:
                    style "attribute_custom_physical_special" + str(all_girls_list[girl_index]["attributes"][key])
                    action SetVariable("attribute_track_index",key),SetVariable("attribute_track_basic",key),SetVariable("dictionary_track_index",7),SetVariable("dictionary_name",dic_slave_attributes),SetVariable("attribute_checkbox",True),SetVariable("attributeisphysical",True),Jump("Home")                    
                    hovered Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", key)
                    unhovered Hide("description_slave_attributes")
        text "Mood" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        text "{u}TRAITS{/u}" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        python:
            traits_skills = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_skills(1/8)"]
            traits_sexual = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_sexual(1/10)"]
            traits_miscellaneous = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_miscellaneous(1/12)"]
            traits_aura = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_aura(1/16)"]
            traits_attributes = all_girls_list[girl_index]["traits"]["traits_hidden"]["traits_attributes(1/20)"]
        for key, values in dic_traits_skills.items():

            $ skill_info = traits_skills[key]
            $ val = skill_info.get("value", 0)
            $ revealed = skill_info.get("revealed", False)
            if val != 0 and revealed:
                if val == -1:
                    $ style_used = "slave_traits_bad1"
                elif val == -2:
                    $ style_used = "slave_traits_bad2"
                elif val == 1:
                    $ style_used = "slave_traits_good1"
                elif val == 2:
                    $ style_used = "slave_traits_good2"
                else:
                    $ style_used = "default_style"

                # Make sure values[val] exists or adjust to keys, here example:
                $ label_text = values.get(val, "Unknown") if isinstance(values, dict) else values[val]

                textbutton label_text:
                    style style_used
                    action SetVariable("attribute_track_index", key), SetVariable("dictionary_track_index", val), SetVariable("dictionary_name", dic_traits_skills_descriptions), SetVariable("customboxcheck", True), Jump("Home")
                    hovered Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", "default")
                    unhovered Hide("description_slave_attributes")
            ################ - i'm a genus -rec3ks
        for key, values in dic_traits_sexual.items():
           
            $ skill_info = traits_sexual[key]
            $ val = skill_info.get("value", 0)
            $ revealed = skill_info.get("revealed", False)

            if val != 0 and revealed:
                if val == -1:
                    $ style_used = "slave_traits_bad1"
                elif val == -2:
                    $ style_used = "slave_traits_bad2"
                elif val == 1:
                    $ style_used = "slave_traits_good1"
                elif val == 2:
                    $ style_used = "slave_traits_good2"
                else:
                    $ style_used = "default_style"

                # Get the description from values dict or list
                $ label_text = values.get(val, "Unknown") if isinstance(values, dict) else values[val]

                textbutton label_text:
                    style style_used
                    action SetVariable("attribute_track_index", key), SetVariable("dictionary_track_index", val), SetVariable("dictionary_name", dic_traits_sexual_description), SetVariable("customboxcheck", True), Jump("Home")
                    hovered Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", "default")
                    unhovered Hide("description_slave_attributes")
        for key, values in dic_traits_miscellaneous.items():

            $ skill_info = traits_miscellaneous[key]
            $ val = skill_info.get("value", 0)
            $ revealed = skill_info.get("revealed", False)

            if val != 0 and revealed:
                if val == -1:
                    $ style_used = "slave_traits_bad1"
                elif val == -2:
                    $ style_used = "slave_traits_bad2"
                elif val == 1:
                    $ style_used = "slave_traits_good1"
                elif val == 2:
                    $ style_used = "slave_traits_good2"
                else:
                    $ style_used = "default_style"

                $ label_text = values.get(val, "Unknown") if isinstance(values, dict) else values[val]

                textbutton label_text:
                    style style_used
                    action SetVariable("attribute_track_index", key),SetVariable("dictionary_track_index", val),SetVariable("dictionary_name", dic_traits_miscellaneous_description),SetVariable("customboxcheck", True),Jump("Home")
                    hovered Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", "wip")
                    unhovered Hide("description_slave_attributes")
        for key, values in dic_traits_aura.items():

            $ skill_info = traits_aura[key]
            $ val = skill_info.get("value", 0)
            $ revealed = skill_info.get("revealed", False)

            if val != 0 and revealed:
                if val == -1:
                    $ style_used = "slave_traits_bad1"
                elif val == -2:
                    $ style_used = "slave_traits_bad2"
                elif val == 1:
                    $ style_used = "slave_traits_good1"
                elif val == 2:
                    $ style_used = "slave_traits_good2"
                else:
                    $ style_used = "default_style"

                $ label_text = values.get(val, "Unknown") if isinstance(values, dict) else values[val]

                textbutton label_text:
                    style style_used
                    action SetVariable("attribute_track_index", key),SetVariable("dictionary_track_index", val),SetVariable("dictionary_name", dic_traits_aura_description),SetVariable("customboxcheck", True),Jump("Home")
                    hovered Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", "default")
                    unhovered Hide("description_slave_attributes")
        for key, values in dic_traits_attributes.items():

            $ skill_info = traits_attributes[key]
            $ val = skill_info.get("value", 0)
            $ revealed = skill_info.get("revealed", False)

            if val != 0 and revealed:
                if val == -1:
                    $ style_used = "slave_traits_bad1"
                elif val == -2:
                    $ style_used = "slave_traits_bad2"
                elif val == 1:
                    $ style_used = "slave_traits_good1"
                elif val == 2:
                    $ style_used = "slave_traits_good2"
                else:
                    $ style_used = "default_style"

                $ label_text = values.get(val, "Unknown") if isinstance(values, dict) else values[val]

                textbutton label_text:
                    style style_used
                    action SetVariable("attribute_track_index", key),SetVariable("dictionary_track_index", val),SetVariable("dictionary_name", dic_traits_attributes_description),SetVariable("customboxcheck", True),Jump("Home")
                    hovered Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", "default")
                    unhovered Hide("description_slave_attributes")
    vbox:
        pos(0.99,0.02)
        anchor (1.0,0.0)
        text "{u}                     SKILLS{/u}" size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        for key, values in dic_slave_skills.items():
            if key in all_girls_list[girl_index]["skills"]:
                textbutton values[all_girls_list[girl_index]["skills"][key]]:
                    style "attribute_custom_slave" + str(all_girls_list[girl_index]["skills"][key]) xalign 1.0
                    action NullAction()
                    hovered Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", key)
                    unhovered Hide("description_slave_attributes")
        text "{u}     SEX TECHNIQUES{/u}" size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        for key, values in dic_slave_skills_sexual.items():
            if key in all_girls_list[girl_index]["sex_experience"][key]:
                textbutton values[all_girls_list[girl_index]["sex_experience"][key][key]]:
                    style "attribute_custom_slave" + str(all_girls_list[girl_index]["sex_experience"][key][key]) xalign 1.0
                    action NullAction()
                    hovered Show("description_slave_attributes"),SetVariable("description_slave_attributes_track_value", key)
                    unhovered Hide("description_slave_attributes")
screen description_slave_attributes():
    $ curx, cury = renpy.get_mouse_pos()
    if description_slave_attributes_track_value == "default":
        frame:
            pos(curx + 150,cury)
            style "description_slave_attributes_frame"
            text "Innate (Cannot learn or forget)" style "description_slave_attributes_frame_text"
    if description_slave_attributes_track_value in ["beauty","exoticism","style","fame"]:
        frame:
            pos(curx + 150,cury)
            style "description_slave_attributes_frame"
            text dic_slave_attributes_description_keys[description_slave_attributes_track_value] + " " + dic_slave_tier_classification[all_girls_list[girl_index]["attributes"][description_slave_attributes_track_value]] style "description_slave_attributes_frame_text"
    if description_slave_attributes_track_value in ["endurance", "empathy", "temperament","intelligence","nature",]:
        frame:
            pos(curx + 150,cury)
            style "description_slave_attributes_frame"
            text dic_slave_attributes_description_keys[description_slave_attributes_track_value] + " " + dic_slave_tier_classification[all_girls_list[girl_index]["attributes"][description_slave_attributes_track_value]] +"; " + str(all_girls_list[girl_index]["experience"]["attributes"][description_slave_attributes_track_value]) + " (+" + str(attributes_max_threshold[all_girls_list[girl_index]["attributes"][description_slave_attributes_track_value]]) + "/" + str(attributes_min_threshold[all_girls_list[girl_index]["attributes"][description_slave_attributes_track_value]]) + ")" style "description_slave_attributes_frame_text"
    if description_slave_attributes_track_value == "pride":
        frame:
            pos(curx + 150,cury)
            style "description_slave_attributes_frame"
            text dic_slave_attributes_description_keys[description_slave_attributes_track_value] + " " + dic_slave_tier_classification_physical[all_girls_list[girl_index]["attributes"][description_slave_attributes_track_value]] +"; " + str(all_girls_list[girl_index]["experience"]["attributes"][description_slave_attributes_track_value]) + " (+" + str(attributes_max_threshold_inverse[all_girls_list[girl_index]["attributes"][description_slave_attributes_track_value]]) + "/" + str(attributes_min_threshold_inverse[all_girls_list[girl_index]["attributes"][description_slave_attributes_track_value]]) + ")" style "description_slave_attributes_frame_text"
    if description_slave_attributes_track_value == "physical":
        frame:
            pos(curx + 150,cury)
            style "description_slave_attributes_frame"
            text dic_slave_attributes_description_keys[description_slave_attributes_track_value] + " " + dic_slave_tier_classification_physical[all_girls_list[girl_index]["attributes"][description_slave_attributes_track_value]] +"; " + str(all_girls_list[girl_index]["experience"]["attributes"][description_slave_attributes_track_value]) + " (+" + str(attributes_max_threshold_inverse[all_girls_list[girl_index]["attributes"][description_slave_attributes_track_value]]) + "/" + str(attributes_min_threshold_inverse[all_girls_list[girl_index]["attributes"][description_slave_attributes_track_value]]) + ")" style "description_slave_attributes_frame_text"
    if description_slave_attributes_track_value == "wip":
        frame:
            pos(curx + 150,cury)
            style "description_slave_attributes_frame"
            text "WIP" style "description_slave_attributes_frame_text"
    if description_slave_attributes_track_value == "petting":
        frame:
            pos(curx - 150,cury)
            style "description_slave_attributes_frame"
            text dic_slave_attributes_description_keys[description_slave_attributes_track_value] + " " + dic_slave_tier_classification[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value][description_slave_attributes_track_value]] + " " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["handjob"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["handjob"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["footjob"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["footjob"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["rubbing"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["rubbing"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["titjob"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["titjob"]]) style "description_slave_attributes_frame_text"
    if description_slave_attributes_track_value == "oral_pleasure":
        frame:
            pos(curx - 150,cury)
            style "description_slave_attributes_frame"
            text dic_slave_attributes_description_keys[description_slave_attributes_track_value] + " " + dic_slave_tier_classification[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value][description_slave_attributes_track_value]] + " " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["kissing"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["kissing"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["licking"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["licking"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["blowjob"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["blowjob"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["deep_throat"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["deep_throat"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["rimming"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["rimming"]]) style "description_slave_attributes_frame_little_text"
    if description_slave_attributes_track_value == "penetration":
        frame:
            pos(curx - 150,cury)
            style "description_slave_attributes_frame"
            text dic_slave_attributes_description_keys[description_slave_attributes_track_value] + " " + dic_slave_tier_classification[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value][description_slave_attributes_track_value]] + " " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["vaginal_sex"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["vaginal_sex"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["fisting"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["fisting"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["anal_sex"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["anal_sex"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["anal_fisting"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["anal_fisting"]]) style "description_slave_attributes_frame_little_text"
    if description_slave_attributes_track_value == "group_sex":
        frame:
            pos(curx - 150,cury)
            style "description_slave_attributes_frame"
            text dic_slave_attributes_description_keys[description_slave_attributes_track_value] + " " + dic_slave_tier_classification[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value][description_slave_attributes_track_value]] + " " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["threesome"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["threesome"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["bukkake"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["bukkake"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["doble_penetration"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["doble_penetration"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["triple_penetration"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["triple_penetration"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["gangbang"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["gangbang"]]) style "description_slave_attributes_frame_little_text"
    if description_slave_attributes_track_value == "demostration":
        frame:
            pos(curx - 150,cury)
            style "description_slave_attributes_frame"
            text dic_slave_attributes_description_keys[description_slave_attributes_track_value] + " " + dic_slave_tier_classification[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value][description_slave_attributes_track_value]] + " " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["seduction"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["seduction"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["masturbation"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["masturbation"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["dildo"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["dildo"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["humiliation"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["humiliation"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["exhibitionism"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["exhibitionism"]]) style "description_slave_attributes_frame_little_text"
    if description_slave_attributes_track_value in all_girls_list[girl_index]["skills"]:
        frame:
            pos(curx - 150,cury)
            style "description_slave_attributes_frame"
            text dic_slave_attributes_description_keys[description_slave_attributes_track_value] + " " + dic_slave_tier_classification_physical[all_girls_list[girl_index]["skills"][description_slave_attributes_track_value]] +"; " + str(all_girls_list[girl_index]["experience"]["skills"][description_slave_attributes_track_value]) + " (+" + str(attributes_max_threshold[all_girls_list[girl_index]["skills"][description_slave_attributes_track_value]]) + ")" style "description_slave_attributes_frame_text"
    if description_slave_attributes_track_value == "fetishism":
        frame:
            pos(curx - 150,cury)
            style "description_slave_attributes_frame"
            text dic_slave_attributes_description_keys[description_slave_attributes_track_value] + " " + dic_slave_tier_classification[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value][description_slave_attributes_track_value]] + " " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["enema"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["enema"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["masochism"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["masochism"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["self-torture"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["self-torture"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["golden_shower"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["golden_shower"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["scat"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["scat"]]) style "description_slave_attributes_frame_little_text"
    if description_slave_attributes_track_value == "xenophily":
        frame:
            pos(curx - 150,cury)
            style "description_slave_attributes_frame"
            text dic_slave_attributes_description_keys[description_slave_attributes_track_value] + " " + dic_slave_tier_classification[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value][description_slave_attributes_track_value]] + " " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["dog_mating"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["dog_mating"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["pig_mating"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["pig_mating"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["house_mating"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["house_mating"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["spider_mating"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["spider_mating"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["sea_tentacle_mating"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["sea_tentacle_mating"]]) + " | " + str(all_girls_list[girl_index]["experience"]["sex_experience"][description_slave_attributes_track_value]["field_mating"]) + "/" + str(attributes_max_threshold[all_girls_list[girl_index]["sex_experience"][description_slave_attributes_track_value]["field_mating"]]) style "description_slave_attributes_frame_little_text"
    if description_slave_attributes_track_value == "fear":
        frame:
            pos(curx ,cury + 50)
            style "description_slave_attributes_frame"
            text "Fear " + str(all_girls_list[girl_index]["aura"]["fear"]) + " ; " + str(all_girls_list[girl_index]["experience"]["aura"]["fear"]) + " (+" + str(attributes_max_threshold[all_girls_list[girl_index]["aura"]["fear"]]) + "/" + str(attributes_min_threshold[all_girls_list[girl_index]["aura"]["fear"]]) + ")" style "description_slave_attributes_frame_text"

    if description_slave_attributes_track_value == "despair":
        frame:
            pos(curx ,cury + 50)
            style "description_slave_attributes_frame"
            text "Despair " + str(all_girls_list[girl_index]["aura"]["despair"]) + " ; " + str(all_girls_list[girl_index]["experience"]["aura"]["despair"]) + " (+" + str(attributes_max_threshold[all_girls_list[girl_index]["aura"]["despair"]]) + "/" + str(attributes_min_threshold[all_girls_list[girl_index]["aura"]["despair"]]) + ")" style "description_slave_attributes_frame_text"

    if description_slave_attributes_track_value == "awareness":
        frame:
            pos(curx ,cury + 50)
            style "description_slave_attributes_frame"
            text "Awareness " + str(all_girls_list[girl_index]["aura"]["awareness"]) + " ; " + str(all_girls_list[girl_index]["experience"]["aura"]["awareness"]) + " (+" + str(attributes_max_threshold[all_girls_list[girl_index]["aura"]["awareness"]]) + "/" + str(attributes_min_threshold[all_girls_list[girl_index]["aura"]["awareness"]]) + ")" style "description_slave_attributes_frame_text"

    if description_slave_attributes_track_value == "taming":
        frame:
            pos(curx ,cury + 50)
            style "description_slave_attributes_frame"  
            text "Taming " + str(all_girls_list[girl_index]["aura"]["taming"]) + " ; " + str(all_girls_list[girl_index]["experience"]["aura"]["taming"]) + " (+" + str(attributes_max_threshold[all_girls_list[girl_index]["aura"]["taming"]]) + "/" + str(attributes_min_threshold[all_girls_list[girl_index]["aura"]["taming"]]) + ")" style "description_slave_attributes_frame_text"

    if description_slave_attributes_track_value == "habit":
        frame:
            pos(curx ,cury + 50)
            style "description_slave_attributes_frame"
            text "Habit " + str(all_girls_list[girl_index]["aura"]["habit"]) + " ; " + str(all_girls_list[girl_index]["experience"]["aura"]["habit"]) + " (+" + str(attributes_max_threshold[all_girls_list[girl_index]["aura"]["habit"]]) + "/" + str(attributes_min_threshold[all_girls_list[girl_index]["aura"]["habit"]]) + ")" style "description_slave_attributes_frame_text"

    if description_slave_attributes_track_value == "spoil":
        frame:
            pos(curx ,cury + 50)
            style "description_slave_attributes_frame"
            text "Spoil " + str(all_girls_list[girl_index]["aura"]["spoil"]) + " ; " + str(all_girls_list[girl_index]["experience"]["aura"]["spoil"]) + " (+" + str(attributes_max_threshold[all_girls_list[girl_index]["aura"]["spoil"]]) + "/" + str(attributes_min_threshold[all_girls_list[girl_index]["aura"]["spoil"]]) + ")" style "description_slave_attributes_frame_text"

    if description_slave_attributes_track_value == "devotion":
        frame:
            pos(curx ,cury + 50)
            style "description_slave_attributes_frame"
            text "Devotion " + str(all_girls_list[girl_index]["aura"]["devotion"]) + " ; " + str(all_girls_list[girl_index]["experience"]["aura"]["devotion"]) + " (+" + str(attributes_max_threshold[all_girls_list[girl_index]["aura"]["devotion"]]) + "/" + str(attributes_min_threshold[all_girls_list[girl_index]["aura"]["devotion"]]) + ")" style "description_slave_attributes_frame_text"
    
    if description_slave_attributes_track_value == "obedience":
        frame:
            pos(curx,cury +50)
            style "description_slave_attributes_frame"
            text "Obedience ; " + str(all_girls_list[girl_index]["obedience"]) style "description_slave_attributes_frame_text"
screen home_attributes_menu():
    vbox:
        pos(0.90,0.05)
        imagebutton anchor (0.5,0.0):
            idle mc_image
            hover mc_image2
            action NullAction()
            at avatar_scale
        add "spacer" size(0,33)
        text "Calm" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        text "Contented" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        text "Pristine" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        add "spacer" size(0,60)
        if girl_index in all_girls_list and "ava_clear" in all_girls_list[girl_index] and all_girls_list[girl_index]["conscience"]:
            imagebutton anchor (0.5,0.5):
                idle all_girls_list[girl_index]["ava_clear"] + ".webp"
                hover all_girls_list[girl_index]["ava_clear"] + "_sepia.webp"
                action SetVariable("current_menu", 100),Jump("Home")
                at avatar_scale
        elif girl_index in all_girls_list and "ava_clear" in all_girls_list[girl_index] and all_girls_list[girl_index]["conscience"]:
            imagebutton anchor (0.5,0.5):
                idle all_girls_list[girl_index]["ava_clear"] + "_sepia.webp"
                hover all_girls_list[girl_index]["ava_clear"] + "_sepia.webp"
                action SetVariable("current_menu", 100),Jump("Home")
                at avatar_scale
        else:
            add "blank_ava.webp" size(140,140) anchor (0.5,0.5)
        add "spacer" size(0,-38)
        if girl_index in all_girls_list and "ava_clear" in all_girls_list[girl_index]:
            text all_girls_list[girl_index]["mood_label"] anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
            text "No achievements" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
            text "Pristine" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        else:
            text "" color "#000000" font "fonts/Segoe Print.ttf" size 12
            text "" color "#000000" font "fonts/Segoe Print.ttf" size 12
            text "" color "#000000" font "fonts/Segoe Print.ttf" size 12
        add "spacer" size(0,63)
        add "blank_ava.webp" size(140,140) anchor (0.5,0.5)
        add "spacer" size(0,-55)
        text "No assistant" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        text "immaculate" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        text "Cannned food" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
    hbox:
        pos(0.91,0.260)
        anchor (0.5,0.0)
        text "Energy" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        add "spacer" size(-10,0)
        $ full_energy = energy_value // 2
        $ has_half = energy_value % 2 == 1
        for i in range(full_energy):
            add energy_image1 size(7,7) anchor (0.5,0.5)
        if has_half:
            add energy_image2 size(7,7) anchor (0.5,0.5)
    if not (girl_index in all_girls_list and "ava_clear" in all_girls_list[girl_index]):
        text "No slave" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12 pos(0.90,0.575)
    hbox:
        pos(0.91,0.575)
        anchor (0.5,0.0)
        if girl_index in all_girls_list and "energy" in all_girls_list[girl_index]:
            text "Energy" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
            add "spacer" size(-10,0)
            $ full_energy = int(all_girls_list[girl_index]["energy"] // 2)
            $ has_half = int(all_girls_list[girl_index]["energy"] % 2 == 1)
            for i in range(full_energy):
                add energy_image1 size(7,7) anchor (0.5,0.5)
            if has_half:
                add energy_image2 size(7,7) anchor (0.5,0.5)
screen bg_home():
    key "K_SPACE" action SetVariable("current_menu", 100), Jump("Home")
    add bgstyle xsize 1280 ysize 720
    add home_decoration xsize 1000 ysize 675 pos (0.002,0.057)
screen msg(msg_text):
    zorder 50
    add "gui/confirm_frame.png" at truecenter
    text msg_text xmaximum  445:
        pos (0.33, 0.28)
        color "#191970"
        size 14
        font "fonts/Segoe Print.ttf"
    text " Press space to close this window.":
        pos (0.33, 0.65)
        color "#191970"
        size 14
        font "fonts/Segoe Print.ttf"
    imagebutton:
        idle "buttons/ok-icon.webp" pos (0.5, 0.7)
        hover "buttons/ok-icon_hover.webp"
        action Hide("msg")
    key "K_SPACE" action Hide("msg")
