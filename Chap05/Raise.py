def rsp(mine, yours):
    allowed = ['가위','바위', '보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError

try:
    rsp('가위', '바')
except ValueError:
    print('잘못된 값을 넣었습니다!')
