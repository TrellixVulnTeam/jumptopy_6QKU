def main_interface():
    print("<<Json기반 주소록 관리 프로그램>>")
    print("1. 학생 정보입력")
    print("2. 학생 정보조회")
    print("3. 학생 정보수정")
    print("4. 학생 정보삭제")
    print("5. 프로그램 종료")

def register_interface():
    st_name = str(input("이름 : "))
    st_old = str(input("나이 : "))
    st_address = str(input("주소 :"))
    return [st_name, st_old, st_address]

def past_interface():
    class_past_count = str(input("과거 수강 횟수 :"))
    return [class_past_count]

def class_interface():
    class_code = str(input("강의 코드 :"))
    class_name = str(input("강의명 :"))
    class_teacher = str(input("강사 :"))
    class_start = str(input("개강일 :"))
    class_end = str(input("종료일 :"))
    return [class_code,class_name,class_teacher,class_start,class_end]

def second_interface():
    print("조회하실 학생 정보를 선택하시오")
    print("1. ID 검색")
    print("2. 이름 검색")
    print("3. 나이 검색")
    print("4. 주소 검색")
    print("5. 과거수강횟수 검색")
    print("6. 강의코드 검색")
    print("7. 강의명 검색")
    print("8. 강사 검색")

if __name__ == "__main__":
    print(register_interface())