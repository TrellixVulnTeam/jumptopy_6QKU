"""
이제 좀 추상층을 높여 봅시다. 현재 각종 언어들 마다 쓰레드를 직접적으로 사용자가 만들어서 사용하는 것을 지양하고 있으며, 추상층을 쌓아올려서 보다 쉽게 하지만 좀 더 적극적으로 사용 할 수 있게 끔 유도하고 있는데요. 그것은 쓰레드를 직접 사용하는데에서 오는 어려움이기 때문일 것입니다. 자바의 경우 5버전부터 더그리(Doug Lea) 에 의해 강력한 동시성 라이브러리들이 추가 되기 시작했는데요. 많이들 사용하시는 Executor 과 같은 것이 파이썬에도 있습니다.
Executors / ThreadPoolExecutor / ProcessPoolExecutor
Executors 를 상속받은 2개의 구현체입니다. 이름에서 나타나듯이 하나는 쓰레드풀이고 하나는 프로세스 풀입니다. 둘은 거의 동일한 구문으로 사용되기 때문에 둘 중에 하나(프로세스풀)만 살펴보죠.
"""
from concurrent.futures import ProcessPoolExecutor
from time import sleep


def return_after_5_secs(message):
    sleep(5)
    return message

if __name__ == '__main__' :
    pool = ProcessPoolExecutor(3)

    future = pool.submit(return_after_5_secs, ("hello"))
    print(future.done())
    sleep(5)
    print(future.done())
    print("Result: " + future.result())





"""
역시 코드가 모든것을 잘 설명해주고 있습니다. 파이썬은 정말 위대합니다.ㅎㅎ
쓰레드 3개를 운용하는 풀을 만들어주고, 하나의 일(Task) 를 제출한 후에 바로 future 를 리턴 받습니다.
리턴 받은 future 에 진짜 값이 들어 올 때까지 대기하다가 실제 값이 있을 경우 (코드에서는 future.done() 이 True일 경우) result 함수를 호출해서 가져옵니다.  동일한 작업을 ThreadPoolExecutor 를 통해서도 쓰레드레벨로 가능합니다.
"""