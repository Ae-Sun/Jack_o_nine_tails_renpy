# I can probably merge characters and mc inicial_stats into a giga big dictionaly, but I'm lazy -rec3ks
define DIC_CHARACTERS = [ #DO NOT ADD ANY VARIABLE TO THIS DICTIONARY -rec3ks
    ("master_noble", "master/master_noble.webp", "master/master_noble_hover.webp",0),
    ("master_torturer", "master/master_torturer.webp", "master/master_torturer_hover.webp",1),
    ("master_pimp", "master/master_pimp.webp", "master/master_pimp_hover.webp",2),
    ("master_vampire", "master/master_vampire.webp", "master/master_vampire_hover.webp",3),
    ("master_fighter", "master/master_fighter.webp", "master/master_fighter_hover.webp",4),
    ("master_teacher", "master/master_teacher.webp", "master/master_teacher_hover.webp",5),
    ("master_impressario", "master/master_impressario.webp", "master/master_impressario_hover.webp",6),
    ("master_butler", "master/master_butler.webp", "master/master_butler_hover.webp",7),
    ("master_doctor", "master/master_doctor.webp", "master/master_doctor_hover.webp",8),
    ("master_werwolf", "master/master_werwolf.webp", "master/master_werwolf_hover.webp",9),
    ("master_granpa", "master/master_granpa.webp", "master/master_granpa_hover.webp",10),
    ("master_nerd", "master/master_nerd.webp", "master/master_nerd_hover.webp",11),
]

##### I should use Json instead of Dict or make a better Dictionary structure, but requiere a lot rework and I'm lazy -rec3ks
define DIC_MC_INICIAL_STATS = { #DO NOT ADD ANY VARIABLE TO THIS DICTIONARY -rec3ks
    "master_noble"      : ["M'lord"     , 4, 4, 0, 2, 4, 0, 0, 0, 5, 0, 5, 2, 2, 3, 2, 4, 0, 4, 3, 0, 3, 2, 4, 3,"Elven Chainmail"     ,""           ,"Fist"         ,"Epée"           ,""                 ,""        ,"Noble Regalia"       ,"","","","","Taurus Great House",8000, "simple difficulty",    5,""                                 , "   An aristocrat with a great education, with \n experience in court and military service. Having all \n the basic skills that are necesarry to teach, the easily \n joined the ranks of the slavers and all agree that a \n wonderful career awaits him..."], 
    "master_torturer"   : ["Robespierre", 5, 1, 0, 3, 3, 0, 0, 0, 5, 0, 5, 1, 1, 0, 3, 3, 0, 5, 5, 5, 2, 2, 4, 4,"Without armor"       ,""           ,"Fist"         ,"Whip"           ,""                 ,""        ,"Worn clothes"        ,"","","","","Taurus Great House",7000, "simple difficulty",    5,""                                 , "   Once upon a time he was a soldier and fought for \n the king in his colonial wars. Then the king was \n overthrown and the revolution needed executioners. \n More than anything, he is proud to have personally \n decapitated the beautiful, but hanghty queen. In the \n Eternal Rome, a hangman's skills some in handy. "],
    "master_pimp"       : ["Silk Daddy" , 3, 4, 0, 3, 4, 0, 0, 0, 5, 0, 5, 3, 2, 2, 1, 1, 0, 0, 2, 2, 4, 4, 5, 5,"Without armor"       ,""           ,"Fist"         ,"Brass Knuckles" ,""                 ,""        ,"Fashionable Attire"  ,"","","","","Serpis Great House",4500, "simple difficulty",    5,""                                 , "   Everyone has his own idea of success. For Silk \n Daddy, establishing himself as a pimp was a dream \n come true. Now he's in a new world, but the work is \n somewhat similar. Black, white, yellow or tailed - \n bitches will always be bitches. They need a big black \n daddy. And Daddy needs a lot of money."],
    "master_vampire"    : ["Saruman"    , 5, 5, 0, 0, 4, 0, 0, 0, 5, 0, 5, 1, 3, 0, 2, 2, 4, 1, 1, 1, 3, 3, 3, 0,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,"Wizard Robes"        ,"","","","","Serpis Great House",5000, "simple difficulty",    5,""                                 , "   Saruman was once a revered sorcerer who delved \n into the forbidden arts and was inadvertently cursed \n with vampirism. At first, Saruman embraced his \n transformation, but soon the thrill of the hunt began \n to wane, leaving a deep sense of loneliness. Desiring a \n worthy companion to share eternity with him, he \n obsessively acquired new thralls until one day he \n unexpectedly stumbled into the mists. There he \n chanced across a black medic to lead him to Rome, \n where Saruman hopes to find his true love at last."],
    "master_fighter"    : ["Blade"      , 5, 2, 0, 3, 3, 0, 0, 0, 5, 0, 5, 1, 1, 0, 2, 6, 0, 2, 2, 2, 2, 2, 4, 2,"Yatserin Mail"       ,""           ,"Fist"         ,"Bastard Sword"  ,""                 ,""        ,"Aketon"              ,"","","","","Taurus Great House",6000, "normal difficulty",    3,""                                 , "   In the harsh world where he was born a natural \n physical strength was very much appreciated. Blade \n was one of the best warriors and confidently walked \n to success, but somehow got to the Fog. Although a \n good fighter will not get lost in the Eternal Rome, we \n all somethimes want to change our lives and achieve \n something more than an ordinary service to the \n mighty of this world."],
    "master_teacher"    : ["Teacher"    , 3, 3, 0, 3, 4, 0, 0, 0, 5, 0, 5, 6, 2, 2, 1, 0, 0, 4, 1, 0, 2, 1, 3, 0,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,"Formal Suit"         ,"","","","","Serpis Great House",3000, "normal difficulty",    3,""                                 , "   He was a ordinary school teacher, nothing \n special. Such a person might find it difficult to adapt \n in the Eternal Rome, but he is hoping that his years \n of experience teaching young minds and maintaining \n strict discipline in the class will be transferable skills. \n Besides, he misses the good old days when you were \n allowed to spank naughty young ladies! Spare the \n rod, spoil the student. But most of all, he simply \n could not bear another class full of nubile girls, so \n close and yet so far."],
    "master_impressario": ["Maestro"    , 2, 4, 0, 1, 3, 0, 0, 0, 5, 0, 5, 3, 1, 6, 0, 0, 0, 3, 0, 0, 3, 5, 4, 1,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,"Formal Suit"         ,"","","","","Taurus Great House",6000, "normal difficulty",    3,""                                 , "   He was the Impresario, famous in the old world, \n the man that playwrights, composers and stars \n kowtowed to. Literally thousands of young starlets \n have knelt beneath his desk or laid on his casting \n couch. But when his fourth trophy wife left him he \n gave it all up for a fresh start in the Eternal Rome, a \n city that still appreciates true talent. And if he had \n to work with one more spoiled diva... so much \n easier to work with a slave."],
    "master_butler"     : ["Butler"     , 3, 3, 0, 2, 3, 0, 0, 0, 5, 0, 5, 3, 6, 1, 1, 0, 0, 2, 0, 2, 0, 1, 2, 0,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,"Livery"              ,"","","","","Taurus Great House",5000, "normal difficulty",    3,""                                 , "   Once in the Eternal Rome, he found himself in a \n delicate situation. Of course, an experienced servant \n in useful everywhere, but he doesn't feel like being a \n slave. He put in a lot of effort to gain the status of a \n slaver. After all, no one trains maids better than a \n butler."],
    "master_doctor"     : ["Doc"        , 3, 3, 0, 2, 2, 0, 0, 0, 5, 0, 5, 2, 1, 0, 6, 0, 0, 0, 3, 0, 2, 1, 3, 0,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,"Medical Gown"        ,"","","","","Serpis Great House",1000, "high difficulty"  ,    2,"He cannot afford an apartment yet", "   He was always a very good doctor with a thriving \n practice. The one little mistake and one huge \n malpractice suit, and suddenly he decided to move \n to the Eternal Rome. It turned out that even Doc has \n insufficient knowledge for the Technosphere's Medical \n Center, but it's no reason to despair, right? He \n always wanted to try to educate witchdoctors in a \n more unfettered manner. Maybe it's his calling?"],
    "master_werwolf"    : ["Fenris"     , 4, 0, 0, 4, 3, 0, 0, 0, 5, 0, 5, 1, 0, 0, 3, 3, 3, 2, 2, 2, 0, 0, 4, 2,"Elven Chaimail"      ,"Morningstar","Katana"       ,"Epée"           ,"Cat o' Nine Tails","Dagger"  ,"Aketon"              ,"","","","","Camira Great House",400 , "high difficulty"  ,    2,"He cannot afford an apartment yet", "   A magical werewolf who must hide his true \n nature. He is constantly on the move to avoid \n detection, which explains his meager circumstances. \n He is a skilled fighter and torturer and has seen his \n share of war. Fenris is an accomplished war medic \n who is known for saving soldiers who had little \n chance of survival. He was also pulled in at times to \n perform interrogations of the enemy while serving in \n various Camira war camps. Fenris miraculously was \n the sole survivor of two war camp slaughters."],
    "master_granpa"     : ["Uncle Tom"  , 2, 1, 0, 0, 1, 0, 0, 0, 5, 0, 5, 2, 1, 0, 1, 0, 0, 2, 1, 0, 4, 3, 1, 4,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,"Housecoat"           ,"","","","","Serpis Great House",800 , "very high difficulty", 1,"He cannot afford an apartment yet", "   Those things he used to make his daughters do? \n Not his fault, really; the sluts had basically asked for \n it. But now he is old and alone, shunned by his \n family, not allowed to see his own granddaughters! \n So unfair! So how does a lonely, dirty old man \n spend his golden years? He's not your typical slaver \n - erectile issues and kind of creepy - but ins't \n training a young slave to be a good girl basically the \n same as raising a daughter? He cashed in his persion \n and came to the Eternal Rome."],
    "master_nerd"       : ["Johny"      , 2, 1, 0, 5, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 5,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,"Worn clothes"        ,"","","","","Serpis Great House",200 , "extreme difficulty",   0,"He cannot afford an apartment yet", "   People just see a quiet, young nerd. Other kids call \n him 'loser'. But in his dreams? He's a great slave \n master. Womn crawl at his feet...no,{i} bitches...{/i}naked \n bitches...with enormous saggy tits. Oh, the disgusting \n things he would force them to do!! The kid jerks off \n a dozen times a day imagining it. He's learned \n enough magic to find the Fogs, but does this horny \n virgin schoolboy really have what it takes to break \n grown women to his will? Will they take him \n seriously? Or will they just think he's a loser, too? "],
    "Jack"              : ["jack"       , 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,""                    ,"","","","",""                  ,6000, "Normal"           ,    3,585]           
    }
define DIC_CHARACTERSONLYNAME = ["master_noble", "master_torturer", "master_pimp", "master_vampire", "master_fighter","master_teacher", "master_impressario", "master_butler", "master_doctor", "master_werwolf", "master_granpa", "master_nerd"]

define DIC_MC_ATTRIBUTE = { #DO NOT ADD ANY VARIABLE TO THIS DICTIONARY -rec3ks
    "STRENGTH"             : ["Frail"               , "Weak"                 , "Unfit"               , "Vigorous"           , "Strong"            , "Herculean"             ,"{b}Inmortal{/b}"                 ,"{b} STRENGTH:{/b} \n Strength commands respect. It is important for a \n trainer  to be strong. Strength affects the force of your \n blows in combat, your endurance in daily tasks, and the \n submissiveness of your slaves. To build and maintain \n strength, avoid lower-quality food, engage in athletics, \n dance, intercourse, or martial arts, firmly discipline \n your slaves, and avoid exhaustion (red energy stars)."],
    "PERSONALITY"          : ["Caitiff"             , "Rube"                 , "Churl"               , "Knave"              , "Vulgarian"         , "Aristocrat"            ,"{b}Aristocrat+{/b}"              ,"{b} PERSONALITY:{/b} \n Charisma, determination and will play a crusial role \n for  a trainer of slaves, as they make it much easier to \n control other people. How you are viewed is a reflection \n of your prestige, which is influenced by your standard \n of living, the location of your residence, the quality \n of your interior decor, and your brand reputation" ],
    "ALLURE"               : ["Repulsive"           , "Unpleasant"           , "Unmemorable"         , "Charming"           , "Captivating"       , "Irresistible"          ,"{b}Irresistible+{/b}"            ,"{b} ALLURE:{/b} \n Slaves are more willing to obey alluring trainers, especially when it comes to sex. Sometimes they do not even need to be forced. An impressive appearance also can help in communicating with customers. To improve appearance, take care of your body, maintain a positive attitude, spruce yourself up, choose appropriate clothing and avoid exhaustion."],
    "LIBIDO"               : ["Impotent"            , "Effete"               , "Lustful"             , "Libidinous"         , "Lubricious"        , "Salacious"             ,"{b}Salacious+{/b} "              ,"{b} LIBIDO:{/b} \n Sex is an essential part of training slaves, and the \n ability to perform without the aid of aphrodisiacs is \n vital. Libido is increased by an active sex life and a \n healthy lifestyle, but is decreased by injuries, illness, \n poor health, and extended periods without sex."],
    "DOMINANCE"            : ["Submissive"          , "Compliant"            , "Passive"             , "Authoritative"      , "Dominant"          , "Imperious"             ,"{b}Imperious+{/b}"               ,"{b} DOMINANCE:{/b} \n Ability to dominate and subdue is just as important \n for a slave trainer as ability to teach. Your level of \n dominance has strong influence on your slave's obedience \n and the effectiveness of some punishments, especially  \n verbals ones. Dominance is also useful when teaching \n sexual skills. Increases automatically when applied."],
    "BRAND REPUTATION"     : ["Unknown"             , "Rumored"              , "Recognized"          , "Celebrity"          , "Famous"            , "Legendary"             ,"{b}Legendary+{/b}"               ,"{b} BRAND REPUTATION:{/b} \n For a slaver in the Eternal Rome, nothing is more important than building up your personal brand. It is your brand, your trademark. The quality of the slaves you train will speak for your reputation. With fame, your personal status will rise and customers will be more accommodating."],
    "GUILD REPUTATION"     : ["Guild Fall Guy"      , "Guild Punching Bag"   , "Guild Lackey"        , "Guild Hotshot"      , "Guild Muscle"      , "Guild Boss"            ,"{b}Guild Boss+{/b}"              ,"{b} GUILD REPUTATION:{/b} \n For a member of the very prestigious Guild of Trainers, nothing is more rewarding than the envy of your peers. The quality of the slaves you train for Guild contracts and auctions will speak for your reputation within the Guild. As you rise in the ranks, more valuable contracts will be offered, the arena will accept multiple contestants, and other benefits may arise."],
    "STANDARD OF LIVING"   : ["Impoverished"        , "Poor"                 , "Basic"               , "Comfortable"        , "Respectable"       , "Luxurious"             ,"{b}Extravagant{/b}"              ,"{b} STANDARD OF LIVING:{/b} \n All the wealth in the world will do nothing to improve your standing if you live like a beggar and never improve your lot in life. Set the standard of living in the menu under 'Domestic Issues'. A standard of living a little above your fame is optimal, but beware of the expense. Assigning a good accountant can optimize your costs. Note: Changes occur next decade."],
    "HYGIENE"              : ["Filthy"              , "Dirty"                , "Unclean"             , "Unsullied"          , "Clean"             , "Pristine"              ,"{b}Pristine+{/b}"                ,"{b} HYGIENE:{/b} \n It's hard to be hygienic in the slums. Better to rent decent housing with a bathroom. Poor hygiene leads to unhappiness and poor health. On the other hand, being bathed by an experienced slave might improve your mood. A visit to the spa or rewarding an obedient slave with a visit to the beach or the hot springs are also options."],
    "MOOD"                 : ["Depressed"           , "Dysphoric"            , "Sullen"              , "Melancholic"        , "Pessimistic"       , "Calm"                  , "Hopeful"          , "Optimistic"        , "Pleased"           , "Euphoric"          , "Ecstatic"           ,"{b}Ecstatic+{/b}",""],
    "INJURIES"             : ["Mortally wounded"    , "Seriously Injured"    , "Moderately Injured"  , "Lightly Injured"    , "Slightly Wounded"  , "Safe and unharmed"     ,"{b}Safe and unharmed+{/b}"       ,"{b} INJURIES:{/b} \n Injuries can occur in combat and heal over time, but sap energy, strength and mood in the process. Eat well, stay clean, and study medicine or obtain a qualified assistant to support healing. With a skilled alchemist, healing balms can be produced using reagents acquired from Mystra of the Outcasts. As a last resort, the Technosphere medical center can cure most ills."],
    "TEACHING"             : ["Incoherent F-"       , "Tutor D-"             , "Mentor C-"           , "Pedagogue B+"       , "Teacher A+"        , "Lecturer S+"           ,"{b}Lecturer S++{/b}"             ,"{b} TEACHING:{/b} \n Teaching is one of the key skills of the slaver. It \n determines the efficiency of training a slave in any \n non-sexual skill. Skill as a teacher improves as you  \n teach your slaves with outcomes A+ or better."],
    "STEWARDSHIP"          : ["Ingenuous Dweller F-", "Peon D-"              , "Houseboy C-"         , "Homemaker B+"       , "Houselord A+"      , "Steward S+"            ,"{b}Master Steward S++{/b}"       ,"{b} STEWARDSHIP:{/b} \n Stewardship combines the knowledge of cooking, \n household and slave management. A good steward can \n cook dinner himself or clean the house, but more \n importantly he can pass his skills to his slaves."],
    "ARTISTRY"             : ["Tasteless F-"        , "Uncultured D-"        , "Dilettante C-"       , "Artist B+"          , "Prodigy A+"        , "Virtuoso S+"           ,"{b}Maestro S++{/b}"              ,"{b} ARTISTRY:{/b} \n Artistry comes in many forms. Dance, music, the \n ability to paint, acting and roleplay (including \n behaving like an animal)… Skill as an artist improves \n as you teach your slaves relevant skills with outcomes \n A+ or better. "],
    "MEDIC"                : ["Homeopath F-"        , "Quack D-"             , "Paramedic C-"        , "Medic B+"           , "Physician A+"      , "Surgeon S+"            ,"{b}Master Surgeon S++{/b}"       ,"{b} MEDIC:{/b} \n A competent medic and alchemist can train  \n witchdoctors, identify health issues and effectively  \n care for sick and injured slaves."],
    "FIGHTER"              : ["Non-Combatant F-"    , "Brawler D-"           , "Duelist C-"          , "Combatant B+"       , "Warrior A+"        , "Champion S+"           ,"{b}Vanquisher S++{/b}"           ,"{b} FIGHTER:{/b} \n Martial skill is useful both to train a gladiatrix  \n and in real combat. Your capacity to learn special \n techniques from the Colosseum trainer and the duration \n of your strikes' effects are dependent upon your combat \n skill. Skill as a fighter improves as you train your \n slaves in combat with outcomes A+ or better and when  \n you are victorious in battle."],
    "MAGIC"                : ["Mundane F-"          , "Esoterist D-"         , "Warlock C-"          , "Sorcerer B+"        , "Mage A+"           , "Archmage S+"           ,"{b}Demi-God S++{/b}"             ,"{b} MAGIC:{/b} \n This skill is responsible for your ability to cast \n spells using sparks and directly affects the \n effectiveness of these spells. The skill of alchemists and \n enchantresses you personally train cannot exceed your \n skill rank in magic. Trained alchemists can brew useful \n potions for you in the lab, but you will need reagents \n that can be found at the 'Rarities of Mystra' in \n the Outcasts' Quarter. Skill in magic improves as you \n train slaves with outcomes A+ or better and apply \n magic of the highest levels available."],
    "FLAGELLATION"         : ["Cannot Whip F-"      , "Poor Whip Skill D-"   , "Basic Whip Skill C-" , "Good Whip Skill B+" , "Whip Expert A+"    , "Master of the Whip S+" ,"{b}Master of the Whip S++{/b}"   ,"{b} FLAGELLATION:{/b} \n Proper use of belt, whip and lash not only improves \n the efficiency of punishment but also reduces \n the risk of leaving unwanted scars on a slave. Skill \n develops through application." ],
    "TORTURE"              : ["Not a Torturer F-"   , "Needler D-"           , "Tormentor C-"        , "Torturer B+"        , "Inquisitor A+"     , "Master Inquisitor S+"  ,"{b}Master Inquisitor S++{/b}"    ,"{b} TORTURE:{/b} \n If you are using a bulky torture unit, it does \n everything for you. But the master of torture can \n achieve no less using modest materials at hand. More \n importantly, skill in this area prevents spoiling the \n appearance and health of slaves. Requires a dungeon. \n Skill develops through application."],
    "BINDING"              : ["Never Restrained F-" , "Novice Rope Binder D-", "Binds Correctly C-"  , "Binds Skillfully B+", "Binds Artfully A+" , "Master of Rope S+"     ,"{b}Master of Rope S++{/b}"       ,"{b} BLINDING:{/b} \n Blinding allows you to leave a slave unattended to \n receive punishment from the rope. Proper painful or \n erotic bondage can be very effective as an educational \n or exciting action. Skill develops through application."],
    "PETTING"              : ["Never touched F-"    , "Petting D-"           , "Petting C-"          , "Petting B+"         , "Petting A+"        , "Petting S+"            ,"{b}Master of Petting S++{/b}"    ,"WIP"],
    "ORAL SEX"             : ["Oral Sex F-"         , "Oral Sex D-"          , "Oral Sex C-"         , "Oral Sex B+"        , "Oral Sex A+"       , "Oral Sex S+"           ,"{b}Master of Oral Sex S++{/b}"   ,"WIP"],
    "PENETRATION"          : ["Virgin F-"           , "Penetration D-"       , "Penetration C-"      , "Penetration B+"     , "Penetration A+"    , "Penetration S+"        ,"{b}Master of Penetration S++{/b}","WIP"],
    "FETISHISM"            : ["Unadventurous F-"    , "Fetishism D-"         , "Fetishism C-"        , "Fetishism B+"       , "Fetishism A+"      , "Worst of Perverts S+"  ,"{b}Worst of Perverts S++{/b}"    ,"WIP"],
    "REPUTATION"           : ["The Slums"           , "Quarter of the Outcasts","Serpentine Quarter" , "Quarter of the Bull", "Necropolis"        , "White Town"            ,"{b} REPUTATION:{/b} \n Reputation measures your personal notoriety (how \n well you are known by the citizens of the Eternal \n Rome) and determines your access to the higher echelons \n of society and to higher-quality, higher-cost living \n conditions. Living in a shack is cheap but very difficult. \n Satisfying clients will improve your reputation with \n their faction and allow you to rent or purchase a \n residence in their vicinity. "]
}
define DIC_MC_NORMAL_SELECTION_TEXTDESCRIPTION ={ 
    "master_noble":       [DIC_MC_INICIAL_STATS["master_noble"][41]," - No particular advantages or disadvantages."],
    "master_torturer":    [DIC_MC_INICIAL_STATS["master_torturer"][41]," - No particular advantages or disadvantages."],
    "master_pimp":        [DIC_MC_INICIAL_STATS["master_pimp"][41]," - No particular advantages or disadvantages."],
    "master_vampire":     [DIC_MC_INICIAL_STATS["master_vampire"][41]," - No particular advantages or disadvantages."],
    "master_fighter":     [DIC_MC_INICIAL_STATS["master_fighter"][41]," - Fighter Skills will not naturally decay."],
    "master_teacher":     [DIC_MC_INICIAL_STATS["master_teacher"][41]," - Teaching Skills will not naturally decay."],
    "master_impressario": [DIC_MC_INICIAL_STATS["master_impressario"][41]," - Artistry Skills will not naturally decay. \n - Get free theather tickets"],
    "master_butler":      [DIC_MC_INICIAL_STATS["master_butler"][41]," - Stewardship Skills will not naturally decay."],
    "master_doctor":      [DIC_MC_INICIAL_STATS["master_doctor"][41]," - Medic Skills will not naturally decay. \n - Free hospital examination"],
    "master_werwolf":     [DIC_MC_INICIAL_STATS["master_werwolf"][41]," - No particular advantages or disadvantages."],
    "master_granpa":      [DIC_MC_INICIAL_STATS["master_granpa"][41]," - No particular advantages or disadvantages."],
    "master_nerd":        [DIC_MC_INICIAL_STATS["master_nerd"][41]," - No particular advantages or disadvantages."],
    "STRENGTH":            [DIC_MC_ATTRIBUTE["STRENGTH"][7]],
    "PERSONALITY":         [DIC_MC_ATTRIBUTE["PERSONALITY"][7]],
    "LIBIDO":              [DIC_MC_ATTRIBUTE["LIBIDO"][7]],
    "ALLURE":              [DIC_MC_ATTRIBUTE["ALLURE"][7]],
    "DOMINANCE":           [DIC_MC_ATTRIBUTE["DOMINANCE"][7]],
    "BRAND REPUTATION":    [DIC_MC_ATTRIBUTE["BRAND REPUTATION"][7]],
    "GUILD REPUTATION":    [DIC_MC_ATTRIBUTE["GUILD REPUTATION"][7]],
    "STANDARD OF LIVING":  [DIC_MC_ATTRIBUTE["STANDARD OF LIVING"][7]],
    "INJURIES":            [DIC_MC_ATTRIBUTE["INJURIES"][7]],
    "HYGIENE":             [DIC_MC_ATTRIBUTE["HYGIENE"][7]],
    "TEACHING":            [DIC_MC_ATTRIBUTE["TEACHING"][7]],
    "STEWARDSHIP":         [DIC_MC_ATTRIBUTE["STEWARDSHIP"][7]],
    "ARTISTRY":            [DIC_MC_ATTRIBUTE["ARTISTRY"][7]],
    "MEDIC":               [DIC_MC_ATTRIBUTE["MEDIC"][7]],
    "FIGHTER":             [DIC_MC_ATTRIBUTE["FIGHTER"][7]],
    "MAGIC":               [DIC_MC_ATTRIBUTE["MAGIC"][7]],
    "FLAGELLATION":        [DIC_MC_ATTRIBUTE["FLAGELLATION"][7]],
    "TORTURE":             [DIC_MC_ATTRIBUTE["TORTURE"][7]],
    "BINDING":             [DIC_MC_ATTRIBUTE["BINDING"][7]],
    "PETTING":             [DIC_MC_ATTRIBUTE["PETTING"][7]],
    "ORAL SEX":            [DIC_MC_ATTRIBUTE["ORAL SEX"][7]],
    "PENETRATION":         [DIC_MC_ATTRIBUTE["PENETRATION"][7]],
    "FETISHISM":           [DIC_MC_ATTRIBUTE["FETISHISM"][7]],
    "REPUTATION":          [DIC_MC_ATTRIBUTE["REPUTATION"][6]],
    "MC NAME":             ["{b} MISCELLANEOUS:{/b} \n Total time played with this character: WIP \n Total number of slave buyed: WIP \n The highest sell slave value: WIP \n Total amount of spark gained: WIP: \n  "],
    "simple difficulty":   ["{b} SIMPLE DIFFICULTY:{/b} \n Perfect for beginners or those looking to enjoy the game \n without too much challenge."],
    "normal difficulty":   ["{b} NORMAL DIFFICULTY:{/b} \n A balanced experience for players seeking a fair \n challenge."],
    "high difficulty":     ["{b} HIGH DIFFICULTY:{/b} \n Designed for experienced players, resources \n are scarcer, and  mistakes are costly."],
    "very high difficulty":["{b} VERY HIGH DIFFICULTY:{/b} \n Only for the truly daring. , resources are rare, and \n every decision counts. One wrong move could be your \n last."],
    "extreme difficulty":  ["{b} EXTREME DIFFICULTY:{/b} \n Brutal and unforgiving. resources are nearly \n nonexistent, and survival demands perfection."],
    "SPARKS":              ["{b} SPARKS:{/b} \n Money, very usefull."],
    "FACTION":             ["{b} FACTION:{/b} \n You can rent a house in this faction at the start of \n game in Trade center, Real State. "],
    "SKILLS":              ["{b} SKILLS:{/b} \n Skills are the abilities and competencies that a person \n develops through learning, practice, or experience,\n which enable them to perform specific tasks \n effectively and efficiently."],
    "SEX TECHNIQUES":      ["{b} SEX TECHNIQUES:{/b} \n Different sex techniques will increase the effectiveness \n of training relevant skills and it will be easier to arouse \n and excite your sexual partners. "],
    "WHITE TOWN":          ["{b} WHITE TOWN:{/b} \n Cannot start in White Town on Normal or Extreme \n difficulty. Only patricians are allowed to live there."],
    "START FAIL":          ["{b} START FAIL:{/b} \n Points must be igual or greater than 0."]
    }
# I know you can use xmaximum and xminimum, just happened I learned that too late, so unless someone want to change it, I will leave it like this with the \n
define DIC_CUSTOM_CHARACTER_SELECTION = {
    "master_noble":        ["custom_master/master_noble.webp", "custom_master/master_noble_hover.webp",0],
    "master_torturer":     ["custom_master/master_torturer.webp", "custom_master/master_torturer_hover.webp",1],
    "master_pimp":         ["custom_master/master_pimp.webp", "custom_master/master_pimp_hover.webp",2],
    "master_vampire":      ["custom_master/master_vampire.webp", "custom_master/master_vampire_hover.webp",3],
    "master_fighter":      ["custom_master/master_fighter.webp", "custom_master/master_fighter_hover.webp",4],
    "master_teacher":      ["custom_master/master_teacher.webp", "custom_master/master_teacher_hover.webp",5],
    "master_impressario":  ["custom_master/master_impressario.webp", "custom_master/master_impressario_hover.webp",6],
    "master_butler":       ["custom_master/master_butler.webp", "custom_master/master_butler_hover.webp",7],
    "master_doctor":       ["custom_master/master_doctor.webp", "custom_master/master_doctor_hover.webp",8],
    "master_werwolf":      ["custom_master/master_werwolf.webp", "custom_master/master_werwolf_hover.webp",9],
    "master_granpa":       ["custom_master/master_granpa.webp", "custom_master/master_granpa_hover.webp",10],
    "master_nerd":         ["custom_master/master_nerd.webp", "custom_master/master_nerd_hover.webp",11],
}
define MASTER_CAPS = {
    "wounds": [10, 20, 40, 80, 160],
    "STRENGTH": [10, 25, 50, 160, 666],
    "PERSONALITY": [10, 20, 40, 80, 160],
    "LIBIDO": [45, 90, 180, 360, 999],
    "BRAND": [5, 15, 30, 70, 100],
    "GUILD REPUTATION": [5, 10, 20, 40, 75],
    "HYGIENE": [10, 20, 40, 60, 80],
    "TEACHING": [15, 75, 150, 300, 600],
    "STEWARDSHIP": [15, 75, 150, 300, 600],
    "ARTISTRY": [15, 75, 150, 300, 600],
    "MEDIC": [15, 75, 150, 300, 600],
    "FIGHTER": [15, 75, 150, 300, 600],
    "MAGIC": [15, 75, 150, 300, 600],
    "DOMINANCE": [45, 90, 180, 360, 999],
    "FLAGELLATION": [1, 20, 40, 80, 160],
    "TORTURE": [1, 20, 40, 80, 160],
    "BINDING": [1, 20, 40, 80, 160],
    "PETTING": [1, 45, 90, 180, 360],
    "ORAL SEX": [1, 45, 90, 180, 360],
    "PENETRATION": [1, 45, 90, 180, 360],
    "FETISHISM": [1, 45, 90, 180, 360],
}
define DIC_MASTER_ITEMS = {
    "man_rugs": {
        "name": "Worn clothes", 
        "price": 5,
        "desc": "Price: 5 sparks\nThese clothes are worn out and out of fashion. They do not meet any of your goals. It would be better to get some new clothes.",
        "image": "scene/item/item_worn_clothes",
        "size": 0,
        "style": -1,
        "item_property": False,
        "equiped":False,
        "effect": {
            "master_moodlet": {"neg_worn_clothes": 100}
        }
    },
    "comfy_robes": {
        "name": "Housecoat",
        "price": 25,
        "desc": "Price: 25 sparks\nComfortable and soft housecoat. Does not look very nice, but very convenient and comfortable to wear. Just what you need to relax!",
        "image": "scene/item/item_Housecoat",
        "size": 0,
        "style": -1,
        "item_property": False,
        "equiped":False,
        "effect": {
            "master_moodlet": {"pos_master_cloth": 100}
        }
    },
    "regal_suit": {
        "name": "Noble Regalia",
        "price": 200,
        "desc": "Price: 200 sparks\nThis heavy clothing is richly decorated with precious inserts and decorative elements, making you look bigger and grander. Beautiful and impressive, of course, but very impractical.",
        "image": "scene/item/item_Noble_regalia",
        "size": 0,
        "style": 2,
        "item_property": False,
        "equiped":False,
        "effect": {
            "master_moodlet": {"neg_master_cloth": 100}
        }
    },
    "fancy_suit": {
        "name": "Fashionable Attire",
        "price": 100,
        "desc": "Price: 100 sparks\nKeeping track of Eternal Rome fashion is almost impossible, but many are trying. In any case, this outfit is a perfect compromise between luxury and convenience.",
        "image": "scene/item/item_Fashionable_attire",
        "size": 0,
        "style": 1,
        "item_property": False,
        "equiped":False,
        "effect": {}
    },
    "formal_suit": {
        "name": "Formal Suit",
        "price": 40,
        "desc": "Price: 40 sparks\nVery formal clothing. Looks old-fashioned and not very charming, but at least you will be taken seriously. It is perfect for the impresario or for an entertainer.",
        "image": "scene/item/item_Formal_suit",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "boost_up": {"master_artdirector": 1}
        }
    },
    "aketon": {
        "name": "Aketon",
        "price": 40,
        "desc": "Price: 40 sparks\nQuilted armor jacket, light enough to be used as everyday wear. Great outfit for a warrior.",
        "image": "scene/item/item_Aketon",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "boost_up": {"master_fighter": 1}
        }
    },
    "livery": {
        "name": "Livery",
        "price": 40,
        "desc": "Price: 40 sparks\nOrnate livery of a senior butler. In this uniform you immediately feel like the sole ruler over your household.",
        "image": "scene/item/item_Livery",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "boost_up": {"master_butler": 1}
        }
    },
    "medic_robes": {
        "name": "Medical Gown",
        "price": 40,
        "desc": "Price: 40 sparks\nVery comfortable and practical clothing for the healthcare worker. Immediately makes you a qualified doctor - even if only due to self-hypnosis.",
        "image": "scene/item/item_Medical_gown",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "boost_up": {"master_medic": 1}
        }
    },
    "wizard_robes": {
        "name": "Wizard Robes",
        "price": 40,
        "desc": "Price: 40 sparks\nThis ritual costume is covered with magical runes. Increases your magical power!",
        "image": "scene/item/item_Wizard robes",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "boost_up": {"master_mage": 1}
        }
    },
    "raven_crown": {
        "name": "Raven Crown",
        "price": 0,
        "desc": "This artifact, called the Raven Crown by its creator, Master Valios, grants permanent auspex, greater insight when looking at others, and strengthens the aura.",
        "image": "scene/item/clear_small",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "auspex": 1,
            "magna_magnifika": 10,
            "item_supermacy_bonus": 1,
        }
    },
    "chimera_earring": {
        "name": "Chimaera's Gem",
        "price": 0,
        "desc": "This earring, taken from or given to me by the strange hissing creature Garsid, increases libido, strengthens the aura and heals wounds rapidly.",
        "image": "scene/item/clear_small",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "item_supermacy_bonus": 2
        }
    },
    "snake_amulet": {
        "name": "Snake Talisman",
        "price": 0,
        "desc": "This amulet, given to me by its maker, Vujin the Wise of House Serpis, increases concentration, personality, resistance to pain and fear, and strengthens the aura of the wearer, while also blocking scanning.",
        "image": "scene/item/clear_small",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "item_supermacy_bonus": 1
        }
    },
    "bull_ring": {
        "name": "Bull Ring",
        "price": 0,
        "desc": "This normal-looking ring, given to me by Sir Aramus of House Taurus, increases stamina and hardiness in battle and strengthens the aura of the wearer.",
        "image": "scene/item/clear_small",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "item_supermacy_bonus": 1
        }
    }
}
define MASTER_INVENTORY_TYPE = {
    "clothes": [
        "man_rugs",
        "comfy_robes",
        "regal_suit",
        "fancy_suit",
        "formal_suit",
        "aketon",
        "livery",
        "medic_robes",
        "wizard_robes"
    ],
    "headgear":[
        "raven_crown"
    ],
    "earrings":[
        "chimera_earring",
    ],
    "neck":[
        "snake_amulet"
    ],
    "accessories1":[
        "bull_ring"
    ],
    "accessories2":[
        "bull_ring"
    ],
    "accessories3":[
        "bull_ring"
    ],
    "accessories4":[
        "bull_ring"
    ],
    "accessories5":[
        "bull_ring"
    ]
}
define DIC_MASTER_SCREEN_TEXT = {
    "":"",
    "auspex":"Allows you to see what is hidden from view, mostly aura. By reading a person's aura, you can learn many interesting things about them",
    "magna_magnifika":"Strengthens the caster's aura for the duration of the spell. Effectiveness depends on the magical skill of the caster.",
    "sententia_veritas":"Sends false signals to the brain to increase the target's feelings of merit or guilt at the next opportunity.",
    "food_delivery":"This allows you to order delivery directly from the 'Virgin's Hips' pub for just 1 extra Spark, applicable at the end of day",
    "eat_slave_food":"The slave meat is certainly cheaper and nutritious, but it is not as delicious as the master's meal. Huge penality if a slave is present",
    "eat_best_food":"Even if a meal is already prepared, it will be replaced if a better one becomes available —potentially wasting the original food."
}

define DIC_MASTER_CAP = {
    "STRENGTH":          [10 , 25 , 50 , 160, 666, 9999],
    "PERSONALITY":       [10 , 20 , 40 , 80 , 160, 9999],
    "ALLURE":            [1  , 2  , 3  , 4  , 5  , 9999],
    "LIBIDO":            [45 , 90 , 180, 360, 999, 9999],
    "BRAND REPUTATION":  [5  , 15 , 30 , 70 , 100, 9999],
    "GUILD REPUTATION":  [5  , 10 , 20 , 40 , 75 , 9999],
    "STANDARD OF LIVING":[1  , 2  , 3  , 4  , 5  , 9999],
    "HYGIENE":           [10 , 20 , 40 , 60 , 80 , 9999],
    "INJURIES":          [160, 80 , 40 , 20 , 10 , 9999],
    "TEACHING":          [15 , 75 , 150, 300, 600, 9999],
    "STEWARDSHIP":       [15 , 75 , 150, 300, 600, 9999],
    "ARTISTRY":          [15 , 75 , 150, 300, 600, 9999],
    "MEDIC":             [15 , 75 , 150, 300, 600, 9999],
    "FIGHTER":           [15 , 75 , 150, 300, 600, 9999],
    "MAGIC":             [15 , 75 , 150, 300, 600, 9999],
    "DOMINANCE":         [45 , 90 , 180, 360, 999, 9999],
    "FLAGELLATION":      [1  , 20 , 40 , 80 , 160, 9999],
    "TORTURE":           [1  , 20 , 40 , 80 , 160, 9999],
    "BINDING":           [1  , 20 , 40 , 80 , 160, 9999],
    "PETTING":           [1  , 45 , 90 , 180, 360, 9999],
    "ORAL SEX":          [1  , 45 , 90 , 180, 360, 9999],
    "PENETRATION":       [1  , 45 , 90 , 180, 360, 9999],
    "FETISHISM":         [1  , 45 , 90 , 180, 360, 9999],
}
define MASTER_COOK_DESCRIPTION = [
    "Peering into the kitchen and scratching your head, you don't see how you can cook anything from all of this. Of course you have some vague ideas, but you are afraid most of them will lead to a catastrophe. Sighing, you just opened a few cans and dumped them on the plate. Will do!",
    "What a cruel irony - a man cooking. In the Eternal Rome, land of female slaves!\nEspecially since you're not a great cook. A simple salad, a few sandwiches, and heated canned food: the top of your cooking art. You'll have to eat the fruit of your labors.",
    "{b}This is woman's work{/b} you think as you roll up your sleeves. In the end, making a salad with dressing or concocting a tasty stew of vegetables and meat is not so difficult. At the very least, your skill will be enough not to ruin the valuable products.",
    "Cooking can be fun if you know which side of the pan is up. And you know it! Quickly evaluating the contents of the stasis chamber you envision a full three-course menu and slowly, tastefully bring your culinary plan to reality. Belissimo!",
    "Cooking is a serious business, and in your kitchen everything is perfectly prepared for such task. You have the best knives and utensils, perfect products and plenty of room. It remains to apply your significant chef talent and voila – an excellent three-course dinner is ready!",
    "Of course, you can entrust this job to slaves, but they will never surpass the cooking arts of such a <i>chef de cuisine</i> as yourself. And a man must cook culinary masterpieces occasionally to stay sharp. Your meals delight not only the stomach but also the eye. Delicious!",
    "Of course, you can entrust this job to slaves, but they will never surpass the cooking arts of such a 'chef de cuisine' as yourself. And a man must cook culinary masterpieces occasionally to stay sharp. Your meals delight not only the stomach but also the eye. Delicious!"
]
define DIC_MASTER_MOOD = {
    "good_mood": {
        "pos_energy"         : "I am fresh and full of energy. Gotta put it to good use!",
        "pos_new_slave"      : "A new day - a new slave. Shopping is always uplifting.",
        "pos_housing"        : "I must admit that I have very decent housing.",
        "pos_house_clean"    : "The house is in perfect cleanliness and order.",
        "pos_master_cloth"   : "I have very comfortable clothes. It is important for comfort.",
        "pos_self_clean"     : "There is nothing better than a good wash. Cleanliness is next to godliness!",
        "pos_toilet"         : "My slave happened to be a great toilet. Much nicer than a conventional toilet.",
        "pos_nice_slave"     : "Girl's education is progressing fine, I'm doing an excellent job.",
        "pos_massage"        : "Mmmm… what bliss. It's nice to be taken care of by a beautiful and gentle woman…",
        "pos_good_morning"   : "Morning blowjob - a perfect start to the day.",
        "pos_satisfied"      : "After such fervent sex, the brain inevitably switches to a positive wave!",
        "pos_optimism"       : "My slave is so cute that I want to communicate with her incessantly.",
        "pos_good_pet"       : "No wonder people get cats - they relieve stress excellently. Even if it's not quite a cat…",
        "pos_show"           : "I had a good time. Just what you need to dispel the boredom!",
        "pos_self_food"      : "I ate well. Simply a holiday flavor!",
        "pos_date"           : "I must say that the date went well.",
        "pos_master_winner"  : "Nice to feel like a winner!",
        "pos_deal"           : "Good deal. Now I have more sparks, which can be spent on something nice!",
        "pos_wealth"         : "It's great when you do not need to limit yourself to money.",
        "pos_kannabis"       : "Cough-cough… This weed is pretty decent I must say… A sudden calmness and serenity, but collecting thoughts together now is difficult…",
        "pos_drunk"          : "Now I'm drunk and I feel that this rotten world full of fucking cannibals and sadistic bastards is not so bad! And I am also not such a bastard…",
        "pos_opium"          : "Essence of oblivion gives peace and relief from all worries. I don't worry about anything right now, except that it can not last forever.",
        "pos_bahus"          : "Why do I want to bite the shield? And why is it such a positive feeling? Nyaaaaarrrrgh!!!!",
        "pos_master_precious": "This magic decoration is perfectly uplifting. When I touch it I immediately calm down and the world seems better. It is just so lovely!"
    },
    "bad_mood": {
        "neg_master_loser"   : "I hate to lose. Although it is not my fault, the slave should have done better!",
        "neg_boring"         : "I'm booooooored… You can not always just work and fuck. It's necessary to have some fun!",
        "neg_tired"          : "Uuuuuhhhh… I'm tired. It is necessary to have a good rest, otherwise it's easy to lose health.",
        "neg_drunk"          : "My head aches and mouth is dry. I need a drink. It is urgent to have a drink… there should have been a bottle somewhere in the closet…",
        "neg_wounded"        : "My wounds ache under the bandages. Every wrong move hurts.",
        "neg_no_koffe"       : "My eyes droop. Where is my morning cup of kamra?",
        "neg_no_opium"       : "I'm having agonies. I'll start climbing the wall at this rate. Feels like I'll fucking die if oblivion is not urgently delivered.",
        "neg_no_meth"        : "Oh, I feel shitty. Need to recover with the use of fairies' pollen - it'll get better immediately and the world will become colorful again.",
        "neg_softcore"       : "Looks like I had too much sex. I had a blast but I feel depleted.",
        "neg_boner"          : "My pants are bursting from the boner. I need urgently to relieve stress.",
        "neg_blazing"        : "Why did I have to play chaste and ignore my sexual desires? Now it hurts like hell, I need to be relieved or it'll drive me insane!",
        "neg_dirty"          : "Ugh, I stink. It is necessary to wash, I disgust myself.",
        "neg_master_ill"     : "Damn it. My dick drips and burns whenever I go to the toilet. Some of these whores infected me with rotphilis!",
        "neg_cleaning"       : "I hate messing around in the mud. I'm a fucking slave trainer. What, there's no one in this house to clean up?!",
        "neg_cook"           : "To eat properly, I have to tinker in the kitchen with pans and dishes. What the hell?",
        "neg_food"           : "This is some kind of shit, not food. Why do I eat worse than some slaves?",
        "neg_housing"        : "I live in a decrepit hovel. No conditions for work and rest.",
        "neg_home_hygiene_value"     : "The house is a dirty mess. Just disgusting to be in here.",
        "neg_wealth"         : "I live just like some kind of beggar. Every penny has to be considered. I'm fed up with this!",
        "neg_accounts"       : "I have to engage in all the paper work. Need a secretary!",
        "neg_worn_clothes"   : "My clothes will not do! Just how long can I wash and mend them? I need to update my wardrobe.",
        "neg_master_cloth"   : "These clothes are very impractical. Just how long will I need to dress up like this?",
        "neg_alone"          : "I don't have a single slave at the moment. Somehow, it feels so lonely…",
        "neg_escape"         : "My slave ran away overnight while I was asleep. What a waste of money and time. Now I have to buy a new slave.",
        "neg_slave_suicidal" : "The ungrateful wretch tried to kill herself! My assistant managed to stop her, but no one slept well last night.",
        "neg_slave_died"     : "I didn't save the slave. Maybe I should have taken her to the hospital… Now it's too late.",
        "neg_slave_killed"   : "The slave died in training. I must be more careful with the merchandise in the future.",
        "neg_slave_starved"  : "I should have fed the slave more. Now I have to take on a new one…",
        "neg_rebell"         : "Slave doesn't listen to me at all. There's still a lot of work to be done…",
        "neg_grumpy"         : "Damn, what a dull person my slave is! I don't even want to work - boredom.",
        "neg_master_precious": "What a pity that I had to take my magic decoration off. It is my precious! I need to put it back and never take it off."
    }
}
define DIC_MASTER_CLEAN = [
    "This place is a pigsty; it’s depressing. \n  As you tidy up you can’t help but think that there is something wrong with this picture. A slaver of your caliber should <i>not</i> have to dirty your hands with such work. \n  Isn’t this what women are for?!",
    "Definition of a loser: a slaver who cleans his own house. With a sad sigh, you start cleaning, solemnly promising yourself that next time your slaves will do this task.",
    "Cleaning isn’t so bad; so long as someone else is doing it, but doing it with your own hands has never been your strong suit. Unfortunately, the place is a mess and it seems it is up to you. Cursing, you quickly clean up the house.",
    "You have enough experience as a butler to handle even a serious mess, but still, there is something seriously wrong when you have to clean your own house.",
    "For such an experienced butler as you, house cleaning, laundry, and dish washing are no trouble. It’s just that you are even better at guiding the work of others.",
    "It does not take long to get the place spic and span. You wash the dishes, shake off the dust, and do other small tasks quickly and efficiently. Nothing complicated, and you can do it without a maid if necessary.",
    "For the first-class butler that you are, your house is clean in no time. You wash the dishes, shake off the dust and do other small tasks quickly and efficiently. Nothing complicated, and you can do it without a maid if necessary."
]

define DIC_MASTER_REPUTATION_OBJECTIVES = {
    "camira_fame" : [
        "I am unknown by non-humans from the Camira House. But they will recognize me if I make at least one personal contract with a representative of this house. Some resident in the Quarter of the Outcasts must need a D+ slave!",
        "Thanks to my customers, I have received permission to live in the Quarter of the Outcasts. But I need to find more customers to start to get respect. I must find a resident there who needs a C+ slave.",
        "I know someone in the Camira House, but to get real influence and access to the Tierra del Citadel, I should make friends with some of the most influential non-humans. I must find one who wants a B+ slave.",
        "I have enough friends in the Camira House to get a pass to the Tierra del Citadel and be introduced to the most notable representatives of the House. I can foresee great bargains!",
        "Thanks to my friendship with the highest hierarchy of Camira House, I can get an interview with Mistress Tiamat, the leader of the Camira House.",
        "Tiamat personally recognized me as \"one of her flock\". This means that the Camira House will stand up for me in any difficult situation!",
        "Tiamat was pleased with her order. Nevertheless, I cannot become a patrician of Camira House, because I'm already a patrician.",
    ],
    "taurus_fame" :[
        "I have no relationship with the Taurus House. I ought to do direct sales in their territory. Some resident of the Bull Quarter must need a D+ slave!",
        "Someone from Taurus House heard of me already. That is enough to get permission to live in the Quarter of the Bull, but nothing more. I must find a resident there who needs a C+ slave.",
        "I made some useful contacts with the representatives of the Taurus House. But to be admitted to the White Palace, it is necessary to make someone important my customer. I must find one who wants a B+ slave.",
        "I have enough influential friends in the Taurus House to get access to the White Palace and start working with elite buyers!",
        "Now that I made friends with one of the top members of the Taurus House, I can get an audience with the King himself!",
        "The King personally initiated me into the knighthood and this means that now I am not just a man - Taurus House is behind me!",
        "The King was pleased with his order. Nevertheless, I cannot become a patrician of Taurus House, because I'm already a patrician.",
    ],
    "serpis_fame" : [
        "I am almost unknown to representatives of Serpis House. If I find at least a seedy client in the Serpentine Quarter - they will hear about me. Some resident in the Anthill must need a D+ slave!",
        "I have enough contacts in the Serpis House to obtain a residence permit in the Anthill, but no more. I need to work on my reputation. I must find a resident there who needs a C+ slave.",
        "Now I have a couple of friends, who are members of the Serpis House, but this is still not enough to access the Administrative Spires. It will be necessary to sell a slave to one of those big shots. I must find one who wants a B+ slave.",
        "I have made many useful connections in the Serpis House and I have enough of influence to go to the Administrative Spires and meet with those who run that place.",
        "Thanks to my acquaintance with the highest ranks of the Serpis House, I can get an audience with Mr. President and offer him my goods. A big step forward!",
        "I received a certificate of Serpis House honorary citizen personally from the hands of Mr. President. This is not a mere formality - there is real strength behind me now!",
        "The President was pleased with his order. Nevertheless, I cannot become a patrician of Serpis House, because I'm already a patrician.",
    ],
    "corvus_fame" : [
        "The undead do not notice me, as if I do not exist at all. If I want to make a name in the Corvus House, I need someone from the ghouls to be my client. Some resident of the Necropolis must need a D+ slave!",
        "Usually undead do not allow people like me to settle in the Necropolis, but I managed to achieve an exclusive status. However in the Corvus House I am still barely known. I must find a resident there who needs a C+ slave.",
        "I have some of acquaintances in the Corvus House, but they are not enough to gain entry to the Raven Tower. I need some of the nobles to be my clients. I must find one who wants a B+ slave.",
        "My fame as a supplier of slaves reached the Raven Tower and now I have the opportunity to meet with the high-ranking undead from Corvus House.",
        "Because I earned approval from the senior hierarchy of Corvus House, I have the opportunity to ask for an audience with the Prince of the Undead himself!",
        "The Prince of the Undead bestowed upon me a title of nobility. Now Corvus House will be on my side in any difficult situation!",
        "The Prince was pleased with his order. Nevertheless, I cannot become a patrician of Corvus House, because I'm already a patrician.",
    ],
    "brand_fame" : [
        "My brand is not known by anybody and this is bad for the price of slaves. I need to sell some slaves under my own brand or make them win competitions for me!",
        "Among all the brands of my guild, mine is valued less than others, but if I sell good slaves under my own brand to influential customers, it will quickly change.",
        "At least my brand is already known, even though it does not add special prices on slaves that I deliver. It is necessary to improve the quality of my goods to C+ or better!",
        "I am known as a supplier of quality products and girls with my brand on a hip are worth something. But this is not the major league yet. It is necessary to improve the quality of my goods to B+ or better!",
        "Work on my image has paid off. My brand is now known by everyone and I am recognized as a great trainer. Selling goods has never been so easy! But this is not the limit. I must improve the quality of my goods to A+ or better!",
        "Maybe I am overestimating myself, but I think that my brand is the best among all members of the guild. Even if I put it on a piece of shit, I will get sparks for that shit!",
    ]
}
define DIC_MASTER_EXCITEMENT = {
    -5: "Shriveled",
    -4: "Flaccid",
    -3: "Hanging",
    -2: "Cold",
    -1: "Sated",
    0: "Contented",
    1: "Aroused",
    2: "Ignited",
    3: "Heated",
    4: "Ardent",
    5: "Blazing",
}
define DIC_MASTER_EXCITEMENT_COLORED = {
    -5: "{color=#cd0000}Shriveled{/color}",
    -4: "{color=#be0000}Flaccid{/color}",
    -3: "{color=#af0000}Hanging{/color}",
    -2: "{color=#a00000}Cold{/color}",
    -1: "{color=#910000}Sated{/color}",
    0: "{color=#000000}Contented{/color}",
    1: "{color=#EA0090}Aroused{/color}",
    2: "{color=#6B0084}Ignited{/color}",
    3: "{color=#0000D8}Heated{/color}",
    4: "{color=#009FEF}Ardent{/color}",
    5: "{color=#009900}Blazing{/color}"
}
define DIC_MASTER_STAT_MAPPING = {
    "STRENGTH": ("strength_value_1", "strength_experience_value_1"),
    "PERSONALITY": ("personality_value_2", "personality_experience_value_2"),
    "LIBIDO": ("libido_value_4", "libido_experience_value_4"),
    "DOMINANCE": ("dominance_value_5", "dominance_experience_value_5"),
    "BRAND REPUTATION": ("brand_reputation_value_6", "brand_reputation_experience_value_6"),
    "GUILD REPUTATION": ("guild_reputation_value_7", "guild_reputation_experience_value_7"),
    "HYGIENE": ("hygiene_value_9", "hygiene_experience_value_9"),
    "INJURIES": ("injuries_value_11", "injuries_experience_value_11"),
    "TEACHING": ("teaching_value_12", "teaching_experience_value_12"),
    "STEWARDSHIP": ("stewardship_value_13", "stewardship_experience_value_13"),
    "ARTISTRY": ("artistry_value_14", "artistry_experience_value_14"),
    "MEDIC": ("medic_value_15", "medic_experience_value_15"),
    "FIGHTER": ("fighter_value_16", "fighter_experience_value_16"),
    "MAGIC": ("magic_value_17", "magic_experience_value_17"),
    "FLAGELLATION": ("flagellation_value_18", "flagellation_experience_value_18"),
    "TORTURE": ("torture_value_19", "torture_experience_value_19"),
    "BINDING": ("binding_value_20", "binding_experience_value_20"),
    "PETTING": ("petting_value_21", "petting_experience_value_21"),
    "ORAL SEX": ("oral_sex_value_22", "oral_sex_experience_value_22"),
    "PENETRATION": ("penetration_value_23", "penetration_experience_value_23"),
    "FETISHISM": ("fetishism_value_24", "fetishism_experience_value_24"),
}
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################

default strength_textvalue_1 = ""
default personality_textvalue_2 = ""
default allure_textvalue_3 = ""
default libido_textvalue_4 = ""
default dominance_textvalue_5 = ""
default brand_reputation_textvalue_6 = ""
default guild_reputation_textvalue_7 = ""
default standard_of_living_textvalue_8 = ""
default hygiene_textvalue_9 = ""
default mood_textvalue_10 = ""
default not_injuries_textvalue_11 = ""
default teaching_textvalue_12 = ""
default stewardship_textvalue_13 = ""
default artistry_textvalue_14 = ""
default medic_textvalue_15 = ""
default fighter_textvalue_16 = ""
default magic_textvalue_17 = ""
default flagellation_textvalue_18 = ""
default torture_textvalue_19 = ""
default binding_textvalue_20 = ""
default petting_textvalue_21 = ""
default oral_sex_textvalue_22 = ""
default penetration_textvalue_23 = ""
default fetishism_textvalue_24 = ""
default reputation_textvalue_1 = ""
default excitement_textvalue = ""
################################## values -rec3ks

default strength_value_1 = 0
default personality_value_2 = 0
default allure_value_3 = 0
default libido_value_4 = 0
default dominance_value_5 = 0
default brand_reputation_value_6 = 0
default guild_reputation_value_7 = 0
default standard_of_living_value_8 = 0
default hygiene_value_9 = 0
default mood_value_10 = 0
default injuries_value_11 = 0
default teaching_value_12 = 0
default stewardship_value_13 = 0
default artistry_value_14 = 0
default medic_value_15 = 0
default fighter_value_16 = 0
default magic_value_17 = 0
default flagellation_value_18 = 0
default torture_value_19 = 0
default binding_value_20 = 0
default petting_value_21 = 0
default oral_sex_value_22 = 0
default penetration_value_23 = 0
default fetishism_value_24 = 0
default reputation_value_1 = 0
default excitement_value = 0

############################################# number value -rec3ks
default strength_experience_value_1 = 0
default personality_experience_value_2 = 0
#default allure_experience_value_3 = 0
default libido_experience_value_4 = 0
default dominance_experience_value_5 = 0
default brand_reputation_experience_value_6 = 0
default guild_reputation_experience_value_7 = 0
#default standard_of_living_experience_value_8 = 0
default hygiene_experience_value_9 = 0
#default mood_experience_value_10 = 0
default injuries_experience_value_11 = 0
default teaching_experience_value_12 = 0
default stewardship_experience_value_13 = 0
default artistry_experience_value_14 = 0
default medic_experience_value_15 = 0
default fighter_experience_value_16 = 0
default magic_experience_value_17 = 0
default flagellation_experience_value_18 = 0
default torture_experience_value_19 = 0
default binding_experience_value_20 = 0
default petting_experience_value_21 = 0
default oral_sex_experience_value_22 = 0
default penetration_experience_value_23 = 0
default fetishism_experience_value_24 = 0
default excitement_experience_value = 0
############################################ textvalue track - herculean
############################################ value track - 5
############################################ number value track 999/999
# default armour_25 = ""
# default Shoulder_26 = ""
# default left_hand_27 = ""
# default righ_hand_28 = ""
# default sleeve_holster_29 = ""
# default boot_holster_30 = ""
default clothes_31 = ""
default headgear_32 = ""
default earring_33 = ""
default neck_34 = ""
default ring_35 =""
##################################################
default faction_36 =""
default sparks_37 =""
###################################################
default master_visage = 0
default master_haircut = 0
default mc ="Jack"
default master_supermacy = 0
default characterOnlyNameIndex = 0
default master_worn_bonus = 0
default master_temporal_mood = 0
default master_past_mood = 0
default master_screen_text = ""
default blazing_counter = 0
default pos_show_counter = 0
default description_master_attributes_track_value = ""
default master_mood_state = {
    "good_mood": {
        "pos_energy"         : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_new_slave"      : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_housing"        : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_house_clean"    : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_master_cloth"   : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_self_clean"     : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_toilet"         : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_nice_slave"     : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_massage"        : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_good_morning"   : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_satisfied"      : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_optimism"       : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_good_pet"       : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_show"           : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_self_food"      : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_date"           : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_master_winner"  : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_deal"           : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_wealth"         : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_kannabis"       : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_drunk"          : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_opium"          : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_bahus"          : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "pos_master_precious": {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1}
    },
    "bad_mood": {
        "neg_master_loser"   : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_boring"         : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_tired"          : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_drunk"          : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_wounded"        : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_no_koffe"       : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_no_opium"       : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_no_meth"        : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_softcore"       : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_boner"          : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_blazing"        : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_dirty"          : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_master_ill"     : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_cleaning"       : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_cook"           : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_food"           : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_housing"        : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_home_hygiene_value": {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_wealth"         : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_accounts"       : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_worn_clothes"   : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_master_cloth"   : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_alone"          : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_escape"         : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_slave_suicidal" : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_slave_died"     : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_slave_killed"   : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_slave_starved"  : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_rebell"         : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_grumpy"         : {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1},
        "neg_master_precious": {"permanent": False , "accustomed": False, "accustomed_value": 5, "active": False, "weight": 1, "duration": 1, "default_duration": 1}
    }
}
default master_house_reputation = {
    "home_estate": "",
    "camira_house": 0,
    "serpis_house": 0,
    "taurus_house": 0,
    "corvus_house": 0,
}
default master_combat_equipment = {
    "armour":"Without armour",
    "weapon":"Fist",
    "weapon2":"Fist",
    "amulet":"",
    "ring":"",
}
default master_equipment = {
    "clothes":"Worn clothes",
    "headgear":"",
    "earrings":"",
    "neck":"",
    "accessories1":"",
    "accessories2":"",
    "accessories3":"",
    "accessories4":"",
    "accessories5":"",
}
