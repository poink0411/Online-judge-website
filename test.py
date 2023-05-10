import json
data = {}
with open('./data/user_info.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

data['21053']['problems_solved'].append(1002)

with open('./data/user_info.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent=4)