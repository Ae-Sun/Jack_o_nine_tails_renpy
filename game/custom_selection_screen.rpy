default follow_story = False
default follow_story_count = 0
default mc_name_save ="rec3ks"
default customcheck = True
default customboxcheck = False
default dic_mc_normal_selection_textdescription_value_index = 0
default dic_custom_start_difficulty_selection_index_index = 1
default alltier_s = False
default custom_points = 0
default green_or_red = "#009900"
default difficult_sparks_mantain = True
default pre_characterOnlyNameIndex = 0
default buttonimage = ""
default buttonimage_hover = ""
default start = False
label Custom_Start:
    scene donotdelete
    show scroll_large 
    if customcheck:
        $ mc_name_save = mc
        $ mc ="Jack"
        $ reputation_value_1 = 0
        $ strength_value_1 = DIC_MC_INICIAL_STATS[mc][1]
        $ personality_value_2 = DIC_MC_INICIAL_STATS[mc][2]
        $ allure_value_3 = DIC_MC_INICIAL_STATS[mc][3]
        $ libido_value_4 = DIC_MC_INICIAL_STATS[mc][4]
        $ dominance_value_5 = DIC_MC_INICIAL_STATS[mc][5]
        $ brand_reputation_value_6 = DIC_MC_INICIAL_STATS[mc][6]
        $ guild_reputation_value_7 = DIC_MC_INICIAL_STATS[mc][7]
        $ standard_of_living_value_8 = DIC_MC_INICIAL_STATS[mc][8]
        $ hygiene_value_9 = DIC_MC_INICIAL_STATS[mc][9]
        $ mood_value_10 = DIC_MC_INICIAL_STATS[mc][10]
        $ injuries_value_11 = DIC_MC_INICIAL_STATS[mc][11]
        $ teaching_value_12 = DIC_MC_INICIAL_STATS[mc][12]
        $ stewardship_value_13 = DIC_MC_INICIAL_STATS[mc][13]
        $ artistry_value_14 = DIC_MC_INICIAL_STATS[mc][14]
        $ medic_value_15 = DIC_MC_INICIAL_STATS[mc][15]
        $ fighter_value_16 = DIC_MC_INICIAL_STATS[mc][16]
        $ magic_value_17 = DIC_MC_INICIAL_STATS[mc][17]
        $ flagellation_value_18 = DIC_MC_INICIAL_STATS[mc][18]
        $ torture_value_19 = DIC_MC_INICIAL_STATS[mc][19]
        $ binding_value_20 = DIC_MC_INICIAL_STATS[mc][20]
        $ petting_value_21 = DIC_MC_INICIAL_STATS[mc][21]
        $ oral_sex_value_22 = DIC_MC_INICIAL_STATS[mc][22]
        $ penetration_value_23 = DIC_MC_INICIAL_STATS[mc][23]
        $ fetishism_value_24 = DIC_MC_INICIAL_STATS[mc][24]
        $ mc = mc_name_save
        $ customcheck = False
        # creating new temporal values
        $ namechange = False

  
    if alltier_s:
        $ reputation_value_1         = 5
        $ strength_value_1           = 6
        $ personality_value_2        = 6
        $ allure_value_3             = 6
        $ libido_value_4             = 6
        $ dominance_value_5          = 6
        $ brand_reputation_value_6   = 6
        $ guild_reputation_value_7   = 6
        $ standard_of_living_value_8 = 6
        $ hygiene_value_9            = 6
        $ mood_value_10              = 6
        $ injuries_value_11          = 6
        $ teaching_value_12          = 6
        $ stewardship_value_13       = 6
        $ artistry_value_14          = 6
        $ medic_value_15             = 6
        $ fighter_value_16           = 6
        $ magic_value_17             = 6
        $ flagellation_value_18      = 6
        $ torture_value_19           = 6
        $ binding_value_20           = 6
        $ petting_value_21           = 6
        $ oral_sex_value_22          = 6
        $ penetration_value_23       = 6
        $ fetishism_value_24         = 6
        $ sparks_37                  = 999999
        $ alltier_s                  = False
    if difficult_sparks_mantain:
        $ sparks_37 = DIC_CUSTOM_START_DIFFICULTY_SELECTION[DIC_CUSTOM_START_DIFFICULTY_SELECTION_INDEX[dic_custom_start_difficulty_selection_index_index]][1]
        $ difficult_sparks_mantain = False
    # creating new temporal values
    $ reputationstyle= 2
    # reassining variables  -rec3ks
    
    if follow_story_count % 2 == 1:
        $ buttonimage = "buttons/unsel_button.webp"
        $ buttonimage_hover = "buttons/unsel_button_hover.webp"
        $ follow_story = True
    else:
        $ buttonimage = "buttons/sel_button.webp"
        $ buttonimage_hover = "buttons/sel_button_hover.webp"
        $ follow_story = False
    #####################################
    $ strength_textvalue_1 = DIC_MC_ATTRIBUTE["STRENGTH"][strength_value_1]
    $ personality_textvalue_2 = DIC_MC_ATTRIBUTE["PERSONALITY"][personality_value_2]
    $ allure_textvalue_3 = DIC_MC_ATTRIBUTE["ALLURE"][allure_value_3]
    $ libido_textvalue_4 = DIC_MC_ATTRIBUTE["LIBIDO"][libido_value_4]
    $ dominance_textvalue_5 = DIC_MC_ATTRIBUTE["DOMINANCE"][dominance_value_5]
    $ brand_reputation_textvalue_6 = DIC_MC_ATTRIBUTE["BRAND REPUTATION"][brand_reputation_value_6]
    $ guild_reputation_textvalue_7 = DIC_MC_ATTRIBUTE["GUILD REPUTATION"][guild_reputation_value_7]
    $ standard_of_living_textvalue_8 = DIC_MC_ATTRIBUTE["STANDARD OF LIVING"][standard_of_living_value_8]
    $ hygiene_textvalue_9 = DIC_MC_ATTRIBUTE["HYGIENE"][hygiene_value_9]
    $ mood_textvalue_10 = DIC_MC_ATTRIBUTE["MOOD"][mood_value_10]
    $ injuries_textvalue_11 = DIC_MC_ATTRIBUTE["INJURIES"][injuries_value_11]
    $ teaching_textvalue_12 = DIC_MC_ATTRIBUTE["TEACHING"][teaching_value_12]
    $ stewardship_textvalue_13 = DIC_MC_ATTRIBUTE["STEWARDSHIP"][stewardship_value_13]
    $ artistry_textvalue_14 = DIC_MC_ATTRIBUTE["ARTISTRY"][artistry_value_14]
    $ medic_textvalue_15 = DIC_MC_ATTRIBUTE["MEDIC"][medic_value_15]
    $ fighter_textvalue_16 = DIC_MC_ATTRIBUTE["FIGHTER"][fighter_value_16]
    $ magic_textvalue_17 = DIC_MC_ATTRIBUTE["MAGIC"][magic_value_17]
    $ flagellation_textvalue_18 = DIC_MC_ATTRIBUTE["FLAGELLATION"][flagellation_value_18]
    $ torture_textvalue_19 = DIC_MC_ATTRIBUTE["TORTURE"][torture_value_19]
    $ binding_textvalue_20 = DIC_MC_ATTRIBUTE["BINDING"][binding_value_20]
    $ petting_textvalue_21 = DIC_MC_ATTRIBUTE["PETTING"][petting_value_21]
    $ oral_sex_textvalue_22 = DIC_MC_ATTRIBUTE["ORAL SEX"][oral_sex_value_22]
    $ penetration_textvalue_23 = DIC_MC_ATTRIBUTE["PENETRATION"][penetration_value_23]
    $ fetishism_textvalue_24 = DIC_MC_ATTRIBUTE["FETISHISM"][fetishism_value_24]
    $ reputation_textvalue_1 = DIC_MC_ATTRIBUTE["REPUTATION"][reputation_value_1]
    $ custom_difficulty_textvalue = DIC_CUSTOM_START_DIFFICULTY_SELECTION[DIC_CUSTOM_START_DIFFICULTY_SELECTION_INDEX[dic_custom_start_difficulty_selection_index_index]][0]
    $ custom_points = DIC_CUSTOM_START_DIFFICULTY_SELECTION[DIC_CUSTOM_START_DIFFICULTY_SELECTION_INDEX[dic_custom_start_difficulty_selection_index_index]][2]
    $ characterOnlyNameIndex = pre_characterOnlyNameIndex % 12
    show screen points_tier_text2
    if namechange == True:
        hide screen points_tier_text
        hide screen points_tier_text2
        python:
            name = renpy.input("Give your character a name. Keep this shorter than 14 character.", length=13)
            name = name.strip()
            if name != "":
                mc = name
        $ namechange = False
        jump Custom_Start
    if dic_custom_start_difficulty_selection_index_index == 0:
        show screen s_tier_button
        hide screen points_tier_text
        if reputationstyle + reputation_value_1 == 7:
            $ reputationstyle = 3
    else:
        hide screen s_tier_button
        show screen points_tier_text
        if reputation_value_1 > 4:
            $ reputation_value_1 = 4
            $ reputation_textvalue_1 = DIC_MC_ATTRIBUTE["REPUTATION"][reputation_value_1]
            $ dic_mc_normal_selection_textdescription_value = "WHITE TOWN"
            show screen custom_value_information2
    $ custom_points = custom_points - CUSTOM_SKILL_COST_VALUE[strength_value_1] - CUSTOM_SKILL_COST_VALUE[personality_value_2] - CUSTOM_SKILL_COST_VALUE[allure_value_3] - CUSTOM_SKILL_COST_VALUE[libido_value_4] - CUSTOM_SKILL_COST_VALUE[dominance_value_5] - CUSTOM_SKILL_COST_VALUE[brand_reputation_value_6] - CUSTOM_SKILL_COST_VALUE[guild_reputation_value_7] - CUSTOM_SKILL_COST_VALUE[standard_of_living_value_8] - CUSTOM_SKILL_COST_VALUE[hygiene_value_9] - CUSTOM_SKILL_COST_VALUE[mood_value_10] - CUSTOM_SKILL_COST_VALUE[injuries_value_11] - CUSTOM_SKILL_COST_VALUE[teaching_value_12] - CUSTOM_SKILL_COST_VALUE[stewardship_value_13] - CUSTOM_SKILL_COST_VALUE[artistry_value_14] - CUSTOM_SKILL_COST_VALUE[medic_value_15] - CUSTOM_SKILL_COST_VALUE[fighter_value_16] - CUSTOM_SKILL_COST_VALUE[magic_value_17] - CUSTOM_SKILL_COST_VALUE[flagellation_value_18] - CUSTOM_SKILL_COST_VALUE[torture_value_19] - CUSTOM_SKILL_COST_VALUE[binding_value_20] - CUSTOM_SKILL_COST_VALUE[petting_value_21] - CUSTOM_SKILL_COST_VALUE[oral_sex_value_22] - CUSTOM_SKILL_COST_VALUE[penetration_value_23] - CUSTOM_SKILL_COST_VALUE[fetishism_value_24] - CUSTOM_SKILL_COST_VALUE[reputation_value_1] - int((sparks_37 - DIC_CUSTOM_START_DIFFICULTY_SELECTION[DIC_CUSTOM_START_DIFFICULTY_SELECTION_INDEX[dic_custom_start_difficulty_selection_index_index]][1])/10)
    
    if custom_points < 0:
        $ green_or_red = "#CD0000"
    else:
        $ green_or_red = "#009900"
    if start:
        if custom_points > 0:
            hide screen custom_value_information2   
            hide screen custom_selection
            hide screen points_tier_text 
            hide screen points_tier_text2
            hide scroll_large
            hide screen s_tier_button
            jump iniciation_label
        else:
            $ dic_mc_normal_selection_textdescription_value = "START FAIL"
            $ start = False
            show screen custom_value_information2
    if customboxcheck:
        show screen custom_selection
        call screen custom_value_information
    call screen custom_selection()
screen custom_value_information():
    zorder 5
    add "gui/confirm_frame.png" at truecenter
    vbox:
        pos (0.5, 0.3)
        text dic_mc_normal_selection_textdescription_value :
            color "#191970" 
            anchor (0.5,0.5)
            size 20
            font "fonts/Segoe Print.ttf"
        if dic_mc_normal_selection_textdescription_value != "INJURIES":
            for values in range(6):
                textbutton DIC_MC_ATTRIBUTE.get(dic_mc_normal_selection_textdescription_value, [""]*6)[values] anchor (0.5,0.5):
                    style "attribute_check_slave" + str(values)
                    action  NullAction()
        else:
            for values in range(6):
                textbutton DIC_MC_ATTRIBUTE.get(dic_mc_normal_selection_textdescription_value, [""]*6)[values] anchor (0.5,0.5):
                    style "attribute_check_injuries" + str(values)
                    action  NullAction()


    text " Press space to close this window.":
        pos (0.33, 0.65)
        color "#191970"
        size 14
        font "fonts/Segoe Print.ttf"

    imagebutton:
        idle "buttons/ok-icon.webp" pos (0.5, 0.7)
        hover "buttons/ok-icon_hover.webp"
        action Hide("custom_value_information"),SetVariable("customboxcheck", False),Show("custom_value_information2")

    key "K_SPACE" action Hide("custom_value_information"),SetVariable("customboxcheck", False),Show("custom_value_information2")
screen custom_value_information2():
    zorder 5
    add "gui/confirm_frame.png" at truecenter

    text DIC_MC_NORMAL_SELECTION_TEXTDESCRIPTION[dic_mc_normal_selection_textdescription_value][dic_mc_normal_selection_textdescription_value_index] xmaximum 445:
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
        action Hide("custom_value_information2"),SetVariable("customboxcheck", False)


    key "K_SPACE" action Hide("custom_value_information2"),SetVariable("customboxcheck", False)
screen s_tier_button():
    zorder 2
    imagebutton:
        idle "buttons/teach_s.webp" pos (0.29, 0.35)
        hover "buttons/teach_s_hover.webp"
        action SetVariable("alltier_s", True),Jump("Custom_Start")
screen points_tier_text():
    zorder 3
    vbox:
        xpos 0.65
        ypos 0.13
        xanchor 0.5
        yanchor 0.0
        text "Points:":
            size 42
            color "000000"
            font "fonts/victoriana.ttf"
            yalign 0.5
            xalign 0.5            
        text str(custom_points):
            size 42
            color green_or_red
            font "fonts/victoriana.ttf"
            yalign 0.5
            xalign 0.5
screen points_tier_text2():
    zorder 4
    vbox:
        xpos 0.65
        ypos 0.26
        xanchor 0.5
        yanchor 0.0
        text "APPEARANCE":
            size 45
            color "000000"
            font "fonts/victoriana.ttf"
            yalign 0.5
            xalign 0.5
        add "spacer" size (0, 5)
        add DIC_CUSTOM_CHARACTER_SELECTION[DIC_CHARACTERSONLYNAME[characterOnlyNameIndex]][0] at truecenter          
        add "spacer" size (0, 5)
        text "{u}Ignore story:{u}":
            size 17
            color "000000"
            font "fonts/segoe print.ttf"
            yalign 0.5
            xalign 0.3
        add "spacer" size (0, -7.5)
        text "{u}CUSTOMIZATION COST:{/u}":
            color "000000"
            size 17
            font "fonts/segoe print.ttf"
            yalign 0.5
            xalign 0.5
        text "Perfection      160 pnts":
            color "996515"
            font "fonts/segoe print.ttf"
            size 16
            yalign 0.0
            xalign 0.0
        text "Astonishing     80  pnts":
            color "009900"
            font "fonts/segoe print.ttf"
            size 16
            yalign 0.0
            xalign 0.0
        text "Excellent         40  pnts":
            color "009FEF"
            font "fonts/segoe print.ttf"
            size 16
            yalign 0.0
            xalign 0.0
        text "Good              20  pnts":
            color "0000D8"
            font "fonts/segoe print.ttf"
            size 16
            yalign 0.0
            xalign 0.0
        text "Mediocre         10  pnts":
            color "6B0084"
            font "fonts/segoe print.ttf"
            size 16
            yalign 0.0
            xalign 0.0
        text "Bad                5   pnts":
            color "EA0090"
            font "fonts/segoe print.ttf"
            size 16
            yalign 0.0
            xalign 0.0
        text "Awful              0   pnts":
            color "CD0000"
            font "fonts/segoe print.ttf"
            size 16
            yalign 0.0
            xalign 0.0
    imagebutton:
        idle buttonimage pos (0.69, 0.55)
        hover buttonimage_hover
        action SetVariable("follow_story_count", follow_story_count+1), Jump("Custom_Start")
    imagebutton:
        idle "buttons/forward_button.webp" pos (0.725,0.265 )
        hover "buttons/forward_button_hover.webp"
        action [
            SetVariable("pre_characterOnlyNameIndex",pre_characterOnlyNameIndex +1),
            Jump("Custom_Start")
        ]
    imagebutton:
        idle "buttons/back_button.webp" pos (0.535, 0.265)
        hover "buttons/back_button_hover.webp"
        action [
            SetVariable("pre_characterOnlyNameIndex",pre_characterOnlyNameIndex -1),
            Jump("Custom_Start")
        ]
screen custom_selection():
    zorder 0

    hbox:
        xpos 0.5
        ypos 0.015
        xanchor 0.5
        yanchor 0.0

        text "Difficulty:":
            size 48
            color "000000"
            font "fonts/victoriana.ttf"
            yalign 0.5

        imagebutton:
            idle "buttons/Minus.webp"
            hover "buttons/Minus_hover.webp"
            action (
                SetVariable("difficult_sparks_mantain", True),
                SetVariable("dic_custom_start_difficulty_selection_index_index", max(dic_custom_start_difficulty_selection_index_index - 1, 0)),
                Jump("Custom_Start")
)            yalign 0.5
        text custom_difficulty_textvalue:
            size 48
            color "000000"
            font "fonts/victoriana.ttf"
            yalign 0.5
        imagebutton:
            idle "buttons/Plus.webp"
            hover "buttons/Plus_hover.webp"
            action (
                SetVariable("difficult_sparks_mantain", True),
                SetVariable("dic_custom_start_difficulty_selection_index_index", min(dic_custom_start_difficulty_selection_index_index + 1, 2)),
                Jump("Custom_Start")
)            yalign 0.5
    hbox:
        xpos 0.5
        ypos 0.1
        xanchor 0.5
        yanchor 0.0

        text "Sparks:":
            size 48
            color "000000"
            font "fonts/victoriana.ttf"
            yalign 0.5

        imagebutton:
            idle "buttons/Minus.webp"
            hover "buttons/Minus_hover.webp"
            action SetVariable("sparks_37",max(sparks_37-100,200)), Jump("Custom_Start")
            yalign 0.5
        text str(sparks_37):
            size 30
            color "0000ff"
            font "fonts/victoriana.ttf"
            yalign 0.5
        imagebutton:
            idle "buttons/Plus.webp"
            hover "buttons/Plus_hover.webp"
            action SetVariable("sparks_37",min(sparks_37+100,CUSTOM_SELECTION_MAX_CAP_SPARKS[dic_custom_start_difficulty_selection_index_index])), Jump("Custom_Start")
            yalign 0.5
    textbutton "Start" pos (0.5, 0.945) anchor (0.5, 0.5):
        style "start_button"
        action SetVariable("customboxcheck", False),Hide("custom_value_information"),SetVariable("start", True), Jump("Custom_Start")
    vbox:
        anchor (0.0, 0.0)  # Aligns the anchor to the top-left corner
        spacing -1.5    # Spacing between all buttons
        xpos 360 
        ypos 115 

        textbutton reputation_textvalue_1:
            style "attribute_button_custom" + str(reputation_value_1 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "REPUTATION")

        textbutton strength_textvalue_1:
            style "attribute_button_custom" + str(strength_value_1 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "STRENGTH")

        textbutton personality_textvalue_2:
            style "attribute_button_custom" + str(personality_value_2 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "PERSONALITY")

        textbutton libido_textvalue_4:
            style "attribute_button_custom" + str(libido_value_4 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "LIBIDO")

        textbutton dominance_textvalue_5:
            style "attribute_button_custom" + str(dominance_value_5 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "DOMINANCE")

        add "spacer" size (0, 35)

        textbutton teaching_textvalue_12:
            style "attribute_button_custom" + str(teaching_value_12 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "TEACHING")

        textbutton stewardship_textvalue_13:
            style "attribute_button_custom" + str(stewardship_value_13 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "STEWARDSHIP")

        textbutton artistry_textvalue_14:
            style "attribute_button_custom" + str(artistry_value_14 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "ARTISTRY")

        textbutton medic_textvalue_15:
            style "attribute_button_custom" + str(medic_value_15 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "MEDIC")

        textbutton fighter_textvalue_16:
            style "attribute_button_custom" + str(fighter_value_16 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "FIGHTER")

        textbutton magic_textvalue_17:
            style "attribute_button_custom" + str(magic_value_17 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "MAGIC")

        textbutton flagellation_textvalue_18:
            style "attribute_button_custom" + str(flagellation_value_18 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "FLAGELLATION")

        textbutton torture_textvalue_19:
            style "attribute_button_custom" + str(torture_value_19 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "TORTURE")

        textbutton binding_textvalue_20:
            style "attribute_button_custom" + str(binding_value_20 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "BINDING")

        add "spacer" size (0, 20)

        textbutton petting_textvalue_21:
            style "attribute_button_custom" + str(petting_value_21 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "PETTING")

        textbutton oral_sex_textvalue_22:
            style "attribute_button_custom" + str(oral_sex_value_22 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "ORAL SEX")

        textbutton penetration_textvalue_23:
            style "attribute_button_custom" + str(penetration_value_23 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "PENETRATION")

        textbutton fetishism_textvalue_24:
            style "attribute_button_custom" + str(fetishism_value_24 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("dic_mc_normal_selection_textdescription_value", "FETISHISM")
    vbox:
        anchor (0.0, 0.0)  # Aligns the anchor to the top-left corner
        spacing -1.5    # Spacing between all buttons
        xpos 290 
        ypos 115 

        textbutton "[[+]":
            style "attribute_button_custom" + str(reputation_value_1 + reputationstyle)
            action SetVariable("reputation_value_1", min(reputation_value_1 + 1, 5)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(strength_value_1 + 2)
            action SetVariable("strength_value_1", min(strength_value_1 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(personality_value_2 + 2)
            action SetVariable("personality_value_2", min(personality_value_2 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(libido_value_4 + 2)
            action SetVariable("libido_value_4", min(libido_value_4 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(dominance_value_5 + 2)
            action SetVariable("dominance_value_5", min(dominance_value_5 + 1, 6)), Jump("Custom_Start")

        add "spacer" size (0, 35)

        textbutton "[[+]":
            style "attribute_button_custom" + str(teaching_value_12 + 2)
            action SetVariable("teaching_value_12", min(teaching_value_12 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(stewardship_value_13 + 2)
            action SetVariable("stewardship_value_13", min(stewardship_value_13 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(artistry_value_14 + 2)
            action SetVariable("artistry_value_14", min(artistry_value_14 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(medic_value_15 + 2)
            action SetVariable("medic_value_15", min(medic_value_15 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(fighter_value_16 + 2)
            action SetVariable("fighter_value_16", min(fighter_value_16 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(magic_value_17 + 2)
            action SetVariable("magic_value_17", min(magic_value_17 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(flagellation_value_18 + 2)
            action SetVariable("flagellation_value_18", min(flagellation_value_18 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(torture_value_19 + 2)
            action SetVariable("torture_value_19", min(torture_value_19 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(binding_value_20 + 2)
            action SetVariable("binding_value_20", min(binding_value_20 + 1, 6)), Jump("Custom_Start")

        add "spacer" size (0, 20)

        textbutton "[[+]":
            style "attribute_button_custom" + str(petting_value_21 + 2)
            action SetVariable("petting_value_21", min(petting_value_21 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(oral_sex_value_22 + 2)
            action SetVariable("oral_sex_value_22", min(oral_sex_value_22 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(penetration_value_23 + 2)
            action SetVariable("penetration_value_23", min(penetration_value_23 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(fetishism_value_24 + 2)
            action SetVariable("fetishism_value_24", min(fetishism_value_24 + 1, 6)), Jump("Custom_Start")
       
    vbox:
        anchor (0.0, 0.0)  # Aligns the anchor to the top-left corner
        spacing -1.5    # Spacing between all buttons
        xpos 328
        ypos 115 
       
        textbutton "[[-]":
            style "attribute_button_custom" + str(reputation_value_1),
            action SetVariable("reputation_value_1", max(reputation_value_1 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(strength_value_1),
            action SetVariable("strength_value_1", max(strength_value_1 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(personality_value_2),
            action SetVariable("personality_value_2", max(personality_value_2 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(libido_value_4),
            action SetVariable("libido_value_4", max(libido_value_4 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(dominance_value_5),
            action SetVariable("dominance_value_5", max(dominance_value_5 - 1, 0)), Jump("Custom_Start")

        # Adding extra spacing here:
        add "spacer" size (0, 35)

        textbutton "[[-]":
            style "attribute_button_custom" + str(teaching_value_12),
            action SetVariable("teaching_value_12", max(teaching_value_12 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(stewardship_value_13),
            action SetVariable("stewardship_value_13", max(stewardship_value_13 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(artistry_value_14),
            action SetVariable("artistry_value_14", max(artistry_value_14 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(medic_value_15),
            action SetVariable("medic_value_15", max(medic_value_15 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(fighter_value_16),
            action SetVariable("fighter_value_16", max(fighter_value_16 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(magic_value_17),
            action SetVariable("magic_value_17", max(magic_value_17 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(flagellation_value_18),
            action SetVariable("flagellation_value_18", max(flagellation_value_18 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(torture_value_19),
            action SetVariable("torture_value_19", max(torture_value_19 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(binding_value_20),
            action SetVariable("binding_value_20", max(binding_value_20 - 1, 0)), Jump("Custom_Start")

        add "spacer" size (0, 20)

        textbutton "[[-]":
            style "attribute_button_custom" + str(petting_value_21),
            action SetVariable("petting_value_21", max(petting_value_21 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(oral_sex_value_22),
            action SetVariable("oral_sex_value_22", max(oral_sex_value_22 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(penetration_value_23),
            action SetVariable("penetration_value_23", max(penetration_value_23 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(fetishism_value_24),
            action SetVariable("fetishism_value_24", max(fetishism_value_24 - 1, 0)), Jump("Custom_Start")
    vbox:
        anchor (0.0, 0.0)
        xpos 315
        ypos 120
        spacing 1.12  # Adjusted for cleaner spacing

        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"

        null height 35  # Spacer

        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"

        null height 20  # Spacer

        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
    imagebutton:
        idle "buttons/close_button.webp" pos (983,12)
        hover "buttons/close_button_hover.webp"
        action MainMenu(confirm=False)
    hbox:
        pos (290, 85)
        spacing 2
        text "Name: [mc]" font "fonts/Segoe Print.ttf" color "#002BA7" size 16 yalign 0.5

        textbutton "[[change]":
            style "change_button"
            yalign 0.5
            action SetVariable("namechange", True), Jump("Custom_Start")
    vbox:
        xpos 290
        ypos 258
        textbutton "{u}SKILLS:{/u}":
            style "custom_information",
            action Show("custom_value_information2"), SetVariable("customboxcheck", False),Show("custom_value_information2"), Hide("custom_value_information"), SetVariable("dic_mc_normal_selection_textdescription_value", "SKILLS")

        null height 230  # Spacer
        textbutton "{u}SEX TECHNIQUES:{/u}":
            style "custom_information",
            action Show("custom_value_information2"), SetVariable("customboxcheck", False),Show("custom_value_information2"), Hide("custom_value_information"), SetVariable("dic_mc_normal_selection_textdescription_value", "SEX TECHNIQUES")
