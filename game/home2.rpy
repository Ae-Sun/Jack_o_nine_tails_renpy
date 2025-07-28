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