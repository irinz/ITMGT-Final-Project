# Dumps the final processed verbs into the dict 
# IMPORTANT: DO NOT run this anymore since the dict has been completed already

import json 

filodict = open("filo_dict.json", "r")
pandiwafile = open("pandiwa_text_processed_final.txt", "r")
allwords = json.load(filodict)

for line in pandiwafile:
    allwords.append(line.strip("\n"))

allwords = list(set(allwords))
allwords.sort()
filodict.close()
filodict = open("filo_dict.json", "w")
json.dump(allwords, filodict)