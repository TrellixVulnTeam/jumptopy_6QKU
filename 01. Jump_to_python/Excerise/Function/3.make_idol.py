def show_candidates(candidate_list):
    for candidate in candidates_list:
        print(candidate,end='')

def make_idol(candidate_list): # 신예 아이돌 (이름) 인기 급상승
    for i in candidate_list:
        idol_msg = "신예 아이돌 %s 인기 급상승!\n" %i
        print(idol_msg,end='')

def make_world_star(candidate_list): # 아이돌 (이름) 월드스타 등극
    for j in candidates_list:
        idol_msg = "아이돌 %s 월드스타 등극!\n" %j
        print(idol_msg,end='')

f = open("D:\\Python_workspace\\jumptopy\\Excerise\\Function\\연습생.txt", 'r', encoding='UTF8')
candidates= f.read()
candidates_list = candidates.split('\n')
show_candidates(candidates_list)
make_idol(candidates_list)
make_world_star(candidates_list)
f.close()