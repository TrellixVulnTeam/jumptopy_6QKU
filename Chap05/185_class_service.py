class Service: # <-- Service 클래스 명
    secret = "영구는 배꼽이 두 개다." # secret <-- 클래스의 멤버 변수 (Member Variable)
    name =""

    def __init__(self,name): # 생성자(Constructor)
        self.name = name # self.name <-- 클래스의 멤버 변수
        print("멤버변수 %s 를 초기화 하였습니다" %self.name)
    def sum(self, a,b): # 멤버 함수 (Member Function)
        result = a + b # Service 멤버함수 sum의 로컬 변수
        print("%s님 %s + %s = %s 입니다." % (self.name,a,b,result))
    def __del__(self):
        print("저희 서비스를 이용해 주셔서 감사합니다.")
input()
pey = Service("홍길동") #pey: 객체, 인스턴스: 클래스와 객체와의 관계
                         # pey는 Service의 인스턴스다.
input()
pey.sum(1,1)
input()
