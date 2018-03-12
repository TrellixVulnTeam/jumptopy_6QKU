import pickle
import re
import os
import Curriculums.Make_Curiculum_class

class academy_information() :
    def __init__(self, name, number, address, web_address, curriculums) :
        self.name = name
        self.number = number
        self.address = address
        self.web_address = web_address
        self.curriculums = curriculums

def make_academy_info() :
    while 1 :
        print("아래를 따라 학원 정보를 입력하십시오. 미 기재시 입력 동작이 재실행 됩니다.")
        academy_name = input("학원 이름을 입력해 주십시오. : ")
        academy_number = input("학원 전화번호를 입력해 주십시오. : ")
        academy_address = input("학원 주소를 입력해 주십시오. : ")
        academy_web_address = input("학원 웹페이지를 입력해 주십시오. : ")
        academy_curriculums = input("학원 강의를 입력해 주십시오.(공백으로 구분) : ")
        try:
            temp_academy_info = academy_information( \
academy_name, academy_number, academy_address, academy_web_address, academy_curriculums)
            return temp_academy_info
        except: continue

def print_all_academies_info() :
    try:
        file = open("..\\..\\Academies.bin", 'rb')
        while 1:
            try:
                temp = pickle.load(file)
                print("----------------------------------------------------")
                print("학원이름 : %s" % temp.name)
                print("전화번호 : %s" % temp.number)
                print("주소 : %s" % temp.address)
                print("홈페이지 : %s" % temp.web_address)
                print("교육과정 : %s" % temp.curriculums)
                print("----------------------------------------------------")
            except:
                break
    except FileNotFoundError:
        print("Academies.bin 파일이 없습니다.")

def print_all_academies_name() :
    try:
        file = open("..\\..\\Academies.bin", 'rb')
        numbering = 1
        while 1:
            try:
                temp = pickle.load(file)
                print("%d.학원 : %s" % (numbering, temp.name))
                numbering += 1
            except:
                break
    except FileNotFoundError:
        print("Academies.bin 파일이 없습니다.")

def search_academy(searching_academy_name) :
    searching = re.compile(searching_academy_name, re.DOTALL)
    try:
        file = open("..\\..\\Academies.bin", 'rb')
        while 1:
            try:
                temp = pickle.load(file)
                searching_result = searching.search(temp.name)
                if searching_result != None :
                    print("----------------------------------------------------")
                    print("학원이름 : %s" % temp.name)
                    print("전화번호 : %s" % temp.number)
                    print("주소 : %s" % temp.address)
                    print("홈페이지 : %s" % temp.web_address)
                    print("교육과정 : %s" % temp.curriculums)
                    print("----------------------------------------------------")
            except:
                print("탐색이 끝났습니다.")
                break
    except FileNotFoundError:
        print("Academies.bin 파일이 없습니다.")

# def search_academy(searching_academy_name):
#     try:
#         file = open("..\\..\\Academies.bin", 'rb')
#         while 1:
#             try:
#                 temp = pickle.load(file)
#                 if temp.name == searching_academy_name:
#                     print("학원이름 : %s" % temp.name)
#                     print("전화번호 : %s" % temp.number)
#                     print("주소 : %s" % temp.address)
#                     print("홈페이지 : %s" % temp.web_address)
#                     print("교육과정 : %s" % temp.curriculums)
#                     break
#             except:
#                 print("찾으시는 학원(%s)이 없습니다." % searching_academy_name)
#                 break
#     except FileNotFoundError:
#         print("Academies.bin 파일이 없습니다.")


# def delet_academy(deleting_academy_name) :
#     try:
#         file = open("..\\..\\Academies.bin", 'rb')
#         file_copy = open("..\\..\\Academies_copy.bin", 'wb')
#         token = "없다"
#         while 1 :
#             try :
#                 temp = pickle.load(file)
#                 if temp.name == deleting_academy_name :
#                     try:
#                         os.rmdir("..\\..\\Academies\\" + deleting_academy_name)
#                         token = "지웠다"
#                     except OSError as e_msg:
#                         print(e_msg)
#                         judge = input("상관없이 다 지우시겠습니까?(1:예 2:아니오) : ")
#                         if judge == '2' : token = "안지웠다"
#                         elif judge == '1' :
#                             dirlist = os.listdir("..\\..\\Academies\\" + deleting_academy_name)
#                             for x in dirlist :
#                                 os.unlink("..\\..\\Academies\\" + deleting_academy_name + "\\" + x)
#                             os.rmdir("..\\..\\Academies\\" + deleting_academy_name)
#                             token = "지웠다"
#                 else : pickle.dump(temp, file_copy)
#             except :
#                 if token == "없다" :
#                     print("%s라는 학원이 없습니다." %deleting_academy_name)
#                     file.close()
#                     file_copy.close()
#                     os.unlink("..\\..\\Academies_copy.bin")
#                     break
#                 elif token == "안지웠다" :
#                     file.close()
#                     file_copy.close()
#                     os.unlink("..\\..\\Academies_copy.bin")
#                     break
#                 elif token == "지웠다" :
#                     file.close()
#                     file_copy.close()
#                     os.unlink("..\\..\\Academies.bin")
#                     os.rename("..\\..\\Academies_copy.bin", "..\\..\\Academies.bin")
#                     break
#     except FileNotFoundError:
#         print("Academies.bin 파일이 없습니다.")

def change_all_academies_info() :
    try:
        file = open("..\\..\\Academies.bin", 'rb')
        file_copy = open("..\\..\\Academies_copy.bin", 'wb')
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
            judge = input("변경하시겠습니까?\n(1:예 2:아니오 3:삭제) : ")
            if judge == '2' :
                pickle.dump(temp, file_copy)
            elif judge == '1' :
                judge_a = input("학원이름을 변경하시겠습니까?(1:예 2:아니오) : ")
                if judge_a == '1' :
                    name_change = input("학원이름을 입력하십시오. : ")
                    os.rename("..\\..\\Academies\\"+temp.name, "..\\..\\Academies\\"+name_change)
                    temp.name = name_change
                judge_a = input("전화번호를 변경하시겠습니까?(1:예 2:아니오) : ")
                if judge_a == '1' : temp.number = input("학원전화번호를 입력하십시오. : ")
                judge_a = input("학원주소를 변경하시겠습니까?(1:예 2:아니오) : ")
                if judge_a == '1' : temp.address = input("학원 주소를 입력하십시오. : ")
                judge_a = input("웹페이지를 변경하시겠습니까?(1:예 2:아니오) : ")
                if judge_a == '1' : temp.web_address = input("학원 웹페이지를 입력하십시오. : ")
                judge_a = input("커리큘럼를 변경하시겠습니까?(1:예 2:아니오) : ")
                if judge_a == '1' : temp.curriculums = input("커리큘럼을 입력하십시오.(공백으로구분) : ")
                pickle.dump(temp, file_copy)
            elif judge == '3' : continue
        except:
            file.close()
            file_copy.close()
            os.unlink("..\\..\\Academies.bin")
            os.rename("..\\..\\Academies_copy.bin", "..\\..\\Academies.bin")
            break

def change_one_academy(changing_academy_name) :
    try:
        file = open("..\\..\\Academies.bin", 'rb')
        file_copy = open("..\\..\\Academies_copy.bin", 'wb')
    except FileNotFoundError:
        print("파일이 없습니다.")
        return None
    while 1:
        try:
            temp = pickle.load(file)
            if temp.name == changing_academy_name :
                print("학원이름 : %s" % temp.name)
                print("전화번호 : %s" % temp.number)
                print("주소 : %s" % temp.address)
                print("홈페이지 : %s" % temp.web_address)
                print("교육과정 : %s" % temp.curriculums)
                judge = input("변경하시겠습니까?\n(1:예 2:아니오 3:삭제) : ")
                if judge == '2' : token = "미수정"
                elif judge == '1' :
                    judge_a = input("학원이름을 변경하시겠습니까?(1:예 2:아니오) : ")
                    if judge_a == '1' :
                        name_change = input("학원이름을 입력하십시오. : ")
                        os.rename("..\\..\\Academies\\"+temp.name, "..\\..\\Academies\\"+name_change)
                        temp.name = name_change
                    judge_a = input("전화번호를 변경하시겠습니까?(1:예 2:아니오) : ")
                    if judge_a == '1' : temp.number = input("학원전화번호를 입력하십시오. : ")
                    judge_a = input("학원주소를 변경하시겠습니까?(1:예 2:아니오) : ")
                    if judge_a == '1' : temp.address = input("학원 주소를 입력하십시오. : ")
                    judge_a = input("웹페이지를 변경하시겠습니까?(1:예 2:아니오) : ")
                    if judge_a == '1' : temp.web_address = input("학원 웹페이지를 입력하십시오. : ")
                    judge_a = input("커리큘럼를 변경하시겠습니까?(1:예 2:아니오) : ")
                    if judge_a == '1' : temp.curriculums = input("커리큘럼을 입력하십시오.(공백으로구분) : ")
                    pickle.dump(temp, file_copy)
                    token = "수정"
                elif judge == '3' :
                    try :
                        os.rmdir("..\\..\\Academies\\" + changing_academy_name)
                        token = "지웠다"
                    except OSError as e_msg :
                        print(e_msg)
                        judge_a = input("상관없이 다 지우시겠습니까?(1:예 2:아니오) : ")
                        if judge_a == '2' :
                            token = "안지웠다"
                        elif judge_a == '1' :
                            dirlist = os.listdir("..\\..\\Academies\\" + changing_academy_name )
                            for x in dirlist:
                                os.unlink("..\\..\\Academies\\" + changing_academy_name + "\\" + x)
                            os.rmdir("..\\..\\Academies\\" + changing_academy_name)
                            token = "지웠다"
            else:
                pickle.dump(temp, file_copy)
        except:
            if token == "미수정" or token == "안지웠다" :
                file.close()
                file_copy.close()
                os.unlink("..\\..\\Academies_copy.bin")
                break
            elif token == "수정" or token == "지웠다" :
                file.close()
                file_copy.close()
                os.unlink("..\\..\\Academies.bin")
                os.rename("..\\..\\Academies_copy.bin", "..\\..\\Academies.bin")
                break

def make_academy(instance) :
    try :
        os.mkdir("..\\..\\Academies\\"+instance.name)
        for x in str(instance.curriculums).split(' ') :
            print("지금 생성하는 강의는 %s입니다. " %x, end = '')
            Curriculums.Make_Curiculum_class.make_curriculum\
(instance.name, Curriculums.Make_Curiculum_class.make_curriculum_info())
        try :
            file = open("..\\..\\Academies.bin", 'rb')
            file.close()
            file = open("..\\..\\Academies.bin", 'ab')
            pickle.dump(instance, file)
            file.close()
        except FileNotFoundError :
            file = open("..\\..\\Academies.bin", 'wb')
            pickle.dump(instance, file)
            file.close()
    except FileExistsError :
        print("%s라는 학원은 이미 생성되었습니다." %instance.name)