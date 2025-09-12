define inicial_girls = [
    ("demo/choose_princess.webp", 0),
    ("demo/choose_amazon.webp", 265),
    ("demo/choose_slave.webp", 530),
]
define dic_slave_attributes_keys = {
    "beauty":       "BEAUTY",
    "endurance":    "ENDURANCE",
    "empathy":      "EMPATHY",
    "temperament":  "TEMPERAMENT",
    "intelligence": "INTELLIGENCE",
    "nature":       "NATURE",
    "pride":        "PRIDE",
    "exoticism":    "EXOTICISM",
    "physical":     "PHYSICAL",
    "style":        "STYLE",
    "fame":         "FAME",
}
define dic_girl_age_text2 = [
    "young","loli","milf"    
]


define dic_girl_choosing_image_condition_short = {
    "slave_auto_sleep":"rest",
    "slave_auto_cook":"cook",
    "slave_auto_maid":"clean",
    "slave_auto_bath":"wash",
    "slave_auto_bath_self":"bath",
    "slave_auto_alarm":"bj"
}
define dic_slave_attributes_description_keys = {
    "beauty": "Beauty",
    "endurance": "Endurance",
    "empathy": "Empathy",
    "temperament": "Temperament",
    "intelligence": "Intelligence",
    "nature": "Nature",
    "pride": "Pride",
    "physical":"Physical",
    "style":"Style",
    "fame":"Fame",
    "exoticism":"Exoticism",
    "cooking": "Cooking",
    "maid": "Maid",
    "secretary": "Secretary",
    "elocution": "Elocution",
    "nursing": "Nursing",
    "alchemy": "Alchemy",
    "witchcraft": "Witchcraft",
    "athletics": "Athletics",
    "gladiatrix": "Gladiatrix",
    "dance": "Dance",
    "music": "Music",
    "painting": "Painting",
    "pet": "Pet",
    "pony": "Pony",
    "cow": "Cow",
    "petting":"Petting",
    "oral_pleasure":"Oral Pleasure",
    "penetration":"Penetration",
    "group_sex":"Group Sex",
    "demostration":"Demostration",
    "fetishism":"Fetishism",
    "xenophily":"Xenophily",
}
define dic_slave_tier_classification = {
    0: "F-",
    1: "D-",
    2: "C-",
    3: "B+",
    4: "A+",
    5: "S+",
    6: "S++",
}
define dic_slave_tier_classification_physical = {
    0: "F-",
    1: "D-",
    2: "B+",
    3: "A+",
    4: "S+",
    5: "F-",
    6: "S++",
}
define dic_rating = {
    0: "F-",
    1: "D-",
    2: "D+",
    3: "C-",
    4: "C+",
    5: "B-",
    6: "B+",
    7: "A-",
    8: "A+",
    9: "S-",
    10: "S+",
    11: "S++",
}
define dic_rating_colored = {
    0: "{color=#CD0000}F-{/color}",
    1: "{color=#EA0190}D-{/color}",
    2: "{color=#FF4FBB}D+{/color}",
    3: "{color=#6B0084}C-{/color}",
    4: "{color=#2e0051}C+{/color}",
    5: "{color=#0000D8}B-{/color}",
    6: "{color=#5858d0}B+{/color}",
    7: "{color=#009FEF}A-{/color}",
    8: "{color=#50ffcb}A+{/color}",
    9: "{color=#009900}S-{/color}",
    10: "{color=#003000}S+{/color}",
    11: "{color=#996515}S++{/color}"
}
define dic_slave_tier_classification_colored = {
    0: "{color=#CD0000}F-{/color}",
    1: "{color=#EA0090}D-{/color}",
    2: "{color=#6B0084}C-{/color}",
    3: "{color=#0000D8}B+{/color}",
    4: "{color=#009FEF}A+{/color}",
    5: "{color=#009900}S+{/color}"
}

define dic_slave_attributes = {
    "beauty":        ["Ugly"            ,"Plain"          ,"Cute"          ,"Pretty   "    ,"Beautiful"    ,"Exquisite"      ,"Goddess"     ,"{b}BEAUTY:{/b}\n  Natural beauty very strongly influences her market price. Your slave's rank will never rise higher than her beauty or fame (whichever is higher). At auctions, beautiful slaves are sold for higher prices.","   ll your efforts to improve the appearance of the slave will influence style, not beauty. Stylishness is important too, but the value of natural beauty is huge. You can increase beauty only by neoplasty surgery in the Technosphere medical center and only once for each slave. Try to buy beautiful slaves if you intend to train them to high ranks. Beauty is decreased while a slave has scars or bruises until they are removed or healed."],
    "endurance":     ["Dyinng"          ,"Feeble"         ,"Weakened"      ,"Healthy"      ,"Tough"        ,"Enduring"       ,"Iron"        ,"{b}ENDURANCE:{/b}\n  Hardy slaves have more energy, can work better and are more attractive for clients. Critical decrease of endurance can kill your slave.","   If your slave is weak, feed her well; it's desirable to prescribe supplements and not let her become exhausted (receive red energy stars), nor over-exercise (when she has purple energy stars, intensive exercise is harmful), nor gain weight if she is overweight, nor end the day with negative calories. Build endurance with gymnastics, athletics, dance, racing, martial arts, pet play or vigorous sex. Heal injuries (a nurse assistant and your own skill helps) and sicknesses, and use drugs sparingly."],
    "empathy":       ["Heartless"       ,"Callous"        ,"Insensitive"   ,"Sensitive"    ,"Caring"       ,"Nurturing"      ,"Nurturing+"  ,"{b}EMPATHY:{/b}\n  On one hand the gentle slave is easier affected by stress and stung by punishments. On the other hand she is turned on much faster and is more lively, which makes her attractive for customers.","   Callousness develops quickly with mistreatment. Severe punishments are especially harmful. While a less sensitive slave is hardened against depression and endures suffering, she is also less valuable. There are no reliable ways to increase a slave's empathy, but refined petting and pleasures may help."],
    "temperament":   ["Apathetic"       ,"Cold"           ,"Reserved"      ,"Reactive"     ,"Lively"       ,"Passionate"     ,"Passionate+" ,"{b}TEMPERAMENT:{/b}\n  Temperamental slaves are uncontrollable and are less susceptible to education but they are passionate lovers and are more interesting for customers, as they have a bright personality. Calm ones are easier to control.","   Temperament is an ambiguous feature. More emotional slaves are harder to control, but cold ones are less valuable. By suppressing initiative, driving her into depression and silencing her you will eventually lower her temperament. Getting her to express herself or interact openly with the slaver will often increase temperament."],
    "intelligence":  ["Retarded"        ,"Stupid"         ,"Dimwitted"     ,"Bright"       ,"Clever"       ,"Intelligent"    ,"Genius"      ,"{b}INTELLIGENCE:{/b}\n  Smart slaves master skills faster and are able to cope with accounting better, so they are more valuable on the market. But it is easier to dominate and manipulate stupid ones.","   Smarts are not always useful, as more intellectual slaves are harder to control and manipulate. On the other hand, rational factors of submission and explanatory conversations will be more effective. Allowing a slave to express herself, training secretarial skills and doing household accounting can contribute to intellectual development."],
    "nature":        ["Spineless"       ,"Coward"         ,"Uncertain"     ,"Independent"  ,"Determined"   ,"Willful"        ,"Willful+"    ,"{b}NATURE:{/b}\n  Strong character makes a slave more interesting and independent but lowers her obedience. It is easier to control weak-willed slaves but their value will be lower too.","   Nature is an ambiguous feature. It is very hard to train a willful slave, but a weak will lowers a slave's value. The more you make a slave do what she does not want to do, the more her nature will break. It is difficult to restore nature, so do not overdo it. Victory in duels, martial arts, sleeping in her own room, assisting in training other slaves, and being given a measure of independence or opportunities to socialize can help in the formation of a solid nature."],
    "pride":         ["Arrogant"        ,"Haughty"        ,"Proud"         ,"Aloof"        ,"Open"         ,"Unashamed"      ,"Unashamed+"  ,"{b}PRIDE:{/b}\n  Pride prevents a slave from being open and enjoying sex. It also causes her to resist your will, and refuse humiliating orders.","   Pride is harmful both in training and in the sale, so you should work on her openness. Force her to do dirty, perverted and degrading things, and assign strict rules. Eventually pride will be broken and the slave will become more open. But do not overdo it, as with pride, you can break the very slave."],
    "exoticism":     ["Ordinary"        ,"Quirky"         ,"Mysterious"    ,"Enigmatic"    ,"Exotic"       ,"Mystical"       ,"Mythical+"   ,"{b}EXOTICISM:{/b}\n  Slaves with unusual, irregular appearance attract attention at once and generally are more interesting for customers.","   Some slaves are exotic inherently. You can increase exoticism with tattoos, piercings, body modifications, as well as flamboyant clothes and wigs."],
    "physical":      ["Corpulent"       ,"Chubby"         ,"Voluptuous"    ,"Slender"      ,"Model"        ,"Bony"           ,"Model+"      ,"{b}PHYSICAL:{/b}\n  You can get more mince from fat slaves but they are not attractive. Weedy starvelings aren't attractive as well, but you can't get a lot of meat from them either. It's better to keep your slave slim, but not skinny.","   Extra weight is generally harmful, as well as a lack of it. To keep your slave slim you need to balance her nutrition in a way that is sufficient, but not excessive. The more a slave works and the more endurance she has, the more food she needs. Physical exercises don't decrease weight directly but are a good way to burn extra calories. If a slave is underweight, feed her well and minimize athletics."],
    "style":         ["Unfashionable"   ,"Unremarkable"   ,"Common"        ,"Stylish"      ,"Refined"      ,"Elegant"        ,"Elegant+"    ,"{b}STYLE:{/b}\n  A slave's appearance is extremely important during the sale. Customers will like well-groomed and well-dressed slaves, and an unappealing slave can be turned down even if she fits the requirements.","   Style depends little on natural abilities and skills, though it is influenced by the ability to communicate (elocution) and presence (dancing). Style suffers from dirt and sloppiness. Hairstyle, make-up, perfume, beautiful clothes and jewelry - all of these improve style and make the slave more attractive to customers. It is not necessary to constantly maintain style - it plays a role only when it is time to show the girl to the customer."],
    "fame":          ["Unknown"         ,"Rumored"        ,"Recognized"    ,"Celebrity"    ,"Famous"       ,"Legendary"      ,"Legendary+"  ,"{b}FAME:{/b}\n  Famous slaves are much more valuable. Your slave's rank can reach the level of her fame, even if she lacks other attributes, beauty included.","   Fame is not the most important parameter for a slave. You can train wonderful product unconcerned about this. Fame will grow with victories in the arena and colosseum.","   Fame is not the most important parameter for a slave. You can train wonderful product unconcerned about this. Fame will grow with victories in the arena and colosseum."]
    }
define dic_slave_misc ={
    "charm_moral": ["No Devotion", "Wavering", "Dutiful", "Loyal", "Devoted", "Zealous","Zealous+"],
    "charm_angst": ["No Despair", "Despondent", "Demoralized", "Disheartened", "Despairing", "Hopeless","No Despair+"],
    "charm_spoil": ["Not Spoiled", "Balky", "Unruly", "Restive", "Entitled", "Contumacious","Not Spoiled+"],
    "hair_style": ["Tangled Hair", "Combed Hair", "Orderly Hair", "Orderly Hair", "Orderly Hair", "Neat Hair", "Neat Hair", "Stylish Hair"],
    "slave_tattoo": ["No Tattoos", "Small Tattoo", "Tattoo Outline", "Colorful Tattoo", "Traced Body", "Adorned Body"]
}
define dic_slave_mood ={
    "good_mood": {
        "slave_winner"           : "[all_girls_list[girl_index][name]]\n- Hooray, we won! That was amazing. I feel much more confident.",
        "multiple_orgasm"        : "[all_girls_list[girl_index][name]]\n- Ohh, it was great sex! Such a heavenly pleasure… I would like to experience this once again.",
        "kannabis"         : "[all_girls_list[girl_index][name]]\n- Oooo… …this weed is a thing. Such bliss, we need to add some relaxing music.",
        "opium"            : "[all_girls_list[girl_index][name]]\n- I feel good. I feel oblivion flowing through my veins, carrying away pain and sorrow.",
        "alco"             : "[all_girls_list[girl_index][name]]\n- I… hic… am soooooo drunk. Why did you get me drunk, eh? You want to take advantage of my… hic… helpless situation?",
        "no_punish"              : "[all_girls_list[girl_index][name]]\n- You decided not to punish me, although I know that I was guilty. Nice to know that you are sorry for me ^ _ ^",
        "ineffective_punishment" : "[all_girls_list[girl_index][name]]\n- I know you meant to punish me, but it was not as bad as I expected…",
        "gentle"                 : "[all_girls_list[girl_index][name]]\n- It's nice to feel someone's care and affection…",
        "praise"                 : "[all_girls_list[girl_index][name]]\n- Your fair words pleased me.",
        "slave_date"             : "[all_girls_list[girl_index][name]]\n- I loved our walk. I would like to go out again some time!",
        "games"                  : "[all_girls_list[girl_index][name]]\n- Free time for entertainment - that's just awesome! So nice to get away from worries.",
        "dessert"                : "[all_girls_list[girl_index][name]]\n- I still remember the flavor of sweet treats. Mmmm… yummy!",
        "reward"                 : "[all_girls_list[girl_index][name]]\n- A reward for good behavior is nice.",
        "spellguarded"           : "[all_girls_list[girl_index][name]]\n- My will was stronger than your spell! I feel much more confident.",
        "cookie"                 : "[all_girls_list[girl_index][name]]\n- I ate very tasty food and it is certainly nice. Food on your table is much better than in my bowl.",
        "sleep"                  : "[all_girls_list[girl_index][name]]\n- I got a good night's sleep in my room. It is so nice sometimes to relax in comfort.",
        "slept_with_master"      : "[all_girls_list[girl_index][name]]\n- It was so nice to sleep in Master's bed last night.",
        "job"                    : "[all_girls_list[girl_index][name]]\n- Since I did my favorite thing, I feel relieved.",
        "cow"                    : "[all_girls_list[girl_index][name]]\n- I'm so proud of these tits… I never thought it was so good to be milked…",
        "barn"                   : "[all_girls_list[girl_index][name]]\n- It was great to laze in my pen: I want to go back in the barn, please… Mooo!",
        "slave_clean"            : "[all_girls_list[girl_index][name]]\n- I washed recently. Nice to feel clean and fresh.",
        "well_rested"            : "[all_girls_list[girl_index][name]]\n- I rested well yesterday, it is pleasant to slack off from time to time.",
        "orgasm"                 : "[all_girls_list[girl_index][name]]\n- Well… It was so nice to get a discharge. I would not mind cumming like that once more…",
        "clothes"                : "[all_girls_list[girl_index][name]]\n- I have very comfortable clothes. Nothing is too tight and it doesn't interfere.",
        "pony"                   : "[all_girls_list[girl_index][name]]\n- I also have my little pony - being with her is always fun!",
        "slave_love"             : "[all_girls_list[girl_index][name]]\n- Some kind of irresistible force beckons me to you. I always think of you. I want to be beside you… forever.",
        "moral"                  : "[all_girls_list[girl_index][name]]\n- I'm always happy to serve my Master. I'm a good girl, right, Master?",
        "default"                : "[all_girls_list[girl_index][name]]\n- I'm all right. Nothing special…",
        "artifact"               : "[all_girls_list[girl_index][name]]\n- This magic decoration just superb. While I wear it, the world seems a lot better than it is. I will never take it off!"
    },
    "bad_mood": {
        "slave"              : "[all_girls_list[girl_index][name]]\n- I got into this strange unfamiliar world and I was immediately made into a slave. How do you think I feel?",
        "angst"              : "[all_girls_list[girl_index][name]]\n- I do not know what will happen to me tomorrow or even the next minute. Why do I live? I feel like howling of hopelessness…",
        "fear"               : "[all_girls_list[girl_index][name]]\n- I know that you can punish me for any wrongdoing, and live in constant fear. Thoughts about various horrors do not go out of my head.",
        "residu_fear"        : "[all_girls_list[girl_index][name]]\n- Even now, thoughts of various horrors do not go out of my head.",
        "meth"               : "[all_girls_list[girl_index][name]]\n- I feel sick. I feel very, very sick. My mouth is dry, I feel weak, my muscles ache… I NEED DUST!",
        "opium"              : "[all_girls_list[girl_index][name]]\n- I can't stand it. I NEED A DOSE, URGENTLY! Oh, please… I beg of you…",
        "koffe"              : "[all_girls_list[girl_index][name]]\n- I can not wake up before I drink some kamra. I can't even open my eyes.",
        "alco"               : "[all_girls_list[girl_index][name]]\n- My head still hurts after yesterday. I can not drink so much.",
        "loser"              : "[all_girls_list[girl_index][name]]\n- I'm not to blame for this loss! They were too strong…",
        "wounded"            : "[all_girls_list[girl_index][name]]\n- My wounds ache. Every wrong move hurts.",
        "ugly"               : "[all_girls_list[girl_index][name]]\n- All these bruises and scratches… They mutilated me. I'm scared to look at myself in the mirror.",
        "hungry"             : "[all_girls_list[girl_index][name]]\n- I did not get enough food and I worked too hard. I feel weak.",
        "starvation"         : "[all_girls_list[girl_index][name]]\n- I feel really bad. I'm dizzy.",
        "exhausted"          : "[all_girls_list[girl_index][name]]\n- I'm very tired. I need to rest.",
        "raped"              : "[all_girls_list[girl_index][name]]\n- You raped me! I feel dirty, abused and trampled.",
        "defloration"        : "[all_girls_list[girl_index][name]]\n- Sex for the first time is painful. I still hurt down there…",
        "barn_plus"          : "[all_girls_list[girl_index][name]]\n- Yes, this place, this… barn… is dreadful and oppressive… It was like a nightmare.",
        "barn"               : "[all_girls_list[girl_index][name]]\n- All this time in a barn… You cannot treat me like some animal! Please, I won't go back there…",
        "cow"                : "[all_girls_list[girl_index][name]]\n- Milk constantly pours from my breasts… It's awful, I don't want to be a cow!",
        "pain"               : "[all_girls_list[girl_index][name]]\n- You hurt me. I still feel it. It does not go away.",
        "forced"             : "[all_girls_list[girl_index][name]]\n- You have coerced me into doing ugly things. I feel so helpless. And my bruises hurt.",
        "spellbound"         : "[all_girls_list[girl_index][name]]\n- Your evil spell put me down. There are strange voices whispering in my head. They drive me crazy!",
        "shame"              : "[all_girls_list[girl_index][name]]\n- God, I'm still embarrassed. Why did you make me display myself like that?",
        "no_praise"          : "[all_girls_list[girl_index][name]]\n- I tried so hard to do well, and you have not even told me a single good word.",
        "abuse"              : "[all_girls_list[girl_index][name]]\n- You were swearing at me so strongly that I still feel sick from it.",
        "disgust"            : "[all_girls_list[girl_index][name]]\n- I can not forget all this horror. Even pain is easier to endure than those hideous, horrible things that you are doing to me.",
        "slave_food"         : "[all_girls_list[girl_index][name]]\n- That food you are giving me, it is not very good. To tell the truth, it is so vile that it is easier to stay hungry than to push it down my throat…",
        "bad_sleep"          : "[all_girls_list[girl_index][name]]\n- Sleeping conditions are just terrible. My whole body is numb and sore from such a 'rest'…",
        "slept_with_master"  : "[all_girls_list[girl_index][name]]\n- Your bed is softer than the floor, but sleep does not come…",
        "slave_mess"         : "[all_girls_list[girl_index][name]]\n- The house now is a terrible mess, dishes are unwashed, everything is upside down. Not the best conditions for life.",
        "slave_ill"          : "[all_girls_list[girl_index][name]]\n- It hurts to go to the toilet and secretions look strange. I guess I caught something…",
        "slave_dirty"        : "[all_girls_list[girl_index][name]]\n- I'm itchy from the dirt and bad smell. It would be nice to wash…",
        "menstruation"       : "[all_girls_list[girl_index][name]]\n- I have these days… during my period. So my mood isn't the best and I'm moody…",
        "pregnant"           : "[all_girls_list[girl_index][name]]\n- I just feel bad, less energy",
        "job"                : "[all_girls_list[girl_index][name]]\n- You make me engage in boring and unpleasant work. From this I have a bad mood.",
        "prisoner"           : "[all_girls_list[girl_index][name]]\n- I spent so much time in prison. Not the most pleasant experience…",
        "naked"              : "[all_girls_list[girl_index][name]]\n- I have to go naked everywhere. It's cold and humiliating.",
        "clothes"            : "[all_girls_list[girl_index][name]]\n- What you put on me is not pleasant to wear.",
        "horny"              : "[all_girls_list[girl_index][name]]\n- Every girl needs a bit of affection from time to time. Without this it is so sad…",
        "rules"              : "[all_girls_list[girl_index][name]]\n- All these terrible rules that you are forcing me to do… they do not add to the joy of life, actually.",
        "spoil"              : "[all_girls_list[girl_index][name]]\n- You do not appreciate me at all! Look, what kind of conditions are these?! Cheer me up or something! I'm bored!",
        "cheap_gift"         : "[all_girls_list[girl_index][name]]\n- When will you give me the special gift you promised?",
        "cheap_reward"       : "[all_girls_list[girl_index][name]]\n- The reward you promised… was that it?",
        "pony_died"          : "[all_girls_list[girl_index][name]]\n- My little pony died!",
        "default"            : "[all_girls_list[girl_index][name]]\n- Nohow, I do not care.",
        "artifact"           : "[all_girls_list[girl_index][name]]\n- My magic decoration! My… My… precioooous… Angry master took it away from us… gollum… poor… poor us… so lonely…",
        "boring"             : "[all_girls_list[girl_index][name]]\n- Doing the same thing everyday is really boring."
    }
}
define dic_slave_skills = {
    "maid": ["Not a Maid F-", "Drudge D-", "Skivvy C-", "Maid B+", "Handmaid A+", "Housekeeper S+", "Mistress of the Manor S++"],
    "cooking": ["Not a Cook F-", "Scullery Trainee D-", "Kitchener C-", "Cook B+", "Chef A+", "Culinary Artist S+", "Gastronomic Legend S++"],
    "secretary": ["Not a Secretary F-", "Paper Shuffler D-", "Novice Clerk C-", "Secretary B+", "Comptroller A+", "Procurator S+", "Chancellor of Ledgers S++"],
    "elocution": ["Not an Elocutionist F-", "Inarticulate D-", "Raconteuse C-", "Elocutionist B+", "Orator A+", "Rhetorician S+", "Voice of the Realm S++"],
    "nursing": ["Not a Nurse F-", "Anatomy Student D-", "Triage Aid C-", "Nurse B+", "Ward Sister A+", "Matron S+", "Healer Supreme S++"],
    "alchemy": ["Not an Alchemist F-", "Potion Apprentice D-", "Alembic Attendant C-", "Alchemist B+", "Arcanist A+", "Mistress of Arcanum S+", "Transmuter of Essence S++"],
    "witchcraft": ["Not a Witch F-", "Young Hag D-", "Theurgist C-", "Witch B+", "Enchantress A+", "Sorceress S+", "Archwitch Eternal S++"],
    "athletics": ["Bedridden F-", "Plodder D-", "Walker C-", "Athlete B+", "Sprinter A+", "Marathonist S+", "Olympian S++"],
    "gladiatrix": ["Not a Gladiatrix F-", "Bustuāria D-", "Prōvocātrīx C-", "Gladiatrix B+", "Bellātrīx A+", "Amazon S+", "Queen Amazon S++"],
    "dance": ["Not a Dancer F-", "Two Left Feet D-", "Figurant C-", "Dancer B+", "Coryphée A+", "Étoile S+", "Divine Muse S++"],
    "music": ["Not a Musician F-", "Solfège Initiate D-", "Trained Ear C-", "Musician B+", "Prodigy A+", "Virtuoso S+", "Maestra S++"],
    "painting": ["Not a Painter F-", "Dauber D-", "Sketcher C-", "Painter B+", "Colorist A+", "Artifex S+", "Master of the Canvas S++"],
    "pet": ["Not a Pet F-", "Feral D-", "Housebroken C-", "Pet B+", "Domesticated A+", "Animalistic S+", "Primal Companion S++"],
    "pony": ["Not a Pony F-", "Nag D-", "Hackney C-", "Pony B+", "Trotter A+", "Racehorse S+", "Champion Steed S++"],
    "cow": ["Not a Cow F-", "Barely Bovine D-", "Learning to Moo C-", "Cow B+", "Heifer A+", "Queen of Kine S+", "Divine Bovine S++"],
}
define dic_slave_skills_sexual = {
    "petting": ["Petting F-", "Petting D-", "Petting C-", "Petting B+", "Petting A+", "Petting S+", "Petting S++"],
    "oral_pleasure": ["Oral Pleasure F-", "Oral Pleasure D-", "Oral Pleasure C-", "Oral Pleasure B+", "Oral Pleasure A+", "Oral Pleasure S+", "Oral Pleasure S++"],
    "penetration": ["Penetration F-", "Penetration D-", "Penetration C-", "Penetration B+", "Penetration A+", "Penetration S+", "Penetration S++"],
    "group_sex": ["Group Sex F-", "Group Sex D-", "Group Sex C-", "Group Sex B+", "Group Sex A+", "Group Sex S+", "Group Sex S++"],
    "demostration": ["Demonstration F-", "Demonstration D-", "Demonstration C-", "Demonstration B+", "Demonstration A+", "Demonstration S+", "Demonstration S++"],
    "fetishism": ["Fetishism F-", "Fetishism D-", "Fetishism C-", "Fetishism B+", "Fetishism A+", "Fetishism S+", "Fetishism S++"],
    "xenophily": ["Xenophily F-", "Xenophily D-", "Xenophily C-", "Xenophily B+", "Xenophily A+", "Xenophily S+", "Xenophily S++"]
}
define dic_sex_experience = {
        "petting":{
            "handjob":0,
            "footjob":0,
            "rubbing":0,
            "titjob":0
        },
        "oral_pleasure":{
            "kissing":0,
            "licking":0,
            "blowjob":0,
            "deep_throat":0,
            "rimming":0
        },
        "penetration":{
            "vaginal_sex":0,
            "fisting":0,
            "anal_sex":0,
            "anal_fisting":0
        },
        "group_sex":{
            "threesome":0,
            "bukkake":0,
            "doble_penetration":0,
            "triple_penetration":0,
            "gangbang":0
        },
        "demostration":{
            "seduction":0,
            "masturbation":0,
            "dildo":0,
            "humiliation":0,
            "exhibitionism":0
        },
        "fetishism":{
            "enema":0,
            "masochism":0,
            "self-torture":0,
            "golden_shower":0,
            "scat":0
        },
        "xenophily":{
            "dog_mating":0,
            "pig_mating":0,
            "house_mating":0,
            "spider_mating":0,
            "sea_tentacle_mating":0,
            "field_mating":0
        }

    }
define attributes_min_threshold = {
    0: -10,
    1: -10,
    2: -10,
    3: -20,
    4: -40,
    5: -80,
}
define attributes_max_threshold = {
    0: 10,
    1: 20,
    2: 40,
    3: 80,
    4: 160,
    5: 10,
}
define attributes_max_threshold_inverse = {
    0: 10,
    1: 160,
    2: 80,
    3: 40,
    4: 20,
    5: 10,
}
define attributes_min_threshold_inverse = {
    0: -80,
    1: -40,
    2: -20,
    3: -10,
    4: -10,
    5: -10,
}
define dic_traits_skills = {
    "cookingtrait":      ["Average", "Good Cook", "Excellent Cook", "Disastrous Cook", "Bad Cook"],
    "maidtrait":         ["Average", "Good Maid", "Excellent Maid", "Disastrous Maid", "Bad Maid"],
    "secretarytrait":    ["Average", "Good Secretary", "Excellent Secretary", "Disastrous Secretary", "Bad Secretary"],
    "elocutiontrait":    ["Average", "Good Speaker", "Excellent Speaker", "Disastrous Speaker", "Bad Speaker"],
    "nursingtrait":      ["Average", "Good Nurse", "Excellent Nurse", "Disastrous Nurse", "Bad Nurse"],
    "alchemytrait":      ["Average", "Good Alchemist", "Excellent Alchemist", "Disastrous Alchemist", "Bad Alchemist"],
    "witchcrafttrait":   ["Average", "Good Witch", "Excellent Witch", "Disastrous Witch", "Bad Witch"],
    "athleticstrait":    ["Average", "Good Athlete", "Excellent Athlete", "Disastrous Athlete", "Bad Athlete"],
    "gladiatrixtrait":   ["Average", "Good Gladiatrix", "Excellent Gladiatrix", "Disastrous Gladiatrix", "Bad Gladiatrix"],
    "dancetrait":        ["Average", "Good Dancer", "Excellent Dancer", "Disastrous Dancer", "Bad Dancer"],
    "musictrait":        ["Average", "Good Musician", "Excellent Musician", "Disastrous Musician", "Bad Musician"],
    "paintingtrait":     ["Average", "Good Painter", "Excellent Painter", "Disastrous Painter", "Bad Painter"],
    "pettrait":          ["Average", "Good Pet", "Excellent Pet", "Disastrous Pet", "Bad Pet"],
    "ponytrait":         ["Average", "Good Pony", "Excellent Pony", "Disastrous Pony", "Bad Pony"],
    "cowtrait":          ["Average", "Good Cow", "Excellent Cow", "Disastrous Cow", "Bad Cow"]
}
define dic_slave_mood_show = {
    "mood":[
    "{color=#cd0000}Depressed{/color}",
    "{color=#be0000}Dysphoric{/color}",
    "{color=#af0000}Sullen{/color}",
    "{color=#a00000}Melancholic{/color}",
    "{color=#910000}Pessimistic{/color}",
    "{color=#0D0D0D}Calm{/color}",
    "{color=#EA0090}Hopeful{/color}",
    "{color=#6B0084}Optimistic{/color}",
    "{color=#0000D8}Pleased{/color}",
    "{color=#009FEF}Euphoric{/color}",
    "{color=#009900}Ecstatic{/color}",
    "{color=#009900}Ecstatic+{/color}"
    ]
}
define dic_traits_skills_descriptions = {
    "cookingtrait": [
        "Null",
        "{b}Good Cook{/b} \nYour slave enjoys cooking. This will allow her to become an excellent cook!",
        "{b}Excellent Cook{/b} \nYour slave enjoys cooking. This will allow her to become an excellent cook! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Cook{/b} \nYour slave shows little interest in cooking. Becoming a good cook may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Cook{/b} \nYour slave shows little interest in cooking. Becoming a good cook may prove difficult for her."
    ],
    "maidtrait": [
        "Null",
        "{b}Good Maid{/b} \nYour slave seems to take great pleasure in keeping order in the house. This will allow her to become an excellent maid!",
        "{b}Excellent Maid{/b} \nYour slave seems to take great pleasure in keeping order in the house. This will allow her to become an excellent maid! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Maid{/b} \nYour slave shows little interest in maintaining order around the house. Becoming a good maid may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Maid{/b} \nYour slave shows little interest in maintaining order around the house. Becoming a good maid may prove difficult for her."
    ],
    "secretarytrait": [
        "Null",
        "{b}Good Secretary{/b} \nYour slave has excellent instincts for a personal assistant – she is collected, attentive, and easily copes with paperwork. You should use this talent to its maximum!",
        "{b}Excellent Secretary{/b} \nYour slave has excellent instincts for a personal assistant – she is collected, attentive, and easily copes with paperwork. You should use this talent to its maximum! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Secretary{/b} \nYour slave shows little interest in administrative tasks. Becoming a good secretary may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Secretary{/b} \nYour slave shows little interest in administrative tasks. Becoming a good secretary may prove difficult for her."
    ],
    "elocutiontrait": [
        "Null",
        "{b}Good Speaker{/b} \nYour slave shows a talent for self-expression. Developing her etiquette and rhetoric will be easy, and this is clearly good news!",
        "{b}Excellent Speaker{/b} \nYour slave shows a talent for self-expression. Developing her etiquette and rhetoric will be easy, and this is clearly good news! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Speaker{/b} \nYour slave shows little interest in speaking skills. Becoming a good orator may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Speaker{/b} \nYour slave shows little interest in speaking skills. Becoming a good orator may prove difficult for her."
    ],
    "nursingtrait": [
        "Null",
        "{b}Good Nurse{/b} \nYour slave shows care and attention toward others. This will allow her to become an excellent nurse!",
        "{b}Excellent Nurse{/b} \nYour slave shows care and attention toward others. This will allow her to become an excellent nurse! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Nurse{/b} \nYour slave shows little interest in nursing. Becoming a good nurse may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Nurse{/b} \nYour slave shows little interest in nursing. Becoming a good nurse may prove difficult for her."
    ],
    "alchemytrait": [
        "Null",
        "{b}Good Alchemist{/b} \nYour slave enjoys experimenting with potions and ingredients. This will allow her to become an excellent alchemist!",
        "{b}Excellent Alchemist{/b} \nYour slave enjoys experimenting with potions and ingredients. This will allow her to become an excellent alchemist! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Alchemist{/b} \nYour slave shows little interest in alchemy. Becoming a good alchemist may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Alchemist{/b} \nYour slave shows little interest in alchemy. Becoming a good alchemist may prove difficult for her."
    ],
    "witchcrafttrait": [
        "Null",
        "{b}Good Witch{/b} \nYour slave is attuned to magical forces. This will allow her to become an excellent witch!",
        "{b}Excellent Witch{/b} \nYour slave is attuned to magical forces. This will allow her to become an excellent witch! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Witch{/b} \nYour slave shows little interest in witchcraft. Becoming a good witch may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Witch{/b} \nYour slave shows little interest in witchcraft. Becoming a good witch may prove difficult for her."
    ],
    "athleticstrait": [
        "Null",
        "{b}Good Athlete{/b} \nYour slave is energetic and enjoys physical activity. This will allow her to become an excellent athlete!",
        "{b}Excellent Athlete{/b} \nYour slave is energetic and enjoys physical activity. This will allow her to become an excellent athlete! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Athlete{/b} \nYour slave shows little interest in athletics. Becoming a good athlete may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Athlete{/b} \nYour slave shows little interest in athletics. Becoming a good athlete may prove difficult for her."
    ],
    "gladiatrixtrait": [
        "Null",
        "{b}Good Gladiatrix{/b} \nYour slave shows confidence and determination in combat training. This will allow her to become an excellent gladiatrix!",
        "{b}Excellent Gladiatrix{/b} \nYour slave shows confidence and determination in combat training. This will allow her to become an excellent gladiatrix! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Gladiatrix{/b} \nYour slave shows little interest in combat training. Becoming a good gladiatrix may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Gladiatrix{/b} \nYour slave shows little interest in combat training. Becoming a good gladiatrix may prove difficult for her."
    ],
    "dancetrait": [
        "Null",
        "{b}Good Dancer{/b} \nYour slave moves gracefully and enjoys expressing herself through dance. This will allow her to become an excellent dancer!",
        "{b}Excellent Dancer{/b} \nYour slave moves gracefully and enjoys expressing herself through dance. This will allow her to become an excellent dancer! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Dancer{/b} \nYour slave shows little interest in dancing. Becoming a good dancer may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Dancer{/b} \nYour slave shows little interest in dancing. Becoming a good dancer may prove difficult for her."
    ],
    "musictrait": [
        "Null",
        "{b}Good Musician{/b} \nYour slave enjoys playing music and has a good sense of rhythm. This will allow her to become an excellent musician!",
        "{b}Excellent Musician{/b} \nYour slave enjoys playing music and has a good sense of rhythm. This will allow her to become an excellent musician! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Musician{/b} \nYour slave shows little interest in music. Becoming a good musician may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Musician{/b} \nYour slave shows little interest in music. Becoming a good musician may prove difficult for her."
    ],
    "paintingtrait": [
        "Null",
        "{b}Good Painter{/b} \nYour slave has a good eye for detail and enjoys creating art. This will allow her to become an excellent painter!",
        "{b}Excellent Painter{/b} \nYour slave has a good eye for detail and enjoys creating art. This will allow her to become an excellent painter! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Painter{/b} \nYour slave shows little interest in painting. Becoming a good painter may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Painter{/b} \nYour slave shows little interest in painting. Becoming a good painter may prove difficult for her."
    ],
    "pettrait": [
        "Null",
        "{b}Good Pet{/b} \nIt seems that your slave really likes to pretend to be a pet. And, most importantly, she is doing it great. Training will go well!",
        "{b}Excellent Pet{/b} \nIt seems that your slave really likes to pretend to be a pet. And, most importantly, she is doing it great. Training will go well! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Pet{/b} \nYour slave shows little interest in pet play. Becoming a good pet may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Pet{/b} \nYour slave shows little interest in pet play. Becoming a good pet may prove difficult for her."
    ],
    "ponytrait": [
        "Null",
        "{b}Good Pony{/b} \nApparently, your slave loves to be a horse. What others would consider humiliating and difficult, she finds fun and interesting. This will allow her to become an excellent pony!",
        "{b}Excellent Pony{/b} \nApparently, your slave loves to be a horse. What others would consider humiliating and difficult, she finds fun and interesting. This will allow her to become an excellent pony! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Pony{/b} \nYour slave shows little interest in pony play. Becoming a good pony may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Pony{/b} \nYour slave shows little interest in pony play. Becoming a good pony may prove difficult for her."
    ],
    "cowtrait": [
        "Null",
        "{b}Good Cow{/b} \nYour slave is not in a hurry to use her body or her mind, and likes to just loaf: perhaps she could be more easily turned into a milk cow?",
        "{b}Excellent Cow{/b} \nYour slave is not in a hurry to use her body or her mind, and likes to just loaf: perhaps she could be more easily turned into a milk cow? She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Cow{/b} \nYour slave shows little interest in the cow lifestyle. Becoming a good cow slave may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Cow{/b} \nYour slave shows little interest in the cow lifestyle. Becoming a good cow slave may prove difficult for her."
    ]
}
define dic_traits_sexual = {
    "pettingtrait":      ["None", "Likes Petting", "Loves Petting", "Hates Petting", "Dislikes Petting"],
    "oral_pleasuretrait":["None", "Likes Oral Pleasure", "Loves Oral Pleasure", "Hates Oral Pleasure", "Dislikes Oral Pleasure"],
    "penetrationtrait":  ["None", "Likes Penetration", "Loves Penetration", "Hates Penetration", "Dislikes Penetration"],
    "group_sextrait":    ["None", "Likes Group Sex", "Loves Group Sex", "Hates Group Sex", "Dislikes Group Sex"],
    "demotrationtrait":  ["None", "Likes Demonstrations", "Loves Demonstrations", "Hates Demonstrations", "Dislikes Demonstrations"],
    "fetishismtrait":    ["None", "Likes Fetishism", "Loves Fetishism", "Hates Fetishism", "Dislikes Fetishism"],
    "xenophily":         ["None", "Likes Xenophily", "Loves Xenophily", "Hates Xenophily", "Dislikes Xenophily"]
}

define dic_traits_sexual_description = {
    "pettingtrait": [
        "Null",
        "{b}Likes Petting{/b} \nYour slave absolutely loves being petted and craves physical closeness. This will greatly enhance her sensuality!",
        "{b}Loves Petting{/b} \nYour slave absolutely loves being petted and craves physical closeness. This will greatly enhance her sensuality! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Petting{/b} \nYour slave shows little interest in petting and gentle touch. Becoming affectionate may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Petting{/b} \nYour slave shows little interest in petting and gentle touch. Becoming affectionate may prove difficult for her."
    ],
    "oral_pleasuretrait": [
        "Null",
        "{b}Likes Oral Pleasure{/b} \nYour slave has a strong passion for oral intimacy and excels at it. This will heighten her desirability!",
        "{b}Loves Oral Pleasure{/b} \nYour slave has a strong passion for oral intimacy and excels at it. This will heighten her desirability! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Oral Pleasure{/b} \nYour slave shows little interest in oral pleasure. Developing skills here may be challenging. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Oral Pleasure{/b} \nYour slave shows little interest in oral pleasure. Developing skills here may be challenging."
    ],
    "penetrationtrait": [
        "Null",
        "{b}Likes Penetration{/b} \nYour slave loves penetration and finds great pleasure in it, enhancing her sexual experiences.",
        "{b}Loves Penetration{/b} \nYour slave loves penetration and finds great pleasure in it, enhancing her sexual experiences. She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Penetration{/b} \nYour slave dislikes penetration and avoids it whenever possible. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Penetration{/b} \nYour slave dislikes penetration and avoids it whenever possible."
    ],
    "group_sextrait": [
        "Null",
        "{b}Likes Group Sex{/b} \nYour slave loves group sex and thrives in shared intimate situations.",
        "{b}Loves Group Sex{/b} \nYour slave loves group sex and thrives in shared intimate situations. She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Group Sex{/b} \nYour slave shows little interest in group sex and prefers one-on-one encounters. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Group Sex{/b} \nYour slave shows little interest in group sex and prefers one-on-one encounters."
    ],
    "demotrationtrait": [
        "Null",
        "{b}Likes Demonstrations{/b} \nYour slave loves being the center of attention and enjoys sexual demonstrations.",
        "{b}Loves Demonstrations{/b} \nYour slave loves being the center of attention and enjoys sexual demonstrations. She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Demonstrations{/b} \nYour slave shows little interest in demonstrating her skills openly. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Demonstrations{/b} \nYour slave shows little interest in demonstrating her skills openly."
    ],
    "fetishismtrait": [
        "Null",
        "{b}Likes Fetishism{/b} \nYour slave loves exploring fetishes and alternative sexual interests.",
        "{b}Loves Fetishism{/b} \nYour slave loves exploring fetishes and alternative sexual interests. She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Fetishism{/b} \nYour slave shows little interest in fetishism and prefers vanilla intimacy. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Fetishism{/b} \nYour slave shows little interest in fetishism and prefers vanilla intimacy."
    ],
    "xenophily": [
        "Null",
        "{b}Likes Xenophily{/b} \nYour slave loves trying new experiences and partners, showing strong xenophily.",
        "{b}Loves Xenophily{/b} \nYour slave loves trying new experiences and partners, showing strong xenophily. She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Xenophily{/b} \nYour slave shows little interest in unfamiliar partners or new experiences. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Xenophily{/b} \nYour slave shows little interest in unfamiliar partners or new experiences."
    ]
}
define dic_traits_miscellaneous = {
    "lust_driver":       ["None", "High lust", "Nymphomanic", "Asexual", "frigid"],
    "sexual_openness":   ["None", "Open", "Pervert", "Puritanical", "Prudish"],
    "masochism":         ["None", "Accustomed to pain", "Masochism", "Pain averse", "Pain sensitive"],
    "exhibitionism":     ["None", "Likes Exhibitionism", "Loves Exhibitionism", "Hates Exhibitionism", "Dislikes Exhibitionism"],
    "sexual_orientation":["None", "Bi-curious", "Bisexual", "Homosexual", "Homoflexible"],
    "abuse_attitude":    ["None", "Likes Roughness", "Loves Roughness", "Hates Roughness", "Dislikes Roughness"],
    "darkness_attitude": ["None", "Likes Darkness", "Loves Darkness", "Hates Darkness", "Dislikes Darkness"],
    "blood_attitude":    ["None", "Likes Blood", "Loves Blood", "Hates Blood", "Dislikes Blood"],
    "fire_attitude":     ["None", "Likes Fire", "Loves Fire", "Hates Fire", "Dislikes Fire"],
    "water_attitude":    ["None", "Likes Water", "Loves Water", "Hates Water", "Dislikes Water"],
    "spider_attitude":   ["None", "Likes Spiders", "Loves Spiders", "Hates Spiders", "Dislikes Spiders"],
    "passion_comfort":   ["None", "Likes Comfort", "Loves Comfort", "Hates Comfort", "Dislikes Comfort"],
    "passion_fame":      ["None", "Likes Fame", "Loves Fame", "Hates Fame", "Dislikes Fame"],
    "passion_luxury":    ["None", "Likes Luxury", "Loves Luxury", "Hates Luxury", "Dislikes Luxury"],
    "passion_sweets":    ["None", "Likes Sweets", "Loves Sweets", "Hates Sweets", "Dislikes Sweets"],
    "fertility":         ["None", "Fertile", "Very Fertile", "Very Infertile", "Infertile"],
    "deprivation_attitude":["None", "Likes Deprivation", "Loves Deprivation", "Hates Deprivation", "Dislikes Deprivation"]
}

define dic_traits_miscellaneous_description = {
    "lust_driver": [
        "Null",
        "{b}High lust{/b}\nYour slave shows a noticeable sexual drive, which influences her desires and responsiveness.",
        "{b}Nymphomanic{/b}\nYour slave is a nymphomaniac, constantly craving and seeking out sexual pleasure.",
        "{b}Asexual{/b}\nYour slave is completely asexual, showing no interest in sexual activity, which greatly limits intimacy.",
        "{b}frigid{/b}\nYour slave is frigid and indifferent to sexual advances, making sexual connection very difficult."
    ],
    "sexual_openness": [
        "Null",
        "{b}Open{/b}\nYour slave is open-minded and enjoys exploring new experiences and partners.",
        "{b}Pervert{/b}\nYour slave is a pervert, she doesn't mind fucking a dog or a sea tentacle",
        "{b}Puritanical{/b}\nYour slave is a puritanical, she hates doing unconvencional things",
        "{b}Prudish{/b}\nYour slave is prudish, she dislikes doing unconvencional things",
    ],
    "masochism": [
        "Null",
        "{b}Accustomed to pain{/b}\nYour slave is somewhat accustomed to pain and can tolerate it in intimate settings.",
        "{b}Masochism{/b}\nYour slave embraces masochism, finding pleasure in pain and submission.",
        "{b}Pain averse{/b}\nYour slave is extremely pain averse, avoiding even mild discomfort during intimacy.",
        "{b}Pain sensitive{/b}\nYour slave is highly sensitive to pain and any discomfort greatly distresses her."
    ],
    "exhibitionism": [
        "Null",
        "{b}Likes Exhibitionism{/b}\nYour slave occasionally enjoys being watched during intimate moments.",
        "{b}Loves Exhibitionism{/b}\nYour slave loves exhibitionism and thrills at the idea of being seen.",
        "{b}Hates Exhibitionism{/b}\nYour slave strongly fears or hates exhibitionism, finding it very distressing.",
        "{b}Dislikes Exhibitionism{/b}\nYour slave is deeply uncomfortable with any form of exposure or being watched."
    ],
    "sexual_orientation": [
        "Null",
        "{b}Bi-curious{/b}\nYour slave is bi-curious, open to exploring her sexuality with different genders.",
        "{b}Bisexual{/b}\nYour slave identifies as bisexual and embraces attraction to multiple genders.",
        "{b}Homosexual{/b}\nYour slave is exclusively homosexual, showing strong preference for the same sex.",
        "{b}Homoflexible{/b}\nYour slave is homoflexible, mostly attracted to one sex but occasionally open."
    ],
    "abuse_attitude": [
        "Null",
        "{b}Likes Roughness{/b}\nYour slave likes roughness in intimacy, which adds excitement to her experiences.",
        "{b}Loves Roughness{/b}\nYour slave loves roughness and seeks dominant, forceful encounters.",
        "{b}Hates Roughness{/b}\nYour slave strongly dislikes roughness and prefers gentle, tender interactions.",
        "{b}Dislikes Roughness{/b}\nYour slave is deeply averse to any rough or abusive behavior during intimacy."
    ],
    "darkness_attitude": [
        "Null",
        "{b}Likes Darkness{/b}\nYour slave likes the allure of darkness and mystery in her intimate moments.",
        "{b}Loves Darkness{/b}\nYour slave loves darkness, finding it stimulating and intriguing.",
        "{b}Hates Darkness{/b}\nYour slave strongly dislikes darkness and prefers well-lit environments.",
        "{b}Dislikes Darkness{/b}\nYour slave is deeply uncomfortable or fearful of darkness."
    ],
    "blood_attitude": [
        "Null",
        "{b}Likes Blood{/b}\nYour slave has a mild fascination with blood in her erotic play.",
        "{b}Loves Blood{/b}\nYour slave loves incorporating blood into her intimate experiences.",
        "{b}Hates Blood{/b}\nYour slave strongly dislikes blood and avoids any activity that involves it.",
        "{b}Dislikes Blood{/b}\nYour slave is disturbed by blood and cannot tolerate it."
    ],
    "fire_attitude": [
        "Null",
        "{b}Likes Fire{/b}\nYour slave enjoys the warmth and thrill that fire brings to intimacy.",
        "{b}Loves Fire{/b}\nYour slave loves fire play and finds it deeply arousing.",
        "{b}Hates Fire{/b}\nYour slave strongly fears fire and avoids any related activities.",
        "{b}Fears Fire{/b}\nYour slave fears fire and refuses any exposure to it."
    ],
    "water_attitude": [
        "Null",
        "{b}Likes Water{/b}\nYour slave likes water and often enjoys aquatic intimacy.",
        "{b}Loves Water{/b}\nYour slave loves water play and finds it sensual and refreshing.",
        "{b}Hates Water{/b}\nYour slave strongly dislikes water and avoids any contact.",
        "{b}Dislikes Water{/b}\nYour slave is uncomfortable with water and refuses any contact."
    ],
    "spider_attitude": [
        "Null",
        "{b}Likes Spiders{/b}\nYour slave is somewhat curious about spiders and their symbolism.",
        "{b}Loves Spiders{/b}\nYour slave loves spiders and loves to include them in her fantasy play.",
        "{b}Hates Spiders{/b}\nYour slave strongly fears or dislikes spiders and panics at the sight of them.",
        "{b}Terrified of Spiders{/b}\nYour slave is terrified of spiders and avoids them."
    ],
    "passion_comfort": [
        "Null",
        "{b}Likes Comfort{/b}\nYour slave likes comfort and values cozy, safe environments.",
        "{b}Loves Comfort{/b}\nYour slave loves comfort and seeks luxurious relaxation.",
        "{b}Dislikes Comfort{/b}\nYour slave dislikes comfort, finding it restrictive or dull.",
        "{b}Rejects Comfort{/b}\nYour slave rejects comfort entirely and prefers harsh conditions."
    ],
    "passion_fame": [
        "Null",
        "{b}Likes Fame{/b}\nYour slave likes the idea of fame and recognition.",
        "{b}Loves Fame{/b}\nYour slave loves being famous and craves public attention.",
        "{b}Dislikes Fame{/b}\nYour slave strongly dislikes fame and shuns the spotlight.",
        "{b}Uncomfortable with Fame{/b}\nYour slave is deeply uncomfortable with any form of recognition."
    ],
    "passion_luxury": [
        "Null",
        "{b}Likes Luxury{/b}\nYour slave enjoys luxury and the finer things in life.",
        "{b}Loves Luxury{/b}\nYour slave loves luxury and indulges in extravagance.",
        "{b}Dislikes Luxury{/b}\nYour slave strongly dislikes luxury and prefers simplicity.",
        "{b}Rejects Luxury{/b}\nYour slave rejects luxury completely and avoids indulgence."
    ],
    "passion_sweets": [
        "Null",
        "{b}Likes Sweets{/b}\nYour slave likes sweets and enjoys occasional treats.",
        "{b}Loves Sweets{/b}\nYour slave loves sweets and often craves sugary delights.",
        "{b}Dislikes Sweets{/b}\nYour slave strongly dislikes sweets and avoids sugary foods.",
        "{b}Aversion to Sweets{/b}\nYour slave has a strong aversion to sweets and refuses them."
    ],
    "fertility": [
        "Null",
        "{b}Fertile{/b}\nYour slave is fertile and capable of conceiving children.",
        "{b}Very Fertile{/b}\nYour slave is very fertile and likely to conceive easily.",
        "{b}Very Infertile{/b}\nYour slave is very infertile and has very little chance to conceive children.",
        "{b}Infertile{/b}\nYour slave is infertile, with little chance of conception."
    ],
    "deprivation_attitude": [
        "Null",
        "{b}Likes Deprivation{/b}\nYour slave likes deprivation and enjoys the challenge of being deprived.",
        "{b}Loves Deprivation{/b}\nYour slave loves deprivation and craves the challenge of being deprived. She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Deprivation{/b}\nYour slave strongly dislikes deprivation and avoids it whenever possible. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Deprivation{/b}\nYour slave strongly dislikes deprivation and avoids it whenever possible."
    ]
}
define dic_traits_aura = {
    "feartrait":       ["Null", "Fearful", "Terrified", "Moronic", "Brave"],
    "despairtrait":    ["Null", "Positive", "High-spirited", "Crushed Spirit", "Hopeless"],
    "awarenesstrait":  ["Null", "Observant", "Highly Perceptive", "Oblivious", "Clueless"],
    "tamingtrait":     ["Null", "Easily Tamed", "Naturally Submissive", "Untamable", "Rebellious"],
    "habittrait":      ["Null", "Well-behaved", "Disciplined", "Undisciplined", "Inconsistent"],
    "spoiltrait":      ["Null", "Self-sufficient", "Stoic", "Spoiled Rotten", "Pampered"],
    "devotiontrait":   ["Null", "Loyal", "Fanatically Devoted", "Disloyal", "Detached"]
}

define dic_traits_aura_description = {
    "feartrait": [
        "Null",
        "{b}Fearful{/b} \nYour slave shows a healthy level of fear that ensures obedience and respect. She is deeply fearful and compliant, making her extremely easy to control.",
        "{b}Terrified{/b} \nYour slave shows a healthy level of fear that ensures obedience and respect. She is deeply fearful and compliant, making her extremely easy to control. She has a bright aura with a special intensity, which will allow her to reach new heights.",
        "{b}Moronic{/b} \nYour slave is brave and unshaken, which may hinder submissive training. She lacks any fear or caution, acting recklessly and challenging authority. She has a dim aura, which will limit her potential for improvement.",
        "{b}Brave{/b} \nYour slave is brave and unshaken, which may hinder submissive training. She lacks any fear or caution, acting recklessly and challenging authority."
    ],
    "despairtrait": [
        "Null",
        "{b}Positive{/b} \nYour slave remains optimistic and adapts well to her circumstances. She is exceptionally spirited and unshakably hopeful, even in adversity.",
        "{b}High-spirited{/b} \nYour slave remains optimistic and adapts well to her circumstances. She is exceptionally spirited and unshakably hopeful, even in adversity. She has a bright aura with a special intensity, which will allow her to reach new heights.",
        "{b}Crushed Spirit{/b} \nYour slave has become hopeless and emotionally unstable. Her spirit is completely crushed, making it hard for her to recover emotionally. She has a dim aura, which will limit her potential for improvement.",
        "{b}Hopeless{/b} \nYour slave has become hopeless and emotionally unstable. Her spirit is completely crushed, making it hard for her to recover emotionally."
    ],
    "awarenesstrait": [
        "Null",
        "{b}{/b} \nYour slave is observant and notices small details others may miss. She is highly perceptive and aware of her surroundings and dynamics.",
        "{b}Highly Perceptive{/b} \nYour slave is observant and notices small details others may miss. She is highly perceptive and aware of her surroundings and dynamics. She has a bright aura with a special intensity, which will allow her to reach new heights.",
        "{b}Oblivious{/b} \nYour slave is clueless and slow to catch on to changes or instructions. She is oblivious to what's going on, which limits her effectiveness. She has a dim aura, which will limit her potential for improvement.",
        "{b}Clueless{/b} \nYour slave is clueless and slow to catch on to changes or instructions. She is oblivious to what's going on, which limits her effectiveness."
    ],
    "tamingtrait": [
        "Null",
        "{b}Easily Tamed{/b} \nYour slave is easily guided and responds well to training. She is naturally submissive and quickly accepts her role.",
        "{b}Naturally Submissive{/b} \nYour slave is easily guided and responds well to training. She is naturally submissive and quickly accepts her role. She has a bright aura with a special intensity, which will allow her to reach new heights.",
        "{b}Untamable{/b} \nYour slave is rebellious and resists taming efforts. She is wild and rejects all forms of control or authority. She has a dim aura, which will limit her potential for improvement.",
        "{b}Rebellious{/b} \nYour slave is rebellious and resists taming efforts. She is wild and rejects all forms of control or authority."
    ],
    "habittrait": [
        "Null",
        "{b}Well-behaved{/b} \nYour slave behaves properly and follows routine with little guidance. She is highly disciplined and consistent in her actions.",
        "{b}Disciplined{/b} \nYour slave behaves properly and follows routine with little guidance. She is highly disciplined and consistent in her actions. She has a bright aura with a special intensity, which will allow her to reach new heights.",
        "{b}Undisciplined{/b} \nYour slave is inconsistent and unreliable in her behavior. She struggles with following rules and frequently acts out. She has a dim aura, which will limit her potential for improvement.",
        "{b}Inconsistent{/b} \nYour slave is inconsistent and unreliable in her behavior. She struggles with following rules and frequently acts out."
    ],
    "spoiltrait": [
        "Null",
        "{b}Self-sufficient{/b} \nYour slave is content with little and rarely demands special treatment. She remains stoic and emotionally resilient, even without luxury.",
        "{b}Stoic{/b} \nYour slave is content with little and rarely demands special treatment. She remains stoic and emotionally resilient, even without luxury. She has a bright aura with a special intensity, which will allow her to reach new heights.",
        "{b}Spoiled Rotten{/b} \nYour slave is pampered and expects constant comfort and attention. She is spoiled rotten and throws tantrums if not indulged. She has a dim aura, which will limit her potential for improvement.",
        "{b}Pampered{/b} \nYour slave is pampered and expects constant comfort and attention. She is spoiled rotten and throws tantrums if not indulged."
    ],
    "devotiontrait": [
        "Null",
        "{b}Loyal{/b} \nYour slave is loyal and shows clear dedication to her master. She is fanatically devoted and lives to serve without question.",
        "{b}Fanatically Devoted{/b} \nYour slave is loyal and shows clear dedication to her master. She is fanatically devoted and lives to serve without question. She has a bright aura with a special intensity, which will allow her to reach new heights.",
        "{b}Disloyal{/b} \nYour slave is emotionally detached and resists forming bonds. She is disloyal and may turn against her master when challenged. She has a dim aura, which will limit her potential for improvement.",
        "{b}Detached{/b} \nYour slave is emotionally detached and resists forming bonds. She is disloyal and may turn against her master when challenged."
    ]
}
define dic_traits_attributes = {
    "beautytrait":       ["Null", "Attractive", "Divine beauty", "Null", "Null"],
    "endurancetrait":    ["Null", "Tough", "Fortitude", "Very Frail", "Weak"],
    "empathytrait":      ["Null", "Compassionate", "Emotional resonancer", "Cold-hearted", "Insensitive"],
    "temperamenttrait":  ["Null", "Warm-hearted", "Fervent", "Very calm", "Calm"],
    "intelligencetrait": ["Null", "Smart", "Prodigy", "Very Dull", "Slow"],
    "naturetrait":       ["Null", "Tenacious disposition", "Unbreakable resolve", "Faint-hearted disposition", "Insecure disposition"],
    "pridetrait":        ["Null", "Meekness", "Very Meekness", "Confident", "Overbearing"],
    "physicaltrait":     ["Null", "Good metabolism", "Excellent metabolism", "Very bad metabolism", "bad metabolism"],
    "exoticismtrait":   ["Null", "Distinctive", "Strikingly Exotic", "Completely common", "Unremarkable"],
    "styletrait":        ["Null", "Graceful", "Very Graceful", "Clumsy", "Ungraceful"]
}
define dic_traits_attributes_description = {
    "beautytrait": [
        "None",
        "{b}Attractive{/b} \nYour slave is attractive and pleasant to look at. She turns heads and draws attention with her charm. She may reach another level of beauty if you train her well.",
        "{b}Divine beauty{/b} \nYour slave is attractive and pleasant to look at. She turns heads and draws attention with her charm. She may reach another level of beauty if you train her well.",
        "{b}Hideous{/b} \nYour slave is unattractive and plain. Her appearance doesn't stand out in any positive way. She is hideous to behold, with features that repel rather than attract. Her looks often make others uncomfortable. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Unattractive{/b} \nYour slave is unattractive and plain. Her appearance doesn't stand out in any positive way. She is hideous to behold, with features that repel rather than attract. Her looks often make others uncomfortable."
    ],
    "endurancetrait": [
        "None",
        "{b}Tough{/b} \nYour slave is tough and endures hardship without complaint. She can handle physical strain well. She has an unshakable fortitude that makes her nearly tireless and able to push through even the harshest conditions.",
        "{b}Fortitude{/b} \nYour slave is tough and endures hardship without complaint. She can handle physical strain well. She has an unshakable fortitude that makes her nearly tireless and able to push through even the harshest conditions. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Very Frail{/b} \nYour slave is weak and struggles with even moderate effort. She tires easily and lacks resilience. She is extremely frail and collapses easily under pressure. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Weak{/b} \nYour slave is weak and struggles with even moderate effort. She tires easily and lacks resilience. She is extremely frail and collapses easily under pressure."
    ],
    "empathytrait": [
        "None",
        "{b}Compassionate{/b} \nYour slave is compassionate and responds to others emotions with care. She connects easily with people. She possesses emotional resonance that lets her deeply understand and soothe others.",
        "{b}Emotional resonancer{/b} \nYour slave is compassionate and responds to others emotions with care. She connects easily with people. She possesses emotional resonance that lets her deeply understand and soothe others. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Cold-hearted{/b} \nYour slave is insensitive and oblivious to others feelings. She struggles with empathy and emotional expression. She is cold-hearted and indifferent to others. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Insensitive{/b} \nYour slave is insensitive and oblivious to others feelings. She struggles with empathy and emotional expression. She is cold-hearted and indifferent to others."
    ],
    "temperamenttrait": [
        "None",
        "{b}Warm-hearted{/b} \nYour slave is warm-hearted and brings comfort to those around her. Her emotional presence is soothing. She burns with fervent emotion and passion, often inspiring those near her with her intensity.",
        "{b}Fervent{/b} \nYour slave is warm-hearted and brings comfort to those around her. Her emotional presence is soothing. She burns with fervent emotion and passion, often inspiring those near her with her intensity. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Very calm{/b} \nYour slave is calm and composed. She keeps her feelings in check but may seem emotionally distant. She is overly calm, to the point of being detached. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Calm{/b} \nYour slave is calm and composed. She keeps her feelings in check but may seem emotionally distant. She is overly calm, to the point of being detached."
    ],
    "intelligencetrait": [
        "None",
        "{b}Smart{/b} \nYour slave is smart and quick-witted. She picks up new concepts with ease and adapts quickly. She is a prodigy with exceptional intellect, easily mastering complex tasks beyond normal expectations.",
        "{b}Prodigy{/b} \nYour slave is smart and quick-witted. She picks up new concepts with ease and adapts quickly. She is a prodigy with exceptional intellect, easily mastering complex tasks beyond normal expectations. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Very Dull{/b} \nYour slave is slow and often confused. She learns slowly and needs repeated guidance. She is very dull and struggles to grasp even simple concepts. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Slow{/b} \nYour slave is slow and often confused. She learns slowly and needs repeated guidance. She is very dull and struggles to grasp even simple concepts."
    ],
    "naturetrait": [
        "None",
        "{b}Tenacious disposition{/b} \nYour slave has a tenacious disposition and rarely gives up. She holds strong even under pressure. Her unbreakable resolve drives her forward through all hardship.",
        "{b}Unbreakable resolve{/b} \nYour slave has a tenacious disposition and rarely gives up. She holds strong even under pressure. Her unbreakable resolve drives her forward through all hardship. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Faint-hearted disposition{/b} \nYour slave has an insecure disposition, doubting herself constantly and often giving in to fear. She is faint-hearted and easily discouraged. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Insecure disposition{/b} \nYour slave has an insecure disposition, doubting herself constantly and often giving in to fear. She is faint-hearted and easily discouraged."
    ],
    "pridetrait": [
        "None",
        "{b}Meekness{/b} \nYour slave displays meekness and knows her place. She acts with humility and rarely challenges authority. She is extremely meek, almost to a fault, making her utterly obedient.",
        "{b}Very Meekness{/b} \nYour slave displays meekness and knows her place. She acts with humility and rarely challenges authority. She is extremely meek, almost to a fault, making her utterly obedient. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Confident{/b} \nYour slave is overbearing and believes herself superior. She resists subservience and expects special treatment. She is confident and bold, often asserting herself. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Overbearing{/b} \nYour slave is overbearing and believes herself superior. She resists subservience and expects special treatment. She is confident and bold, often asserting herself."
    ],
    "physicaltrait": [
        "None",
        "{b}Good metabolism{/b} \nYour slave has a good metabolism, maintaining her health and energy easily. She handles physical labor well. She possesses an excellent metabolism, giving her great physical vitality and stamina.",
        "{b}Excellent metabolism{/b} \nYour slave has a good metabolism, maintaining her health and energy easily. She handles physical labor well. She possesses an excellent metabolism, giving her great physical vitality and stamina. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Very bad metabolism{/b} \nYour slave has a bad metabolism and struggles with energy and body regulation. She tires quickly and lacks fitness. She suffers from a very bad metabolism, gaining weight or losing energy easily. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Bad metabolism{/b} \nYour slave has a bad metabolism and struggles with energy and body regulation. She tires quickly and lacks fitness. She suffers from a very bad metabolism, gaining weight or losing energy easily."
    ],
    "exoticismtrait": [
        "None",
        "{b}Distinctive{/b} \nYour slave is distinctive and stands out with a unique charm. Her look draws attention and interest. She is strikingly exotic and exudes an allure few can resist.",
        "{b}Strikingly Exotic{/b} \nYour slave is distinctive and stands out with a unique charm. Her look draws attention and interest. She is strikingly exotic and exudes an allure few can resist. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Completely common{/b} \nYour slave is unremarkable, lacking any distinguishing features. Her look fails to attract attention in any way. She is completely common in appearance and blends into the crowd. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Unremarkable{/b} \nYour slave is unremarkable, lacking any distinguishing features. Her look fails to attract attention in any way. She is completely common in appearance and blends into the crowd."
    ],
    "styletrait": [
        "None",
        "{b}Graceful{/b} \nYour slave is graceful and moves with ease. She exudes a natural elegance and poise, making her movements fluid and graceful.",
        "{b}Very Graceful{/b} \nYour slave is graceful and moves with ease. She exudes a natural elegance and poise, making her movements fluid and graceful. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Clumsy{/b} \nYour slave is clumsy and moves with difficulty. She struggles with balance and coordination, often tripping or bumping into things. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Ungraceful{/b} \nYour slave is clumsy and moves with difficulty. She struggles with balance and coordination, often tripping or bumping into things."
    ]
}
define aura_descriptions = {
    "obedience": [
        "You try to find signs of obedience, but stable structures cannot form. There are no spikes of rebellion, alas there are no buds of obedience as well.",
        "You concentrate on the signs of obedience, but you can only see {color=#009900}one open bud of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}a pair of open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}three open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}four open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}five open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}six open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}seven open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}eight open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}nine open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}a lot of open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}one sharp thorn of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}a pair of sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}three sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}four sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}five sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}six sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}seven sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}eight sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}nine sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}a lot of sharp thorns of rebellion{/color}."
    ],

    "supermacy": [
        "{color=#cd0000}The aura of your slave shines considerably brighter than yours{/color}.",
        "{color=#EA0090}The aura of your slave shines brighter than yours{/color}.",
        "{color=#0000D8}The aura of your slave is approximately equal to yours{/color}.",
        "{color=#009900}The aura of your slave is fainter than yours{/color}.",
        "{color=#009900}The aura of your slave is considerably fainter than yours{/color}."
    ]
}
define aura_descriptions_no_color = {
    "obedience": [
        "You try to find signs of obedience, but stable structures cannot form. There are no spikes of rebellion, alas there are no buds of obedience as well.",
        "You concentrate on the signs of obedience, but you can only see one open bud of obedience.",
        "You concentrate on the signs of obedience and count a pair of open buds of obedience.",
        "You concentrate on the signs of obedience and count three open buds of obedience.",
        "You concentrate on the signs of obedience and count four open buds of obedience.",
        "You concentrate on the signs of obedience and count five open buds of obedience.",
        "You concentrate on the signs of obedience and count six open buds of obedience.",
        "You concentrate on the signs of obedience and count seven open buds of obedience.",
        "You concentrate on the signs of obedience and count eight open buds of obedience.",
        "You concentrate on the signs of obedience and count nine open buds of obedience.",
        "You concentrate on the signs of obedience and count a lot of open buds of obedience.",
        "You concentrate on the signs of obedience and count one sharp thorn of rebellion.",
        "You concentrate on the signs of obedience and count a pair of sharp thorns of rebellion.",
        "You concentrate on the signs of obedience and count three sharp thorns of rebellion.",
        "You concentrate on the signs of obedience and count four sharp thorns of rebellion.",
        "You concentrate on the signs of obedience and count five sharp thorns of rebellion.",
        "You concentrate on the signs of obedience and count six sharp thorns of rebellion.",
        "You concentrate on the signs of obedience and count seven sharp thorns of rebellion.",
        "You concentrate on the signs of obedience and count eight sharp thorns of rebellion.",
        "You concentrate on the signs of obedience and count nine sharp thorns of rebellion.",
        "You concentrate on the signs of obedience and count a lot of sharp thorns of rebellion."
    ],

    "supermacy": [
        "The aura of your slave shines considerably brighter than yours.",
        "The aura of your slave shines brighter than yours.",
        "The aura of your slave is approximately equal to yours.",
        "The aura of your slave is fainter than yours.",
        "The aura of your slave is considerably fainter than yours."
    ]
}


define aura_descriptions2 = {
    "arousal": [
        "{color=#000000}The aura moves slowly and smoothly, almost without pulsation. You don't notice any signs of sexual desire.{/color}",
        "{color=#000000}Light twitching of the aura suggests to you that there is slight sexual desire present.{/color}",
        "{color=#000000}Sensual aura fluctuations indicate the presence of significant sexual arousal.{/color}",
        "{color=#000000}The aura is clearly trembling, twisting and then unwinding in an erotic rhythm. This indicates a strong sexual arousal.{/color}",
        "{color=#000000}The aura is pulsing sensually and eagerly, stretching and arching your way. This is a sign of powerful sexual arousal and almost uncontrollable desire.{/color}",
        "{color=#000000}Almost epileptic flicker speed and modulations suggest ultimate sexual arousal. All colors are mixed in a fast paced whirlwind, like on the surface of a spinning whirligig.{/color}"

    ],

    "fear": [
        "{color=#960018}Ruby flashes of fear{/color}{color=#009900} are insignificant{/color}.",
        "{color=#960018}Ruby flashes of fear{/color} are rare, in one minute you noticed just {color=#EA0090}one{/color}.",
        "{color=#960018}Ruby flashes of fear{/color} appear from time to time, you counted {color=#6B0084}a pair{/color} of them in a minute.",
        "{color=#960018}Ruby flashes of fear{/color} appear quite often. You counted {color=#0000D8}three{/color} of them.",
        "{color=#960018}Ruby flashes of fear{/color} are quite bright and noticeable. You counted {color=#EA0090}four{/color} especially strong ones.",
        "{color=#960018}Ruby flashes of fear{/color} appear one by one and are not in a hurry to fade, pulsing like a heart overflowing with adrenaline. You counted as many as {color=#CD0000}five{/color} just in one minute."
    ],

    "despair": [
        "{color=#464451}Anthracite colored despair{/color}{color=#009900} is almost imperceptible{/color}.",
        "{color=#464451}Anthracite colored despair{/color} has formed {color=#cd0000}one{/color} tentacle, permeating through the whole aura of your slave.",
        "{color=#464451}Anthracite colored despair{/color} has formed {color=#cd0000}two{/color} tentacles, tightly gripping the aura of your slave from both sides.",
        "{color=#464451}Anthracite colored despair{/color} has formed a dense clot, with {color=#cd0000}three{/color} disgusting writhing tentacles sticking from it.",
        "{color=#464451}Anthracite colored despair{/color} has grown and released {color=#009FEF}four{/color} tentacles, engulfing the aura of your slave from all sides.",
        "{color=#464451}Anthracite colored despair{/color} permeates the entire aura of your slave. You can clearly see {color=#cd0000}five{/color} fat, disgusting writhing tentacles, which tear all other colors to shreds."
    ],

    "awareness": [
        "{color=#B452CD}Amethyst core of awareness{/color}{color=#cd0000} is not formed{/color}.",
        "{color=#B452CD}Amethyst core of awareness{/color} is very small, being formed by {color=#EA0090}only one{/color} globule.",
        "{color=#B452CD}Amethyst core of awareness{/color} is formed by {color=#6B0084}two{/color} tightly agglutinated globules.",
        "{color=#B452CD}Amethyst core of awareness{/color} is medium-sized. You counted {color=#0000D8}three{/color} globules in it.",
        "{color=#B452CD}Amethyst core of awareness{/color} is big and dense, formed by {color=#009FEF}four{/color} crisp globules.",
        "{color=#B452CD}Amethyst core of awareness{/color} predominates in the central portion. Its shape indicates the presence of at least {color=#009900}five{/color} well-formed globules."
    ],

    "taming": [
        "{color=#CD9B1D}Golden strings of taming{/color}{color=#cd0000} are hardly noticeable{/color}.",
        "{color=#CD9B1D}Golden strings of taming{/color} are hardly formed. Just {color=#EA0090}one{/color} of them seems to be strong enough.",
        "{color=#CD9B1D}Golden strings of taming{/color} are seen here and there. You find {color=#6B0084}a pair{/color} of strong ones.",
        "{color=#CD9B1D}Golden strings of taming{/color} are noticeable in lots of places. {color=#0000D8}Three{/color} of them seem to be particularly strong.",
        "{color=#CD9B1D}Golden strings of taming{/color} are seen everywhere. {color=#009FEF}Four{/color} especially bright coils pass on the perimeter of the aura, like the meridians on the globe.",
        "{color=#CD9B1D}Golden strings of taming{/color}{color=#009900} cover the whole aura{/color}, making it look like a piece of ham in a tight braid."
    ],

    "habit": [
        "{color=#082567}Sapphire flicker of habit{/color}{color=#cd0000} is completely absent{/color}.",
        "{color=#082567}Sapphire flicker of habit{/color} looks very dull and only noticeable in {color=#EA0090}one{/color} place.",
        "{color=#082567}Sapphire flicker of habit{/color} appears rather poorly and only in {color=#6B0084}a pair{/color} of places.",
        "{color=#082567}Sapphire flicker of habit{/color} is fairly stable. You find {color=#0000D8}three{/color} points of its concentration.",
        "{color=#082567}Sapphire flicker of habit{/color} meanders over the entire surface of the aura of your slave, covering it from {color=#009FEF}four{/color} sides.",
        "{color=#082567}Sapphire flicker of habit{/color}{color=#009900} envelops the whole aura{/color} of your slave, like a soft misty haze. It softens and masks all angles, ledges and bright colors."
    ],

    "spoil": [
        "{color=#EE1289}Vulgar-pink iridescence of spoiling{/color}{color=#009900} does not spoil the aura{/color} of your slave.",
        "{color=#EE1289}Vulgar-pink iridescence of spoiling{/color} is gathered in {color=#009FEF}one{/color} place, forming a disgusting wormhole.",
        "{color=#EE1289}Vulgar-pink iridescence of spoiling{/color} forms {color=#cd0000}two{/color} loathsome sores in the aura of your slave.",
        "{color=#EE1289}Vulgar-pink iridescence of spoiling{/color} forms {color=#cd0000}three{/color} nasty sores in the aura of your slave.",
        "{color=#EE1289}Vulgar-pink iridescence of spoiling{/color} forms {color=#cd0000}four{/color} ugly ulcerations on the aura of your slave.",
        "{color=#EE1289}Vulgar-pink iridescence of spoiling{/color}{color=#cd0000} is seen everywhere{/color}, speckling your slave's aura with bloody sore-like structures."
    ],

    "devotion": [
        "{color=#00a86b}Emerald glow of devotion{/color}{color=#cd0000} does not manifest at all{/color}.",
        "{color=#00a86b}Emerald glow of devotion{/color} is seen {color=#EA0090}just in one{/color} place, like a dim star on the cloudy sky.",
        "{color=#00a86b}Emerald glow of devotion{/color} forms {color=#6B0084}a pair{/color} of softly shining stars.",
        "{color=#00a86b}Emerald glow of devotion{/color} comes from {color=#0000D8}three{/color} well-marked stars.",
        "{color=#00a86b}Emerald glow of devotion{/color} comes from {color=#009FEF}four{/color} bright stars, illuminating the aura of your slave.",
        "{color=#00a86b}Emerald glow of devotion{/color} dominates the aura of your slave, dotting it with {color=#009900}myriads{/color} of bright and clear stars."
    ]
}
define aura_descriptions2_no_color = {
    "arousal": [
        "The aura moves slowly and smoothly, almost without pulsation. You don't notice any signs of sexual desire.",
        "Light twitching of the aura suggests to you that there is slight sexual desire present.",
        "Sensual aura fluctuations indicate the presence of significant sexual arousal.",
        "The aura is clearly trembling, twisting and then unwinding in an erotic rhythm. This indicates a strong sexual arousal.",
        "The aura is pulsing sensually and eagerly, stretching and arching your way. This is a sign of powerful sexual arousal and almost uncontrollable desire.",
        "Almost epileptic flicker speed and modulations suggest ultimate sexual arousal. All colors are mixed in a fast paced whirlwind, like on the surface of a spinning whirligig."
    ],

    "fear": [
        "Ruby flashes of fear are insignificant.",
        "Ruby flashes of fear are rare, in one minute you noticed just one.",
        "Ruby flashes of fear appear from time to time, you counted a pair of them in a minute.",
        "Ruby flashes of fear appear quite often. You counted three of them.",
        "Ruby flashes of fear are quite bright and noticeable. You counted four especially strong ones.",
        "Ruby flashes of fear appear one by one and are not in a hurry to fade, pulsing like a heart overflowing with adrenaline. You counted as many as five just in one minute."
    ],

    "despair": [
        "Anthracite colored despair is almost imperceptible.",
        "Anthracite colored despair has formed one tentacle, permeating through the whole aura of your slave.",
        "Anthracite colored despair has formed two tentacles, tightly gripping the aura of your slave from both sides.",
        "Anthracite colored despair has formed a dense clot, with three disgusting writhing tentacles sticking from it.",
        "Anthracite colored despair has grown and released four tentacles, engulfing the aura of your slave from all sides.",
        "Anthracite colored despair permeates the entire aura of your slave. You can clearly see five fat, disgusting writhing tentacles, which tear all other colors to shreds."
    ],

    "awareness": [
        "Amethyst core of awareness is not formed.",
        "Amethyst core of awareness is very small, being formed by only one globule.",
        "Amethyst core of awareness is formed by two tightly agglutinated globules.",
        "Amethyst core of awareness is medium-sized. You counted three globules in it.",
        "Amethyst core of awareness is big and dense, formed by four crisp globules.",
        "Amethyst core of awareness predominates in the central portion. Its shape indicates the presence of at least five well-formed globules."
    ],

    "taming": [
        "Golden strings of taming are hardly noticeable.",
        "Golden strings of taming are hardly formed. Just one of them seems to be strong enough.",
        "Golden strings of taming are seen here and there. You find a pair of strong ones.",
        "Golden strings of taming are noticeable in lots of places. Three of them seem to be particularly strong.",
        "Golden strings of taming are seen everywhere. Four especially bright coils pass on the perimeter of the aura, like the meridians on the globe.",
        "Golden strings of taming cover the whole aura, making it look like a piece of ham in a tight braid."
    ],

    "habit": [
        "Sapphire flicker of habit is completely absent.",
        "Sapphire flicker of habit looks very dull and only noticeable in one place.",
        "Sapphire flicker of habit appears rather poorly and only in a pair of places.",
        "Sapphire flicker of habit is fairly stable. You find three points of its concentration.",
        "Sapphire flicker of habit meanders over the entire surface of the aura of your slave, covering it from four sides.",
        "Sapphire flicker of habit envelops the whole aura of your slave, like a soft misty haze. It softens and masks all angles, ledges and bright colors."
    ],

    "spoil": [
        "Vulgar-pink iridescence of spoiling does not spoil the aura of your slave.",
        "Vulgar-pink iridescence of spoiling is gathered in one place, forming a disgusting wormhole.",
        "Vulgar-pink iridescence of spoiling forms two loathsome sores in the aura of your slave.",
        "Vulgar-pink iridescence of spoiling forms three nasty sores in the aura of your slave.",
        "Vulgar-pink iridescence of spoiling forms four ugly ulcerations on the aura of your slave.",
        "Vulgar-pink iridescence of spoiling is seen everywhere, speckling your slave's aura with bloody sore-like structures."
    ],

    "devotion": [
        "Emerald glow of devotion does not manifest at all.",
        "Emerald glow of devotion is seen just in one place, like a dim star on the cloudy sky.",
        "Emerald glow of devotion forms a pair of softly shining stars.",
        "Emerald glow of devotion comes from three well-marked stars.",
        "Emerald glow of devotion comes from four bright stars, illuminating the aura of your slave.",
        "Emerald glow of devotion dominates the aura of your slave, dotting it with myriads of bright and clear stars."
    ]
}
define dic_slave_conditions = {
    "in_the_cells": "  Prison - a tiny dark room. It is impossible to lie down or completely stretch out. A night in this cell is able to break the will to resist, but it can also damage health, not to mention the bad dreams. Has an especially strong effect on people with claustrophobia.",
    "On_the_floor": "  You took away the bedroll from your slave to show her that comfort should be earned. A night on the cold hard floor is neither good for resting, nor for her health, but [all_girls_list[girl_index]['name']] certainly will be a little more compliant. (TODO: But if she does not feel guilty, it may drive her into depression.)",
    "On_a_bedroll": "  It is a common thing for slaves to sleep on a hard bedroll right on the floor. A small warm blanket and cushion filled with rice husks will keep her warm at night and enable her to sleep well, although it's not comfortable at all.",
    "In_my_bed": "  As a special encouragement, your slave can be allowed to sleep with her master on his bed. This will let her sleep deeper and more comfortably. Sleeping with her owner is a great source of happiness for an obedient and devoted slave, but a poorly trained or moody girl will not be pleased at all.",
    "Do_not_sleep": "  Order her to not sleep at all. This will be a great punishment for a slave, but also greatly damage her health.",
    "No_food": "  In the Eternal Rome there are almost no opportunities to grow your own food. All food is brought from the worlds that lie beyond the Fog and because of that it costs fair amount of money. By depriving your slave of food you will kill two birds with one stone - it will teach her to be more obedient and you will save money. Of course, it is not good for her health.",
    "Dehydrated_food": "  Dzhulbars Jumas' dehydrated pet food is the choice of leading slave traders. It is delivered in ten-liter cellophane bags, and due to its low weight it is cheap to transport through the Fogs. Contains all the nutrients and fiber a female slave needs, but it tastes disgusting.",
    "Canned_food": "  Canned food for pets. It perfectly matches the composition of nutrients for female slaves and it tastes better than dry food or fiend cum. Unfortunately, it is rather expensive - fresh food weighs a lot, and it is necessary to import it from other worlds. This should be used as a reward for excellent obedience and moderate devotion, otherwise you risk spoiling your slave.",
    "Fiend_cum": "  Fiends are the scourge and blessing of Rome. They are dangerous, but they can produce huge masses of nasty but nutritious sperm. It is not easy to milk these creatures so the seed is not cheap. However, if you have your own fiend and a good milker, feeding your slave becomes a lot easier. Only if you are able to make her eat it of course…",
    "No_leftovers": "  Not every slave deserves to eat scraps from her master's table. This honor must be earned. Also, do not forget about the slave's shape.\n\n  If you are fattening a woman up in a barn you could feed her the scraps, instead.",
    "Eats_leftovers": "  Your slave may eat your left-overs. Table scraps are more delicious than ordinary slave food although usually not enough to be sated. You can consider this dessert, a nice addition to the staple food. This should be used as a reward for excellent obedience and moderate devotion, otherwise you risk spoiling your slave.",
    "Restricted": "  Just enough for your slave not to starve, as long as you do not over-spend her calories. It is unlikely that she will be satisfied, but she will lose weight and understand who's the boss. And you will save some money.",
    "Moderate": "  Just the right amount of food for your slave to maintain her weight, as long as you do not over-spend her calories. For an accurate calculation of calories, a medical assistant would be helpful. Instead, you do everything by eye; it should be fine.",
    "Generous": "  Your slave's bowl is filled to the brim. She can eat as much as she wants. This is, of course, wasteful, but she will not be hungry, as long as you do not over-spend her calories. She might gain a little weight though.",
    "Calculated": "  With your medical expertise, you will prepare carefully calculated meals from the food available, designed to keep your slave's weight ideal by managing the caloric intake. Of course, you must still ensure the slave does not exceed her limits and spend more calories than she obtains from her food. (Costs half energy per day )",
    "supplements": "  High-tech complex of biologically active additives with fancy descriptions like \"25% more nanomolecules\" and \"does not contain GM food\". What the hell?… If your slave's health is below average, it might help. If your slave is already healthy though, it is only a waste of money.\n\n  Costs one spark per day, billed each decade.",
    "cook_rules": "  You give an order to your slave to cook meals for you. Now, if only she can find enough time and has energy left, she will do it herself without your further reminders.",
    "cook_rules_abort": "  You allow your slave not to waste energy on a daily cooking. You have other plans in this regard.",
    "maid_rules": "  You give an order to your slave to take care of cleanliness and order in the house. Now, if she can find enough time and has energy left, she will do it herself without your further reminders.",
    "maid_rules_abort": "  You allow your slave not to waste time on keeping order in the house. You have other plans in this regard.",
    "bath_slave_rules": "  There is no need to wash yourself; this work can be assigned to a beautiful and gentle girl. You order your slave to help you wash.",
    "bath_slave_rules_abort": "  You decide to wash yourself, in order not to distract your slave from more important matters.",
    "behave_alarm_rules": "  You will use your slave as a human alarm clock. Every morning at the appointed time, [all_girls_list[girl_index]['name']] should wake you by taking care of your morning wood with a gentle, deep blowjob. This approach will improve your mood in the morning and prepare your slave for sexual practices.",
    "behave_alarm_rules_abort": "  You decide to wake up in the morning without being distracted by the slave's attempts to make you feel good or evade from her responsibilities.",
    "behave_humility_rules": "  You order the slave to behave as a well-mannered slave should from now on. She is to always call you politely, \"Master\". This way she will quickly get accustomed to absolute obedience.",
    "behave_humility_rules_abort": "  You allow the slave to address you familiarly without following formal rules of communication between slave and master.",
    "behave_pet_rules": "  You order the slave to behave like a pet: she should always walk on all fours and make sounds that befit an animal. This will help teach her humility, while developing flexibility.",
    "behave_pet_rules_abort": "  You let the slave behave like a human again.",
    "behave_silence_rules": "  You order the slave to remain silent until she is asked about anything. This will help her to develop sensitivity, humility and expressiveness of movements but can suppress temperament.",
    "behave_silence_rules_abort": "  You allow the slave to talk on her own and express her opinion.",
    "behave_toilet_rules": "  You will use the slave as a human toilet. [all_girls_list[girl_index]['name']] should swallow everything and gently scrub you with her tongue. There is no better way to get rid of unnecessary pride. In addition, a well-trained toilet is a comfort at home and lifts your mood. And if nothing else, the slave at least will learn something. Harmful to health and hygiene.",
    "behave_toilet_rules_abort": "  You tell to your slave that you will use the ordinary toilet, and her services in the near future are not needed.",
    "behave_urinal_rules": "  You will use the slave as a human urinal. [all_girls_list[girl_index]['name']] must carefully swallow all your urine and lick up any that has been spilled. This will seriously reduce her pride and will enhance your mood. It will also teach the slave necessary skills if they are not developed yet. It has a bad effect on hygiene.",
    "behave_urinal_rules_abort": "  You tell your slave that you will use the ordinary toilet, and her services in the near future are not needed.",
    "deny_orgasm_rules": "  You forbid the slave to experience orgasm, unless you gave her a special permission. Whenever she can restrain from cumming, her arousal and sensitivity will increase.",
    "deny_orgasm_rules_abort": "  You tell the slave she may orgasm without permission, allowing her release, but you warn her that you can change your mind!",
    "deny_toileting_rules": "  You forbid the slave go to the toilet without your permission. She will be allowed to visit the restroom rarely and only under your supervision. This will help teach her humility, though the price will be the slave mood.",
    "deny_toileting_rules_abort": "  You let the slave go to the toilet by herself whenever she wants. At least she will not distract you with her constant tears and pleas.",
    "slave_tentacle_rules": "  You order the slave to take care of your fiend and regularly milk it so that it does not wither in captivity.",
    "slave_tentacle_rules_abort": "  You say that the slave can forget about the fiend and need not take care of him.",
    "no_masturbation_rules": "  You order your slave not to masturbate unless you instruct her otherwise. This will prevent her from relieving her arousal if she obeys, and successfully resisting the urge to masturbate will slightly increase her taming.",
    "no_masturbation_rules_abort": "  You let your slave masturbate freely.",
    "use_vaginal_beads_rules": "  You put vaginal beads in the slave's pussy and order her to wear them all the time, so she can develop her sensitivity and desire.",
    "use_vaginal_beads_rules_abort": "  You order the slave to remove the vaginal beads, wash them well, and give to you. Her excitement must be controlled so that it does not become an obstacle to learning.",
    "enforce_rules": "  You tell the slave that you will use various tools such as anal pears, gags, chastity belts, pet suits and toilet racks, as well as special supervision of your assistant in order to prevent her from ignoring the rules. Of course, this may make her miserable and depressed, but it will also humble her and teach her that compliance is in her own best interest.",
    "enforce_rules_abort": "  You tell the slave that henceforth she should obediently follow all her rules without the help of your special tools and additional supervision. Of course, this does not mean that ignoring orders will leave her unpunished…",    
    "default":""
}
define dic_slave_conditions_sleep ={
    0:"in_the_cells",
    1:"On_the_floor",
    2:"On_a_bedroll",
    3:"In_my_bed",
    4:"Do_not_sleep" 
}
define dic_slave_conditions_food ={
    0:"Dehydrated_food",
    1:"Canned_food",
    2:"Fiend_cum",
    3:"No_food"
}
define dic_slave_conditions_portion ={
    0:"Restricted",
    1:"Moderate",
    2:"Generous",
    3:"Calculated"
}
define dic_girl_age_text ={
    0: "Young",
    1: "Loli",
    2: "Madure"
}

define dic_girl_boobs_text ={
    "young": [
        "Flat chested",
        "Small perky boobs",
        "Round, handful-sized breasts",
        "Big[boobs1]",
        "Huge[boobs2]",
        "Massive [boobs3]",
        "Stupendous [boobs3]",
    ],
    "loli": [
        "Flat chested",
        "Budding boobies",
        "Very large breasts",
        "{i}Enormous{/i}, womanly breasts",
    ],
    "mature": [
        "Flat chested",
        "Small drooping breasts",
        "Soft handful-sized breasts",
        "Big[boobs4]",
        "Huge[boobs5]",
        "Enormous [boobs6]",
        "Colossal [boobs6]",
    ],
}
define dic_girl_breast_modification ={
    0:"No Breast Modifications",
    1:"Breast Size Modified",
    2:"Vagina Breasts",
    3:"Nipple-Mouths",
}
define dic_girl_vaginal_tightness ={
    0:"Virgin",
    1:"Restored Hymen",
    2:"Firm Vagina",
    3:"Relaxed Vagina",
}
define dic_girl_anal_tightness ={
    0:"Tight Anus",
    1:"Stiff Anus",
    2:"Firm Anus",
    3:"Developed Anus",
    4:"Relaxed Anus",
    5:"Loose Anus",
}
define dic_girl_vagina_modification ={
    0:"No Vaginal Modifications",
    1:"Vaginal Ball Implants",
    2:"Lubricative Glands+",
    3:"Vagina Tongue",
    4:"Egg Birthing",
}
define dic_girl_brand ={
    0:"No Brand",
    1:"Tattoo brand",
    2:"Someone else's brand",
    3:"Guild brand",
    4:"Fire brand",
    5:"Magical brand",
    6:"Special quest (cannot brand)",
}
define dic_color_level ={
    0:"CD0000",
    1:"EA0090",
    2:"6B0084",
    3:"0000D8",
    4:"009FEF",
    5:"009900",
    6:"996515",
}
define learn_bonus ={
    "sex":0,
    "endurance":0,
    "taming":0,
    "cook":0,
    "nurse":0,
    "athletics":0,
    "alchemy":0,
    "service":0,
    "gladiatrix":0,
    "enchanter":0,
    "stamina":0,
}
define dic_overnight_rules_count =[0,2,4]

define dic_girl_clothing_dress = {
    "naked": {
        "name": "Naked",
        "price": 0,
        "desc": "Your slave is completely naked. This is helpful for some types of training, and it will remind her of her place, but she might be happier if she had something to wear.",
    },
    "common_apron": {
        "name": "Frilly Apron",
        "price": 5,
        "desc": "Price: 5 sparks\nAprons are most useful in the kitchen. This apron is worn without any other clothing, leaving plenty of opportunities to enjoy the sight of your woman working in the kitchen.",
        "icon": "scene/item/item_apron1",
    },
    "maid_dress": {
        "name": "Maid Outfit",
        "price": 5,
        "desc": "Price: 5 sparks\nClassic French maid uniform. Many parts of the uniform have been left out in order to preserve fabric. Most customers actually like this design.",
        "icon": "scene/item/item_maido",
    },
    "nurse_dress": {
        "name": "Nurse Outfit",
        "price": 5,
        "desc": "Price: 5 sparks\nA flashy white nurse dress. This is what you need to lift the spirit of any patient.",
        "icon": "scene/item/item_nurse",
    },
    "leotard": {
        "name": "Athletic Leotard",
        "price": 5,
        "desc": "Price: 5 sparks\nA tight leotard which emphasizes the shape of your slave while not hampering her movements. Perfect for any sports activity, except for battles.",
        "icon": "scene/item/item_leotard",
    },
    "chainmail_bikini": {
        "name": "Chainmail Bikini",
        "price": 5,
        "desc": "Price: 5 sparks\nClassic gladiatrix clothing. I repeat - clothing. It's not an armor, it's a stage props, made of light and gleaming anodized aluminum. The cut is so minimal that it almost hides nothing.",
        "icon": "scene/item/item_chainmail_bikini",
    },
    "enchanter_robe": {
        "name": "Sorceress Robes",
        "price": 5,
        "desc": "Price: 5 sparks\nMade of a very light but opaque fabric - this arcane robe with a hood completely hides the shape of your slave. Not very sexy, but very mysterious and helps to tune in to a mystical way.",
        "icon": "scene/item/item_robe",
    },
    "sun_dress": {
        "name": "Light Sundress",
        "price": 5,
        "desc": "Price: 5 sparks\nThis cute little dress is perfect for relaxing and raises the mood of those who wear it. Of course, there are more beautiful or functional dresses, but wearing a sundress is just very nice.",
        "icon": "scene/item/item_sundress",
    },
    "laced_underwear": {
        "name": "Lace Underwear",
        "price": 5,
        "desc": "Price: 5 sparks\nIn this set of sexy lace underwear that includes bra, panties, lightweight corset and stockings with garters, any girl would look desirable. Treat yourself to a beautiful sight and tune your slave for a rough night!",
        "icon": "scene/item/item_laced_underwear",
    },
    "sailor_foku": {
        "name": "School Uniform",
        "price": 10,
        "desc": "Price: 10 sparks\nUniform of the Academy of St. Peter. If your slave will ever attend classes there, this dress will make her feel at home. In any case, what can be more charming and naive than a young schoolgirl?",
        "icon": "scene/item/item_sailor",
    },
    "cocktail_dress": {
        "name": "Gown",
        "price": 10,
        "desc": "Price: 10 sparks\nA dress made only of the finest fabric. This dress will make your slave stand out at any party. Very stylish and quite affordable - a great choice.",
        "icon": "scene/item/item_laced_dress",  # fixed typo here
    },
    "rubber_dress": {
        "name": "Latex Dress",
        "price": 20,
        "desc": "Price: 20 sparks\nThis dress made of thin latex will fit the body of your slave so tightly that every aspect of her body will be highlighted. Easily associable with sex, this outfit will constantly remind your slave that she is expected to learn fast and to be diligent when it comes to any sexual lesson. At the same time, the dress has a strict cut, so it can be worn at dinner parties.",
        "icon": "scene/item/item_rubber_dress",
    },
    "ukata": {
        "name": "Kimono-Yukata",
        "price": 20,
        "desc": "Price: 20 sparks\nBeautiful but strict Japanese clothes - the choice of a Geisha. Bright fabric colors and a lush wide belt will help to emphasize the beauty of the dress, and the strict cut will complement formal communication in any elite company.",
        "icon": "scene/item/item_ukata",
    },
    "bellydance": {
        "name": "Exotic Outfit",
        "price": 25,
        "desc": "Price: 25 sparks\nIn our city, it is difficult to surprise someone with exotic clothes. This dress with transparent sleeves, baggy trousers, shiny gold and ringing monists is definitely suited for such a task. And belly dancing too!",
        "icon": "scene/item/item_bellydance",
    },
    "leather_corset": {
        "name": "Leather Corset",
        "price": 50,
        "desc": "Price: 50 sparks\nA brace dress - the best choice for any sex slave! This hard corset with metal edges has an open front which reveals her breasts and pussy. The gentle brush of air over her exposed erogenous zones will stimulate her and direct her sexual interest towards her master! Moreover, she is certain to be more focused in any sexual training. Beautiful, exciting and practical!",
        "icon": "scene/item/item_corset",
    },
    "rich_dress": {
        "name": "Gorgeous Dress",
        "price": 50,
        "desc": "Price: 50 sparks\nYes, this dress is expensive and not very comfortable, but it is GORGEOUS! Talented designers made sure that anyone wearing this dress will appear elegant and tasteful.",
        "icon": "scene/item/item_rich_dress",
    },
    "wedding_dress": {
        "name": "Wedding Dress",
        "price": 100,
        "desc": "Price: 100 sparks\nThere is nothing better than a wedding dress. This is not just a luxury outfit, it's a symbol of purity and happiness, especially for a devoted slave. Every girl dreams of wearing a wedding dress and it will make every girl irresistible! For special ceremonies there is a sexy open front option.",
        "icon": "scene/item/item_wedding_dress",
    }
}

define dic_girl_clothing_hand ={
    "rubber_gloves": {
        "name": "Rubber Gloves",
        "desc": "Although rubber gloves do not complement any costume and will not decorate the hands of your slave, they have a lot of applications. These gloves will protect the delicate skin of the slave while cleaning and washing dishes. It also comes in handy for some medical procedures.",
        "icon": "scene/item/item_rubber_gloves",
        "price": 5
    },
    "laced_gloves": {
        "name": "Lace Gloves",
        "desc": "Elbow-length laced gloves are elegant and well suited for accentuating the style and charm of your slave's outfit. This pair covers the skin from elbow to fingertip with delicate lace.",
        "icon": "scene/item/item_laced_gloves",
        "price": 5
    },
    "leather_gloves": {
        "name": "Leather Gloves",
        "desc": "Elegant and durable leather gloves not only serve a stylish addition to most outfits, but also protect the hands of your slave during weapon training or alchemy.",
        "icon": "scene/item/item_leather_gloves",
        "price": 5
    },
    "plastic_bracers": {
        "name": "Carbon Fiber Gloves",
        "desc": "Lightweight and durable bracers from black carbon fiber hardly will add elegance to your slave. It will however protect her hands during combat training. And health is sometimes more important than beauty.",
        "icon": "scene/item/item_bracers",
        "price": 10
    },
    "fluffy_gloves": {
        "name": "Fluffy Paws",
        "desc": "These plump and fluffy gloves are made in the form of soft cat paws. It is not functional, but a very nice addition to the wardrobe of your slave. It is easier for her to feel like a pet!",
        "icon": "scene/item/item_fluffy_gloves",
        "price": 5
    }
}
define dic_girl_clothing_feet ={
    "tabi": {
        "name": "Tabi Socks",
        "desc": "This type of thick socks is cut with a separate thumb. Classic footwear for martial arts and silent movement. These socks will last through any sort of training.",
        "icon": "scene/item/item_tabi",
        "price": 5
    },
    "fluffy_stepins": {
        "name": "Soft Slippers",
        "desc": "These soft and fluffy slippers create an incredible feeling of warmth and comfort. They have a simple design, open at the back and with a pair of soft tassel balls on each slipper, decorated with tiny ribbons.",
        "icon": "scene/item/item_fluffy_stepins",
        "price": 5
    },
    "pointes": {
        "name": "Pointes",
        "desc": "Indispensable attribute of every ballerina - pointes. The most comfortable shoes for ballroom dancing.",
        "icon": "scene/item/item_pointes",
        "price": 5
    },
    "sneakers": {
        "name": "Sneakers",
        "desc": "Comfortable and practical footwear for sports and everyday wear.",
        "icon": "scene/item/item_sneakers",
        "price": 5
    },
    "high_heels": {
        "name": "Heels",
        "desc": "These shoes with high and sharp heels are a sample of elegance and style. A wide range of styles and colors means there is a fitting pair for every dress. No elegant outfit would be complete without a set of high heels.",
        "icon": "scene/item/item_high_heels",
        "price": 5
    },
    "high_boots": {
        "name": "High Boots",
        "desc": "High leather boots with shiny buckles and elegant heel. These are not only as elegant as high heels, but also emphasize the sexuality and unbridled temper of your slave.",
        "icon": "scene/item/item_high_boots",
        "price": 20
    }
}
define dic_girl_clothing_jewelry ={
    "plain_ring": {
        "name": "Elegant Ring",
        "desc": "A well crafted and beautiful ring made out of precious metals.",
        "icon": "scene/item/item_plain_ring",
        "price": 3
    },
    "incrusted_ring": {
        "name": "Gemstone Ring",
        "desc": "This ring is made out of higher quality metal and the inlaid stone enhances the beauty of anyone wearing this ring.",
        "icon": "scene/item/item_incrusted_ring",
        "price": 5
    },
}
define dic_girl_clothing_piercing ={
    "plain_earrings": {
        "name": "Small Hoop",
        "desc": "These elegant little hoops are perfectly suited for all pierced areas of the body.",
        "icon": "scene/item/item_plain_earring",
        "price": 3
    },
    "incrusted_earrings": {
        "name": "Gemstone Stud",
        "desc": "This drop stud is encrusted with synthetic crystals, which are generally more rare and exotic than standard gemstones. For the ears there is an option with clips that does not require piercing.",
        "icon": "scene/item/item_incrusted_earring",
        "price": 5
    },
    "barbells": {
        "name": "Barbell",
        "desc": "These barbells are made out of precious metal and polished to perfection with a rare gemstone on either end. Barbells can provide mild stimulation to a pierced tongue, nipple, navel or clit.",
        "icon": "scene/service/service_tongue_piercing",
        "price": 10
    },
    "nipple_chain": {
        "name": "Nipple Chain",
        "desc": "A pair of rings linked with a chain, which is meant to connect the nipples of a slave. This will give your slave a slightly exotic look. The rings provide constant stimulation, and knowing that you can always pull the chain, she will behave more respectfully - as pulling it hurts.",
        "icon": "scene/item/item_nipple_chain",
        "price": 10
    },
    "heavy_gauge_rings": {
        "name": "Thick Steel Ring",
        "desc": "Add drama to any piercing and remind your slave of her place. Because nothing says 'slave' like heavy gauge steel. Exotic, but not the most elegant, of course. A trio of these make a good complement for a nipple chain and a nose ring.",
        "icon": "scene/item/item_heavy_gauge",
        "price": 30
    }
}
define dic_girl_clothing_head ={
    "plain_headband": {
        "name": "Headband",
        "desc": "This accessory is designed not only as an accessory, but for everyday use. The lightweight and flexible headband allows to neatly tuck away hair so that it does not conceal the face or fall into the pot.",
        "icon": "scene/item/item_headband",
        "price": 3
    },
    "hijab": {
        "name": "Hijab",
        "desc": "A hijab completely covers the hair. Perhaps not the best kind of jewelry for the head, but it is very practical in everyday affairs. The hair will not fall into the soup or interfere during cleaning!",
        "icon": "scene/item/item_hijab",
        "price": 3
    },
    "crown_of_thorns": {
        "name": "Crown of Thorns",
        "desc": "Of course this is only the name, it has no thorns. These rims are made out of barbed wire. The trick is the attachment mechanism - it is arranged such as to cause pain, but not to injure and not be removed so easily. Constant, though mild pain reminds a slave of humility.",
        "icon": "scene/item/item_thorns",
        "price": 5
    },
    "plain_tiara": {
        "name": "Ornamented Diadem",
        "desc": "A stylish diadem from precious metal. It perfectly complements the hairstyle of your slave and surrounds her with an aura of luxury.",
        "icon": "scene/item/item_plain_tiara",
        "price": 10
    },
    "hairnet": {
        "name": "Hairnet",
        "desc": "Elegant hair mesh decorated with pearls and preciously woven, it will not only accentuate the style of your slave, but also permanently retain her hairstyle. In addition to the product itself, a set of silver pins and a pearl comb are included.",
        "icon": "scene/item/item_hairnet",
        "price": 10
    },
    "glasses": {
        "name": "Stylish Glasses",
        "desc": "Beautiful and practical accessory. The expertly selected lenses are optimal for the slave's vision correction, allowing her to read documents more efficiently. And a stylish frame from precious metal accentuates the unique style of the girl.",
        "icon": "scene/item/item_glasses",
        "price": 10
    },
    "nekomimi": {
        "name": "Cat Ears",
        "desc": "Large fur cat ears with a flexible rim certainly attract the attention of others and will help your slave feel like a real pet.",
        "icon": "scene/item/item_nekomimi",
        "price": 10
    },
    "incrusted_tiara": {
        "name": "Precious Tiara",
        "desc": "This massive tiara is decorated with shimmering gems of the highest quality - it will certainly attract attention and emphasize the beauty of your slave.",
        "icon": "scene/item/item_incrusted_tiara",
        "price": 20
    },
    "exotic_wig": {
        "name": "Exotic Wig",
        "desc": "Want to raise the exotic nature of your slave? Use a gorgeous exotic wig. Incredible colors, feathers, dreadlocks as well as shiny jewelry woven into the hair literally attract glances.",
        "icon": "scene/item/item_exotic_wig",
        "price": 20
    }
}
define dic_girl_clothing_neck = {
    "plain_pendant": {
        "name": "Chain with Pendant",
        "desc": "A chain from precious metal with a shaped pendant perfectly accentuates the style and elegance of your slave.",
        "icon": "scene/item/item_plain_pendant",
        "price": 5,
        "escape": True,
    },
    "incrusted_necklace": {
        "name": "Gemstone Necklace",
        "desc": "Figured necklace, studded with beautiful gems.",
        "icon": "scene/item/item_incrusted_necklace",
        "price": 10,
        "escape": True,
    },
    "dog_collar": {
        "name": "Collar and Leash",
        "desc": "Provided with a leash, it is immediately obvious that this is not made for humans, but for a pet. Helps set up a slave in the right mood, but it's easy to remove. This collar is not meant to remind your slave of her fate, as it is obviously a pet collar, not a slave collar.",
        "icon": "scene/item/item_dog_collar",
        "price": 5,
        "escape": True,
    },
    "leather_collar": {
        "name": "Leather Collar",
        "desc": "Wide leather collar with studs and rings for attaching a leash and shackles. Wearing one of these, your slave will never forget about her fate. Not to mention the fact that it's just very practical for many games. It is equipped with your name token to get her back in case of loss.",
        "icon": "scene/item/item_leather_collar",
        "price": 3,
        "escape": False,
    },
    "steel_collar": {
        "name": "Steel Collar",
        "desc": "Durable steel collar - heavy reminder of the fate of the slave from which it is impossible to escape. Wearing a steel collar is not a pleasant experience - it rubs the neck and grazes the skin. Not to mention the impact on the pride and conceit. It is engraved with your name and address to get her back in case of loss.",
        "icon": "scene/item/item_steel_collar",
        "price": 10,
        "escape": False,
    },
    "spiked_collar": {
        "name": "Spiked Collar",
        "desc": "Brutal form of a collar decorated with long and sharp steel spikes. It not only reminds the slave of her status, but also makes her feel more aggressive. Good accessory for a gladiatrix, and indeed for any temperamental bitch. It is equipped with your name token to get her back in case of loss.",
        "icon": "scene/item/item_spiked_collar",
        "price": 10,
        "escape": False,
    },
    "shock_collar": {
        "name": "Shock Collar",
        "desc": "A technogenic shock collar. Serpis developed these to discipline cloned soldiers and reached an agreement with the Guild of Trainers for non-military use. It not only reminds a slave of her status but continuously monitors mental patterns during speech and applies an effect similar to Cruciato when it senses an attitude lacking in humility. It is equipped with your name token in case of loss.",
        "icon": "scene/item/item_shock_collar",
        "price": 25,
        "escape": False,
    },
    "golden_collar": {
        "name": "Ornamented Collar",
        "desc": "A luxurious wide and golden collar. It is adorned with exotic jewels and equipped with your name token to get her back in case of loss. Multiple rings allow for attaching leash and shackles. This stylish accessory will make sure that the slave will not forget that you are her master and she has to obey.",
        "icon": "scene/item/item_golden_collar",
        "price": 20,
        "escape": False,
    }
}


define dic_girl_clothing_hand_or_feet = {
    "leather_straps": {
        "name": "Leather Shackles",
        "desc": "A pair of sturdy leather bracelets with steel rings for fixing chains. This accessory will make sure that the slave will not forget that you are her master and she has to obey. Can be worn on the hands or feet, and successfully used in any bondage. Very practical!",
        "icon": "scene/item/item_leather_straps",
        "price": 5
    }
}
define dic_girl_clothing_pony = {
    "anal_tail":{
        "name": "Anal tail",
        "desc":"This device consists of two parts - a large plastic phallus with an extension that provides a secure fit in the ass, and a set of removable tails. Well suited for animal play and increases the arousal of your slave.",
        "icon": "scene/item/item_anal_tail",
        "price": 10
    },
    "pony_plume": {
        "name": "Plumed Bridle",
        "desc": "It's just a necessary accessory for any ponygirl. The leather bridle is securely locked in the mouth gag and a bit and reins are already connected. Thick leather blinkers allow for the slave only to look straight ahead and a bright and high plume makes the whole construction look pleasing to the eye.",
        "icon": "scene/item/item_pony_plume",
        "price": 15
    },
    "ponygirl_harness": {
        "name": "Pony Harness",
        "desc": "The main objective of this leather corset is to fix a ponygirl's hands behind her back so that she can no longer use them. A big ring in the area of the fixed hands provides the convenience of rides and additional straps in the front provide a fixation and emphasize the breasts.",
        "icon": "scene/item/item_harness",
        "price": 20
    },
    "hoofed_boots": {
        "name": "Hooved Boots",
        "desc": "This is a special kind of boots with heels, imitating horse hooves. Walking with them is even more uncomfortable than with usual heels, but they look stylish and they can be used to stomp loudly, showing your temper.",
        "icon": "scene/item/item_hoofs",
        "price": 25
    },
    "cow_gear": {
        "name": "Cow Gear",
        "desc": "Tail, ears, and a nice bell with your name engraved on it: all indispensable elements to remind your cow of her role. The ringing can be a bit mind-numbing, though.",
        "icon": "scene/item/item_cow_gear",
        "price": 25
    },
    "petsuit": {
        "name": "Petsuit",
        "desc": "This version of a deprivation suit does not impede vision or hearing. It is made so that the wearer acts like a cat or a dog. Allows you to move only on all fours, leaning on elbows and knees.",
        "icon": "scene/item/item_petsuit",
        "price": 25
    },
    "deprivation_suit": {
        "name": "Deprivation Suit",
        "desc": "Although it is called a suit, it is not intended to be worn as such, it's for radical bondage. The thick rubber shell and durable leather belts prevent any movement and apply a constant uniform pressure. The eyes, ears and mouth are tightly shut to completely cut off the wearer from the outside world.",
        "icon": "scene/item/item_dsuit",
        "price": 50
    }
}
define dic_girl_clothing_enforce = {
    "vaginal_balls": {
        "name": "Vaginal Beads",
        "desc": "A pair of beads on a string with a ring designed for extended wear in the vagina. They are excellent to help build arousal and develop muscles.",
        "icon": "scene/item/item_vaginal_balls",
        "price": 5
    },
    "anal_plug": {
        "name": "Anal Pear",
        "desc": "Unlike the normal anal plug, this pear has a screw that allows you to expand it after inserting it in the ass. The screw is fixed with a small padlock, so there is no way to remove the pear without the key.",
        "icon": "scene/item/item_toys",
        "price": 20
    },
    "secure_gag": {
        "name": "Reliable Gag",
        "desc": "This impressive steel structure inherits the best traits of the horse bridle and dental reamer. You cannot remove it without the key and the mouth is fixed in the maximum open state.",
        "icon": "scene/item/item_secure_gag",
        "price": 20
    },
    "chastity_belt": {
        "name": "Chastity Belt",
        "desc": "A solid garment of steel and leather that prevents all access to the vagina for anybody but the keyholder.",
        "icon": "scene/item/item_chastity_belt",
        "price": 30
    },
    "pissuar_stable": {
        "name": "Urinal Rack",
        "desc": "This piece of furniture does not take up too much space, as its main component is a slave. The rack is equipped with robust clamps for hands, feet and the head. It comes with a ring expander for the mouth as well as a nose clip. You can also set a transparent headband bowl of a «drink or choke» type.",
        "icon": "scene/item/item_pissuar",
        "price": 100
    },
    "toilet_stable": {
        "name": "Toilet Seat",
        "desc": "A pretty massive piece of furniture, but it is well worth it. The construct completely immobilizes the slave and only her head sticks out. A special device makes sure that her mouth is open at all times so it can be used to take a dump. The massive construction prevents any attempts to escape.",
        "icon": "scene/item/item_toilet",
        "price": 250
    }
}

define dic_girl_clothing_gift = {
    "bouqet": {
        "name": "Bouquet of Flowers ($2)",
        "desc": "A small but very beautiful bouquet of flowers. This is a special ripening variety, grown hydroponically in the technosphere - only blooms for one day, but quite affordable.",
        "icon": "scene/item/item_bouqet",
        "price": 2
    },
    "plaid": {
        "name": "Warm Plaid ($9)",
        "desc": "Great soft weave with a scot-pattern. Wrapped in this plaid, a slave will feel comfortable and warm when she rests during the day or in her bedroll, and it will be easier to go through difficult times in life.",
        "icon": "scene/item/item_plaid",
        "price": 9
    },
    "stuffed_toy": {
        "name": "Plush Toy ($15)",
        "desc": "A rather large and expensive toy will be a good gift. Will also keep the slave warm, lying on a thin bedroll near the door.",
        "icon": "scene/item/item_stuffed_toy",
        "price": 15
    },
    "perfume": {
        "name": "Perfume ($20)",
        "desc": "A beautiful bottle of perfume with a magnificent composition, brought through the fog. Of course, such a gift will please any woman, but you are pursuing two purposes - your slave will also be more stylish and more desirable for customers. And using it will help her grow accustomed to her fate.",
        "icon": "scene/item/item_perfume",
        "price": 20
    },
    "pony": {
        "name": "Mini-Pony ($50)",
        "desc": "These incredibly cute creatures the size of a cat are grown from eggs in the technosphere. Their life expectancy is not very long and they are inedible, but they are faithful and lovely. You will have to pay for food regularly. (1 spark/day)",
        "icon": "scene/item/item_pony",
        "price": 50
    }
}
define dic_girl_clothing_full ={
    "naked": {
        "name": "Naked",
        "price": 0,
        "desc": "Your slave is completely naked. This is helpful for some types of training, and it will remind her of her place, but she might be happier if she had something to wear.",
        "icon":"scene/item/clear_small",
    },
    "common_apron": {
        "name": "Frilly Apron",
        "price": 5,
        "desc": "Price: 5 sparks\nAprons are most useful in the kitchen. This apron is worn without any other clothing, leaving plenty of opportunities to enjoy the sight of your woman working in the kitchen.",
        "icon":"scene/item/item_apron1",
    },
    "maid_dress": {
        "name": "Maid Outfit",
        "price": 5,
        "desc": "Price: 5 sparks\nClassic French maid uniform. Many parts of the uniform have been left out in order to preserve fabric. Most customers actually like this design.",
        "icon":"scene/item/item_maido",
    },
    "nurse_dress": {
        "name": "Nurse Outfit",
        "price": 5,
        "desc": "Price: 5 sparks\nA flashy white nurse dress. This is what you need to lift the spirit of any patient.",
        "icon":"scene/item/item_nurse",
    },
    "leotard": {
        "name": "Athletic Leotard",
        "price": 5,
        "desc": "Price: 5 sparks\nA tight leotard which emphasizes the shape of your slave while not hampering her movements. Perfect for any sports activity, except for battles.",
        "icon":"scene/item/item_leotard",
    },
    "chainmail_bikini": {
        "name": "Chainmail Bikini",
        "price": 5,
        "desc": "Price: 5 sparks\nClassic gladiatrix clothing. I repeat - clothing. It's not an armor, it's a stage props, made of light and gleaming anodized aluminum. The cut is so minimal that it almost hides nothing.",
        "icon":"scene/item/item_chainmail_bikini",
    },
    "enchanter_robe": {
        "name": "Sorceress Robes",
        "price": 5,
        "desc": "Price: 5 sparks\nMade of a very light but opaque fabric - this arcane robe with a hood completely hides the shape of your slave. Not very sexy, but very mysterious and helps to tune in to a mystical way.",
        "icon":"scene/item/item_robe",
    },
    "sun_dress": {
        "name": "Light Sundress",
        "price": 5,
        "desc": "Price: 5 sparks\nThis cute little dress is perfect for relaxing and raises the mood of those who wear it. Of course, there are more beautiful or functional dresses, but wearing a sundress is just very nice.",
        "icon":"scene/item/item_sundress",
    },
    "laced_underwear": {
        "name": "Lace Underwear",
        "price": 5,
        "desc": "Price: 5 sparks\nIn this set of sexy lace underwear that includes bra, panties, lightweight corset and stockings with garters, any girl would look desirable. Treat yourself to a beautiful sight and tune your slave for a rough night!",
        "icon":"scene/item/item_laced_underwear",
    },
    "sailor_foku": {
        "name": "School Uniform",
        "price": 10,
        "desc": "Price: 10 sparks\nUniform of the Academy of St. Peter. If your slave will ever attend classes there, this dress will make her feel at home. In any case, what can be more charming and naive than a young schoolgirl?",
        "icon":"scene/item/item_sailor",
    },
    "cocktail_dress": {
        "name": "Gown",
        "price": 10,
        "desc": "Price: 10 sparks\nA dress made only of the finest fabric. This dress will make your slave stand out at any party. Very stylish and quite affordable - a great choice.",
        "icon":"scene/item/item_laced_dress",
    },
    "rubber_dress": {
        "name": "Latex Dress",
        "price": 20,
        "desc": "Price: 20 sparks\nThis dress made of thin latex will fit the body of your slave so tightly that every aspect of her body will be highlighted. Easily associable with sex, this outfit will constantly remind your slave that she is expected to learn fast and to be diligent when it comes to any sexual lesson. At the same time, the dress has a strict cut, so it can be worn at dinner parties.",
        "icon":"scene/item/item_rubber_dress",
    },
    "ukata": {
        "name": "Kimono-Yukata",
        "price": 20,
        "desc": "Price: 20 sparks\nBeautiful but strict Japanese clothes - the choice of a Geisha. Bright fabric colors and a lush wide belt will help to emphasize the beauty of the dress, and the strict cut will complement formal communication in any elite company.",
        "icon":"scene/item/item_ukata",
    },
    "bellydance": {
        "name": "Exotic Outfit",
        "price": 25,
        "desc": "Price: 25 sparks\nIn our city, it is difficult to surprise someone with exotic clothes. This dress with transparent sleeves, baggy trousers, shiny gold and ringing monists is definitely suited for such a task. And belly dancing too!",
        "icon":"scene/item/item_bellydance",
    },
    "leather_corset": {
        "name": "Leather Corset",
        "price": 50,
        "desc": "Price: 50 sparks\nA brace dress - the best choice for any sex slave! This hard corset with metal edges has an open front which reveals her breasts and pussy. The gentle brush of air over her exposed erogenous zones will stimulate her and direct her sexual interest towards her master! Moreover, she is certain to be more focused in any sexual training. Beautiful, exciting and practical!",
        "icon": "scene/item/item_corset",
    },
    "rich_dress": {
        "name": "Gorgeous Dress",
        "price": 50,
        "desc": "Price: 50 sparks\nYes, this dress is expensive and not very comfortable, but it is GORGEOUS! Talented designers made sure that anyone wearing this dress will appear elegant and tasteful.",
        "icon": "scene/item/item_rich_dress",
    },
    "wedding_dress": {
        "name": "Wedding Dress",
        "price": 100,
        "desc": "Price: 100 sparks\nThere is nothing better than a wedding dress. This is not just a luxury outfit, it's a symbol of purity and happiness, especially for a devoted slave. Every girl dreams of wearing a wedding dress and it will make every girl irresistible! For special ceremonies there is a sexy open front option.",
        "icon": "scene/item/item_wedding_dress",
    },
    "rubber_gloves": {
        "name": "Rubber Gloves",
        "desc": "Although rubber gloves do not complement any costume and will not decorate the hands of your slave, they have a lot of applications. These gloves will protect the delicate skin of the slave while cleaning and washing dishes. It also comes in handy for some medical procedures.",
        "icon": "scene/item/item_rubber_gloves",
        "price": 5
    },
    "laced_gloves": {
        "name": "Lace Gloves",
        "desc": "Elbow-length laced gloves are elegant and well suited for accentuating the style and charm of your slave's outfit. This pair covers the skin from elbow to fingertip with delicate lace.",
        "icon": "scene/item/item_laced_gloves",
        "price": 5
    },
    "leather_gloves": {
        "name": "Leather Gloves",
        "desc": "Elegant and durable leather gloves not only serve a stylish addition to most outfits, but also protect the hands of your slave during weapon training or alchemy.",
        "icon": "scene/item/item_leather_gloves",
        "price": 5
    },
    "plastic_bracers": {
        "name": "Carbon Fiber Gloves",
        "desc": "Lightweight and durable bracers from black carbon fiber hardly will add elegance to your slave. It will however protect her hands during combat training. And health is sometimes more important than beauty.",
        "icon": "scene/item/item_bracers",
        "price": 10
    },
    "fluffy_gloves": {
        "name": "Fluffy Paws",
        "desc": "These plump and fluffy gloves are made in the form of soft cat paws. It is not functional, but a very nice addition to the wardrobe of your slave. It is easier for her to feel like a pet!",
        "icon": "scene/item/item_fluffy_gloves",
        "price": 5
    },
    "tabi": {
        "name": "Tabi Socks",
        "desc": "This type of thick socks is cut with a separate thumb. Classic footwear for martial arts and silent movement. These socks will last through any sort of training.",
        "icon": "scene/item/item_tabi",
        "price": 5
    },
    "fluffy_stepins": {
        "name": "Soft Slippers",
        "desc": "These soft and fluffy slippers create an incredible feeling of warmth and comfort. They have a simple design, open at the back and with a pair of soft tassel balls on each slipper, decorated with tiny ribbons.",
        "icon": "scene/item/item_fluffy_stepins",
        "price": 5
    },
    "pointes": {
        "name": "Pointes",
        "desc": "Indispensable attribute of every ballerina - pointes. The most comfortable shoes for ballroom dancing.",
        "icon": "scene/item/item_pointes",
        "price": 5
    },
    "sneakers": {
        "name": "Sneakers",
        "desc": "Comfortable and practical footwear for sports and everyday wear.",
        "icon": "scene/item/item_sneakers",
        "price": 5
    },
    "high_heels": {
        "name": "Heels",
        "desc": "These shoes with high and sharp heels are a sample of elegance and style. A wide range of styles and colors means there is a fitting pair for every dress. No elegant outfit would be complete without a set of high heels.",
        "icon": "scene/item/item_high_heels",
        "price": 5
    },
    "high_boots": {
        "name": "High Boots",
        "desc": "High leather boots with shiny buckles and elegant heel. These are not only as elegant as high heels, but also emphasize the sexuality and unbridled temper of your slave.",
        "icon": "scene/item/item_high_boots",
        "price": 20
    },
    "plain_ring": {
        "name": "Elegant Ring",
        "desc": "A well crafted and beautiful ring made out of precious metals.",
        "icon": "scene/item/item_plain_ring",
        "price": 3
    },
    "incrusted_ring": {
        "name": "Gemstone Ring",
        "desc": "This ring is made out of higher quality metal and the inlaid stone enhances the beauty of anyone wearing this ring.",
        "icon": "scene/item/item_incrusted_ring",
        "price": 5
    },
    "plain_earrings": {
        "name": "Small Hoop",
        "desc": "These elegant little hoops are perfectly suited for all pierced areas of the body.",
        "icon": "scene/item/item_plain_earring",
        "price": 3
    },
    "incrusted_earrings": {
        "name": "Gemstone Stud",
        "desc": "This drop stud is encrusted with synthetic crystals, which are generally more rare and exotic than standard gemstones. For the ears there is an option with clips that does not require piercing.",
        "icon": "scene/item/item_incrusted_earring",
        "price": 5
    },
    "barbells": {
        "name": "Barbell",
        "desc": "These barbells are made out of precious metal and polished to perfection with a rare gemstone on either end. Barbells can provide mild stimulation to a pierced tongue, nipples, navel or clit.",
        "icon": "scene/service/service_tongue_piercing",
        "price": 10
    },
    "nipple_chain": {
        "name": "Nipple Chain",
        "desc": "A pair of rings linked with a chain, which is meant to connect the nipples of a slave. This will give your slave a slightly exotic look. The rings provide constant stimulation, and knowing that you can always pull the chain, she will behave more respectfully - as pulling it hurts.",
        "icon": "scene/item/item_nipple_chain",
        "price": 10
    },
    "heavy_gauge_rings": {
        "name": "Thick Steel Ring",
        "desc": "Add drama to any piercing and remind your slave of her place. Because nothing says 'slave' like heavy gauge steel. Exotic, but not the most elegant, of course. A trio of these make a good complement for a nipple chain and a nose ring.",
        "icon": "scene/item/item_heavy_gauge",
        "price": 30
    },
    "plain_headband": {
        "name": "Headband",
        "desc": "This accessory is designed not only as an accessory, but for everyday use. The lightweight and flexible headband allows to neatly tuck away hair so that it does not conceal the face or fall into the pot.",
        "icon": "scene/item/item_headband",
        "price": 3
    },
    "hijab": {
        "name": "Hijab",
        "desc": "A hijab completely covers the hair. Perhaps not the best kind of jewelry for the head, but it is very practical in everyday affairs. The hair will not fall into the soup or interfere during cleaning!",
        "icon": "scene/item/item_hijab",
        "price": 3
    },
    "crown_of_thorns": {
        "name": "Crown of Thorns",
        "desc": "Of course this is only the name, it has no thorns. These rims are made out of barbed wire. The trick is the attachment mechanism - it is arranged such as to cause pain, but not to injure and not be removed so easily. Constant, though mild pain reminds a slave of humility.",
        "icon": "scene/item/item_thorns",
        "price": 5
    },
    "plain_tiara": {
        "name": "Ornamented Diadem",
        "desc": "A stylish diadem from precious metal. It perfectly complements the hairstyle of your slave and surrounds her with an aura of luxury.",
        "icon": "scene/item/item_plain_tiara",
        "price": 10
    },
    "hairnet": {
        "name": "Hairnet",
        "desc": "Elegant hair mesh decorated with pearls and preciously woven, it will not only accentuate the style of your slave, but also permanently retain her hairstyle. In addition to the product itself, a set of silver pins and a pearl comb are included.",
        "icon": "scene/item/item_hairnet",
        "price": 10
    },
    "glasses": {
        "name": "Stylish Glasses",
        "desc": "Beautiful and practical accessory. The expertly selected lenses are optimal for the slave's vision correction, allowing her to read documents more efficiently. And a stylish frame from precious metal accentuates the unique style of the girl.",
        "icon": "scene/item/item_glasses",
        "price": 10
    },
    "nekomimi": {
        "name": "Cat Ears",
        "desc": "Large fur cat ears with a flexible rim certainly attract the attention of others and will help your slave feel like a real pet.",
        "icon": "scene/item/item_nekomimi",
        "price": 10
    },
    "incrusted_tiara": {
        "name": "Precious Tiara",
        "desc": "This massive tiara is decorated with shimmering gems of the highest quality - it will certainly attract attention and emphasize the beauty of your slave.",
        "icon": "scene/item/item_incrusted_tiara",
        "price": 20
    },
    "exotic_wig": {
        "name": "Exotic Wig",
        "desc": "Want to raise the exotic nature of your slave? Use a gorgeous exotic wig. Incredible colors, feathers, dreadlocks as well as shiny jewelry woven into the hair literally attract glances.",
        "icon": "scene/item/item_exotic_wig",
        "price": 20
    },
    "plain_pendant": {
        "name": "Chain with Pendant",
        "desc": "A chain from precious metal with a shaped pendant perfectly accentuates the style and elegance of your slave.",
        "icon": "scene/item/item_plain_pendant",
        "price": 5,
        "escape": True,
    },
    "incrusted_necklace": {
        "name": "Gemstone Necklace",
        "desc": "Figured necklace, studded with beautiful gems.",
        "icon": "scene/item/item_incrusted_necklace",
        "price": 10,
        "escape": True,
    },
    "dog_collar": {
        "name": "Collar and Leash",
        "desc": "Provided with a leash, it is immediately obvious that this is not made for humans, but for a pet. Helps set up a slave in the right mood, but it's easy to remove. This collar is not meant to remind your slave of her fate, as it is obviously a pet collar, not a slave collar.",
        "icon": "scene/item/item_dog_collar",
        "price": 5,
        "escape": True,
    },
    "leather_collar": {
        "name": "Leather Collar",
        "desc": "Wide leather collar with studs and rings for attaching a leash and shackles. Wearing one of these, your slave will never forget about her fate. Not to mention the fact that it's just very practical for many games. It is equipped with your name token to get her back in case of loss.",
        "icon": "scene/item/item_leather_collar",
        "price": 3,
        "escape": False,
    },
    "steel_collar": {
        "name": "Steel Collar",
        "desc": "Durable steel collar - heavy reminder of the fate of the slave from which it is impossible to escape. Wearing a steel collar is not a pleasant experience - it rubs the neck and grazes the skin. Not to mention the impact on the pride and conceit. It is engraved with your name and address to get her back in case of loss.",
        "icon": "scene/item/item_steel_collar",
        "price": 10,
        "escape": False,
    },
    "spiked_collar": {
        "name": "Spiked Collar",
        "desc": "Brutal form of a collar decorated with long and sharp steel spikes. It not only reminds the slave of her status, but also makes her feel more aggressive. Good accessory for a gladiatrix, and indeed for any temperamental bitch. It is equipped with your name token to get her back in case of loss.",
        "icon": "scene/item/item_spiked_collar",
        "price": 10,
        "escape": False,
    },
    "shock_collar": {
        "name": "Shock Collar",
        "desc": "A technogenic shock collar. Serpis developed these to discipline cloned soldiers and reached an agreement with the Guild of Trainers for non-military use. It not only reminds a slave of her status but continuously monitors mental patterns during speech and applies an effect similar to Cruciato when it senses an attitude lacking in humility. It is equipped with your name token in case of loss.",
        "icon": "scene/item/item_shock_collar",
        "price": 25,
        "escape": False,
    },
    "golden_collar": {
        "name": "Ornamented Collar",
        "desc": "A luxurious wide and golden collar. It is adorned with exotic jewels and equipped with your name token to get her back in case of loss. Multiple rings allow for attaching leash and shackles. This stylish accessory will make sure that the slave will not forget that you are her master and she has to obey.",
        "icon": "scene/item/item_golden_collar",
        "price": 20,
        "escape": False,
    },
    "leather_straps": {
        "name": "Leather Shackles",
        "desc": "A pair of sturdy leather bracelets with steel rings for fixing chains. This accessory will make sure that the slave will not forget that you are her master and she has to obey. Can be worn on the hands or feet, and successfully used in any bondage. Very practical!",
        "icon": "scene/item/item_leather_straps",
        "price": 5
    },
    "anal_tail":{
        "name": "Anal tail",
        "desc":"This device consists of two parts - a large plastic phallus with an extension that provides a secure fit in the ass, and a set of removable tails. Well suited for animal play and increases the arousal of your slave.",
        "icon": "scene/item/item_anal_tail",
        "price": 10
    },
    "pony_plume": {
        "name": "Plumed Bridle",
        "desc": "It's just a necessary accessory for any ponygirl. The leather bridle is securely locked in the mouth gag and a bit and reins are already connected. Thick leather blinkers allow for the slave only to look straight ahead and a bright and high plume makes the whole construction look pleasing to the eye.",
        "icon": "scene/item/item_pony_plume",
        "price": 15
    },
    "ponygirl_harness": {
        "name": "Pony Harness",
        "desc": "The main objective of this leather corset is to fix a ponygirl's hands behind her back so that she can no longer use them. A big ring in the area of the fixed hands provides the convenience of rides and additional straps in the front provide a fixation and emphasize the breasts.",
        "icon": "scene/item/item_harness",
        "price": 20
    },
    "hoofed_boots": {
        "name": "Hooved Boots",
        "desc": "This is a special kind of boots with heels, imitating horse hooves. Walking with them is even more uncomfortable than with usual heels, but they look stylish and they can be used to stomp loudly, showing your temper.",
        "icon": "scene/item/item_hoofs",
        "price": 25
    },
    "cow_gear": {
        "name": "Cow Gear",
        "desc": "Tail, ears, and a nice bell with your name engraved on it: all indispensable elements to remind your cow of her role. The ringing can be a bit mind-numbing, though.",
        "icon": "scene/item/item_cow_gear",
        "price": 25
    },
    "petsuit": {
        "name": "Petsuit",
        "desc": "This version of a deprivation suit does not impede vision or hearing. It is made so that the wearer acts like a cat or a dog. Allows you to move only on all fours, leaning on elbows and knees.",
        "icon": "scene/item/item_petsuit",
        "price": 25
    },
    "deprivation_suit": {
        "name": "Deprivation Suit",
        "desc": "Although it is called a suit, it is not intended to be worn as such, it's for radical bondage. The thick rubber shell and durable leather belts prevent any movement and apply a constant uniform pressure. The eyes, ears and mouth are tightly shut to completely cut off the wearer from the outside world.",
        "icon": "scene/item/item_dsuit",
        "price": 50
    },
    "vaginal_balls": {
        "name": "Vaginal Beads",
        "desc": "A pair of beads on a string with a ring designed for extended wear in the vagina. They are excellent to help build arousal and develop muscles.",
        "icon": "scene/item/item_vaginal_balls",
        "price": 5
    },
    "anal_plug": {
        "name": "Anal Pear",
        "desc": "Unlike the normal anal plug, this pear has a screw that allows you to expand it after inserting it in the ass. The screw is fixed with a small padlock, so there is no way to remove the pear without the key.",
        "icon": "scene/item/item_toys",
        "price": 20
    },
    "secure_gag": {
        "name": "Reliable Gag",
        "desc": "This impressive steel structure inherits the best traits of the horse bridle and dental reamer. You cannot remove it without the key and the mouth is fixed in the maximum open state.",
        "icon": "scene/item/item_secure_gag",
        "price": 20
    },
    "chastity_belt": {
        "name": "Chastity Belt",
        "desc": "A solid garment of steel and leather that prevents all access to the vagina for anybody but the keyholder.",
        "icon": "scene/item/item_chastity_belt",
        "price": 30
    },
    "pissuar_stable": {
        "name": "Urinal Rack",
        "desc": "This piece of furniture does not take up too much space, as its main component is a slave. The rack is equipped with robust clamps for hands, feet and the head. It comes with a ring expander for the mouth as well as a nose clip. You can also set a transparent headband bowl of a «drink or choke» type.",
        "icon": "scene/item/item_pissuar",
        "price": 100
    },
    "toilet_stable": {
        "name": "Toilet Seat",
        "desc": "A pretty massive piece of furniture, but it is well worth it. The construct completely immobilizes the slave and only her head sticks out. A special device makes sure that her mouth is open at all times so it can be used to take a dump. The massive construction prevents any attempts to escape.",
        "icon": "scene/item/item_toilet",
        "price": 250
    },
    "bouqet": {
        "name": "Bouquet of Flowers ($2)",
        "desc": "A small but very beautiful bouquet of flowers. This is a special ripening variety, grown hydroponically in the technosphere - only blooms for one day, but quite affordable.",
        "icon": "scene/item/item_bouqet",
        "price": 2
    },
    "plaid": {
        "name": "Warm Plaid ($9)",
        "desc": "Great soft weave with a scot-pattern. Wrapped in this plaid, a slave will feel comfortable and warm when she rests during the day or in her bedroll, and it will be easier to go through difficult times in life.",
        "icon": "scene/item/item_plaid",
        "price": 9
    },
    "stuffed_toy": {
        "name": "Plush Toy ($15)",
        "desc": "A rather large and expensive toy will be a good gift. Will also keep the slave warm, lying on a thin bedroll near the door.",
        "icon": "scene/item/item_stuffed_toy",
        "price": 15
    },
    "perfume": {
        "name": "Perfume ($20)",
        "desc": "A beautiful bottle of perfume with a magnificent composition, brought through the fog. Of course, such a gift will please any woman, but you are pursuing two purposes - your slave will also be more stylish and more desirable for customers. And using it will help her grow accustomed to her fate.",
        "icon": "scene/item/item_perfume",
        "price": 20
    },
    "pony": {
        "name": "Mini-Pony ($50)",
        "desc": "These incredibly cute creatures the size of a cat are grown from eggs in the technosphere. Their life expectancy is not very long and they are inedible, but they are faithful and lovely. You will have to pay for food regularly. (1 spark/day)",
        "icon": "scene/item/item_pony",
        "price": 50
    },
    "remove": {
        "name": "",
        "desc": "You removed the item from the slave",
        "icon": "scene/item/clear_small",
        "price": 0
    }
}
define dic_girl_psy_status = {
    "arrogant": 2,
    "broken": -100,
    "depresive": -1,
    "docile": -1,
    "frightened": -2,
    "hateful": 4,
    "horny": 0,
    "hysteric": 3,
    "lachrymose": -1,
    "obedient": 0,
    "optimistic": 0,
    "reluctant": 0,
    "resistant": 3,
    "servile": 0,
    "soft": 0,
}
default dic_cook = [
    "You send [all_girls_list[girl_index]['name']] to the kitchen to prepare dinner. She is obviously not confident in her abilities, but never mind - let her work! When you come check her work an hour later it turns out that she just opened the canned food and placed it on plates.",
    "[all_girls_list[girl_index]['name']] was busy with pots and pans for about an hour, but her cooked dishes are not any tastier as a result. Some food was undercooked, some food was overcooked, and the rest is over-salted. You can eat it, but her cooking is severely lacking.",
    "[all_girls_list[girl_index]['name']] is in the kitchen for several hours. Despite such an impressive amount of time, the dishes are pretty simple - nothing fancy. Well, at least she prepared everything correctly, and it is certainly better than canned food.",
    "[all_girls_list[girl_index]['name']] prepares dinner without much delay. She knows when to stop adding in the seasonings and did not overcook anything, although she doesn't know how to add any refinement or finesse to the meal. Nevertheless, she made a great home-cooked meal, nourishing and delicious.",
    "[all_girls_list[girl_index]['name']] starts cooking as a living food processor. She so expertly wielded knives, pans, ingredients, and seasonings that the food is cooked very well. Pleasant aromas from the kitchen are so enticing that you hardly wait for an invitation to dinner. Yummy!",
    "In the kitchen [all_girls_list[girl_index]['name']] literally transformed the meal into something spectacular. The process of cooking looks like a real show. Even with the most simple meals she is able to create something so magnificent that it is a delight to the senses. Having her is the dream of every gourmet!"
]
define inventory_type = {
    "armour": [
        "Without armour", "Aramid Suit", "Leather Armor", "Adaptive Suit",
        "Phantom Aegis Suit", "Elven Chainmail", "Combined Armor", "Adaptive armor",
        "Semi-perfect armor", "Iron Armor", "Obsidian Bulwark", "Gothic plate", "Mithril Mail"
    ],
    "weapon": [
        "Fist", "Baton", "Rapier", "Koncerz", "Whip", "Epee", "Gladius", "katana",
        "Blowgun Darts", "shuriken", "Buckler", "Adarga", "Huge mace", "Baseball Bat",
        "Gattle Prod", "Naginata"
    ],
    "weapon2": [
        "Fist", "Baton", "Rapier", "Koncerz", "Whip", "Epee", "Gladius", "katana",
        "Blowgun Darts", "shuriken", "Buckler", "Adarga", "Huge mace", "Baseball Bat",
        "Gattle Prod", "Naginata"
    ],
    "amulet": [
        "remove", "magic_protection", "physical_protection", "stamina_restore", "penetration",
        "Lucky", "speed"
    ],
    "ring": [
        "remove", "bleeding_ring", "stun_ring", "confusion_ring", "injured_ring", "sleep_ring", "pain_ring"
    ],
    "clothes": [
        "naked", "common_apron", "maid_dress", "nurse_dress", "leotard", "chainmail_bikini",
        "enchanter_robe", "sun_dress", "laced_underwear", "sailor_foku", "cocktail_dress",
        "rubber_dress", "ukata", "bellydance", "leather_corset", "rich_dress", "wedding_dress",
        "petsuit", "deprivation_suit", "cow_gear"
    ],
    "headgear": [
        "remove", "pony_plume", "plain_headband", "hijab", "crown_of_thorns", "plain_tiara", "hairnet",
        "glasses", "nekomimi", "incrusted_tiara", "exotic_wig"
    ],
    "neck": [
        "remove", "plain_pendant", "incrusted_necklace", "dog_collar", "leather_collar", "steel_collar",
        "spiked_collar", "shock_collar", "golden_collar"
    ],
    "hands": [
        "remove", "rubber_gloves", "laced_gloves", "leather_gloves", "plastic_bracers",
        "fluffy_gloves", "ponygirl_harness", "leather_straps"
    ],
    "feet": [
        "remove", "tabi", "fluffy_stepins", "pointes", "sneakers", "high_heels",
        "high_boots", "hoofed_boots", "leather_straps"
    ],
    "ring1": [
        "remove", "plain_ring", "incrusted_ring"
    ],
    "ring2": [
        "remove", "plain_ring", "incrusted_ring"
    ],
    "earrings": [
        "remove", "plain_earrings", "incrusted_earrings", "heavy_gauge_rings"
    ],
    "tongue": [
        "remove", "plain_earrings", "barbells", "heavy_gauge_rings"
    ],
    "nipples": [
        "remove", "plain_earrings", "barbells", "nipple_chain", "heavy_gauge_rings"
    ],
    "navel": [
        "remove", "plain_earrings", "barbells", "heavy_gauge_rings", "incrusted_earrings"
    ],
    "clitoris": [
        "remove", "plain_earrings", "barbells", "heavy_gauge_rings", "incrusted_earrings"
    ],
    "anus": [
        "remove", "anal_plug", "anal_tail"
    ]
}
define dic_inventory_move_up = {
    'clothes': 0,
    'headgear': 1,
    'neck': 2,
    'hands': 3,
    'feet': 4,
    'ring1': 5,
    'ring2': 6,
    'earrings': 7,
    'tongue': 8,
    'nipples': 9,
    'navel': 10,
    'clitoris': 11,
    'anus': 12
}
define dic_inventory_move_down = {
    0: 'clothes',
    1: 'headgear',
    2: 'neck',
    3: 'hands',
    4: 'feet',
    5: 'ring1',
    6: 'ring2',
    7: 'earrings',
    8: 'tongue',
    9: 'nipples',
    10: 'navel',
    11: 'clitoris',
    12: 'anus'
}
define dic_slave_aura_conditions = {
    "nocast": "  Without spells reinforcing auspex, the aura of your slave is seen as pale and indistinct shadow. You can not determine the color, strength or direction of her spiritual field.",
    "casted": "  Auspex allows you to distinguish between colors, direction and strength of the spiritual field of your slave. After analyzing them, you get detailed information."
}
define shared_families = {
        "prehistoric": ["tribe", "amazon"],
        "barbarian": ["amazon", "nomad", "pesant", "hunter", "fisher", "viking", "barbarian_king"],
        "sns": ["amazon", "nomad", "pesant", "hunter", "fisher", "viking", "barbarian_king"],
        "medieval": ["orphan", "bondman", "gypsy", "church", "craftsman", "merchant", "valetry", "knight", "mprincess"],
        "darkfantasy": ["orphan", "bondman", "gypsy", "church", "craftsman", "merchant", "valetry", "knight", "mprincess"],
        "highfantasy": ["orphan", "bondman", "gypsy", "church", "craftsman", "merchant", "valetry", "knight", "mprincess"],
        "steampunk": ["farmers", "workhouse", "proletarian", "clerk", "naturalist", "ingeneer", "doctor", "servant", "magnat", "bankeer", "mayor", "mafiosi"],
        "industrial": ["farmers", "workhouse", "proletarian", "clerk", "naturalist", "ingeneer", "doctor", "servant", "magnat", "bankeer", "mayor", "mafiosi"],
        "modern": ["orpnange", "worker", "policeman", "manager", "biologist", "programmer", "surgeon", "businessman", "finance", "general"],
        "cyberpunk": ["orpnange", "worker", "policeman", "manager", "biologist", "programmer", "surgeon", "businessman", "finance", "general", "gendesigner"],
        "utopia": ["poet", "artist", "architect", "operator"],
        "darkfuture": ["jailer", "bioreactor", "minitruth", "anter"],
        "space": ["freetrader", "astrofarm", "asteroid", "astrogator", "admiral", "nanofarmacist", "gendesigner"]
}

define worlds = {
    1: {
        "name": "prehistoric",
        "families": shared_families["prehistoric"],
        "descriptions": [
            "In my world, as far as the eye can see, wild forests stretch everywhere. Sweet air. Good hunting. You can go many days, but only trees will be around. There's a lot of prey, but the forests are inhabited by terrible beasts: saber-toothed tigers, cave bears and swamp lizards.",
            "In my country everything is covered with snow and ice, from horizon to horizon. People wrap themselves in the skins of large animals and make a fire in caves to keep warm. Often many days there is no food, but when the hunters manage to get the mammoth, the whole tribe rejoices and we all eat our fill.",
            "Where I was born there are a lot of trees with broad leaves and swamps over which gnats swarm. In the trees colorful birds flutter and at the bottom of the muddy river lurk huge crocodiles. We gather fruit and hunt in the jungle, using poisoned arrows."
        ]
    },
    2: {
        "name": "barbarian",
        "families": shared_families["barbarian"],
        "descriptions": [
            "In my homelands steppes stretches without end. There, a herd of mustangs cleaves the waves of golden feather grass, sky greener than emeralds and three beautiful moons shine brightly in the sky at night. People often at war, because the richer great leaders are, if the more loot they take in the war.",
            "In my country a lot of forests, rivers and hills. In the woods there are countless fur animals, and lakes teem with fish. In the hills and valleys - good pasture for sheep. Some people settle in cities, behind high walls, while others wander from place to place, driving huge herds.",
            "I was born on the seacoast, the waters of which are black, like the night. Wind incessantly sings in the fjords and the waves foam, breaking against the rocks. There are a lot of different people, and everyone has their own life. Some sail or fish, some tend the nomadic flocks, while the rest settle in the fortified cities."
        ]
    },
    3: {
        "name": "sns",
        "families": shared_families["sns"],
        "descriptions": [
            "In my world lives a lot of different nations, and they constantly fight for a place under the sun. Innumerable hordes of nomads besiege rich cities, surrounded by high walls. Wild tribes inhabit the forests and swamps, earning a living from caravans robbery. Great kings rule huge empires.",
            "My world is great and immense. I know that at the east lies the endless sea. The far south is inhabited by wild people with skin as black as the night itself. In the north is impenetrable forests in which live undersized, but evil tribes of hunters. Western steppes ruled by nomads who live with robbery, plundering the cities.",
            "In my world there are many different cultures and nations. There are kings whose treasuries are full of gold, black magicians, whose power is above that of kings, and fearless heroes who are not afraid of even magicians. But there was more, of course, an ordinary people - peasants, soldiers, artisans, and merchants."
        ]
    },
    4: {
        "name": "medieval",
        "families": shared_families["medieval"],
        "descriptions": [
            "My country has a very beautiful nature: a lot of forests, meadows, rivers and lakes. The mountains are covered with shiny snowcaps. All the lands are owned by the barons and knights, who serve to the king and collect tributes from peasants living near their castles. Ordinary people live a difficult life.",
            "In my world every man has his place and everyone knows what to do. Kings and barons ruled their lands, knights fight with enemies, artisans make pots and tools, farmers plow the land, and the priests are praying for all of them and help with good advice.",
            "My world is very big, so I do not know everything about it. People in cities live richly, but it is dirty, crowded, and smells bad. Barons and knights sit in their stone castles, or go on the military campaigns. And the peasants in the villages plow all year round to feed the nobles and themselves."
        ]
    },
    5: {
        "name": "darkfantasy",
        "families": shared_families["darkfantasy"],
        "descriptions": [
            "As I can remember, we always had a hard time. It is said that once upon a time, under the old empire, people live richly and happily. But now the forests are full of robbers and wild animals, barons cannot, or do not, want to maintain order in their lands, and the peasants under their oppression starve almost every winter.",
            "Life in my world is not easy. In the dark forests lurk terrible creatures that can ruin an entire village. Eastern necromancers raise an army of undead, and warlocks rule with western lands, whispering orders to kings. Of course there are heroes who fight back evil, but they are too few.",
            "The priests say that our world is dying, and the end is near. Dead arise from their graves and roam at night through abandoned ancient cities. Dragons burn down villages and devour cattle. The Black Death decimates children and the elderly. And each year is worse than the previous one."
        ]
    },
    6: {
        "name": "highfantasy",
        "families": shared_families["highfantasy"],
        "descriptions": [
            "My world is ruled by powerful archmages, who form the Great Conclave and decide the fate of mortals on it. But they do not interfere in ordinary life. Cities thrive, although, of course, wealth breeds corruption and theft. And sorcerers' experiments sometimes end with serious troubles.",
            "My world is arena of war between good and evil. Union of elves, humans, and dwarves from immemorial time opposes the machinations of King Necromancer who wants to enslave all the free land and populate them with his ugly slaves: goblins, trolls and dragons.",
            "Our world is very large. I know nothing about the lands beyond the seas, but in my homeland there were seven kingdoms. Now they are united into one great empire. It is said that in the north, behind the Great Wall, Ancient Evil is waiting in the wings. And when the Long Winter comes, the Evil will wake up and brings innumerable troubles to people of the Empire."
        ]
    },
    7: {
        "name": "steampunk",
        "families": shared_families["steampunk"],
        "descriptions": [
            "My world is ruled by science and technology. There are several advanced empires that are vying for influence in the underdeveloped but resource-rich, colonies. The advantage will go to the one with the most modern battleships, airships and steam engines.",
            "Science and technology is developed very high in my world. We use advanced steam engines for transport and industry. To plan production we use a powerful arithmometers. For transcontinental flights we have giant zeppelins.",
            "In my world there are a few advanced countries, where the industrial revolution was accomplished. Military and technological power is based on coal and steel. Villages are low on people, because youth are going to work to the cities. Sometimes it is impossible to breathe from factory soot, and the fish in the rivers suffocate due to toxic waste."
        ]
    },
    8: {
        "name": "industrial",
        "families": shared_families["industrial"],
        "descriptions": [
            "Although in my world there are many different states, everyone understands that the real power is in the hands of bankers and industrialists. Working people create trade unions and go on strike, but the government will not tolerate such disturbances and suppress them very severely. People are angry, many of them live in poverty and cannot find work.",
            "In my world there is a very big war, it is even called World War, because it involves almost all the states. Bombing, artillery shelling, gas attacks - all this has become habitually not only for the soldiers in the trenches but also for civilians. The food is not enough, everything is rationed.",
            "In my world a great war recently ended. It was so terrible that after settlement agreement all the countries of the world have united in the World League, to prevent its recurrence. Industry is gradually recovering, but still there is a lot of devastation. Sometimes even revolutions occur, regimes are changed."
        ]
    },
    9: {
        "name": "modern",
        "families": shared_families["modern"],
        "descriptions": [
            "In my world there are a lot of different countries, but only some of them are really well developed and rich. In the others reigns poverty and devastation, many of them ruled by dictators. These backward countries are hotbeds of terrorism and for the civilized countries sometimes it is necessary to use force.",
            "We have one country that is richer and more powerful than the others. But although everyone tries to be equal to it, there is now a severe crisis and because of that economy suffers all over the world. Unemployment growing, inflation rising. People all over the world go out to the demonstrations. In many countries civil wars have already started.",
            "Once in my world, there were two great Empires that fought each other for dominance in the world. But then one of them broke in pieces and now most of the world adopted a common value system. Most likely, over time, the border between the states will disappear and the world will be united."
        ]
    },
    10: {
        "name": "cyberpunk",
        "families": shared_families["cyberpunk"],
        "descriptions": [
            "My world is ruled by information. Global network connects the most remote corners of the planet. In the Web you can find everything: movies, music, games, and every sort of pornography. 95% of the population lives on allowances, barely enough for food. But as long as there is entertainment, there are no objections.",
            "My world is divided into States and Enclaves. Though more people live in the States, they are just the dying form of social organization. Enclaves are entirely owned by corporations and obey corporate laws. And it is Enclaves that own most of the wealth and technology.",
            "My world is ruled by multinational corporations. The state as a form of government does not exist, the laws are written by corporate management, and their one goal - profit. Those who have money can afford anything. And those who have not… there will always be a place in the shade of a society among scum and synthetic drugs."
        ]
    },
    11: {
        "name": "utopia",
        "families": shared_families["utopia"],
        "descriptions": [
            "In my world people have reached harmony with nature and forget forever about famine, wars, crimes, and diseases. A flexible system of governance involving all the adult population of the planet can quickly solve any problems and fairly distribute the resources.",
            "In our world science and technology have developed so far that there is no need for hard work and competition for resources. Laws are written by outstanding people of culture and only in the poetic form. In the upbringing of children special attention is paid to the development of the aesthetic sense.",
            "Thanks to social progress we have been able to arrange society so perfectly that we have eradicated the need for states, wars, police, and other instruments of violence. All people live in peace and prosperity. Every citizen should draw well and compose poems. Conflicts are settled only through negotiations."
        ]
    },
    12: {
        "name": "darkfuture",
        "families": shared_families["darkfuture"],
        "descriptions": [
            "In my world I come from the one true state. We live by the precepts of the Great Leader and are constantly fighting for freedom and brotherhood. The enemies are trying to break us and poison with their propaganda, but we know that only our people live happily and freely. All that is necessary is distributed equitably.",
            "In my world there are three states, but only in ours do people live organized and happily. Big Brother is always watching over us and helps not to go astray. Ministry of Truth explains all the unclear questions. Norms on human food are growing steadily, and the war is about to end with our unconditional victory.",
            "I live in a world of justice and equality. We all wear the same uniform, there is no difference between races and genders. Homes are the same, with transparent walls. We are governed by the Benefactor, which is always elected unanimously. Feelings are under strict medicinal control in order to avoid suffering."
        ]
    },
    13: {
        "name": "space",
        "families": shared_families["space"],
        "descriptions": [
            "The universe contains many inhabited worlds, and we can move freely between them thanks to the hyperdrive. Thousands of planets are united in the Galactic Republic, controlled by the Senate. Of course, each of the worlds has their own view of life, and conflicts are frequent. The threat of separatism is greater than ever.",
            "The universe is much bigger than any one world. Our planet has united into a global state and colonized many worlds. But the universe is infinite. We were exploring it, getting acquainted with alien civilizations, learning and developing.",
            "Under the shadow of the Golden Throne of the Eternal Emperor, the people's empire thrives in thousands of worlds. But the dangers are innumerable: xenos, heretics, nightmarish creatures of the Warp. Only thanks to the dedication of the Imperial Guard, Space Marines, Inquisition, and Ecclesiarchy we are still alive."
        ]
    }
}

default occupation = {
    "tribe": ["tribal_girl", "shaman"],
    "amazon": ["heroine", "shaman", "huntress"],
    "nomad": ["heroine", "shaman", "huntress"],
    "pesant": ["bride", "viking_wife", "witch", "herbalist"],
    "hunter": ["bride", "viking_wife", "heroine", "witch", "herbalist"],
    "fisher": ["bride", "viking_wife", "witch"],
    "viking": ["heroine", "viking_wife", "witch"],
    "barbarian_king": ["barbarian_princess"],
    "orphan": ["thief", "beggar", "whore", "markitane", "valertry", "heroine", "sorceress", "thug"],
    "bondman": ["poor_bride", "herbalist", "brigand", "markitane", "valertry", "sorceress", "nun"],
    "gypsy": ["thief", "gypsy", "whore", "markitane", "brigand", "heroine", "sorceress", "thug"],
    "church": ["beggar", "nun", "valertry", "nun", "nun"],
    "craftsman": ["poor_bride", "nun", "whore", "brothel", "thug", "valertry", "sorceress", "poor_bride"],
    "merchant": ["rich_bride", "nun", "sorceress", "rich_bride", "heroine"],
    "valetry": ["valertry", "nun", "markitane", "herbalist", "brigand", "valertry", "sorceress", "heroine"],
    "knight": ["noble_bride", "heroine", "sorceress", "brigand", "noble_bride", "heroine"],
    "mprincess": ["mprincess"],
    "farmers": ["farmer", "milker", "swiner", "poor_bride"],
    "workhouse": ["thief", "beggar", "whore", "weaver", "freaser", "thug", "sufragist", "maid", "maid"],
    "proletarian": ["thief", "beggar", "whore", "weaver", "freaser", "thug", "sufragist", "brothel", "maid", "maid"],
    "clerk": ["thief", "nun", "oficiant", "weaver", "freaser", "teacher", "sufragist", "nurse"],
    "naturalist": ["avanturiste", "sufragist", "teacher", "nurse"],
    "ingeneer": ["avanturiste", "nurse", "oficiant", "sufragist", "freaser", "teacher"],
    "doctor": ["avanturiste", "nurse", "oficiant", "sufragist", "freaser", "teacher"],
    "servant": ["thief", "beggar", "whore", "weaver", "freaser", "maid", "sufragist", "brothel", "maid"],
    "magnat": ["avanturiste", "rich_bride", "rich_bride", "sufragist"],
    "bankeer": ["avanturiste", "rich_bride", "rich_bride", "sufragist"],
    "mayor": ["avanturiste", "rich_bride", "rich_bride", "sufragist"],
    "mafiosi": ["avanturiste", "rich_bride", "rich_bride", "sufragist"],
    "orpnange": ["thief", "nurse", "punk", "oficiant", "secretary", "teacher", "voleyball", "karateka", "hymnast", "policewoman", "whore", "hacker", "brothel"],
    "worker": ["student", "nurse", "punk", "oficiant", "secretary", "teacher", "voleyball", "karateka", "hymnast", "policewoman", "hacker"],
    "policeman": ["student", "nurse", "punk", "oficiant", "secretary", "teacher", "voleyball", "karateka", "hymnast", "policewoman"],
    "manager": ["student", "nurse", "punk", "oficiant", "secretary", "teacher", "voleyball", "karateka", "hymnast", "policewoman", "model", "hacker", "writer"],
    "biologist": ["student", "nurse", "writer", "oficiant", "secretary", "teacher", "voleyball", "karateka", "hymnast", "hacker", "artist"],
    "programmer": ["student", "nurse", "punk", "oficiant", "secretary", "teacher", "voleyball", "karateka", "hymnast", "policewoman", "model", "hacker", "writer"],
    "surgeon": ["student", "nurse", "writer", "oficiant", "secretary", "teacher", "voleyball", "karateka", "hymnast", "hacker", "artist"],
    "businessman": ["major", "model", "writer", "artist"],
    "finance": ["major", "model", "writer", "artist"],
    "general": ["major", "model", "writer", "artist"],
    "poet": ["student", "hymnast", "writer", "artist"],
    "operator": ["student", "hymnast", "writer", "artist"],
    "artist": ["student", "hymnast", "writer", "artist"],
    "architect": ["student", "hymnast", "writer", "artist"],
    "jailer": ["mind_contol", "time_plice", "jailer", "anter"],
    "bioreactor": ["mind_contol", "time_plice", "jailer", "anter"],
    "minitruth": ["mind_contol", "time_plice", "jailer", "anter"],
    "anter": ["mind_contol", "time_plice", "jailer", "anter"],
    "freetrader": ["academy", "mech", "contraband"],
    "asteroid": ["time_plice", "academy", "mech", "astrofarmer", "installer", "contraband"],
    "astrofarm": ["time_plice", "academy", "mech", "astrofarmer", "installer", "contraband"],
    "astrogator": ["time_plice", "academy", "mech", "contraband"],
    "admiral": ["time_plice", "academy", "mech", "contraband"],
    "nanofarmacist": ["time_plice", "academy", "mech", "contraband"],
    "gendesigner": ["time_plice", "academy", "mech", "contraband"],
}
default family_description = {
    "tribe": "Our tribe roamed the lands of ancestors in search of a good hunting. If we find a good place, we built a hut or occupy a comfortable cave. Then, when the prey went, we walked behind it. Like the all little kids, I played in the woods, far away from the camps, gathering roots and berries.",
    "amazon": "In my tribe was not men. Our women take husbands for one month, and then killed them. If a boy is born he is thrown off a cliff, and if a girl - then from her we raised a hunter and warrior. Men were afraid of us like the plague; we were the strongest of all.",
    "nomad": "Our horde wandered across the steppe. During the day we went into the tent, driving behind a herd of horses and flocks of sheep, and on the night we camped in marquees. We danced around the fires, drank kumis and ate meat. Our warriors were the strongest, and the inhabitants of the cities were shaking from only our Khan's name. Everyone paid tribute to us.",
    "pesant": "My parents were an ordinary peasants. Father plowed field using a large plow, which he harness an ox, and mother spun yarn and prepared food. I helped babysit the younger children and carried lunch to the father and brothers in the cornfield. In the winter I was gathering firewood in the forest and playing with friends in a snowball fight.",
    "hunter": "My father was a hunter, and I do not remember my mother - she died when I was very young. Dad often brought to home rabbits and partridges, but sometimes it was a deer, wild boar, or even a bear. He traded skins and meat in the village to the necessary things, so we lived well.",
    "fisher": "My father and brother were fishing in the sea. My father had a durable boat and a large fishnet. If there were a lot of fish, then we traded it on the market for all sorts of necessary things. I helped my dad to repair the net, although it caused severe pain to fingers. I also had a little sister, but she drowned in the sea.",
    "viking": "My father was a brave and fearless warrior. Every year he went on a campaign for the sea, and jarl always put him at the helm of the largest drakkar. Ships brought to home a lot of gold and all sorts of interesting things. I herded sheep on the hills, and helped my mother make yarn from their wool.",
    "barbarian_king": "My father was a wise ruler and a brave warrior. He led his troops in the campaign and brought the booty, a lot of gold and slaves. I lived in the palace, where hundreds of servants was ready to fulfill any of my wishes at any moment.",
    "orphan": "I do not remember my parents, maybe they died when I was little, or maybe they left me in order to avoid feeding an extra mouth. Overall, my family became a homeless beggars and other waifs. Since childhood I had to learn to gather food and spend the night on the street.",
    "bondman": "I was born in a very ordinary family in a village not far from the castle of our lord. Father and brothers worked in the fields or in the woods, and I helped mother to spin yarn and grazed geese. With the other children we used to play tags and hide-and-seek at the forest edge.",
    "gypsy": "I was brought up by gypsies, in a traveling encampment that did not stay in one place for more than a few weeks. My life was pretty carefree, though hungry. Wearing whatever came to hand, I stole and begged for change, but I was free as the wind.",
    "church": "Since infancy, I became an orphan, but I was lucky to get into a church shelter. The monks taught us how to behave, help with the housework and to worship God. The most talented of us studied reading and writing. Of course, sometimes we were naughty, and because of that I was often flogged or locked in a cell.",
    "craftsman": "Since I can remember, I have lived in the city. My father had a pottery and a shop with it. My brothers kneaded clay, father molded pots, and I with my mother painted them in bright colors. Sometimes I was able to walk, although they rarely let me go beyond the city wall.",
    "merchant": "My father was a merchant and led caravans from distant countries. Me and my sisters often received different wonderful goodies, especially if he was leaving for a long time. We lived better than many of the townspeople, and of course better than the peasants in the villages.",
    "valetry": "My mother was a servant in the knight's castle, and I never knew my father. It is possible that even the old lord don't know him, though I do not remember him much too. From early childhood I was taught to help and serve, but I also had a lot of time for games.",
    "knight": "I grew up in the castle of my father, together with my sisters and brothers. However, my brothers left the castle as soon as they turned seven, to learn manners in the courts of other lords. My mother taught me with my sisters herself. Father was absent for a long time when he went on military campaigns.",
    "mprincess": "From childhood I was accustomed to luxury befitting a princess. Although I was the youngest daughter, I was the most beloved. Mom and dad doted on me and everyone in the castle executed my whims. Together with my sisters and the servants, we often played in the garden.",
    "farmers": "My family had a farm in about twenty acres. We cultivated corn, beans, and had a decent herd of cows. Since childhood I helped my parents on the farm, and in my spare time played with neighborhood children in the nearby forest.",
    "workhouse": "My parents died when I was young, and under the law of the homeless I was assigned to be raised in a workhouse. We lived like in prison, working from sunrise to sunset on the looms. If someone was not doing his share, he was flogged.",
    "proletarian": "I was born in a working class family. Father worked in a steel mill, and mother at a textile factory. They worked twelve hours per day and were very tired, so I had to keep the house and care for my sick grandmother.",
    "clerk": "My father worked as a clerk at the factory administration, and my mother ran the household at home and raised me with my brothers and sisters. I cannot say that we lived like the rich, but at least we had our own apartment and enough food.",
    "naturalist": "My father was a scientist and naturalist who studied wildlife and wrote on this topic thick boring books with strange pictures. He was interested in his children less than exotic animals, but my mother spent almost all her time with us. She was very kind and beautiful.",
    "ingeneer": "I was born in the family of an engineer. Father maintained and repaired boilers and other units of the nearest factory. This work is very important, because without machines all the factory will stop working.",
    "doctor": "My father was a famous doctor and he treated rich people: industrialists, bankers, scientists. Everyone loved and respected him, and in our house there were always a lot of guests, and we arranged poetry readings. I had a lot of beautiful dolls and outfits.",
    "servant": "My parents served in the estate of a wealthy industrialist. My father was a senior butler, and my mother was in charge of the kitchen. Our host was a pretty good person, but I almost never communicated with him. On the other hand we played and were friends with his children.",
    "magnat": "I was born in a good family. My grandfather owned several factories, and my father worked on the board of directors. Mom mostly stayed at home and worked on our upbringing: I had brothers and sisters. And, of course, our house was full of servants who perform different jobs.",
    "bankeer": "My family has long been involved in banking, so I was born in a very wealthy family. My father always said that the world moves around money and money itself moves around him. We had a big beautiful house and many servants: chauffeur, gardener, cook and maids.",
    "mayor": "My father - is a very powerful man. He held the post as mayor of a big city and there is nothing that happens without his permission. Our house always had many guests, very serious people: rulers of urban services, bankers and industrialists. Honestly, they were all veeeery boring.",
    "mafiosi": "My dad was one of the dons in a very influential family. Politicians, trade unions, banks - all of them he held in his hand. We had a large and rich house, which was always guarded by armed men. Mom often went to theaters and shops, and because of that I was brought up by a wet nurse and tutors.",
    "orpnange": "I grew up in an orphanage without parents. I do not know who they were. We were brought up quite strictly, and children do not stand on ceremony with each other. Toys were not enough, but we found ways to entertain ourselves on our own.",
    "worker": "My father worked as an engineer at an engineering plant. He always came home tired and angry, drank beer and watched TV. I think he doesn't care about me, but my mother always has a kind word for me. I attended a school and played with other children.",
    "policeman": "My dad is a district police officer, and mom a school teacher. We lived not too rich but not worse than others. But there always were girls in the school who had more chic outfits and expensive toys. I also wanted that, but my parents bought for me only stupid dolls.",
    "manager": "Mom and dad both worked very hard in the office, so they had little time for me. I was raised by my grandmother. She was very kind, and she knew a lot of fairy tales and interesting stories and always helped to do my homework. I walked a lot and played with the other girls in the neighborhood.",
    "biologist": "I grew up in an intellectual family. Father taught microbiology at the university, and mother was a research fellow at the institute. We rarely spent time together, but my parents worked hard so that I could get into a good school, and I was determined in all sorts of creative development circles.",
    "programmer": "My father worked with computers, something associated with distributed computing environments. I do not know exactly, but they paid him very well. Enough so that my mother did not have to work and could take care of the household. I had two brothers and an older sister.",
    "surgeon": "My dad owned a small private clinic and specialized in plastic surgery. There he met my mother. Since I can remember, she has always been obsessed with beauty. And from childhood I was forced to wear dental braces and use a whole bunch of medical cosmetics.",
    "businessman": "I grew up in a fairly wealthy family. Father owned an office in wholesale trade of spare parts, and my mother was a homemaker. And we also had a housekeeper. They taught me at home, because my dad did not trust the quality of general education: he said that is for rednecks and beggars.",
    "finance": "My father was a tough stockbroker, and mother an artist in the theater. However, when I grew up, she no longer worked. Dad spent little time at home. Mom suspected him of infidelity and drank a lot. She was addicted to painkillers. Sometimes she got angry at me, so I also did not like to sit at home.",
    "general": "My father was a general, and he kept strict order in the family. I think he wanted me to be a boy, then he could force me to march and do other stupid things. Although we were financially independent, I was jealous of other children who don't have such harsh rules at home.",
    "poet": "My parents had a unique sense of language. My mother was a structural linguist, and my father was a poet, and besides very famous. We had a rule in the house that it was permitted to talk only in verse and they taught me to do so as soon as I began to speak.",
    "artist": "My mother was a great artist. Her talent is recognized all over the world. She, of course, gladly shared her secrets with young artists and declaimed a course of color expression at the open university. I inherited a love of drawing from her.",
    "architect": "My parents were architects and always worked only as a pair. In our world, architecture is very important, because it is necessary not only to make the houses functional, but also to perfectly fit them into the urban landscape, at the same time giving the building an unique aesthetic value.",
    "operator": "My mother worked as a production operator in the polar replication center. I did not have a father, and the far north is not the best place for a child. Therefore, I was brought up in a public childcare center, and I came to visit mother only on weekends.",
    "jailer": "I was born and grew up in a giant prison complex. My father worked there as a security guard, and according to the law housing was provided to citizens in the workplace. Our free state has a lot of domestic enemies, and because of that it needs big prisons.",
    "bioreactor": "I grew up in an underground complex where my parents worked. They maintained the bioreactor that turns enemies and other dregs of society into a valuable fertilizer. Is this not a clear demonstration of the wisdom of our great Leader and his concern for the people's welfare?",
    "minitruth": "My parents held important positions in the Ministry of Truth, so we had much better rations than the simple proles. Kind but strict teachers instilled in me an understanding of the Grand Design, so that I also could instruct the proles when I grow up.",
    "anter": "My childhood was the most common. In the school-anthill, we were trained from our youngest years in labor practices and doing our civic duty, working for the good of our great country. In my sub-group there were twenty girls, and I was one of the best.",
    "freetrader": "In my childhood I have seen many planets but only from space. Like all children of free traders, my sisters and I were brought up directly on the ships, where we had all the conditions needed for a comfortable life. Space for games was always limited, so we had fun in virtual reality.",
    "astrofarm": "My parents owned a large astrofarm orbiting an industrial colony. We had decent incomes, and I could play among the greenery and not in the polluted atmosphere of the planet. I studied with hypnofilms. And, of course, I helped my parents on the farm.",
    "asteroid": "I grew up on a space drilling station in the belly of an asteroid that was rich with ilmenite ore. My parents had no money to send me to study on the planet. There were few other children on the asteroid and even less places for games. In general, it was boring.",
    "astrogator": "I grew up with my mother and saw my father very rarely. He worked as astronavigator on a hyperspace transporter. However, he contacted us at every opportunity to communicate and even told me bedtime stories by videophone. He was very clever and kind.",
    "admiral": "I grew up in an officer's family. My father was a starfleet captain, and my grandfather was an admiral. The fleet of all sectors was subordinated to my grandfather. I was brought up in his house on the planet, because my dad was always in deep space. I received my education in the best private school.",
    "nanofarmacist": "I grew up on a giant orbital station, where my parents worked. They were nanopharmacologists and developed new symbidrugs for the military. They did not trust hypnocourses and taught me themselves. I always dreamed of living on a planet with more children.",
    "gendesigner": "My mom raised me by herself alone. I do not even know who my father was. Given who was my mother, maybe there was no father at all. My mother is a famous genetic designer. She creates unique bio-forms for rich people's entertainment.",
}
default occupation_description = {
    "tribal_girl": "When I grew up, I began along with other women taking care of the maintenance of fire: big trouble for the entire tribe, if the fire goes out. Many young hunters wanted to take me for a wife, but my brother was very jealous and would not let me any. He loved to kiss me himself.",
    "shaman": "Since childhood, I was able to listen the wind, animals, birds and trees, so when I grew up, I became a shaman student. This is a very honorable occupation. Everyone bring gifts to shaman, so that he appeases the spirits before the hunt, heals wounds from the clutches of a ferocious beast and asks a wise advice from ancestors.",
    "heroine": "Natural enemies attacked my family and killed all; they left alive only me, thinking that I was not dangerous. But I vowed revenge. I grew up as a strong and fearless warrior. I experienced many adventures, but damn Fogs took me before I fulfilled my vow.",
    "huntress": "Wild forest became my home - I knew every tree, every leaf, every blade of grass there. I hunted for any prey, whether partridge, wild boar or elk. Many men want to take me as their wife, but I refused to all of them. What they could give to me?",
    "bride": "Parents really wanted to pick up a good husband for me. I had a not very big dowry, so it was difficult to marry a rich husband. And I did not like all of them. There was a guy with whom we were kissing in the moonlight, but the parents did not want to give me for him. And then I got into the Fogs.",
    "viking_wife": "When I was fourteen years old, I got married to a brave sea dog. He was gentle with me and brought different rarities from overseas. But we rarely saw each other, because my husband devote more time to the seas and distant shores than me.",
    "witch": "My parents died early, and I went to live with my grandmother in the forest lodge. My grandmother was a sorceress. From all the surrounding villages people went to her to bewitch a loved one or to cure illness. My grandmother taught me the herbs and spells, how to talk to spirits and brew potions.",
    "herbalist": "Since my childhood I was able to recognize, collect and dry all sorts of herbs. Sometimes people even came from the big cities, in order to get desired collection or decoction from me. I've wandered through the forests, meadows and hills, and loved solitude. People are poorly understand me and tried to avoid me.",
    "barbarian_princess": "Dad always wanted me to marry, but I did not like any of my bridegrooms. And although he was very angry, I always knew how to calm him down. Daddy loved me. Maybe he is not so wanted to give me in marriage to another kingdom, despite the fact that such an alliance would promise a great benefit.",
    "thief": "I survived on my own. My nimble fingers helped me lift wallets from gawkers. That's how I lived — until the cursed Fogs got me.",
    "beggar": "There was no honest work and I refused to steal or sell myself, so I begged. It was barely enough to survive, and everyone took their cut. I don't know how long I could have lasted.",
    "gypsy": "I learned to sing, dance, juggle, and read fortunes. People paid for my talents, and though life in the camp was rough, it was also free. We just roamed and sang songs.",
    "whore": "I had no choice but to sell my body to survive. The clients were poor, the pimp was cruel — but I endured. I even dreamed of saving up to start over.",
    "markitane": "I followed the army, sharing beds with soldiers in exchange for bread or wine. After battles, I scavenged and helped the wounded. It wasn't a noble life, but it was mine.",
    "brothel": "I ended up working at the city's biggest brothel. Warm, safe, with food and a roof — better than the streets. The madam took care of us, so I didn't complain.",
    "nun": "The world's pain was too heavy. I withdrew to a convent, devoting myself to God. Strict rules, yes, but peace for both the body and the soul.",
    "valertry": "I worked as a servant at a castle, washing and cleaning. One day, while rinsing clothes by the river, I wandered into the thickening Fog… and was lost.",
    "sorceress": "I served a famous sorceress in exchange for magical training. I cleaned, obeyed, and endured, for I longed to wield the power she promised.",
    "thug": "I beat up boys as a kid, and I didn't stop as an adult. I joined a street gang and helped control entire quarters. The guards couldn't touch us.",
    "poor_bride": "Father picked out suitors for me. One I liked. If the Fog hadn't taken me while foraging for mushrooms, I'd have married him and had children by now.",
    "poor_wife": "Father found me a husband. He wasn't a treasure, but I was faithful. I kept the house, endured my mother-in-law, and was loved. That was life.",
    "brigand": "I was stronger than most men, and times were hard. I joined a forest band, robbing travelers — but never killing. Locals helped us, and we helped them.",
    "noble_bride": "I was betrothed to a lord's son since I was twelve. The wedding was near when the Fog took me. I'd be his wife now, if not for that.",
    "noble_wife": "With wealth and status came endless suitors. I married at eighteen. My husband was older and often away at war, so I ran the estate myself.",
    "mprincess": "Father wanted to marry me off to some nasty foreign noble. I demanded he solve three riddles first. No one succeeded — so I stayed free.",
    "farmer": "I worked on a cotton plantation. It was hot, hard work, but decent pay. Machines can't pick cotton like women can.",
    "milker": "I loved cows since I was a girl, so I became a milkmaid. The job was easy, life was simple… until the Fog took me.",
    "swiner": "I worked as a swineherd on a big farm. Pigs are smart and valuable. I liked the stability. I'd still be there if not for the Fog.",
    "weaver": "I got a job in a weaving factory. Grueling shifts, poor pay, no breaks — but it was honest work. No time for daydreaming.",
    "freaser": "The Army needed tanks, so even kids like me worked. I mastered a milling machine and became one of the best. No resort, just duty.",
    "maid": "I served in a wealthy household — with gardeners, chefs, and chauffeurs. The butler mentored me kindly. I learned a lot there.",
    "sufragist": "We worked in factories, but had no rights. I joined the struggle for equality and helped organize mass rallies. We made a difference.",
    "nurse": "I finished medical school and became a nurse. It wasn't easy, but it mattered. I could help people when they needed it most.",
    "teacher": "I taught young children at school. They were a handful, but I loved teaching. It felt like a calling, not just a job.",
    "oficiant": "I waited tables while studying. Tips were good, though shared unfairly. Still, it paid rent. That's how things were.",
    "avanturiste": "I mingled with the rich and powerful. Seduction, forgery, blackmail — all part of the game. A girl's got to make a living somehow.",
    "rich_bride": "Many men wanted to marry me for my family's wealth. I loved the butler. We planned to elope… but the Fog took me first.",
    "rich_wife": "My family chose a husband for me. He was fat, ugly, and unfaithful. But I didn't hold back either. Let him choke on his riches!",
    "punk": "Society? One big cesspool. I hated conformity. I dyed my hair wild colors, blasted metal, and partied in graveyards with friends. It was chaotic. It was freedom.",
    "student": "I worked hard to get into a prestigious university — it took two tries, but I made it. I studied with distinction, despite the stress nearly breaking me.",
    "secretary": "I became a secretary at a small office — just enough to afford a tiny apartment. I had dreams of rising higher, but life didn't wait.",
    "voleyball": "I was always athletic, and volleyball became my passion. I won junior tournaments and set my sights on going pro. The court was my world.",
    "karateka": "People said girls shouldn't fight — I proved them wrong. Kickboxing, medals, underground fights. Not sport, but blood and grit. I earned respect.",
    "hymnast": "I was a graceful gymnast from a young age, but never won big titles. When I aged out of competition, I decided to become a coach instead.",
    "policewoman": "Crime was rampant, and I couldn't sit idle. I joined the police academy to protect the innocent and serve justice — no matter the danger.",
    "model": "I had the perfect body for the catwalk. Modeling was exhausting, but glamorous too — fast cars, designer clothes, wild parties… and no regrets.",
    "hacker": "In a world ruled by machines, I learned to rule them. I hacked terminals before I was even legal — dodging trouble because I was still a minor.",
    "writer": "Writing was my gift. Poems, stories, and praise followed. I even got published. But the masterpiece I started — I never got to finish it.",
    "major": "Teen drama gave way to wild nights and street races. I was a party queen, wrecking luxury cars for thrills. It was a hell of a ride.",
    "artist": "Art consumed me from childhood. I painted passionately, showed my work, but always felt my style wasn't complete. I dreamed of starting an artistic revolution.",
    "mind_contol": "Ordinary crimes are easy to spot — but thoughts? They're the real danger. I joined the thought-police to protect our society from traitors within.",
    "time_plice": "Time travel exists, but it's forbidden. Crsiminals exploit it to change history. I joined the time-police to hunt them down before they succeeded.",
    "jailer": "Prisons aren't efficient, but our enemies are many. I worked in a high-security facility, watching over the condemned, awaiting their final sentence.",
    "anter": "At legal age, I proudly joined a weapons factory. Fourteen-hour days, personal beds, and Leaders who care. A life of purpose and production.",
    "academy": "I dreamed of the stars and joined Starfleet Academy. I studied everything — from hyperspace physics to zero-G tactics. I was ready for the cosmos.",
    "mech": "I had sharp reflexes and a craving for adrenaline, so I trained to pilot battle mechs. It was risky, intense — and the real fights never came.",
    "contraband": "I got lucky and scored a fast little ship. Smuggling through deep space was risky but profitable. I stayed ahead of the law… barely.",
    "astrofarmer": "I ran a space farm. Just a handful of people and machines keeping everything alive. Quiet, isolated, with the same faces every day. Lonely, but steady.",
    "installer": "With few options, I joined a space rigging crew. Heavy exosuits, zero-G welding — rough work, but it suited me. It felt real."
}
define dic_girl_equipment_neck_mod = {
    "Chain with Pendant": {
        "desc": "A chain from precious metal with a shaped pendant perfectly accentuates the style and elegance of your slave.",
        "icon": "scene/item/item_plain_pendant",
        "price": 5,
        "escape": True,
    },
    "Gemstone Necklace": {
        "desc": "Figured necklace, studded with beautiful gems.",
        "icon": "scene/item/item_incrusted_necklace",
        "price": 10,
        "escape": True,
    },
    "Collar and Leash": {
        "desc": "Provided with a leash, it is immediately obvious that this is not made for humans, but for a pet. Helps set up a slave in the right mood, but it's easy to remove. This collar is not meant to remind your slave of her fate, as it is obviously a pet collar, not a slave collar.",
        "icon": "scene/item/item_dog_collar",
        "price": 5,
        "escape": True,
    },
    "Leather Collar": {
        "desc": "Wide leather collar with studs and rings for attaching a leash and shackles. Wearing one of these, your slave will never forget about her fate. Not to mention the fact that it's just very practical for many games. It is equipped with your name token to get her back in case of loss.",
        "icon": "scene/item/item_leather_collar",
        "price": 3,
        "escape": False,
    },
    "Steel Collar": {
        "desc": "Durable steel collar - heavy reminder of the fate of the slave from which it is impossible to escape. Wearing a steel collar is not a pleasant experience - it rubs the neck and grazes the skin. Not to mention the impact on the pride and conceit. It is engraved with your name and address to get her back in case of loss.",
        "icon": "scene/item/item_steel_collar",
        "price": 10,
        "escape": False,
    },
    "Spiked Collar": {
        "desc": "Brutal form of a collar decorated with long and sharp steel spikes. It not only reminds the slave of her status, but also makes her feel more aggressive. Good accessory for a gladiatrix, and indeed for any temperamental bitch. It is equipped with your name token to get her back in case of loss.",
        "icon": "scene/item/item_spiked_collar",
        "price": 10,
        "escape": False,
    },
    "Shock Collar": {
        "desc": "A technogenic shock collar. Serpis developed these to discipline cloned soldiers and reached an agreement with the Guild of Trainers for non-military use. It not only reminds a slave of her status but continuously monitors mental patterns during speech and applies an effect similar to Cruciato when it senses an attitude lacking in humility. It is equipped with your name token in case of loss.",
        "icon": "scene/item/item_shock_collar",
        "price": 25,
        "escape": False,
    },
    "Ornamented Collar": {
        "desc": "A luxurious wide and golden collar. It is adorned with exotic jewels and equipped with your name token to get her back in case of loss. Multiple rings allow for attaching leash and shackles. This stylish accessory will make sure that the slave will not forget that you are her master and she has to obey.",
        "icon": "scene/item/item_golden_collar",
        "price": 20,
        "escape": False,
    },
}
define dic_slave_moodlevel = {
    0:  "{color=#cd0000}Depressed{/color}",
    1:  "{color=#be0000}Dysphoric{/color}",
    2:  "{color=#af0000}Sullen{/color}",
    3:  "{color=#a00000}Melancholic{/color}",
    4:  "{color=#910000}Pessimistic{/color}",
    5:  "{color=#0D0D0D}Calm{/color}",
    6:  "{color=#EA0090}Hopeful{/color}",
    7:  "{color=#6B0084}Optimistic{/color}",
    8:  "{color=#0000D8}Pleased{/color}",
    9:  "{color=#009FEF}Euphoric{/color}",
    10: "{color=#009900}Ecstatic{/color}",
    11: "{color=#009900}Ecstatic+{/color}"
}

# I know is part is a bullshit, but it works
define dic_slave_moodlevel_no_color = {
    "{color=#cd0000}Depressed{/color}": "Depressed",
    "Depressed": "Depressed",
    "{color=#be0000}Dysphoric{/color}": "Dysphoric",
    "Dysphoric": "Dysphoric",
    "{color=#af0000}Sullen{/color}": "Sullen",
    "Sullen": "Sullen",
    "{color=#a00000}Melancholic{/color}": "Melancholic",
    "Melancholic": "Melancholic",
    "{color=#910000}Pessimistic{/color}": "Pessimistic",
    "Pessimistic": "Pessimistic",
    "{color=#0D0D0D}Calm{/color}": "Calm",
    "Calm": "Calm",
    "{color=#EA0090}Hopeful{/color}": "Hopeful",
    "Hopeful": "Hopeful",
    "{color=#6B0084}Optimistic{/color}": "Optimistic",
    "Optimistic": "Optimistic",
    "{color=#0000D8}Pleased{/color}": "Pleased",
    "Pleased": "Pleased",
    "{color=#009FEF}Euphoric{/color}": "Euphoric",
    "Euphoric": "Euphoric",
    "{color=#009900}Ecstatic{/color}": "Ecstatic",
    "Ecstatic": "Ecstatic",
    "{color=#009900}Ecstatic+{/color}": "Ecstatic+",
    "Ecstatic+": "Ecstatic+"
}
define dic_slave_moodlevel2 = {
    "Depressed": "{color=#cd0000}Depressed{/color}",
    "{color=#cd0000}Depressed{/color}": "{color=#cd0000}Depressed{/color}",
    "Dysphoric": "{color=#be0000}Dysphoric{/color}",
    "{color=#be0000}Dysphoric{/color}": "{color=#be0000}Dysphoric{/color}",
    "Sullen": "{color=#af0000}Sullen{/color}",
    "{color=#af0000}Sullen{/color}": "{color=#af0000}Sullen{/color}",
    "Melancholic": "{color=#a00000}Melancholic{/color}",
    "{color=#a00000}Melancholic{/color}": "{color=#a00000}Melancholic{/color}",
    "Pessimistic": "{color=#910000}Pessimistic{/color}",
    "{color=#910000}Pessimistic{/color}": "{color=#910000}Pessimistic{/color}",
    "Calm": "{color=#0D0D0D}Calm{/color}",
    "{color=#0D0D0D}Calm{/color}": "{color=#0D0D0D}Calm{/color}",
    "Hopeful": "{color=#EA0090}Hopeful{/color}",
    "{color=#EA0090}Hopeful{/color}": "{color=#EA0090}Hopeful{/color}",
    "Optimistic": "{color=#6B0084}Optimistic{/color}",
    "{color=#6B0084}Optimistic{/color}": "{color=#6B0084}Optimistic{/color}",
    "Pleased": "{color=#0000D8}Pleased{/color}",
    "{color=#0000D8}Pleased{/color}": "{color=#0000D8}Pleased{/color}",
    "Euphoric": "{color=#009FEF}Euphoric{/color}",
    "{color=#009FEF}Euphoric{/color}": "{color=#009FEF}Euphoric{/color}",
    "Ecstatic": "{color=#009900}Ecstatic{/color}",
    "{color=#009900}Ecstatic{/color}": "{color=#009900}Ecstatic{/color}",
    "Ecstatic+": "{color=#009900}Ecstatic+{/color}",
    "{color=#009900}Ecstatic+{/color}": "{color=#009900}Ecstatic+{/color}"
}
define dic_idle = [
    "sits at the window, leaning her elbows on the sill and looking at the street. Either she counts crows, or stares at passers-by. Perhaps she is bored, but it's still better than many of the lessons that you could burden her with.",
    "aimlessly wanders around the house, examining different parts of the interior. Perhaps she is bored, but it's still better than many of the lessons that you could burden her with.",
    "lays down to rest and spends her leisure time in blissful slumber. Perhaps she is bored, but it's still better than many of the lessons that you could burden her with.",
    "spends her free time immersed in her own feelings, whispering something under her breath. Perhaps she is bored, but it's still better than many of the lessons that you could burden her with.",
    "spends her free time quietly humming a song of her distant homeland. Perhaps she is bored, but it's still better than many of the lessons that you could burden her with."
]
define dic_maid = [
    "[all_girls_list[girl_index]['name']] has spent an hour doing the housework but did not achieve any success. She only aggravated the existing mess: raised dust, put things in piles, and could not even wash the clothes or make the bed.",
    "[all_girls_list[girl_index]['name']] spent too much time on cleaning, especially when you consider her modest results. The room became a little tidier, but the order is not perfect, and some things remained unmade and unfinished.",
    "[all_girls_list[girl_index]['name']] conscientiously collected the dirty clothes and washed them, washed the dishes, swept the floor, and made the bed. Your premises have become noticeably cleaner, although the order is still not ideal.",
    "[all_girls_list[girl_index]['name']] washed all the dishes, washed clothes and hung them out to dry, washed the floor, made the bed and wiped all dusty surfaces. You must admit that the work is done quite efficiently and quickly.",
    "[all_girls_list[girl_index]['name']] restored order quickly and competently. She washed up all the dishes, washed and hung clothes out to dry, washed the floor, made the bed and wiped down all dusty surfaces.",
    "Like a typhoon with a broom, [all_girls_list[girl_index]['name']] sweeps through the house, leaving a trail of order and cleanliness. Only half an hour's work - and all the rooms of the house shine with pristine purity. She leaves nothing left undone! Spotless!"
]
define dic_bath_master = [
    "  In your bath you relax and enjoy the warm waters. Sweat, tears, vaginal secretions, and worse – all just part of a slave master’s life. It’s an endless, glamorless, thankless job that’s gotta be done, but ahh, there’ nothing like washing off a hard day at work. Cleanliness – It’s the guarantee of health!",
    "  [all_girls_list[girl_index]['name']] helps you to relax and freshen up before bedtime. She carefully and gently cleanses your whole body, then wipes you dry with a soft towel and delivers the bathrobe and slippers.",
    "  [all_girls_list[girl_index]['name']] helps you to relax and freshen up before bedtime. She carefully and gently cleanses your whole body, then wipes you dry with a soft towel and delivers the bathrobe and slippers.",
    "  [all_girls_list[girl_index]['name']] takes away your slave to the bathroom and cleans her well with soap and sponge."
]
define bathing_slave_alone = {
    "arrogant": "  Eying you with a disdainful look and strictly demanding that you not spy on her, [all_girls_list[girl_index]['name']] proceeds to the bathroom and indulges herself with water procedures. Of course, you unceremoniously drop in to make sure she is cleaning up carefully and understands who sets the rules here.",
    "broken": "  With a completely indifferent face [all_girls_list[girl_index]['name']] proceeds to the bathroom, turns the water on and begins to methodically lather and bathe, like some retarded machine. She does not pay attention to you watching her. The whole process takes less than ten minutes.",
    "depresive": "  [all_girls_list[girl_index]['name']] dejectedly goes to the bathroom and begins to wash. It seems that this procedure is not interesting for her: she is thinking about something else and sighs often. You have to hurry her not to waste time in vain.",
    "docile": "  Following your instructions to keep herself clean, [all_girls_list[girl_index]['name']] goes to wash. You follow her to watch the process and demand she scrub herself inside as well as out to increase the sense of humiliation. [all_girls_list[girl_index]['name']] does not dare to contradict you, though she obviously feels uncomfortable.",
    "frightened": "  [all_girls_list[girl_index]['name']] slips quietly into the bathroom and turns on the water. Even in warm water, she does not relax for a second, looking at the unclosed door all the time.",
    "hateful": "  [all_girls_list[girl_index]['name']] goes into the bathroom and starts to rub herself with the washcloth so furiously, as if it would help her wash away your touch. When you look inside to watch the process, she hurls a bar of soap with anger at you and then gets a well-deserved slap for bad behavior.",
    "horny": "  [all_girls_list[girl_index]['name']] goes to the bathroom but stops at the door, asking you whether you wish to join her. Having been refused she sighs and turns on the water. Judging by the time spent on the procedure, she had not only thoroughly cleaned up but also played with herself using the warm water jets.",
    "hysteric": "  [all_girls_list[girl_index]['name']] runs into the bathroom and slams the door loudly behind her. You go in to strictly warn her to behave and to be careful not to splash water everywhere. The slave deliberately ignores your words but cleans herself nevertheless. After finishing the procedure, she slyly shows you her tongue.",
    "lachrymose": "  [all_girls_list[girl_index]['name']] goes into the bathroom and remains there for a suspiciously long time. When you go in to check on her, you find her crying, sitting on a wet floor in an embrace with a washcloth. You shout at her to continue bathing and not waste time on foolishness.",
    "obedient": "  [all_girls_list[girl_index]['name']] goes to the bathroom, leaving the door open so you can sit back and watch. She washes herself very carefully but does not spend so much time as to cause you displeasure.",
    "optimistic": "  With a satisfied smile [all_girls_list[girl_index]['name']] proceeds to the bathroom. Looking in on her, she is obviously pleased to thoroughly wash and relax in warm water.",
    "reluctant": "  [all_girls_list[girl_index]['name']] looks at you suspiciously and goes to the bathroom. Apparently, she fears that someone will peep on her, which very possible, given that the door is not locked. Despite the discomfort, your slave washes carefully and with obvious pleasure.",
    "resistant": "  [all_girls_list[girl_index]['name']] looks long and carefully at you, as if assessing whether she should wash if it is necessary not only for her but also for you. In the end, she still decides that being clean is more important than being persistent and proceeds to the bathroom.",
    "servile": "  [all_girls_list[girl_index]['name']] goes to the bathroom, leaving the door open so you can sit back and watch. She washes herself very carefully, clearly trying to give you maximum viewing pleasure.",
    "soft": "  [all_girls_list[girl_index]['name']] is obviously pleased to be able to wash off the dirt and soak in warm water. You hear her humming softly, and you peer in at her."
}

define dic_specializations = {
    "Servant": ["maid", "cooking"],
    "Assistant": ["secretary", "elocution"],
    "Witch Doctor": ["nursing", "alchemy", "witchcraft"],
    "Gladiatrix": ["gladiatrix", "athletics", "nature", "temperament"],
    "Artist": ["dance", "music", "painting"],
    "Pet Ponygirl": ["pet", "pony"],
    "Cow": ["cow"],
    "Concubine":["sex"]
}

define dic_girl_rules_broken_explain = {
    "act_as_cook": " [all_girls_list[girl_index]['name']] refuses to prepare meals for you.",
    "act_as_maid": " [all_girls_list[girl_index]['name']] refuses to clean the house.",
    "bath_slave": " [all_girls_list[girl_index]['name']] refuses to bathe you.",
    "behave_alarm": " [all_girls_list[girl_index]['name']] does not come to your room to provide your morning blowjob.",
    "behave_humility": " [all_girls_list[girl_index]['name']] refuses to call you 'Master'.",
    "behave_pet": " [all_girls_list[girl_index]['name']] refuses to behave like a pet.",
    "behave_silence": " [all_girls_list[girl_index]['name']] speaks as if she was allowed to.",
    "behave_toilet":" [all_girls_list[girl_index]['name']] refuses to take your shit. Using a special toilet seat could solve the problem.",
    "behave_urinal": " [all_girls_list[girl_index]['name']] refuses to take your urine. Tying her with a urinal rack could solve the problem.",
    "deny_orgasm":" [all_girls_list[girl_index]['name']] WIP.",
    "deny_toileting":" [all_girls_list[girl_index]['name']] uses the toilet as if it was allowed. You recall one of the slaver maxims: an anal pear each day keeps the shitting at bay.",
    "milk_the_fiend":" [all_girls_list[girl_index]['name']] refuses to milk the fiend.",
    "no_masturbation":" [all_girls_list[girl_index]['name']] WIP.",
    "use_vaginal_beads":" [all_girls_list[girl_index]['name']] refuses to use the vaginal beads."
}
define dic_girl_rules_special_text = {
    "behave_alarm":{
        "assistant_pass":" [all_girls_list[girl_index]['name']] does not want to provide your morning blowjob, so your assistant forces her.",
        "assistant_fail":" [all_girls_list[girl_index]['name']] Your assistant lacks the strength and fighting skill to compel her.",
        "poor_job"      :" Though she tried, she could not make you cum. Disgust, distress and guilt is visible on her face.",
        "disgust"       :" Disgust and distress is visible on her face.",
        "good_job"      :" You leave her with a mouthful of cum and a satisfied smile on her face.",
        "not_enough_excitement":" Though she tried diligently, she could not get you hard. She looks guilty.",
        "almost_enough_excitement":" Though she tried diligently, she could not make you cum. She looks guilty."
    },
    "behave_humility":{
        "force_rule":" [all_girls_list[girl_index]['name']] calls you 'Master' as her collar inexorably enforces.",
        "poor_job":" [all_girls_list[girl_index]['name']]  But she is clearly too willful or proud to enjoy it",
        "good_job":" [all_girls_list[girl_index]['name']]  And she seems to derive some satisfaction from it."
    },
    "behave_pet":{
        "force_rule":" [all_girls_list[girl_index]['name']] cannot break out of her pet suit, maintaining her on all fours all day long.",
        "poor_job":" [all_girls_list[girl_index]['name']]  She seems to resent this.",
        "good_job":" [all_girls_list[girl_index]['name']]  She seems to enjoy it."
    },
    "behave_silence":{
        "force_rule":" [all_girls_list[girl_index]['name']] regularly moans behind her gag.",
        "poor_job":" [all_girls_list[girl_index]['name']] She is clearly unhappy with this suppression of her temperament.",
        "good_job":" [all_girls_list[girl_index]['name']] She seems happy to attend to you without words."
    },
    "behave_toilet":{
        "force_rule":" [all_girls_list[girl_index]['name']] would keep her mouth sealed or run away if not for the gag that force-spreads her lips and the toilet rack to which she is steadily tied.",
        "poor_job":" [all_girls_list[girl_index]['name']] Being befouled with your waste seems to upset her.",
        "good_job":" [all_girls_list[girl_index]['name']] She seems happy to receive your waste."
    },
    "behave_urinal":{
        "force_rule":" [all_girls_list[girl_index]['name']] would flee if not restrained on the urinal rack.",
        "poor_job":" [all_girls_list[girl_index]['name']] Being befouled with your urine seems to upset her.",
        "good_job":" [all_girls_list[girl_index]['name']]  She seems happy to receive your waste."
    },
    "deny_toileting":{
        "force_rule":" [all_girls_list[girl_index]['name']] regularly tries to remove her anal plug, unsuccessfully.",
        "poor_job":" [all_girls_list[girl_index]['name']] She seems resentful.",
        "good_job":" [all_girls_list[girl_index]['name']] She seems pleased to have more time with you."
    },
    "milk_the_fiend":{
        "inexperience":" [all_girls_list[girl_index]['name']]  She is not familiar with the procedure."
    },

    "use_vaginal_beads":{
        "force_rule":" [all_girls_list[girl_index]['name']] only uses the vaginal beads because the chastity belt prevents her from removing them.",
        "poor_job":" [all_girls_list[girl_index]['name']] Too much self-esteem or a lack of experience makes this painful to her.",
        "good_job":" [all_girls_list[girl_index]['name']] She seems to enjoy the sensations."
    }
}
define dic_auto_tasks = {
    "slave_auto_sleep": {
        "condition": "slave_auto_sleep",
        "text": night_rules_fuctions.sleep_text,
        "room": night_rules_fuctions.sleep_room,
    },
    "slave_auto_cook": {
        "condition": "slave_auto_cook",
        "text": night_rules_fuctions.cook_text,
        "room": night_rules_fuctions.cook_room,
        "extra": night_rules_fuctions.cook_extra,
    },
    "slave_auto_maid": {
        "condition": "slave_auto_maid",
        "text": night_rules_fuctions.maid_text,
        "room": night_rules_fuctions.maid_room,
    },
    "slave_auto_bath": {
        "condition": "slave_auto_bath",
        "text": night_rules_fuctions.bath_text,
        "room": night_rules_fuctions.bath_room,
    },
    "slave_auto_bath_self": {
        "condition": "slave_auto_bath_self",
        "text": night_rules_fuctions.bath_self_text,
        "room": night_rules_fuctions.bath_self_room,
    },
    "slave_auto_alarm": {
        "condition":"slave_auto_alarm",
        "text": night_rules_fuctions.alarm_text,
        "room": night_rules_fuctions.alarm_room,
        "extra": night_rules_fuctions.alarm_extra,
    }
}
define dic_slave_rules = {
    "act_as_cook": {
        "condition": rules_fuctions.act_as_cook_condition,
        "extra": rules_fuctions.act_as_cook_extra,
        "active": "cook_rules",
        "disable": "cook_rules_abort",
        "count": True
    },
    "act_as_maid": {
        "condition": rules_fuctions.act_as_maid_condition,
        "active": "maid_rules",
        "disable": "maid_rules_abort",
        "count": True
    },
    "bath_slave": {
        "condition": rules_fuctions.bath_slave_condition,
        "extra": rules_fuctions.bath_slave_extra,
        "active": "bath_slave_rules",
        "disable": "bath_slave_rules_abort",
        "count": True
    },
    "behave_alarm": {
        "condition": rules_fuctions.behave_alarm_condition,
        "active": "behave_alarm_rules",
        "disable": "behave_alarm_rules_abort",
        "count": True
    },
    "behave_humility": {
        "condition": rules_fuctions.behave_humility_condition,
        "active": "behave_humility_rules",
        "disable": "behave_humility_rules_abort",
        "count": True
    },
    "behave_pet": {
        "condition": rules_fuctions.behave_pet_condition,
        "active": "behave_pet_rules",
        "disable": "behave_pet_rules_abort",
        "count": True
    },
    "behave_silence": {
        "condition": rules_fuctions.behave_silence_condition,
        "active": "behave_silence_rules",
        "disable": "behave_silence_rules_abort",
        "count": True
    },
    "behave_toilet": {
        "condition": rules_fuctions.behave_toilet_condition,
        "active": "behave_toilet_rules",
        "disable": "behave_toilet_rules_abort",
        "count": True
    },
    "behave_urinal": {
        "condition": rules_fuctions.behave_urinal_condition,
        "active": "behave_urinal_rules",
        "disable": "behave_urinal_rules_abort",
        "count": True
    },
    "deny_orgasm": {
        "condition": rules_fuctions.deny_orgasm_condition,
        "active": "deny_orgasm_rules",
        "disable": "deny_orgasm_rules_abort",
        "count": True
    },
    "deny_toileting": {
        "condition": rules_fuctions.deny_toileting_condition,
        "active": "deny_toileting_rules",
        "disable": "deny_toileting_rules_abort",
        "count": True
    },
    "milk_the_fiend": {
        "condition": rules_fuctions.milk_the_fiend_condition,
        "extra": rules_fuctions.milk_the_fiend_extra,
        "active": "slave_tentacle_rules",
        "disable": "slave_tentacle_rules_abort",
        "count": True
    },
    "no_masturbation": {
        "condition": rules_fuctions.no_masturbation_condition,
        "active": "no_masturbation_rules",
        "disable": "no_masturbation_rules_abort",
        "count": True
    },
    "use_vaginal_beads": {
        "condition": rules_fuctions.use_vaginal_beads_condition,
        "active": "use_vaginal_beads_rules",
        "disable": "use_vaginal_beads_rules_abort",
        "count": True
    },
    "enforce_rules": {
        "condition": rules_fuctions.enforce_rules_condition,
        "active": "enforce_rules",
        "disable": "enforce_rules_abort",
        "count": False
    }
}
define dic_slave_rules_capital = {
    "act_as_cook": "Act as cook -",
    "act_as_maid": "Act as maid -",
    "bath_slave": "Bath slave -",
    "behave_alarm": "Behave: alarm -",
    "behave_humility": "Behave: humility -",
    "behave_pet": "Behave: pet -",
    "behave_silence": "Behave: silence -",
    "behave_toilet": "Behave: toilet -",
    "behave_urinal": "Behave: urinal -",
    "deny_orgasm": "Deny orgasm -",
    "deny_toileting": "Deny toileting -",
    "milk_the_fiend": "Milk the fiend -",
    "no_masturbation": "No masturbation -",
    "use_vaginal_beads": "Use vaginal beads -",
    "enforce_rules": "Enforce rules -"
}

