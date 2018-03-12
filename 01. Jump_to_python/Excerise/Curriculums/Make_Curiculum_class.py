import pickle
import os

class curriculum_information() :
    def __init__(self, name, tutors, time, students) :
        self.name = name
        self.tutors = tutors
        self.time = time
        self.students = students

class curriculums() :
    def search_curriculum_info(self):
        order = input("검색 옵션을 설정해 주십시오.\n1.과정전체정보출력 2.과정명만출력 3.과정찾기 4.과정지우기 : ")
        # os.chdir("D:\Pycharm_projects\Emigration\Managing_Academies\Academies")
        listdir_name = os.listdir("D:\\Pycharm_projects\\Emigration\\Managing_Academies\\Academies")

        if order == '1' :
            for x in listdir_name :
                for y in os.listdir("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies\\"+x) :
                    file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\\Academies\
\\"+x+"\\"+y,'rb')
                    try :
                        temp = pickle.load(file)
                        print("학원명 : %s" %x)
                        print("과정명 : %s" %temp.name)
                        print("강사진 : ", end = '')
                        print(temp.tutors)
                        print("수업시간 : %s" %temp.time)
                        print("학생들 : ", end = '')
                        print(temp.students, end = "\n\n")
                    except : pass
        elif order == '2' :
            for x in listdir_name :
                curr_name = os.listdir("D:\\Pycharm_projects\\Emigration\
\\Managing_Academies\\Academies\\"+x)
                for y in curr_name :
                    print("%s : " %x, end = '')
                    print(y.split('.')[0])
            print()
        elif order == '3' :
            search_curriculum_name = input("과정명을 치세요. : ")
            token = 0
            for x in listdir_name :
                try :
                    file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies\\"+x+"\\"+search_curriculum_name+".bin", 'rb')
                    temp = pickle.load(file)
                    print("학원명 : %s" %x)
                    print("과정명 : %s" %temp.name)
                    print("강사진 : ", end = '')
                    print(temp.tutors)
                    print("수업시간 : %s" %temp.time)
                    print("학생들 : ", end = '')
                    print(temp.students, end = "\n")
                    file.close()
                    token = 1
                    continue
                except FileNotFoundError : continue
                except EOFError : pass
            if token == 0 : print("찾는 과정(%s)이 없거나 내부정보가 없습니다." %search_curriculum_name)
            print()
        elif order == '4' :
            try :
                delet_curriculum_name = input("학원명,과정명을 치세요. : ").split(' ')
                os.unlink("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies\\"+delet_curriculum_name[0]+"\\"+delet_curriculum_name[1]+".bin")
            except FileNotFoundError : print("해당 학원 혹은 과정이 없습니다.")

    def make_curriculum(self,academy_name, instance) :
        try :
            file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies\\"+academy_name+"\\"+instance.name+".bin", 'rb')
            judge = input("파일이 존재합니다. 덮어 쓰시겠습니까?(1:예 2:아니오")
            if judge == '2' :
                file.close()
                pass
            elif judge == '1' :
                file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies\\"+academy_name+"\\"+instance.name+".bin", 'wb')
                pickle.dump(instance, file)
                file.close()
        except FileNotFoundError :
            file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies\\"+academy_name+"\\"+instance.name+".bin", 'wb')
            pickle.dump(instance, file)
            file.close()

# if __name__ == "__main__" :
#     a = Make_Academy_class.academy_information("한국it교육원a", "어느시 어느동 어느번지a", "0532456653a",\
# "www.gkit.coma", "이거,저거,요거,많이a")
#     b = Make_Academy_class.academy_information("한국it교육원b", "어느시 어느동 어느번지b", "0532456653b",\
# "www.gkit.comb", "이거,저거,요거,많이b")
#     c = Make_Academy_class.academy_information("한국it교육원c", "어느시 어느동 어느번지c", "0532456653c",\
# "www.gkit.comc", "이거,저거,요거,많이c")
#     last = Make_Academy_class.academy_information("!@#$", "어느시 어느동 어느번지last", "0532456653last",\
# "www.gkit.comlast", "이거,저거,요거,많이last")

    # test = Make_Academy_class.academies()
    # test.make_academy(a)
    # test.make_academy(b)
    # test.make_academy(c)
    # test.make_academy(last)
    # test.serch_academy_info()

    # aa = curriculum_information("a", {"a" : "1", "aa" : "2"}, "09:00~17:30", {"a" : "1", "aa" : "2"})
    # bb = curriculum_information("b", {"b" : "1", "bb" : "2"}, "09:00~17:30", {"a" : "1", "bb" : "2"})
    # cc = curriculum_information("c", {"c" : "1", "cc" : "2"}, "09:00~17:30", {"c" : "1", "cc" : "2"})
    #
    # ttest = curriculums()
    # ttest.make_curriculum("한국it교육원a", aa)
    # ttest.make_curriculum("한국it교육원b", bb)
    # ttest.make_curriculum("한국it교육원c", cc)
    # ttest.search_curriculum_info()
    # while 1 :
    #     test = Make_Academy_class.academies()
    #     test.serch_academy_info()
    #     ttest = curriculums()
    #     ttest.search_curriculum_info()
