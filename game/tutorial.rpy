default angelika_speech_text_count = 0
default lecture_name = ""
default last_girl_selection = "demo/choose_slave.webp"
default demo_girl_text_index = 0
default demo_girl_selection = "Helen"
default all_girls_list = {}
default girl_index = 0
default premiun_girl_tutorial_selected_localization = "girl_packs/original_premiun_slaves_pack/helen.json"
default dictionary_track_index = 0
default attribute_track_index = ""
default attribute_track_basic = ""
default dictionary_name = {}
default girl_selection_list_for_text_display = ""
default attribute_checkbox = False
default attributeisphysical = False
default girl_selection_list = []
default girl_selection_list_image = []
default is_tutorial = False
default infobox_jump ="choose_inicial_girl"
screen tutorial_bg():
    add "bg/guild.webp"pos(0.004,0.007111) anchor (0.0, 0.0) xsize 795 ysize 535
screen mistress_angelika():
    add "characters/mistress_angelika.webp"pos(0.3, 0.3785) anchor (0.5, 0.5) xsize 795 ysize 535
    key "K_SPACE" action SetVariable("angelika_speech_text_count", angelika_speech_text_count + 1),Jump("Lecture")
screen mistress_angelika2():
    add "characters/mistress_angelika.webp"pos(0.3, 0.3785) anchor (0.5, 0.5) xsize 795 ysize 535
    key "K_SPACE" action SetVariable("angelika_speech_text_count", angelika_speech_text_count + 1),Jump("Tutorial")
screen angelika_speech():
    text angelika_speech_text[angelika_speech_text_count] pos (0.02, 0.78) size 20 font "consolas.ttf" xmaximum 750 
screen angelika_buttons():
    vbox:
        xalign 0.655
        yalign 0.96
        imagebutton:
            idle tutorial_backbutton anchor (0.5, 0.5)
            hover tutorial_backbutton_hover
            action SetVariable("angelika_speech_text_count", max(angelika_speech_text_count - 1,0)),Jump("Tutorial")
        imagebutton:
            idle "buttons/auk_fwrd.webp" anchor (0.5, 0.5)
            hover "buttons/auk_fwrd_hover.webp"
            action SetVariable("angelika_speech_text_count", angelika_speech_text_count + 1),Jump("Tutorial")
screen angelika_display():
    vbox:
        pos(0.82,0.05)
        text "Mistress Angelika" size 45 color "#000000" font "fonts/victoriana.ttf" anchor (0.5, 0.5)
        add "spacer" size (0,-10)
        text "Slavers Guild Master"size 30 color "#000000" font "fonts/victoriana.ttf" anchor (0.5, 0.5)
        text "Neutrals"size 30 color "#000000" font "fonts/victoriana.ttf" anchor (0.5, 0.5)
        add "spacer" size (0,20)
        text "Information for consideration:" size 30 color "#000000" font "fonts/victoriana.ttf" anchor (0.5, 0.5)
    vbox:
        pos(0.650,0.25)
        text attitude_text["haughty"][0] size 20 color "#191970" font "fonts/Segoe Print.ttf" anchor (0.0,0.0)
        add "spacer" size (0,60)    
        text "   It seems from this lady depends the final decision about my entry into the guild. Most likely, this is just a formality, but it is necessary to remain vigilant. She looks like a person who does not forgive weakness and enjoys suffering neighbors…" xmaximum 425 size 20 color "#191970" font "fonts/Segoe Print.ttf" anchor (0.0,0.0)
        text "   What the hell?! She looks like a complete bitch, though sexy." xmaximum 425 size 20 color "#191970" font "fonts/Segoe Print.ttf" anchor (0.0,0.0)
screen slaver_guild():
    vbox:
        pos(0.82,0.05)
        text "Slavers Guild" size 45 color "#000000" font "fonts/victoriana.ttf" anchor (0.5, 0.5)
        add "spacer" size (0,-10)
        text "Vatican Suburbs"size 30 color "#000000" font "fonts/victoriana.ttf" anchor (0.5, 0.5)
        add "spacer" size (0,20)
        text "Information for consideration:" size 30 color "#000000" font "fonts/victoriana.ttf" anchor (0.5, 0.5)
    vbox:
        pos(0.650,0.25)
        text "   Judging by the interior of this place, you can say that the Slavers Guild members have a high place in the social hierarchy. The rooms all distinguish themselves by their apparent class and comfort, with the exception of the prisons and dungeons, of course…" xmaximum 425 size 20 color "#191970" font "fonts/Segoe Print.ttf" anchor (0.0,0.0)
    vbox:
        pos(0.165,0.05)
        spacing 18  
        textbutton "Lecture I: Components of success":
            style "lecture_button"
            action SetVariable("angelika_speech_text_count",0),SetVariable("lecture_name","tutorial_lecture1"),Jump("Lecture")
        textbutton "Lecture II: Psychology of submission":
            style "lecture_button"
            action SetVariable("angelika_speech_text_count",0),SetVariable("lecture_name","tutorial_lecture2"),Jump("Lecture")
        textbutton "Lecture III: Sticks and carrots":
            style "lecture_button"
            action SetVariable("angelika_speech_text_count",0),SetVariable("lecture_name","tutorial_lecture3"),Jump("Lecture")
        textbutton "Lecture IV: Kitchen slavery":
            style "lecture_button"
            action SetVariable("angelika_speech_text_count",0),SetVariable("lecture_name","tutorial_lecture4"),Jump("Lecture")
        textbutton "Check the conditions of the exam":
            style "lecture_button"
            action SetVariable("angelika_speech_text_count",0),SetVariable("lecture_name","tutorial_lecture5"),Jump("Lecture")
        
        if len(all_girls_list) > 0: #need to check
            textbutton "Back to work":
                style "lecture_button"
                action Jump("Home")
        else:
            textbutton "Start the practical examination":
                style "lecture_button"
                action Jump("choose_inicial_girl")
            textbutton "Leave the guild":
                style "lecture_button"
                action MainMenu(confirm=False)
    text "{color=#000000}I must choose which lecture I want to hear, or I can ask about the conditions of the examination or ask to start when I am ready.{/color}" pos (0.02, 0.78) size 20 font "consolas.ttf" xmaximum 750 
screen lecture_screen():
    text tutorial_lectureGIGA[lecture_name][angelika_speech_text_count] pos (0.02, 0.78) size 20 font "consolas.ttf" xmaximum 750 color "#000000"
screen lecture_screenbuttons():   
    vbox:
        xalign 0.655
        yalign 0.96
        imagebutton:
            idle tutorial_backbutton anchor (0.5, 0.5)
            hover tutorial_backbutton_hover
            action SetVariable("angelika_speech_text_count", max(angelika_speech_text_count - 1,0)),Jump("Lecture")
        imagebutton:
            idle "buttons/auk_fwrd.webp" anchor (0.5, 0.5)
            hover "buttons/auk_fwrd_hover.webp"
            action SetVariable("angelika_speech_text_count", angelika_speech_text_count + 1),Jump("Lecture")
screen choose_inicial_girl_screen():
    add "bg/interiors/classic_dungeon.webp"pos(0.004,0.007111) anchor (0.0, 0.0) xsize 795 ysize 535
    text "Choose your slave" pos(0.315, 0.04) anchor (0.5, 0.5) size 36 color "#ffff00" font "fonts/victoriana.ttf"
    text demo_girl_text[demo_girl_text_index] pos (0.02, 0.78) size 20 font "consolas.ttf" xmaximum 750 color "#000000"
    add "demo/choose_slave_standard.webp" pos(0.004,0.007111) anchor (0.0, 0.0) xsize 795 ysize 535
    for girl in girl_selection_list_image:
        add girl pos(0.004,0.007111) anchor (0.0, 0.0) xsize 795 ysize 535
    text "Girls selected: [girl_selection_list_for_text_display]" pos(0.01, 0.01)size 12 color "#d36f1e" font "consolas.ttf"
    vbox:
        xpos 850
        ypos 35
        spacing 2
        text "{u}ATTRIBUTES{/u}" font "fonts/Segoe Print.ttf" color "000000" size 16
        for key, values in dic_slave_attributes.items():
            if key != "physical":
                textbutton values[all_girls_list[girl_index]["attributes"][key]]:
                    style "attribute_custom_slave" + str(all_girls_list[girl_index]["attributes"][key])
                    action SetVariable("attribute_track_index",key),SetVariable("attribute_track_basic",key),SetVariable("dictionary_track_index",7),SetVariable("dictionary_name",dic_slave_attributes),SetVariable("attribute_checkbox",True),SetVariable("attributeisphysical",False),Jump("choose_inicial_girl")
            else:
                textbutton values[all_girls_list[girl_index]["attributes"][key]]:
                    style "attribute_custom_physical_special" + str(all_girls_list[girl_index]["attributes"][key])
                    action SetVariable("attribute_track_index",key),SetVariable("attribute_track_basic",key),SetVariable("dictionary_track_index",7),SetVariable("dictionary_name",dic_slave_attributes),SetVariable("attribute_checkbox",True),SetVariable("attributeisphysical",True),Jump("choose_inicial_girl")                    
 


        add "spacer" size(0,20) 
        text "{u}TRAITS{/u}"font "fonts/Segoe Print.ttf" color "000000" size 16


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
                    action SetVariable("attribute_track_index", key), SetVariable("dictionary_track_index", val), SetVariable("dictionary_name", dic_traits_skills_descriptions), SetVariable("customboxcheck", True), Jump("choose_inicial_girl")
     
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
                    action SetVariable("attribute_track_index", key), SetVariable("dictionary_track_index", val), SetVariable("dictionary_name", dic_traits_sexual_description), SetVariable("customboxcheck", True), Jump("choose_inicial_girl")
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
                    action SetVariable("attribute_track_index", key),SetVariable("dictionary_track_index", val),SetVariable("dictionary_name", dic_traits_miscellaneous_description),SetVariable("customboxcheck", True),Jump("choose_inicial_girl")
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
                    action SetVariable("attribute_track_index", key),SetVariable("dictionary_track_index", val),SetVariable("dictionary_name", dic_traits_aura_description),SetVariable("customboxcheck", True),Jump("choose_inicial_girl")
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
                    action SetVariable("attribute_track_index", key),SetVariable("dictionary_track_index", val),SetVariable("dictionary_name", dic_traits_attributes_description),SetVariable("customboxcheck", True),Jump("choose_inicial_girl")


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
            action SetVariable("is_tutorial",True),Jump("iniciation_label")
    for girl_path, xpos in inicial_girls:
        button:
            xpos xpos
            ypos 0
            xsize 265
            ysize 515
            action SetVariable("last_girl_selection", girl_path), Jump("choose_inicial_girl")
screen tutorial_attribute():
    zorder 5
    add "gui/confirm_frame.png" at truecenter
    text dictionary_name[attribute_track_index][dictionary_track_index] xmaximum  445:
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
        action Hide("tutorial_attribute"),SetVariable("customboxcheck", False)
    key "K_SPACE" action Hide("tutorial_attribute"),SetVariable("customboxcheck", False)
screen tutorial_description():
    zorder 5
    add "gui/confirm_frame.png" at truecenter
    vbox:
        pos (0.5, 0.3)
  
        text dic_slave_attributes_keys[attribute_track_basic]:
            color "#191970" 
            anchor (0.5,0.5)
            size 20
            font "fonts/Segoe Print.ttf"
        for values in range(6):  # 0 to 5 inclusive
            textbutton dic_slave_attributes[attribute_track_basic][values] anchor (0.5,0.5):
                style "attribute_check_slave" + str(values)
                action Jump(infobox_jump)

    text " Press space to close this window.":
        pos (0.33, 0.65)
        color "#191970"
        size 14
        font "fonts/Segoe Print.ttf"
    imagebutton:
        idle "buttons/ok-icon.webp" pos (0.5, 0.7)
        hover "buttons/ok-icon_hover.webp"
        action Hide("tutorial_description"),SetVariable("attribute_checkbox", False),Show("tutorial_description2"),Jump(infobox_jump)
    key "K_SPACE" action Hide("tutorial_description"),SetVariable("attribute_checkbox", False),Show("tutorial_description2"),Jump(infobox_jump)
screen tutorial_descriptionphysical():
    zorder 5
    add "gui/confirm_frame.png" at truecenter
    vbox:
        pos (0.5, 0.3)
  
        text dic_slave_attributes_keys[attribute_track_basic]:
            color "#191970" 
            anchor (0.5,0.5)
            size 20
            font "fonts/Segoe Print.ttf"
        for values in range(6):  # 0 to 5 inclusive
            textbutton dic_slave_attributes[attribute_track_basic][values] anchor (0.5,0.5):
                style "attribute_custom_physical" + str(values)
                action Jump(infobox_jump)

    text " Press space to close this window.":
        pos (0.33, 0.65)
        color "#191970"
        size 14
        font "fonts/Segoe Print.ttf"
    imagebutton:
        idle "buttons/ok-icon.webp" pos (0.5, 0.7)
        hover "buttons/ok-icon_hover.webp"
        action Hide("tutorial_descriptionphysical"),SetVariable("attribute_checkbox", False),Show("tutorial_description2"),Jump(infobox_jump)
    key "K_SPACE" action Hide("tutorial_descriptionphysical"),SetVariable("attribute_checkbox", False),Show("tutorial_description2"),Jump(infobox_jump)
screen tutorial_description2():
    zorder 5
    add "gui/confirm_frame.png" at truecenter
    text dictionary_name[attribute_track_index][dictionary_track_index] xmaximum  445:
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
        action Hide("tutorial_description2"),SetVariable("attribute_checkbox", False),Jump(infobox_jump)
    key "K_SPACE" action Hide("tutorial_description2"),SetVariable("attribute_checkbox", False),Jump(infobox_jump)
screen bg_old_tutorial():
    zorder -10
    add bgstyle2 xsize 1280 ysize 720
label Tutorial:
    show screen bg_old_tutorial()
    show screen tutorial_bg()
    show screen angelika_buttons()
    show screen mistress_angelika2()
    show screen angelika_display()
    hide screen choose_inicial_girl_screen
    hide screen bg_home
    hide screen goguild
    hide screen home_attributes_menu

    if angelika_speech_text_count == 0:
        $ tutorial_backbutton = "buttons/demo_noback_button.webp"
        $ tutorial_backbutton_hover = "buttons/demo_noback_button_hover.webp"
    else:
        $ tutorial_backbutton = "buttons/demo_back_button.webp"
        $ tutorial_backbutton_hover = "buttons/demo_back_button_hover.webp"
    if angelika_speech_text_count == 1:
        python:
            name = renpy.input("My name is... (Keep this shorter than 14 character.)", length=13)
            name = name.strip()
            if name != "":
                mc = name
    if angelika_speech_text_count == 2:
        $ mynamebugfix = True
    if angelika_speech_text_count == 4:
        hide screen angelika_buttons
        hide screen mistress_angelika2
        hide screen angelika_display
        hide screen lecture_screen
        show screen slaver_guild()
        $ mynamebugfix = False
    call screen angelika_speech()   
    return
label Lecture:
    show screen mistress_angelika
    hide screen slaver_guild
    show screen lecture_screen
    show screen angelika_display
    if angelika_speech_text_count == 0:
        $ tutorial_backbutton = "buttons/demo_noback_button.webp"
        $ tutorial_backbutton_hover = "buttons/demo_noback_button_hover.webp"
    else:
        $ tutorial_backbutton = "buttons/demo_back_button.webp"
        $ tutorial_backbutton_hover = "buttons/demo_back_button_hover.webp"
    if lecture_name == "tutorial_lecture1":
        if angelika_speech_text_count == 8:
            hide screen mistress_angelika
            hide lecture_screen
            hide screen angelika_display
            call screen slaver_guild
    if lecture_name == "tutorial_lecture2":
        if angelika_speech_text_count == 27:
            hide screen mistress_angelika
            hide lecture_screen
            hide screen angelika_display
            call screen slaver_guild
    if lecture_name == "tutorial_lecture3":
        if angelika_speech_text_count == 24:
            hide screen mistress_angelika
            hide lecture_screen
            hide screen angelika_display
            call screen slaver_guild
    if lecture_name == "tutorial_lecture4":
        if angelika_speech_text_count == 11:
            hide screen mistress_angelika
            hide lecture_screen
            hide screen angelika_display
            call screen slaver_guild
    if lecture_name == "tutorial_lecture5":
        if angelika_speech_text_count == 6:
            hide screen mistress_angelika
            hide lecture_screen
            hide screen angelika_display
            call screen slaver_guild
    call screen lecture_screenbuttons
    return
label choose_inicial_girl:
    $ strength_value_1 = 3
    $ personality_value_2 = 3
    $ allure_value_3 = 5
    $ libido_value_4 = 3
    $ dominance_value_5 = 3
    $ brand_reputation_value_6 = 3
    $ guild_reputation_value_7 = 3
    $ standard_of_living_value_8 = 3
    $ hygiene_value_9 = 5
    $ mood_value_10 = 3
    $ injuries_value_11 = 5
    $ teaching_value_12 = 3
    $ stewardship_value_13 = 3
    $ artistry_value_14 = 3
    $ medic_value_15 = 3
    $ fighter_value_16 = 3
    $ magic_value_17 = 3
    $ flagellation_value_18 = 3
    $ torture_value_19 = 3
    $ binding_value_20 = 3
    $ petting_value_21 = 3
    $ oral_sex_value_22 = 3
    $ penetration_value_23 = 3
    $ fetishism_value_24 = 3
    $ faction_36 = 3
    $ sparks_37 = 80000
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
    hide screen slaver_guild
    python:
        if last_girl_selection == "demo/choose_slave.webp":
            demo_girl_text_index = 0
            demo_girl_selection = "Helen"
            premiun_girl_tutorial_selected_localization = "girl_packs/original_premiun_slaves_pack/helen.json"
            if len(all_girls_list) < 3 and demo_girl_selection not in girl_selection_list:
                all_girls_list[len(all_girls_list)]={}
                girl_index = len(all_girls_list) - 1
                girl_selection_list.append(demo_girl_selection)
                girl_selection_list_image.append("demo/choose_slave.webp")
                all_girls_list[girl_index] = load_json(premiun_girl_tutorial_selected_localization)
                generation_slave()
            elif demo_girl_selection in girl_selection_list and len(all_girls_list) > 1:
                del all_girls_list[girl_selection_list.index(demo_girl_selection)]
                girl_selection_list.remove(demo_girl_selection)
                girl_selection_list_image.remove("demo/choose_slave.webp")
                all_girls_list = {i: v for i, v in enumerate(all_girls_list.values())}
        if last_girl_selection == "demo/choose_amazon.webp":
            demo_girl_text_index = 1
            demo_girl_selection = "Yasmin"
            premiun_girl_tutorial_selected_localization = "girl_packs/original_premiun_slaves_pack/yasmin.json"
            if len(all_girls_list) < 3 and demo_girl_selection not in girl_selection_list:
                all_girls_list[len(all_girls_list)]={}
                girl_index = len(all_girls_list) - 1
                girl_selection_list.append(demo_girl_selection)
                girl_selection_list_image.append("demo/choose_amazon.webp")
                all_girls_list[girl_index] = load_json(premiun_girl_tutorial_selected_localization)
                generation_slave()
            elif demo_girl_selection in girl_selection_list and len(all_girls_list) > 1:
                del all_girls_list[girl_selection_list.index(demo_girl_selection)]
                girl_selection_list.remove(demo_girl_selection)
                girl_selection_list_image.remove("demo/choose_amazon.webp")
                all_girls_list = {i: v for i, v in enumerate(all_girls_list.values())}
        if last_girl_selection == "demo/choose_princess.webp":
            demo_girl_text_index = 2         
            demo_girl_selection = "Wilhelmine"
            premiun_girl_tutorial_selected_localization = "girl_packs/original_premiun_slaves_pack/wilhelmine.json"
            if len(all_girls_list) < 3 and demo_girl_selection not in girl_selection_list:
                all_girls_list[len(all_girls_list)]={}
                girl_index = len(all_girls_list) - 1
                girl_selection_list.append(demo_girl_selection)
                girl_selection_list_image.append("demo/choose_princess.webp")
                all_girls_list[girl_index] = load_json(premiun_girl_tutorial_selected_localization)
                generation_slave()
            elif demo_girl_selection in girl_selection_list and len(all_girls_list) > 1:
                del all_girls_list[girl_selection_list.index(demo_girl_selection)]
                girl_selection_list.remove(demo_girl_selection)
                girl_selection_list_image.remove("demo/choose_princess.webp")
                all_girls_list = {i: v for i, v in enumerate(all_girls_list.values())}
        try:
            girl_index = girl_selection_list.index(demo_girl_selection)
        except ValueError: 
            girl_index = 0
            if girl_selection_list[0] == "Helen":
                demo_girl_text_index = 0
            elif girl_selection_list[0] == "Yasmin":
                demo_girl_text_index = 1
            elif girl_selection_list[0] == "Wilhelmine":
                demo_girl_text_index = 2

        girl_selection_list_for_text_display = ", ".join(girl_selection_list)
    
    call screen choose_inicial_girl_screen
    return

