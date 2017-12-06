class HousePark:
    lastname = "박"
    def __init__(self,name):
        self.fullname = self.lastname + name
#    def setname(self, name):
#        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s 여행을 가다."%(self.fullname,where))

pey = HousePark("응용")
pey.travel("부산")

class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where,day):
        print("%s, %s 여행을 %d일 가다."%(self.fullname,where,day))

juliet = HouseKim("줄리엣")
juliet.travel("독도",3)