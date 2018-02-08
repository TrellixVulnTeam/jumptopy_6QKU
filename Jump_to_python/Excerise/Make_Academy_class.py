import pickle
import os

class academy_information() :
    def __init__(self, name, number, address, web_address, curriculums) :
        self.name = name
        self.number = number
        self.address = address
        self.web_address = web_address
        self.curriculums = curriculums

class academies() :
    def serch_academy_info(self):
        order = input("검색 옵션을 설정해 주십시오.\n1.학원전체정보출력 2.학원명만출력 3.학원찾기 4.학원삭제 : ")
        print()
        try :
            file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies.bin", 'rb')
        except FileNotFoundError :
            print("파일이 없습니다.")
            exit()

        if order == '1' :
            while 1 :
                try :
                    temp = pickle.load(file)
                    print("학원이름 : %s" %temp.name)
                    print("전화번호 : %s" %temp.number)
                    print("주소 : %s" %temp.address)
                    print("홈페이지 : %s" %temp.web_address)
                    print("교육과정 : %s" %temp.curriculums, end = "\n\n")
                except : break
        elif order == '2' :
            numbering = 1
            while 1 :
                try :
                    temp = pickle.load(file)
                    print("%d.학원 : %s" %(numbering, temp.name))
                    numbering += 1
                except : break
            print()
        elif order == '3' :
            search_academy_name = input("학원 이름을 치세요. : ")
            while 1 :
                try :
                    temp = pickle.load(file)
                    if temp.name == search_academy_name :
                        print("학원이름 : %s" % temp.name)
                        print("전화번호 : %s" % temp.number)
                        print("주소 : %s" % temp.address)
                        print("홈페이지 : %s" % temp.web_address)
                        print("교육과정 : %s" % temp.curriculums)
                        break
                except :
                    print("찾으시는 학원(%s)이 없습니다." %search_academy_name)
                    break
            print()
        elif order == '4' :
            delet_dir_name = input("삭제하려는 학원 이름을 입력하십시오. : ")
            try :
                os.rmdir("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies\\"+delet_dir_name)
            except OSError as e_msg :print(e_msg)
        file.close()

    def make_academy(self, instance) :
        try :
            if instance.name != "!@#$" :
                os.mkdir("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies\\"+instance.name)
                for x in str(instance.curriculums).split(',') :
                    try :
                        ffile = open("D:\Pycharm_projects\Emigration\Managing_Academies\Academies\
\\"+instance.name+"\\"+x+".bin", 'rb')
                        ffile.close()
                    except FileNotFoundError :
                        ffile = open("D:\Pycharm_projects\Emigration\Managing_Academies\Academies\
\\"+instance.name+"\\"+x+".bin", 'wb')
                        ffile.close()
            try :
                file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies.bin", 'rb')
                file.close()
                file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies.bin", 'ab')
                pickle.dump(instance, file)
                file.close()
            except FileNotFoundError :
                file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
\\Academies.bin", 'wb')
                pickle.dump(instance, file)
                file.close()

        except FileExistsError :
            print("%s라는 학원은 이미 생성되었습니다." %instance.name)

# class academy_information() :
#     def __init__(self, name, number, address, web_address, curriculums) :
#         self.name = name
#         self.number = number
#         self.address = address
#         self.web_address = web_address
#         self.curriculums = curriculums
#
# class academies() :
#     def serch_academy_info(self):
#         order = input("검색 옵션을 설정해 주십시오.\n1.학원전체정보출력 2.학원명만출력 3.학원찾기 : ")
#         print()
#         try :
#             file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
# \\Academies.bin", 'rb')
#         except FileNotFoundError :
#             print("파일이 없습니다.")
#             exit()
#
#         if order == '1' :
#             while 1 :
#                 temp = pickle.load(file)
#                 if temp.name == "!@#$" : break
#                 else :
#                     print("학원이름 : %s" %temp.name)
#                     print("전화번호 : %s" %temp.number)
#                     print("주소 : %s" %temp.address)
#                     print("홈페이지 : %s" %temp.web_address)
#                     print("교육과정 : %s" %temp.curriculums, end = "\n\n")
#         elif order == '2' :
#             numbering = 1
#             while 1 :
#                 temp = pickle.load(file)
#                 if temp.name == "!@#$" : break
#                 else :
#                     print("%d.학원 : %s" %(numbering, temp.name))
#                     numbering += 1
#             print()
#         elif order == '3' :
#             search_academy_name = input("학원 이름을 치세요. : ")
#             while 1 :
#                 temp = pickle.load(file)
#                 if temp.name == "!@#$" :
#                     print("찾으시는 학원(%s)이 없습니다." %search_academy_name)
#                     break
#                 elif temp.name == search_academy_name :
#                     print("학원이름 : %s" % temp.name)
#                     print("전화번호 : %s" % temp.number)
#                     print("주소 : %s" % temp.address)
#                     print("홈페이지 : %s" % temp.web_address)
#                     print("교육과정 : %s" % temp.curriculums)
#                     break
#             print()
#         file.close()
#
#     def make_academy(self, instance) :
# #         file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
# # \\Academies.bin", 'ab')
# #         pickle.dump(instance, file)
#         try :
#             if instance.name != "!@#$" :
#                 os.mkdir("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
# \\Academies\\"+instance.name)
#                 for x in str(instance.curriculums).split(',') :
#                     try :
#                         ffile = open("D:\Pycharm_projects\Emigration\Managing_Academies\Academies\
# \\"+instance.name+"\\"+x+".bin", 'rb')
#                         ffile.close()
#                     except FileNotFoundError :
#                         ffile = open("D:\Pycharm_projects\Emigration\Managing_Academies\Academies\
# \\"+instance.name+"\\"+x+".bin", 'wb')
#                         ffile.close()
#
#             file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\
# \\Academies.bin", 'ab')
#             pickle.dump(instance, file)
#             file.close()
#         except FileExistsError :
#             print("%s라는 학원은 이미 생성되었습니다." %instance.name)

# if __name__ == "__main__" :
#     a = academy_information("한국it교육원a", "어느시 어느동 어느번지a", "0532456653a",\
# "www.gkit.coma", "이거,저거,요거,많이a")
#     b = academy_information("한국it교육원b", "어느시 어느동 어느번지b", "0532456653b",\
# "www.gkit.comb", "이거,저거,요거,많이b")
#     c = academy_information("한국it교육원c", "어느시 어느동 어느번지c", "0532456653c",\
# "www.gkit.comc", "이거,저거,요거,많이c")
#     last = academy_information("!@#$", "어느시 어느동 어느번지last", "0532456653last",\
# "www.gkit.comlast", "이거,저거,요거,많이last")
#
#     test = academies()
#     test.make_academy(a)
#     test.make_academy(b)
#     test.make_academy(c)
#     test.make_academy(last)
#     test.serch_academy_info()

    # class academy_information() :
    #     academy_name = ""
    #     academy_number = ""
    #     academy_address = ""
    #     academy_web_address = ""
    #     academy_curiculums = ""
    #
    #     def make_academy_info(self, name, number, address, web_address, curiculums) :
    #         self.academy_name = name
    #         self.academy_number = number
    #         self.academy_address = address
    #         self.academy_web_address = web_address
    #         self.academy_curiculums = curiculums
    #
    # class academies(academy_information) :
    #     def serch_academy_info(self):
    #         order = input("검색 옵션을 설정해 주십시오.\n1.학원전체정보출력 2.학원명만출력 3.학원찾기 : ")
    #         try :
    #             file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\\Academies.bin", 'rb')
    #         except FileNotFoundError :
    #             print("파일이 없습니다.")
    #             exit()
    #
    #         if order == '1' :
    #             while 1 :
    #                 temp = pickle.load(file)
    #                 if temp.academy_name == "!@#$" : break
    #                 else :
    #                     print("학원이름 : %s" %temp.academy_name)
    #                     print("전화번호 : %s" %temp.academy_number)
    #                     print("주소 : %s" %temp.academy_address)
    #                     print("홈페이지 : %s" %temp.academy_web_address)
    #                     print("교육과정 : %s" %temp.academy_curiculums)
    #         elif order == '2' :
    #             while 1 :
    #                 temp = pickle.load(file)
    #                 if temp.academy_name == "!@#$" : break
    #                 else :
    #                     print("학원이름 : %s" %temp.academy_name)
    #         elif order == '3' :
    #             serch_academy_name = input("학원 이름을 치세요. : ")
    #             while 1 :
    #                 temp = pickle.load(file)
    #                 if temp.academy_name == "!@#$" :
    #                     print("찾으시는 학원(%s)이(가) 없습니다." %serch_academy_name)
    #                     break
    #                 elif temp.name == serch_academy_name :
    #                     print("학원이름 : %s" % temp.academy_name)
    #                     print("전화번호 : %s" % temp.academy_number)
    #                     print("주소 : %s" % temp.academy_address)
    #                     print("홈페이지 : %s" % temp.academy_web_address)
    #                     print("교육과정 : %s" % temp.academy_curiculums)
    #         file.close()
    #
    #     def make_academy(self, instance) :
    #         file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\\Academies.bin", 'ab')
    #         pickle.dump(instance, file)
    #
    # if __name__ == "__main__" :
    #     a = academy_information
    #     a.make_academy_info(a, "한국it교육원a", "어느시 어느동 어느번지a", "0532456653a",\
    # "www.gkit.coma", "이거,저거,요거,많이a")
    #     b = academy_information
    #     b.make_academy_info(b, "한국it교육원b", "어느시 어느동 어느번지b", "0532456653b",\
    # "www.gkit.comb", "이거,저거,요거,많이b")
    #     c = academy_information
    #     c.make_academy_info(c, "한국it교육원c", "어느시 어느동 어느번지c", "0532456653c",\
    # "www.gkit.comc", "이거,저거,요거,많이c")
    #     last = academy_information
    #     last.make_academy_info(last, "!@#$", "어느시 어느동 어느번지last", "0532456653last",\
    # "www.gkit.comlast", "이거,저거,요거,많이last")
    #
    #     test = academies()
    #     test.make_academy(a)
    #     test.make_academy(b)
    #     test.make_academy(c)
    #     test.make_academy(last)
    #
    #     test.serch_academy_info()


# class academies() :
#     name = ""
#     number = ""
#     address = ""
#     web_address = ""
#     curriculums = ""
#
#     def serch_academy_info(self):
#         order = input("검색 옵션을 설정해 주십시오.\n1.학원전체정보출력 2.학원명만출력 3.학원찾기 : ")
#         try :
#             file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\\Academies.bin", 'rb')
#         except FileNotFoundError :
#             print("파일이 없습니다.")
#             exit()
#
#         if order == '1' :
#             while 1 :
#                 try:
#                     temp = pickle.load(file)
#                 except AttributeError as e:
#                     print(e)
#                 if temp.name == "!@#$" : break
#                 else :
#                     print("학원이름 : %s" %temp.name)
#                     print("전화번호 : %s" %temp.number)
#                     print("주소 : %s" %temp.address)
#                     print("홈페이지 : %s" %temp.web_address)
#                     print("교육과정 : %s" %temp.curriculums)
#         elif order == '2' :
#             while 1 :
#                 temp = pickle.load(file)
#                 if temp.name == "!@#$" : break
#                 else :
#                     print("학원이름 : %s" %temp.name)
#         elif order == '3' :
#             serch_academy_name = input("학원 이름을 치세요. : ")
#             while 1 :
#                 temp = pickle.load(file)
#                 if temp.name == "!@#$" :
#                     print("찾으시는 학원(%s)이(가) 없습니다." %serch_academy_name)
#                     break
#                 elif temp.name == serch_academy_name :
#                     print("학원이름 : %s" % temp.name)
#                     print("전화번호 : %s" % temp.number)
#                     print("주소 : %s" % temp.address)
#                     print("홈페이지 : %s" % temp.web_address)
#                     print("교육과정 : %s" % temp.curriculums)
#         file.close()
#
#     def make_academy_info(self, name, number, address, web_address, curriculums) :
#         self.name = name
#         self.number = number
#         self.address = address
#         self.web_address = web_address
#         self.curriculums = curriculums
#
#     def make_academy(self, instance) :
#         file = open("D:\\Pycharm_projects\\Emigration\\Managing_Academies\\Academies.bin", 'ab')
#         pickle.dump(instance, file)
#         file.close()
#
# # if __name__ == "__main__" :
# #     a = academies
# #     a.make_academy_info("한국it교육원a", "어느시 어느동 어느번지a", "0532456653a",\
# # "www.gkit.coma", "이거,저거,요거,많이a")
# #     b = academies
# #     b.make_academy_info("한국it교육원b", "어느시 어느동 어느번지b", "0532456653b",\
# # "www.gkit.comb", "이거,저거,요거,많이b")
# #     c = academies
# #     c.make_academy_info("한국it교육원c", "어느시 어느동 어느번지c", "0532456653c",\
# # "www.gkit.comc", "이거,저거,요거,많이c")
# #     last = academies
# #     last.make_academy_info("!@#$", "어느시 어느동 어느번지last", "0532456653last",\
# # "www.gkit.comlast", "이거,저거,요거,많이last")
# #
# #     test = academies()
# #     test.make_academy(a)
# #     test.make_academy(b)
# #     test.make_academy(c)
# #     test.make_academy(last)
# #
# #     test.serch_academy_info()
#
# if __name__ == "__main__" :
#     a = academies()
#     a.make_academy_info("한국it교육원a", "어느시 어느동 어느번지a", "0532456653a", \
# "www.gkit.coma", "이거,저거,요거,많이a")
#     b = academies()
#     b.make_academy_info("한국it교육원b", "어느시 어느동 어느번지b", "0532456653b", \
# "www.gkit.comb", "이거,저거,요거,많이b")
#     c = academies()
#     c.make_academy_info("한국it교육원c", "어느시 어느동 어느번지c", "0532456653c", \
# "www.gkit.comc", "이거,저거,요거,많이c")
#     last = academies()
#     last.make_academy_info("!@#$", "어느시 어느동 어느번지last", "0532456653last", \
# "www.gkit.comlast", "이거,저거,요거,많이last")
#
#     test = academies()
#     # test.make_academy(a)
#     # test.make_academy(b)
#     # test.make_academy(c)
#     # test.make_academy(last)
#
#     test.serch_academy_info()