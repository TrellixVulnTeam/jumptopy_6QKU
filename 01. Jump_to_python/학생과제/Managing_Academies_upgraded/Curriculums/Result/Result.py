import sys
import os
# sys.path.append("..\\..\\..\\Managing_Academies_upgraded")
original_path = os.getcwd()
os.chdir("..\\..\\..")
cur_path = os.getcwd()
sys.path.append(cur_path + "\\Managing_Academies_upgraded")
os.chdir(original_path)
import Make_Academy_class
import Curriculums.Make_Curiculum_class

print("Managing_Academies에 오신것을 환영합니다.\n하단의 메뉴 중 원하는 동작을 선택하십시오.")
while 1 :
    order_menu = \
input("1:학원(강의)정보생성 2:학원(강의)정보조회 3:학원(강의)정보수정&삭제 4:종료 : ")
    if order_menu == '4' : break
    elif order_menu == '1' :
        while 1:
            order_create = input("1:학원생성 2:강의생성 3:메인메뉴로 돌아가기 : ")
            if order_create == '3': break
            elif order_create == '1' :
                while 1 :
                    Make_Academy_class.make_academy(Make_Academy_class.make_academy_info())
                    judge = input("더 입력하시겠습니까?(1:예 2:아니오) : ")
                    if judge == '2' : break
                    elif judge == '1' : continue
            elif order_create == '2' :
                while 1 :
                    curriculum_academy_name = input("학원 이름을 입력하십시오. : ")
                    Curriculums.Make_Curiculum_class.make_curriculum(curriculum_academy_name,\
Curriculums.Make_Curiculum_class.make_curriculum_info())
                    print("학원의 강의정보에 해당하는 부분을 수정하십시오.")
                    Make_Academy_class.change_one_academy(curriculum_academy_name)
                    judge = input("더 입력하시겠습니까?(1:예 2:아니오) : ")
                    if judge == '2': break
                    elif judge == '1': continue
    elif order_menu == '2' :
        while 1 :
            order_search_and_print = input("1:학원전체정보출력 2:학원명만출력 3:학원찾기 4:강의전체정보출력 \
5:강의명만출력 6:강의찾기 7:메인메뉴로가기 : ")
            if order_search_and_print == '7' : break
            elif order_search_and_print == '1' : Make_Academy_class.print_all_academies_info()
            elif order_search_and_print == '2' : Make_Academy_class.print_all_academies_name()
            elif order_search_and_print == '4' : Curriculums.Make_Curiculum_class.print_all_curriculmums_info()
            elif order_search_and_print == '5' : Curriculums.Make_Curiculum_class.print_all_curriculums_name()
            elif order_search_and_print == '3' :
                searching_academy_name = input("찾으시려는 학원 이름을 입력해 주십시오. : ")
                Make_Academy_class.search_academy(searching_academy_name)
            elif order_search_and_print == '6' :
                searching_curriculum_name = input("찾으시려는 강의 이름을 입력해 주십시오. : ")
                Curriculums.Make_Curiculum_class.search_curriculum(searching_curriculum_name)
    elif order_menu == '3' :
        while 1 :
            order_change = input("1:전체학원정보수정 2:특정학원정보수정&삭제 3:강의정보수정&삭제 \
4:메인메뉴로가기 : ")
            if order_change == '4' : break
            elif order_change == '1' : Make_Academy_class.change_all_academies_info()
            elif order_change == '2' :
                changing_academy_name = input("수정&삭제하려는 학원이름을 입력하십시오. : ")
                Make_Academy_class.change_one_academy(changing_academy_name)
            elif order_change == '3' :
                changing_curriculum_info = input("변경&삭제 학원이름과 강의명을 입력하십시오.\n\
e.g)한국it교육원 Python\n학원이름 강의명 : ").split(' ')
                Curriculums.Make_Curiculum_class.update_curriculum\
(changing_curriculum_info[0], changing_curriculum_info[1])




                    # while 1 :
#     order_1 = input("학원관리스스템을 실행하시겠습니까?(1:예, 2:아니오, 3:학원갱신)")
#     if order_1 == '2' : break
#     elif order_1 == '3' :
#         try:
#             file = open("..\\..\\Academies.bin", 'rb')
#             file_copy = open("..\\..\\Academies_copy.bin", 'wb')
#         except FileNotFoundError:
#             print("파일이 없습니다.")
#             exit()
#         while 1:
#             try:
#                 temp = pickle.load(file)
#                 print("학원이름 : %s" % temp.name)
#                 print("전화번호 : %s" % temp.number)
#                 print("주소 : %s" % temp.address)
#                 print("홈페이지 : %s" % temp.web_address)
#                 print("교육과정 : %s" % temp.curriculums)
#                 judge = input("변경하시겠습니까?\n(1:예 2:아니오 3:삭제) : ")
#                 if judge == '2' :
#                     pickle.dump(temp, file_copy)
#                 elif judge == '1' :
#                     judge_a = input("학원이름을 변경하시겠습니까?(1:예 2:아니오) : ")
#                     if judge_a == '1' :
#                         name_change = input("학원이름을 입력하십시오. : ")
#                         os.rename("..\\..\\Academies\\"+temp.name, "..\\..\\Academies\\"+name_change)
#                         temp.name = name_change
#                     judge_a = input("전화번호를 변경하시겠습니까?(1:예 2:아니오) : ")
#                     if judge_a == '1' : temp.number = input("학원전화번호를 입력하십시오. : ")
#                     judge_a = input("학원주소를 변경하시겠습니까?(1:예 2:아니오) : ")
#                     if judge_a == '1' : temp.address = input("학원 주소를 입력하십시오. : ")
#                     judge_a = input("웹페이지를 변경하시겠습니까?(1:예 2:아니오) : ")
#                     if judge_a == '1' : temp.web_address = input("학원 웹페이지를 입력하십시오. : ")
#                     judge_a = input("커리큘럼를 변경하시겠습니까?(1:예 2:아니오) : ")
#                     if judge_a == '1' : temp.curriculums = input("커리큘럼을 입력하십시오.(공백으로구분) : ")
#                     pickle.dump(temp, file_copy)
#                 elif judge == '3' : continue
#             except:
#                 file.close()
#                 file_copy.close()
#                 os.unlink("..\\..\\Academies.bin")
#                 os.rename("..\\..\\Academies_copy.bin", "..\\..\\Academies.bin")
#                 break
#     elif order_1 == "1" :
#         temp_acafunc = Make_Academy_class.academies()
#         temp_curriculum_func = Curriculums.Make_Curiculum_class.curriculums()
#         while 1 :
#             order_2 = input("학원정보를 입력하시겠습니까?(1:예, 2:아니오) : ")
#             if order_2 == "1" :
#                 # academy_info = input("학원 정보를 입력해 주십시오.\
# # \ne.g) 한국it교육원 053)123-4567 www.hgit.com Java,Python,C,C++\
# # \n이름,번호,웹페이지,과정명(,) : ").split(' ')
#                 print("아래를 따라 학원 정보를 입력하십시오. 미 기재시 입력 동작이 재실행 됩니다.")
#                 academy_name = input("학원 이름을 입력해 주십시오. : ")
#                 academy_number = input("학원 전화번호를 입력해 주십시오. : ")
#                 academy_address = input("학원 주소를 입력해 주십시오. : ")
#                 academy_web_address = input("학원 웹페이지를 입력해 주십시오. : ")
#                 academy_curriculums = input("학원의 커리큘럼을 입력해 주십시오.(공백으로 구분) : ")
#                 try :
#                     temp_academy_info = Make_Academy_class.academy_information(\
# academy_name, academy_number, academy_address, academy_web_address,academy_curriculums)
#                     temp_acafunc.make_academy(temp_academy_info)
#                 except : continue
#             elif order_2 == "2" : break
#         while 1 :
#             order_3 = input("학원정보들을 검색하시겠습니까?(1:예, 2:아니오) : ")
#             if order_3 == "1" : temp_acafunc.serch_academy_info()
#             elif order_3 == "2" : break
#         while 1 :
#             order_4 = input("각 과정의 정보를 입력하시겠습니까?(1:예 2:아니오)")
#             if order_4 == "2" : break
#             elif order_4 == "1" :
#                 print("아래를 따라 학원 정보를 입력하십시오. 미 기재시 혹은 오류 입력 시 동작이 재실행 됩니다.")
#                 curriculum_info_tutors = {}
#                 curriculum_info_students = {}
#                 # temp_curriculum_info = input("과정 정보를 입력 하세요.\ne.g)한국it교욱원 Java 09:30~17:30\
# # \n학원명,강좌명,수업시간 : ").split(' ')
#                 curriculum_academy_name = input("과정의 학원 이름을 입력하십시오. : ")
#                 curriculum_name = input("과정명을 입력하십시오. : ")
#                 curriculum_time = input("과정 수업 시간을 입력하십시오. : ")
#                 curriculum_info_tutors_input = input("강사 정보를 입력하세요.\n\
# e.g)김이박 010-2777-4444 최정강 010-7777-8888 조윤장 010-4562-7894\n강사명 전화번호 : ").split(' ')
#                 x = 0
#                 while x < len(curriculum_info_tutors_input) :
#                     try : curriculum_info_tutors[curriculum_info_tutors_input[x]] = curriculum_info_tutors_input[x+1]
#                     except:
#                         print("강사 정보를 잘 못 입력하셨습니다.")
#                         # curriculum_info_tutors_input = input("다시 입력해 주십시오..\n\
# # e.g)김이박 010-2777-4444 최정강 010-7777-8888 조윤장 010-4562-7894\\n강사명 전화번호 : ").split(' ')
#                         x = -1
#                         break
#                     x = x+2
#                 if x == -1 : continue
#                 curriculum_info_students_input = input("수강생 정보를 입력하세요.\n\
# e.g)김이박 010-2777-4444 최정강 010-7777-8888 조윤장 010-4562-7894\n학생명 전화번호 : ").split(' ')
#                 x = 0
#                 while x < len(curriculum_info_students_input) :
#                     try : curriculum_info_students[curriculum_info_students_input[x]] = curriculum_info_students_input[x+1]
#                     except:
#                         print("수강생 정보를 잘 못 입력하셨습니다.")
#                         x = -1
#                         break
#                     x = x+2
#                 if x == -1 : continue
#                 try :
#                     curriculum_info = Curriculums.Make_Curiculum_class.curriculum_information(\
# curriculum_name, curriculum_info_tutors, curriculum_time, curriculum_info_students)
#                     temp_curriculum_func.make_curriculum(curriculum_academy_name, curriculum_info)
#                 except : continue
#         while 1 :
#             order_5 = input("과정정보를 검색하시겠습니까?(1:예 2:아니오) : ")
#             if order_5 == '2' : break
#             elif order_5 == '1' : temp_curriculum_func.search_curriculum_info()