init python:
    class night_rules_fuctions:
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

