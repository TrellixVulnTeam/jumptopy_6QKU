from Environment import Interface

def past_class_info():
    past_class_dir = {}
    import_data = Interface.past_interface()
    past_info = import_data[0]
    past_info = dict(zip(["과거수강횟수"], past_info))
    past_class_dir = past_info
    return past_class_dir

def institute_return_info(count):
    institute_dir = {}
    import_info = Interface.class_interface()
    institute_info = import_info[:]
    institute_info = dict(zip(["강의코드", "강의명", "강사", "개강일", "종료일"],institute_info))
    institute_dir["강좌"+str(count)] = institute_info
    return institute_dir


