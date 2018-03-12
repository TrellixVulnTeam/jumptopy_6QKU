from Search import Partial_Value
import Checkfile


def search_result(object):
    if len(object) == 1:  #
        for i in range(len(Checkfile.load_json_file())):
            for p in object:
                if p == Checkfile.load_json_file()[i]["학생ID"] or p == Checkfile.load_json_file()[i]["학생정보"]["이름"] :
                    print(("학생ID: %s" % Checkfile.load_json_file()[i]["학생ID"]) + "\n" +
                          ("이름: %s" % Checkfile.load_json_file()[i]["학생정보"]["이름"]) + "\n" +
                          ("나이: %s" % Checkfile.load_json_file()[i]["학생정보"]["나이"]) + "\n" +
                          ("주소: %s" % Checkfile.load_json_file()[i]["학생정보"]["주소"]) + "\n\n" +
                          ("과거수강횟수: %s" % Checkfile.load_json_file()[i]["수강정보"]["과거수강횟수"]) + "\n")
                    for x in range(len(Checkfile.load_json_file()[i]["수강정보"]) - 1):
                        print(("강좌" + str(x + 1)) + "\n\n" +
                              ("강의코드" + str(x + 1) + ": " + "%s" %
                               Checkfile.load_json_file()[i]["수강정보"]["강좌" + str(x)]["강의코드"]) + "\n" +
                              ("강의명" + str(x + 1) + ": " + "%s" %
                               Checkfile.load_json_file()[i]["수강정보"]["강좌" + str(x)]["강의명"]) + "\n" +
                              ("강사" + str(x + 1) + ": " + "%s" %
                               Checkfile.load_json_file()[i]["수강정보"]["강좌" + str(x)]["강사"]) + "\n" +
                              ("개강일" + str(x + 1) + ": " + "%s" %
                               Checkfile.load_json_file()[i]["수강정보"]["강좌" + str(x)]["개강일"]) + "\n" +
                              ("종료일" + str(x + 1) + ": " + "%s" %
                               Checkfile.load_json_file()[i]["수강정보"]["강좌" + str(x)]["종료일"]) + "\n")
                        continue

    if len(object) >= 2:
        print(("중복된 값으로 인한 학생ID 요약"))
        for i in range(len(Checkfile.load_json_file())):
            for x in object:

                if x == Checkfile.load_json_file()[i]["학생ID"] or x == Checkfile.load_json_file()[i]["학생정보"]["이름"] or x == \
                        Checkfile.load_json_file()[i]["학생정보"]["나이"] or x == Checkfile.load_json_file()[i]["학생정보"]["주소"]:
                    print("")
                    print(("학생이름: %s" % Checkfile.load_json_file()[i]["학생정보"]["이름"]))
                    print(("학생ID: %s" % Checkfile.load_json_file()[i]["학생ID"]))
                    break


