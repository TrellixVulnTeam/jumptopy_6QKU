import json

json_file_name = 'jtbcnews_facebook_2018-01-01_2018-01-11.json'

print('JSON File Load Start..')

with open(json_file_name,encoding='UTF8') as json_file: json_object = json.load(json_file)

json_string = json.dumps(json_object)

json_big_data = json.loads(json_string)

print('JSON File Load End..')

