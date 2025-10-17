import os
import re
superlist = []
count = 0
content = ["mc_stats_iniciation.rpy","dictionary.rpy","girls_stats_iniciation.rpy"]
ubication = "c:\\Users\\User\\Downloads\\Jack_o_nine_tails_renpy\\game\\"
for file in os.listdir(ubication):
    if file in content:
        if count % 10 == 0:
            print("Reading")
        if file.endswith(".rpy"):
            with open(ubication + file, "r", encoding="utf-8") as f:
                for linea in f:
                    if linea.startswith("define"):
                        a = linea[6:].split("=")[0]
                        _ = a.replace(" ","").replace(":","")
                        superlist.append(_)
    count += 1

for file in os.listdir(ubication):
    if count % 10 == 0:
        print("Writing")
    if file.endswith(".rpy") and file != "gui.rpy":
        with open(ubication + file, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        with open(ubication + file, "w", encoding="utf-8") as f:
            for linea in lineas:
                for i in superlist:
                    if i in linea:
                        linea = re.sub(rf"\b{i}\b|\b{i}(?=\[)", i.upper(), linea)
                f.write(linea)
    count += 1
print("finish")
         



    


        