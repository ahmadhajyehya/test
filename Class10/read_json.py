import json

json_file = open('data.json', 'r')
data = json.load(json_file)
print(data)
