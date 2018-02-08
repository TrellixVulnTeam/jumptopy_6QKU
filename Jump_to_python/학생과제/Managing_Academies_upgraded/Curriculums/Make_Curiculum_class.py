import pickle
import os
import re
import Make_Academy_class

class curriculum_information() :
    def __init__(self, name, tutors, time, students) :
        self.name = name
        self.tutors = tutors
        self.time = time
        self.students = students

def make_curriculum_info() :
    while 1 :
        curriculum_info_tutors = {}
        curriculum_info_students = {}
        print("아래를 따라 강의 정보를 입력하십시오. 미 기재시 혹은 오류 입력 시 동작이 재실행 됩니다.")
        curriculum_name = input("강의명을 입력하십시오. : ")
        curriculum_time = input("강의 수업 시간을 입력하십시오. : ")
        while 1 :
            curriculum_info_tutors_input = input("강사진을 입력하세요.\n\
e.g)김이박 010-2777-4444 최정강 010-7777-8888 조윤장 010-4562-7894\n강사명 전화번호 : ").split(' ')
            x = 0
            while x < len(curriculum_info_tutors_input):
                try:
                    curriculum_info_tutors[curriculum_info_tutors_input[x]] \
= curriculum_info_tutors_input[x + 1]
                    x = x + 2
                except:
                    print("강사진을 잘 못 입력하셨습니다.")
                    x = -1
                    break
            if x == -1 : continue
            elif x != 0 and x != -1 : break
        while 1 :
            curriculum_info_students_input = input("수강생을 입력하세요.\n\
e.g)김이박 010-2777-4444 최정강 010-7777-8888 조윤장 010-4562-7894\n수강생명 전화번호 : ").split(' ')
            x = 0
            while x < len(curriculum_info_students_input):
                try:
                    curriculum_info_students[curriculum_info_students_input[x]] \
= curriculum_info_students_input[x + 1]
                    x = x + 2
                except:
                    print("수강생을 잘 못 입력하셨습니다.")
                    x = -1
                    break
            if x == -1: continue
            elif x != 0 and x != -1 : break
        try :
            curriculum_info = curriculum_information( \
curriculum_name, curriculum_info_tutors, curriculum_time, curriculum_info_students)
            return curriculum_info
        except :
            print("재입력이 필요합니다.")
            continue

def print_all_curriculmums_info() :
    listdir_name = os.listdir("..\\..\\Academies")
    for x in listdir_name:
        for y in os.listdir("..\\..\\Academies\\" + x):
            file = open("..\\..\\Academies\\" + x + "\\" + y, 'rb')
            try:
                temp = pickle.load(file)
                print("----------------------------------------------------")
                print("학원명 : %s" % x)
                print("과정명 : %s" % temp.name)
                print("강사진 : ", end='')
                print(temp.tutors)
                print("수업시간 : %s" % temp.time)
                print("학생들 : ", end='')
                print(temp.students, end="\n\n")
                print("----------------------------------------------------")
            except:
                pass

def print_all_curriculums_name() :
    listdir_name = os.listdir("..\\..\\Academies")
    for x in listdir_name:
        curr_name = os.listdir("..\\..\\Academies\\" + x)
        for y in curr_name:
            print("학원명 : %s - 과정명 : " % x, end='')
            print(y.split('.')[0])

def search_curriculum(searching_curriculum_name) :
    searching = re.compile(searching_curriculum_name, re.DOTALL)
    listdir_name = os.listdir("..\\..\\Academies")
    for x in listdir_name:
        listfile_name = os.listdir("..\\..\\Academies\\"+x)
        for y in listfile_name :
            searching_result = searching.search(y)
            if searching_result != None :
                file = open("..\\..\\Academies\\" + x + "\\" + y, 'rb')
                temp = pickle.load(file)
                print("----------------------------------------------------")
                print("학원명 : %s" % x)
                print("과정명 : %s" % temp.name)
                print("강사진 : ", end='')
                print(temp.tutors)
                print("수업시간 : %s" % temp.time)
                print("학생들 : ", end='')
                print(temp.students, end="\n")
                print("----------------------------------------------------")
                file.close()
    print("탐색이 끝났습니다.")

# def search_curriculum(searching_curriculum_name) :
#     listdir_name = os.listdir("..\\..\\Academies")
#     token = 0
#     for x in listdir_name:
#         try:
#             file = open("..\\..\\Academies\\" + x + "\\" + searching_curriculum_name + ".bin", 'rb')
#             temp = pickle.load(file)
#             print("학원명 : %s" % x)
#             print("과정명 : %s" % temp.name)
#             print("강사진 : ", end='')
#             print(temp.tutors)
#             print("수업시간 : %s" % temp.time)
#             print("학생들 : ", end='')
#             print(temp.students, end="\n")
#             file.close()
#             token = 1
#             continue
#         except FileNotFoundError:
#             continue
#         except EOFError:
#             pass
#     if token == 0: print("찾는 과정(%s)이 없거나 내부정보가 없습니다." %searching_curriculum_name)

None

# def delet_curriculum(deleting_academy_name, deleting_curriculum_name) :
#     try:
#         os.unlink("..\\..\\Academies\\" + deleting_academy_name + "\\" + deleting_curriculum_name + ".bin")
#     except FileNotFoundError:
#         print("해당 학원 혹은 과정이 없습니다.")

def make_curriculum(academy_name, instance) :
    file = open("..\\..\\Academies\\"+academy_name+"\\"+instance.name+".bin", 'wb')
    pickle.dump(instance, file)
    file.close()

def update_curriculum(updating_academy_name, updating_curriculum_name) :
    temp_change_tutors = {}
    temp_change_students = {}
    try :
        file = open("..\\..\\Academies\\"+updating_academy_name+"\\"+updating_curriculum_name+".bin", 'rb')
        temp = pickle.load(file)
        print("학원이름 : %s" %updating_academy_name)
        print("강의이름 : %s" %temp.name)
        print("강사진 : ", end = '')
        print(temp.tutors)
        print("강의시간 : %s" %temp.time)
        print("수강생 : ", end = '')
        print(temp.students)
        judge = input("강의정보를 변경하시겠습니까?(1:예 2:아니오 3:삭제) : ")
        if judge == '2' :
            file.close()
            return None
        if judge == '1' :
            file_copy = open("..\\..\\Academies\\" + updating_academy_name + "\\curriculum_copy.bin", 'wb')
            judge_a = input("강의명를 변경하시겠습니까?(1:예 2:아니오) : ")
            if judge_a == '1': temp.name = input("강의명을 입력하십시오. : ")
            judge_a = input("강사진을 변경하시겠습니까?(1:예 2:아니오) : ")
            if judge_a == '1':
                while 1 :
                    temp_change_tutors = input("강사진을 입력하세요.\n\
e.g)김이박 010-2777-4444 최정강 010-7777-8888 조윤장 010-4562-7894\n강사명 전화번호 : ").split(' ')
                    x = 0
                    while x < len(temp_change_tutors):
                        try:
                            temp_change_tutors[x] = temp_change_tutors[x + 1]
                            x = x + 2
                        except:
                            print("강사 정보를 잘 못 입력하셨습니다.")
                            x = -1
                            break
                    if x == -1 : continue
                    elif x != 0 and x != -1 :
                        temp.tutors = temp_change_tutors
                        break
            judge_a = input("강의시간을 변경하시겠습니까?(1:예 2:아니오) : ")
            if judge_a == '1': temp.time = input("학원 주소를 입력하십시오. : ")
            judge_a = input("수강생을 변경하시겠습니까?(1:예 2:아니오) : ")
            if judge_a == '1':
                while 1 :
                    temp_change_students = input("수강생을 입력하세요.\n\
e.g)김이박 010-2777-4444 최정강 010-7777-8888 조윤장 010-4562-7894\n수강생명 전화번호 : ").split(' ')
                    x = 0
                    while x < len(temp_change_students):
                        try :
                            temp_change_students[x] = temp_change_students[x + 1]
                            x = x + 2
                        except:
                            print("수강생을 잘 못 입력하셨습니다.")
                            x = -1
                            break
                    if x == -1: continue
                    elif x != 0 and x != 1 :
                        temp.students = temp_change_students
                        break
            pickle.dump(temp, file_copy)
            file.close()
            file_copy.close()
            os.unlink("..\\..\\Academies\\"+updating_academy_name+"\\"+updating_curriculum_name+".bin")
            os.rename("..\\..\\Academies\\"+updating_academy_name+"\\curriculum_copy.bin"\
,"..\\..\\Academies\\"+updating_academy_name+"\\"+updating_curriculum_name+".bin")
        elif judge == '3' :
            file.close()
            os.unlink("..\\..\\Academies\\" + updating_academy_name + \
"\\" + updating_curriculum_name + ".bin")
            print("학원의 강의정보에 해당하는 부분을 수정하십시오.")
            Make_Academy_class.change_one_academy(updating_academy_name)
    except FileNotFoundError : print("강의(%s)가 없습니다." %updating_curriculum_name)