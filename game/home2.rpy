# This is a direct continuation of home.rpy.
# The file was split into multiple parts because it became too large for the AI (autocomplete).
screen master_diary_menu():
    add "bg/page_blank.webp" xsize 795 ysize 535 pos(0.5028,0.42) anchor (0.5,0.5)
    python:
        n = 0
        m = 0
    vbox:
        pos(0.24,0.068)
        text "{u}DAY [day_tracker]:{/u}" size 16 color "#0000D8" font "fonts/Segoe Print.ttf"
        text "{u}GOOD MOOD MOODLETS:{/u}" size 16 color "#0000D8" font "fonts/Segoe Print.ttf"
        for values in master_mood_state["good_mood"]:
            if master_mood_state["good_mood"][values]["active"]:
                text dic_master_mood["good_mood"][values] size 16 color "#0000D8" font "fonts/Segoe Print.ttf" xmaximum 700
                python:
                    n += 1
        if n == 0:
            text "You have no good moodlet effects" size 16 color "#0000D8" font "fonts/Segoe Print.ttf" xmaximum 700
        add "spacer" size(0,40)
        text "{u}BAD MOOD MOODLETS:{/u}" size 16 color "#0000D8" font "fonts/Segoe Print.ttf"
        for values in master_mood_state["bad_mood"]:
            if master_mood_state["bad_mood"][values]["active"]:
                text dic_master_mood["bad_mood"][values] size 16 color "#0000D8" font "fonts/Segoe Print.ttf" xmaximum 700
                python:
                    m += 1
        if m == 0:
            text "You have no bad moodlet effects" size 16 color "#0000D8" font "fonts/Segoe Print.ttf" xmaximum 700
label slave_bathing_label():
    python:
        choosing_image_condition = "slave_auto_bath_self"
        pic_displayed = display_pic()
        room_name = "Bath"
        slave_bath_selfwash_ask()
        setup_interaction_screen()
        interaction_textdisplay_screen_text = bathing_slave_alone[all_girls_list[girl_index]["psy_status"]]
    call screen interaction_textdisplay_screen()



screen interaction_screen():
    add bgstyle2 xsize 1280 ysize 720 
    add pic_displayed xsize 795 ysize 535
    
screen interaction_textdisplay_screen():
    text interaction_textdisplay_screen_text pos (0.02, 0.78) size 20 font "consolas.ttf" xmaximum 750 color "#000000"
    key "K_SPACE" action SetVariable("current_menu", 0),Jump("Home")
    vbox:
        xalign 0.655
        yalign 0.96
        imagebutton:
            idle "buttons/auk_fwrd.webp" anchor (0.5, 0.5)
            hover "buttons/auk_fwrd_hover.webp"
            action Jump("Home")
label master_bathing_label():
    python:
        interaction_textdisplay_screen_text = dic_bath_master[0]
        master_bath()
        setup_interaction_screen()
    call screen interaction_textdisplay_screen()
    
screen excitement_screen():
    zorder 50
    add "gui/confirm_frame.png" at truecenter
    vbox:
        pos (0.5, 0.28)
        text "{b}EXCITEMENT:{/b}" xmaximum  445:
            color "#191970"
            anchor(0.5,0.0)
            size 14
            font "fonts/Segoe Print.ttf"
        add "spacer" size(0,12)
        for a in dic_master_excitement_colored:
            textbutton dic_master_excitement_colored[a] anchor (0.5,0.5): 
                style "attribute_mood"
                action NullAction()
    text " Press space to close this window.":
        pos (0.33, 0.65)
        color "#191970"
        size 14
        font "fonts/Segoe Print.ttf"
    imagebutton:
        idle "buttons/ok-icon.webp" pos (0.5, 0.7)
        hover "buttons/ok-icon_hover.webp"
        action Hide("excitement_screen")
    key "K_SPACE" action Hide("excitement_screen")
