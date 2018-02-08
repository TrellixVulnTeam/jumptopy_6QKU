import json
import os
import time
import GetWeatherInfo, GetPollutionInfo

dir_name = time.strftime("%m%d", time.localtime(time.time()))
dir_weather = "weather"
dir_pollution = "pollution"
dir_movie = "movie"
file_number = time.strftime("%H%M%S", time.localtime(time.time()))
weather_file = "Weather_Info"
pollution_file = "Pollution_Info"
movie_file = "Movie_Info"
file_delimeter = "//"
json_form = ".json"
weather_address = dir_name + file_delimeter + dir_weather + file_delimeter
pollution_address = dir_name + file_delimeter + dir_pollution + file_delimeter

def allfiles(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(file)
    return file_list

def file_date_output(path):
    date_list = []
    file_list = allfiles(path)
    for i in range(len(file_list)):
        date = file_list[i].split("_")
        date_list.append(date[0])
    return date_list

def file_sorting(path):
    file_date_sorting = sorted(file_date_output(path), reverse=True)
    for i in range(len(allfiles(path))):
        if file_date_sorting[0] in allfiles(path)[i]:
            return allfiles(path)[i]

def auto_save_weatherinfo():
    destination_json = weather_address + file_number + "_" + weather_file + json_form
    with open(destination_json, 'w', encoding='utf8') as outfile:
        retJson = json.dumps(GetWeatherInfo.main(), indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

def auto_save_pollutioninfo():
    destination_json = pollution_address + file_number + "_" + pollution_file + json_form
    with open(destination_json, 'w', encoding='utf8') as outfile:
        retJson = json.dumps(GetPollutionInfo.main(),indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

# def auto_save_movieinfo():
#     destination_json = dir_name + file_delimeter + dir_movie + file_delimeter + file_number + "_" + movie_file + json_form
#     with open(destination_json, 'w', encoding='utf8') as outfile:
#         retJson = json.dumps("xx", indent=4, sort_keys=True, ensure_ascii=False)
#         outfile.write(retJson)

def auto_load_weatherinfo():
    destination_json = dir_name + file_delimeter + dir_weather + file_delimeter + file_sorting(weather_address)
    with open(destination_json, encoding='utf8') as weather_data:
        json_data_load = json.load(weather_data)
        json_data_string = json.dumps(json_data_load)
        json_big_data = json.loads(json_data_string)
    return json_big_data

def auto_load_pollutioninfo():
    destination_json = dir_name + file_delimeter + dir_pollution + file_delimeter + file_sorting(pollution_address)
    with open(destination_json, encoding='utf8') as pollution_data:
        json_data_load = json.load(pollution_data)
        json_data_string = json.dumps(json_data_load)
        json_big_data = json.loads(json_data_string)
        return json_big_data

# def auto_load_movieinfo():
#    with open(destination_json, encoding='utf8') as pollution_data:
#         json_data_load = json.load(pollution_data)
#         json_data_string = json.dumps(json_data_load)
#         json_big_data = json.loads(json_data_string)
#     return json_big_data

