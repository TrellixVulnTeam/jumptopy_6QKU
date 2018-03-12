from Environment import Interface

def student_return_info():
    personnel_dir = {}
    import_data = Interface.register_interface()
    personnel_info = import_data[:]
    personnel_info = dict(zip(["이름", "나이", "주소"], personnel_info))
    personnel_dir["개인정보"] = personnel_info
    return personnel_dir


