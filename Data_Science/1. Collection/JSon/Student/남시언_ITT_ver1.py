import json

def Main_Display():
    print("<<json기반 주소록 관리 프로그램>>")
    print("1. 학생 정보입력")
    print("2. 학생 정보조회")
    print("3. 학생 정보수정")
    print("4. 학생 정보삭제")
    print("5. 프로그램 종료")

def Student_info_Create():
    temp=[] # 여러개의 강의 정보를 입력할때 쓰는 리스트
    Action_Flag=0
    name = input("이름을 입력하세요")
    age = input("나이를 입력하세요")
    addr = input("주소도 입력하세요")
    print('강의 관련 정보를 입력합니다.')
    count = input("과거 수강 횟수 입력")

    while 1:
        code = input('강의코드를 입력하세요(생략시 엔터 입력)')#########여기서부터 생략 가능
        if code == '':
            break
        else:
            lecture_name = input('강의명을 입력하세요')  #
            teacher_name = input('강사명을 입력하세요')  #
            Starting_Date = input('개강일을 입력하세요')  #
            End_Date = input('종료일을 입력하세요')  #
            temp.append([code]+[lecture_name]+[teacher_name]+[Starting_Date]+[End_Date])
            Action_Flag=1

    additional={'과거수강횟수':count}
    append=[]
    if Action_Flag==1:
        for i in range(len(temp)):# 문법 오류는 없으나 자꾸 덮어씌운다.
            # temp2['강의관련 정보'] = [{'강의코드':temp[i][0],'강의명':temp[i][1],'강사명':temp[i][2],'개강일':temp[i][3],'종료일':temp[i][4]}]
            append.append({'강의코드': temp[i][0], '강의명': temp[i][1], '강사명': temp[i][2], '개강일': temp[i][3], '종료일': temp[i][4]})
    print(append)
    additional['강의관련 정보']=append
    # Input_Data.update(temp2) #딕셔너리 뒤에 딕셔너리 붙이기. 리스트의 append 같은 개념
    Input_Data = {'이름': name, '나이': age, '주소': addr, '종합정보':additional}
    print(Input_Data)
    IDnumber="ITT"+str(len(Students_Info_List)+1).zfill(3)
    Input_Data['학생 ID']=IDnumber

    Students_Info_List.append(Input_Data)
    print("리스트에 추가되었습니다.")

def Student_search(search_word,Option,Depth):
    count = 0
    i = 0
    temp = [] # 학생 ID 를 수집하기 위해(여러개의 데이터가 나올때 보여줘야 되니까) 임시로 만든 리스트

    if Depth=="1":# 가장 바깥쪽 딕셔너리의 key를 찾는 경우
        Uniq_Flag = 1  # 오직 하나의 데이터만 찾은 경우에만 참이 되도록 유지.
        Uniq_order = 0 # 고유한 데이터가 몇번째 딕셔너리에 들어있는지 기억하자
        while i<len(Students_Info_List):
            if search_word in Students_Info_List[i][Option]:#
                print(i)
                count+=1
                temp.append(Students_Info_List[i]["학생 ID"])
                print(Uniq_Flag,count)
                if Uniq_Flag == 1 and count == 1: # 뭔가를 찾은 기록이 있고 고유깃발이 켜진 상태면
                    print(i)
                    Uniq_order = i #현재의 위치를 기억한다.
                    # print(Uniq_order,Uniq_Flag)
                Uniq_Flag=0
            i+=1
        if count==1:# 검색결과가 하나만 있다면 검색 결과의 모든 정보 출력
            print(Uniq_order)
            print(Students_Info_List[Uniq_order])
        elif count>1:# 검색결과가 2개 이상이라면 학생 ID들만 출력
            for i in range(len(temp)):
                print("%s "%temp[i],end="")
            print()
        elif count==0:
            print('%s을(를) 찾을 수 없습니다.' % search_word)
    elif Depth == "2": # 딕셔너리안의 딕셔너리의 key를 찾는 경우
        Uniq_Flag=1  # 오직 하나의 데이터만 찾은 경우에 참이 되도록 유지.
        Uniq_order=0 # 고유한 데이터가 몇번째 딕셔너리에 들어있는지 기억하자
        while i<len(Students_Info_List):
            if search_word in Students_Info_List[i]["종합정보"][Option]:  # 딕셔너리 안의 딕셔너리를 참조 할땐 다르게 해야됨
                count+=1
                temp.append(Students_Info_List[i]["학생 ID"])
                if Uniq_Flag==1 & count > 0: # 뭔가를 찾은 기록이 있고 고유깃발이 켜진 상태면
                    Uniq_order=i
                Uniq_Flag=0
            i+=1
        if count==1:# 검색결과가 하나만 있다면 검색 결과의 모든 정보 출력
            print(Students_Info_List[Uniq_order])
        elif count>1:# 검색결과가 2개 이상이라면 학생 ID들만 출력
            for i in range(len(temp)):
                print("%s "%temp[i],end="")
            print()
        elif count==0:
            print('%s을(를) 찾을 수 없습니다.' % search_word)
    elif Depth == "3": # 가장 깊숙한 그곳.
        Uniq_Flag = 1  # 오직 하나의 데이터만 찾은 경우에 참이 되도록 유지.
        Uniq_order = 0 # 고유한 데이터가 몇번째 딕셔너리에 들어있는지 기억하자
        while i < len(Students_Info_List):
            for j in range(len(Students_Info_List[i]["종합정보"]["강의관련 정보"])): # 과목 몇개인지 갯수 잘 센다.
                if search_word in Students_Info_List[i]["종합정보"]["강의관련 정보"][j].get(Option):
                    count += 1
                    temp.append(Students_Info_List[i]["학생 ID"])
                    if Uniq_Flag == 1 & count > 0:  # 뭔가를 찾은 기록이 있고 고유깃발이 켜진 상태면
                        Uniq_order = i
                    Uniq_Flag = 0
            i += 1
        if count == 1:  # 검색결과가 하나만 있다면 검색 결과의 모든 정보 출력
            print(Students_Info_List[Uniq_order])
        elif count > 1:  # 검색결과가 2개 이상이라면 학생 ID들만 출력
            for i in range(len(temp)):
                print("%s " % temp[i], end="")
            print()
        elif count == 0:
            print('%s을(를) 찾을 수 없습니다.'%search_word)

def Student_info_Read(Condition):
    search_word=input("검색어를 입력하세요")
    if Condition=='1':#학생 ID로 검색
        Student_search(search_word,"학생 ID","1")# 3번째 파라미터 값은 Depth를 의미. 찾으려는 key값이 몇번을 딕셔너리 안으로 들어가야 되는지를 뜻함
    elif Condition=='2':# 학생 이름으로 검색
        Student_search(search_word, "이름","1")
    elif Condition=='3':# 나이로 검색
        Student_search(search_word, "나이","1")
    elif Condition== '4':# 주소로 검색
        Student_search(search_word, "주소","1")
    elif Condition=='5': # 과거 수강 횟수로 검색
        Student_search(search_word, "과거수강횟수","2")
    elif Condition=='6': # 현재 수강 과목의 강의명
        Student_search(search_word, "강의명","3")
    elif Condition=='7': # 현재 수강 과목의 강사명
        Student_search(search_word, "강사명","3")

def Student_info_Modified():####데이터 수정하기
    select=input("수정하려는 학생의 ID를 입력해주세요")
    i=0
    Found=0
    while i<len(Students_Info_List):
        if select in Students_Info_List[i]["학생 ID"]:
            # print("있다")
            Found=1
            break
        i += 1
    if Found==1:# 검색한 데이터를 찾았을 경우에만.
        print("1.학생ID 2.학생이름 3. 학생나이 4.학생주소 5.과거수강횟수 6.강사명 7.강의명 8.강의코드 9.개강일 10.종료일")
        Key = input("수정할 key 값을 입력하세요(번호선택 또는 직접 입력")
        if Key=='1' or Key=='학생 ID':
            Students_Info_List[i]['학생 ID']=input("바꿔 넣을 Value값을 입력하세요")
        elif Key=='2' or Key=='이름':
            Students_Info_List[i]['이름']=input("바꿔 넣을 Value값을 입력하세요")
        elif Key=='3' or Key=='나이':
            Students_Info_List[i]['나이']=input("바꿔 넣을 Value값을 입력하세요")
        elif Key=='4' or Key=='주소':
            Students_Info_List[i]['주소']=input("바꿔 넣을 Value값을 입력하세요")
        elif Key=='5' or Key=='과거수강횟수':
            Students_Info_List[i]['종합정보']['과거수강횟수']=input("바꿔 넣을 Value값을 입력하세요")
        elif Key=='6' or Key=='강사명':#####################################################헬...#########################################################################
            input_code=input('수정하기 위해서 해당 데이터의 강의코드를 입력해주세요.')######### 하필 강의코드냐면.. 고유한 키 값 같아서!
            for j in range(len(Students_Info_List[i]['종합정보']['강의관련 정보'])):
                if  input_code == Students_Info_List[i]['종합정보']['강의관련 정보'][j].get('강의코드'):
                    Students_Info_List[i]['종합정보']['강의관련 정보'][j]['강사명'] = input("바꿔 넣을 Value값을 입력하세요")

        elif Key=='7' or Key=='강의명':
            input_code = input('수정하기 위해서 해당 데이터의 강의코드를 입력해주세요.')  ######### 하필 강의코드냐면.. 고유한 키 값 같아서!
            for j in range(len(Students_Info_List[i]['종합정보']['강의관련 정보'])):
                if input_code == Students_Info_List[i]['종합정보']['강의관련 정보'][j].get('강의코드'):
                    Students_Info_List[i]['종합정보']['강의관련 정보'][j]['강의명'] = input("바꿔 넣을 Value값을 입력하세요")

        elif Key=='8' or Key=='강의코드':
            input_code = input('수정하기 위해서 해당 데이터의 강의코드를 입력해주세요.')  ######### 하필 강의코드냐면.. 고유한 키 값 같아서!
            for j in range(len(Students_Info_List[i]['종합정보']['강의관련 정보'])):
                if input_code == Students_Info_List[i]['종합정보']['강의관련 정보'][j].get('강의코드'):
                    Students_Info_List[i]['종합정보']['강의관련 정보'][j]['강의코드'] = input("바꿔 넣을 Value값을 입력하세요")

        elif Key=='9' or Key=='개강일':
            input_code = input('수정하기 위해서 해당 데이터의 강의코드를 입력해주세요.')  ######### 하필 강의코드냐면.. 고유한 키 값 같아서!
            for j in range(len(Students_Info_List[i]['종합정보']['강의관련 정보'])):
                if input_code == Students_Info_List[i]['종합정보']['강의관련 정보'][j].get('강의코드'):
                    Students_Info_List[i]['종합정보']['강의관련 정보'][j]['개강일'] = input("바꿔 넣을 Value값을 입력하세요")

        elif Key=='10' or Key=='종료일':
            input_code = input('수정하기 위해서 해당 데이터의 강의코드를 입력해주세요.')  ######### 하필 강의코드냐면.. 고유한 키 값 같아서!
            for j in range(len(Students_Info_List[i]['종합정보']['강의관련 정보'])):
                if input_code == Students_Info_List[i]['종합정보']['강의관련 정보'][j].get('강의코드'):
                    Students_Info_List[i]['종합정보']['강의관련 정보'][j]['종료일'] = input("바꿔 넣을 Value값을 입력하세요")

def Student_info_delete():# 회원 데이터 삭제하기
    select=input("삭제하려는 학생의 ID를 입력해주세요")
    i=0
    Found=0
    while i<len(Students_Info_List):
        if select in Students_Info_List[i]["학생 ID"]:
            Found=1
            break
        i += 1
    if Found==1:# 검색한 데이터를 찾았을 경우에만.
        yes_no=input("아이디 "+Students_Info_List[i]["학생 ID"]+"를 정말로 삭제하시겠습니까? y/n")
        if yes_no=='y' or 'yes':
            del Students_Info_List[i]
        else:
            print("취소")

def Save_Data(jsonResult):
    with open(json_file_name,'w',encoding='utf8') as outfile:
        readable_result=json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
        print(json_file_name+' Saved')

json_file_name='ITT_Student.json'#####################################entry point
try:# json 파일이 있는 경우 읽고
    with open(json_file_name,encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        Students_Info_List = json.loads(json_string)
        print(json_file_name + "Loaded")
        # print(Students_Info_List)
except: # 없는 경우.
    print("경로에 파일이 없습니다. 어떻게 하시겠습니까?")
    choice=input("1. 경로를 입력합니다. 2. 기본 경로로 생성하겠습니다.")
    if choice=='1':
        json_file_name=input("경로를 입력하세요.")
    elif choice=='2':# 프로그램 끌때 생성하는 걸로 ..
        pass
    Students_Info_List=[]###
    IDcount=0

while True:
    Main_Display()
    select=input("메뉴를 선택하세요")
    if select=='1':#학생 정보 입력
        Student_info_Create()
    elif select=='2': # 검색
        print('데이터를 읽기 위해 검색을 합니다.')
        print('검색 조건을 선택하세요')
        print("1.ID 2.이름 3.나이 4.주소 5.과거 수강 횟수")
        Condition=input('6.현재 수강 과목의 강의명 7.현재 수강 과목의 강사명')
        Student_info_Read(Condition)
    elif select=='3': # 학생 정보 수정
        Student_info_Modified()
    elif select=='4': # 학생 정보 삭제
        Student_info_delete()
    elif select=='5':
        Save_Data(Students_Info_List)
        print("프로그램을 종료합니다.")
        break