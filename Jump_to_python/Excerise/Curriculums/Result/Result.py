import pickle
import os
import Make_Academy_class
import Curriculums.Make_Curiculum_class

while 1 :
    order_1 = input("학원관리스스템을 실행하시겠습니까?(1:예, 2:아니오, 3:학원갱신)")
    if order_1 == '2' : break
    elif order_1 == '3' :
        try:
            file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies.bin", 'rb')
            file_copy = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies_copy.bin", 'wb')
        except FileNotFoundError:
            print("파일이 없습니다.")
            exit()
        while 1:
            try:
                temp = pickle.load(file)
                print("학원이름 : %s" % temp.name)
                print("전화번호 : %s" % temp.number)
                print("주소 : %s" % temp.address)
                print("홈페이지 : %s" % temp.web_address)
                print("교육과정 : %s" % temp.curriculums)
                judge = input("변경하시겠습니까?(단, 학원명은 변경할 수 없습니다)\n(1:예 2:아니오 3:삭제) : ")
                if judge == '2' :
                    pickle.dump(temp, file_copy)
                elif judge == '1' :
                    judge_a = input("전화번호를 변경하시겠습니까?(1:예 2:아니오) : ")
                    if judge_a == '1' : temp.number = input("학원전화번호를 입력하십시오. : ")
                    judge_a = input("학원주소를 변경하시겠습니까?(1:예 2:아니오) : ")
                    if judge_a == '1' : temp.address = input("학원 주소를 입력하십시오. : ")
                    judge_a = input("웹페이지를 변경하시겠습니까?(1:예 2:아니오) : ")
                    if judge_a == '1' : temp.web_address = input("학원 웹페이지를 입력하십시오. : ")
                    judge_a = input("커리큘럼를 변경하시겠습니까?(1:예 2:아니오) : ")
                    if judge_a == '1' : temp.curriculums = input("커리큘럼을 입력하십시오.(,) : ")
                    pickle.dump(temp, file_copy)
                elif judge == '3' : continue
            except:
                file.close()
                file_copy.close()
                os.unlink("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies.bin")
                os.rename("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies_copy.bin", "D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies.bin")
                break
    elif order_1 == "1" :
        temp_acafunc = Make_Academy_class.academies()
        temp_curriculum_func = Curriculums.Make_Curiculum_class.curriculums()
        while 1 :
            order_2 = input("학원정보를 입력하시겠습니까?(1:예, 2:아니오) : ")
            if order_2 == "1" :
                academy_info = input("학원 정보를 입력해 주십시오.\n이름,번호,주소,웹주소,과정명(,) : ")
                academy_info = academy_info.split(' ')
                try :
                    temp_academy_info = Make_Academy_class.academy_information(academy_info[0], academy_info[1], academy_info[2],\
academy_info[3], academy_info[4])
                    temp_acafunc.make_academy(temp_academy_info)
                except : print("잘 못 된 입력")
            elif order_2 == "2" : break
        while 1 :
            order_3 = input("학원정보들을 검색하시겠습니까?(1:예, 2:아니오) : ")
            if order_3 == "1" : temp_acafunc.serch_academy_info()
            elif order_3 == "2" : break
        while 1 :
            order_4 = input("각 과정의 정보를 입력하시겠습니까?(1:예 2:아니오)")
            if order_4 == "2" : break
            elif order_4 == "1" :
                curriculum_info_tutors = {}
                curriculum_info_students = {}
                temp_curriculum_info = input("과정 정보를 입력.\n학원명,강좌명,수업시간 : ").split(' ')
                curriculum_info_tutors_input = input("강사명과 전화번호 입력 : ").split(' ')

                x = 0
                while x < len(curriculum_info_tutors_input) :
                    try : curriculum_info_tutors[curriculum_info_tutors_input[x]] = curriculum_info_tutors_input[x+1]
                    except:
                        print("잘 못 된 입력")
                        break
                    x = x+2
                curriculum_info_students_input = input("학생명과 전화번호 입력 : ").split(' ')

                x = 0
                while x < len(curriculum_info_students_input) :
                    try : curriculum_info_students[curriculum_info_students_input[x]] = curriculum_info_students_input[x+1]
                    except:
                        print("잘 못 된 입력")
                        break
                    x = x+2
                try :
                    curriculum_info = Curriculums.Make_Curiculum_class.curriculum_information(\
temp_curriculum_info[1], curriculum_info_tutors, temp_curriculum_info[2], curriculum_info_students)
                    temp_curriculum_func.make_curriculum(temp_curriculum_info[0], curriculum_info)
                except : print("잘 못 된 입력")
        while 1 :
            order_5 = input("과정정보를 검색하시겠습니까?(1:예 2:아니오) : ")
            if order_5 == '2' : break
            elif order_5 == '1' : temp_curriculum_func.search_curriculum_info()