def input_ingredient() :
    ingredient_list= []
    while 1 :
        ingredient = input("안녕하세요. 원하시는 재료를 입력하세요. : ")
        if ingredient == "종료" :
            return  ingredient_list
        else :
            ingredient_list.append(ingredient)

def make_sandwiches(ingredient_list) :
    print("샌드위치를 만들겠습니다.")
    for ingredient in ingredient_list :
        print("%s를 추가합니다." %ingredient)

order = input("안녕하세요. 저희 가게에 방문해 주셔서 갑사합니다.\n1.주문\n2.종료\n  입력 : ")
if int(order) == 1 :
    ingredient_list = input_ingredient()
    make_sandwiches(ingredient_list)
    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")
else:
    print("이용해 주셔서 감사합니다.")