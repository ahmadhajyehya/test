import json

json_file = open('nested_data.json', 'r')
data = json.load(json_file)
for user in data['users']:
    print(user)
