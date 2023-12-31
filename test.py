import json
 
# Opening JSON file
f = open('assets/dados.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data:
    print(data[i]['country'])
 
# Closing file
f.close()