import json



with open('words.json', 'w') as json_file:
    json.dump(common.json, json_file, indent=4)