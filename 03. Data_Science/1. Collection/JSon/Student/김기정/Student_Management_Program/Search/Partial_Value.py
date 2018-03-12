from Checkfile import load_json_file

def check_value(input,key):         # id 혹은 과거수강경력
    index = 0
    while True:
        storage = []
        if index < len(load_json_file()):
            for dic_data in load_json_file():
                if input in dic_data[key]:
                    storage.append(dic_data[key])
                    index += 1
        return storage

def check_value_student(input,key):         # 학생조회
    index = 0
    while True:
        storage = []
        if index < len(load_json_file()):
            for dic_data in load_json_file():
                if input in dic_data["개인정보"][key]:
                    storage.append(dic_data["개인정보"][key])
                    index += 1
        return storage

def check_value_institute(input,key):         # 수업조회
    index = 0
    while True:
        storage = []
        if index < len(load_json_file()):
            for dic_data in load_json_file():
                for x in range(len(dic_data["수강정보"]) - 1):
                    if input in dic_data["수강정보"]["강좌"+str(x)][key]:
                        storage.append(dic_data["수강정보"]["강좌"+str(x)][key])
                        index += 1
        return storage