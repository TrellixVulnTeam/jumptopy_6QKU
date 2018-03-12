import json

def Main_Display():
    print("<<json기반 주소록 관리 프로그램>>")
    print("1. 학생 정보입력")
    print("2. 학생 정보조회")
    print("3. 학생 정보수정")
    print("4. 학생 정보삭제")
    print("5. 프로그램 종료")

def Student_ID_num_Create():
    # if 0 == len(Students_Info_List):
    if not Students_Info_List: # 빈 리스트라면..== 정상적으로 프로그램을 만들었다면 처음 만든 경우밖에 없음
        IDnumber = "ITT001"
        return IDnumber
    else:
        temp = list(Students_Info_List[-1]["학생 ID"])
        hund = int(temp[3]) * 100
        ten = int(temp[4]) * 10
        one = int(temp[5])
        return "ITT" + str(hund + ten + one + 1).zfill(3)

def Student_info_Create():
    temp=[] # 여러개의 강의 정보를 입력할때 쓰는 리스트
    Action_Flag=0
    Message_List=["이름을 입력하세요(예: 홍길동) : ", "나이를 입력하세요(예: 25) : ", "주소를 입력하세요(예: 대구광역시 동구 신암동 144-22) : ",
                  "과거 수강 횟수를 입력하세요 : ", "강의코드를 입력하세요(예: IB171106)(생략시 엔터 입력) : ", "강의명을 입력하세요(예: IoT 빅데이터 실무반) : ",
                  "강사명을 입력하세요(예: 임꺽정) : ", "개강일을 입력하세요(예: 1970-01-01) : ","종료일을 입력하세요(예: 2018-12-31) : "]
    name = input(Message_List[0])
    age = input(Message_List[1])
    addr = input(Message_List[2])
    count = input(Message_List[3])

    Answer=input('현재 수강중인 과목이 있습니까? (y/n) : ')
    if Answer == 'y' or Answer=='1' or Answer=='yes':
        Add_Message=''
        while 1:
            if Action_Flag==1:
                Add_Message='추가 '
            code = input("%s%s" %(Add_Message,Message_List[4]))  #########여기서부터 생략 가능
            if code == '':
                break
            else:
                lecture_name = input(Message_List[5])  # 강의명
                teacher_name = input(Message_List[6])  # 강사명
                Starting_Date = input(Message_List[7])  # 개강일
                End_Date = input(Message_List[8])  # 종료일
                temp.append([code] + [lecture_name] + [teacher_name] + [Starting_Date] + [End_Date])
                Action_Flag = 1

    additional={'과거수강횟수':count}
    lecture_info=[]
    if Action_Flag==1:
        # print("템플릿의 길이는? %d"%len(temp))
        for i in range(len(temp)):
            # temp2['강의관련 정보'] = [{'강의코드':temp[i][0],'강의명':temp[i][1],'강사명':temp[i][2],'개강일':temp[i][3],'종료일':temp[i][4]}]
            lecture_info.append({'강의코드': temp[i][0], '강의명': temp[i][1], '강사명': temp[i][2], '개강일': temp[i][3], '종료일': temp[i][4]})

    additional['강의관련 정보']=lecture_info
    # Input_Data.update(temp2) #딕셔너리 뒤에 딕셔너리 붙이기. 리스트의 append 같은 개념
    Input_Data = {'이름': name, '나이': age, '주소': addr, '종합정보':additional}

    Input_Data['학생 ID']=Student_ID_num_Create()#########ID 넣기

    Students_Info_List.append(Input_Data)
    Student_Data_print(Students_Info_List[-1])  ###입력한 데이터 잘 나오나 확인하기
    print("리스트에 추가되었습니다.\n")

def Student_Data_print(data):
    print('\n"이름": "%s",'%data["이름"])
    print('"나이": "%s",'%data["나이"])
    print('"주소": "%s",'%data["주소"])
    print('"학생 ID": "%s",'%data["학생 ID"])
    print('"종합정보": \n{')#######여기까지 depth 1. 종합정보 안의 내용 보여주기 시작.

    print('\t"과거수강횟수": "%s",'%data["종합정보"]["과거수강횟수"]) ###여기부터 depth 2
    print('\t"강의관련 정보": ')

    for i in range(len(data["종합정보"]["강의관련 정보"])):###for문 안이 depth 3
        print("\t[") # 강의관련 정보의 시작
        print('\t\t"강사명": "%s",'%data["종합정보"]["강의관련 정보"][i]["강사명"])
        print('\t\t"강의명": "%s",'%data["종합정보"]["강의관련 정보"][i]["강의명"])
        print('\t\t"강의코드": "%s",'%data["종합정보"]["강의관련 정보"][i]["강의코드"])
        print('\t\t"개강일": "%s",'%data["종합정보"]["강의관련 정보"][i]["개강일"])
        print('\t\t"종료일": "%s"' % data["종합정보"]["강의관련 정보"][i]["종료일"])
        if (i+1)!=len((data["종합정보"]["강의관련 정보"])): # 끝이 아닐때는 콤마 찍고
            print("\t],")
        else: # 끝일때는 콤마 안찍는다.
            print("\t]") # 강의관련 정보의 끝
    print("}\n")#종합정보의 끝

def Student_search(search_word,Option,Depth):
    count = 0
    i = 0
    temp = [] # 학생 ID 를 수집하기 위해(여러개의 데이터가 나올때 보여줘야 되니까) 임시로 만든 리스트

    if Depth=="1":# 가장 바깥쪽 딕셔너리의 key를 찾는 경우
        Uniq_Flag = 1  # 오직 하나의 데이터만 찾은 경우에만 참이 되도록 유지.
        Uniq_order = 0 # 고유한 데이터가 몇번째 딕셔너리에 들어있는지 기억하자
        while i<len(Students_Info_List):
            if search_word in Students_Info_List[i][Option]:#
                count+=1
                temp.append(Students_Info_List[i]["학생 ID"])
                if Uniq_Flag == 1 and count == 1: # 뭔가를 찾은 기록이 있고 고유깃발이 켜진 상태면
                    Uniq_order = i #현재의 위치를 기억한다.
                Uniq_Flag=0
            i+=1
        if count==1:# 검색결과가 하나만 있다면 검색 결과의 모든 정보 출력
            # print(Students_Info_List[Uniq_order])
            Student_Data_print(Students_Info_List[Uniq_order])
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
            Student_Data_print(Students_Info_List[Uniq_order])
        elif count>1:# 검색결과가 2개 이상이라면 학생 ID들만 출력
            for i in range(len(temp)):
                print("%s "%temp[i],end="")
            print()
        elif count==0:
            print('%s을(를) 찾을 수 없습니다.' % search_word)
    elif Depth == "3": # 레벨이 가장 높은 곳. 깊은 곳
        Uniq_Flag = 1  # 오직 하나의 데이터만 찾은 경우에 참이 되도록 유지.
        Uniq_order = 0 # 고유한 데이터가 몇번째 딕셔너리에 들어있는지 기억하자
        while i < len(Students_Info_List):
            for j in range(len(Students_Info_List[i]["종합정보"]["강의관련 정보"])): # 과목 몇개인지 갯수 센다.
                if search_word in Students_Info_List[i]["종합정보"]["강의관련 정보"][j].get(Option):
                    count += 1
                    temp.append(Students_Info_List[i]["학생 ID"])
                    if Uniq_Flag == 1 & count > 0:  # 뭔가를 찾은 기록이 있고 고유깃발이 켜진 상태면(찾은 기록이 있고 그것이 한 번 뿐이라면)
                        Uniq_order = i
                    Uniq_Flag = 0
            i += 1
        if count == 1:  # 검색결과가 하나만 있다면 검색 결과의 모든 정보 출력
            Student_Data_print(Students_Info_List[Uniq_order])
        elif count > 1:  # 검색결과가 2개 이상이라면 학생 ID들만 출력
            print("일치하는 데이터가 2개 이상이므로 해당 ID를 출력합니다.")
            for i in range(len(temp)):
                print("%s" % temp[i])
        elif count == 0:
            print('%s을(를) 찾을 수 없습니다.'%search_word)

def Student_info_Read(Condition,all=0):
    if all==0:# 모든 데이터를 출력하는 경우가 아니면~
        search_word = input("검색어를 입력하세요(취소시 ! 입력) : ")
        if search_word !='!': #취소가 아니면
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
        else:
            print("검색을 취소하고 메인으로 돌아갑니다.")
    else: # 모든 데이터를 출력하려면 이 부분이 실행된다.
        for i in range(len(Students_Info_List)):
            Student_Data_print(Students_Info_List[i])

def Student_info_Modified():####데이터 수정하기
    select=input("\n(※메인으로 돌아가려면 'exit'를 입력하세요)\n수정하려는 학생의 ID를 정확히 입력해주세요 (예: ITT001): ")
    if select !='exit' and select !="'exit'":
        i=0
        Found=0
        while i<len(Students_Info_List):
            if select == Students_Info_List[i]["학생 ID"]:
                Found=1
                break
            i += 1
        if Found==1:# 검색한 데이터를 찾았을 경우에만.
            print("1.학생이름 2. 학생나이 3.학생주소 4.과거수강횟수 5.강사명 6.강의명 7.강의코드 8.개강일 9.종료일 0.수정취소 11.수강 과목 추가")
            Key = input("수정할 항목을 선택하세요 (예 : 1): ")
            if Key=='1':
                Students_Info_List[i]['이름']=input("바꿔 넣을 값을 입력하세요 : ")
            elif Key=='2':
                Students_Info_List[i]['나이']=input("바꿔 넣을 값을 입력하세요 : ")
            elif Key=='3':
                Students_Info_List[i]['주소']=input("바꿔 넣을 값을 입력하세요 : ")
            elif Key=='4':
                Students_Info_List[i]['종합정보']['과거수강횟수']=input("바꿔 넣을 값을 입력하세요 : ")

            elif Key=='5':
                input_code=input('수정하기 위해서 해당 데이터의 강의코드를 입력해주세요. : ')######### 하필 강의코드냐면.. 고유한 키 값 같아서!
                for j in range(len(Students_Info_List[i]['종합정보']['강의관련 정보'])):
                    if  input_code == Students_Info_List[i]['종합정보']['강의관련 정보'][j].get('강의코드'):
                        Students_Info_List[i]['종합정보']['강의관련 정보'][j]['강사명'] = input("바꿔 넣을 값을 입력하세요 : ")

            elif Key=='6':
                input_code = input('수정하기 위해서 해당 데이터의 강의코드를 입력해주세요. : ')  ######### 하필 강의코드냐면.. 고유한 키 값 같아서!
                for j in range(len(Students_Info_List[i]['종합정보']['강의관련 정보'])):
                    if input_code == Students_Info_List[i]['종합정보']['강의관련 정보'][j].get('강의코드'):
                        Students_Info_List[i]['종합정보']['강의관련 정보'][j]['강의명'] = input("바꿔 넣을 값을 입력하세요 : ")

            elif Key=='7':
                input_code = input('수정하기 위해서 해당 데이터의 강의코드를 입력해주세요. : ')  ######### 하필 강의코드냐면.. 고유한 키 값 같아서!
                for j in range(len(Students_Info_List[i]['종합정보']['강의관련 정보'])):
                    if input_code == Students_Info_List[i]['종합정보']['강의관련 정보'][j].get('강의코드'):
                        Students_Info_List[i]['종합정보']['강의관련 정보'][j]['강의코드'] = input("바꿔 넣을 값을 입력하세요 : ")

            elif Key=='8':
                input_code = input('수정하기 위해서 해당 데이터의 강의코드를 입력해주세요. : ')  ######### 하필 강의코드냐면.. 고유한 키 값 같아서!
                for j in range(len(Students_Info_List[i]['종합정보']['강의관련 정보'])):
                    if input_code == Students_Info_List[i]['종합정보']['강의관련 정보'][j].get('강의코드'):
                        Students_Info_List[i]['종합정보']['강의관련 정보'][j]['개강일'] = input("바꿔 넣을 값을 입력하세요 : ")

            elif Key=='9':
                input_code = input('수정하기 위해서 해당 데이터의 강의코드를 입력해주세요. : ')  ######### 하필 강의코드냐면.. 고유한 키 값 같아서!
                for j in range(len(Students_Info_List[i]['종합정보']['강의관련 정보'])):
                    if input_code == Students_Info_List[i]['종합정보']['강의관련 정보'][j].get('강의코드'):
                        Students_Info_List[i]['종합정보']['강의관련 정보'][j]['종료일'] = input("바꿔 넣을 값을 입력하세요 : ")
                print("변경되었습니다.\n메인으로 돌아갑니다.\n")
            elif Key=='11': # 수강 과목을 추가하자. append를 하면 될듯.
                temp=[]
                code = input("강의코드를 입력하세요(예: IB171106)(생략시 엔터 입력) : ")
                lecture_name = input("강의명을 입력하세요(예: IoT 빅데이터 실무반) : ")  # 강의명
                teacher_name = input("강사명을 입력하세요(예: 임꺽정) : ")  # 강사명
                Starting_Date = input("개강일을 입력하세요(예: 1970-01-01) : ")  # 개강일
                End_Date = input("종료일을 입력하세요(예: 2018-12-31) : ")  # 종료일
                temp.append([code] + [lecture_name] + [teacher_name] + [Starting_Date] + [End_Date])

                lecture_info = []

                for i in range(len(temp)):
                    lecture_info.append({'강의코드': temp[i][0], '강의명': temp[i][1], '강사명': temp[i][2], '개강일': temp[i][3],
                                         '종료일': temp[i][4]})

                additional= {'강의관련 정보': lecture_info}
                Students_Info_List[i]["종합정보"].update(additional)  # 딕셔너리 뒤에 딕셔너리 붙이기. 리스트의 append 같은 개념
                print("추가되었습니다.\n")
            else:# 0을 누르면 수정 취소인데.. 귀찮으니까 나머지 경우는 무조건 취소하기로 함.
                print("수정이 취소됐습니다\n메인으로 돌아갑니다.\n")
        else:# 찾지 못한 경우
            print("%s을(를) 목록에서 찾을 수 없습니다.\n"%select)
    else:# exit 나 'exit'를 누른 경우
        print("수정이 취소됐습니다\n메인으로 돌아갑니다.\n")

def Student_info_delete():# 회원 데이터 삭제하기
    select=input("삭제하려는 학생의 ID를 정확히 입력해주세요 (이전메뉴 돌아가기: !exit): ")
    if select!='!exit':
        i=0
        Found=0
        while i<len(Students_Info_List):
            if select in Students_Info_List[i]["학생 ID"]:
                Found=1
                break
            i += 1
        if Found==1:# 검색한 데이터를 찾았을 경우에만.
            select=input("1.찾은 회원 정보를 모두 삭제합니다. 2.찾은 회원 정보 중 현재 수강 강의 정보만을 삭제합니다. (예. 1): ")
            if select == '1':

                yes_no=input("아이디 "+Students_Info_List[i]["학생 ID"]+"를 정말로 삭제하시겠습니까? (y/n or yes/no) : ")
                if yes_no=='y' or yes_no=='yes' or yes_no=='Y' or yes_no=='Yes' or yes_no=='YES':
                    del Students_Info_List[i]
                    print("해당 회원 데이터가 모두 삭제되었습니다.\n")
                else:
                    print("삭제를 취소했습니다.\n메인으로 돌아갑니다.\n")
            else: # 현재 수강 강의 정보만 삭제하기
                lecture_code=input("강의를 삭제하기 위해 해당 강의 코드를 정확히 입력하세요.(예: IB171106) : ")
                for j in range(len(Students_Info_List[i]["종합정보"]["강의관련 정보"])):
                    if lecture_code == Students_Info_List[i]["종합정보"]["강의관련 정보"][j].get("강의코드"):
                        del Students_Info_List[i]["종합정보"]["강의관련 정보"][j]
                        print('삭제되었습니다\n메인으로 돌아갑니다.\n')
                        break

        else: # 검색어로 아이디 못 찾았을때
            print("%s을(를) 찾을 수 없습니다.\n"%select)
    else:
        print("메인으로 돌아갑니다.\n")

def Save_Data(jsonResult):
    with open(json_file_name,'w',encoding='utf8') as outfile:
        readable_result=json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
        print(json_file_name+' Saved')

json_file_name='ITT_Student.json'##################################################entry point############################################################
try:# json 파일이 있는 경우 읽고
    with open(json_file_name,encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        Students_Info_List = json.loads(json_string)

        print(json_file_name + "Loaded\n")
except: # 없는 경우. 처음 실행했을때만 여기를 거쳐간다.
    print("경로에 파일이 없습니다. 어떻게 하시겠습니까?")
    choice=input("1. 경로를 입력합니다. 2. 기본 경로로 생성하겠습니다. : ")
    if choice=='1':
        json_file_name=input("경로를 입력하세요. : ")
    elif choice=='2':# 프로그램 끌때 생성하는 걸로 ..
        print()
    Students_Info_List=[]###

while True:
    Main_Display()
    select=input("\n메뉴를 선택하세요 : ")
    if select=='1':#학생 정보 입력
        Student_info_Create()
    elif select=='2': # 검색
        print('데이터를 읽기 위해 검색을 합니다.')
        print('검색 조건을 선택하세요')
        print("1.ID 2.이름 3.나이 4.주소 5.과거 수강 횟수 6.현재 수강 과목의 강의명")
        Choice=input('7.현재 수강 과목의 강사명 8.검색 취소하기 9.모든 데이터 보기 : ')
        if Choice!='8' and Choice !='9':
            Student_info_Read(Choice)
        elif Choice == '9':
            Student_info_Read(Choice,1)
        else:
            print("\n검색을 취소했습니다.\n메인으로 돌아갑니다.\n")
    elif select=='3': # 학생 정보 수정
        Student_info_Modified()
    elif select=='4': # 학생 정보 삭제
        Student_info_delete()
    elif select=='5':
        Save_Data(Students_Info_List)
        ON_OFF=input("종료하시겠습니까? (y 또는 yes를 누르면 종료됩니다.) : ")
        if ON_OFF=='y' or ON_OFF=='yes' or ON_OFF=='Y' or ON_OFF=='YES':
            print("종료합니다.")
            break