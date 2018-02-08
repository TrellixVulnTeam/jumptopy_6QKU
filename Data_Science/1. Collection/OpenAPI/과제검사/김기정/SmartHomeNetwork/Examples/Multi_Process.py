import multiprocessing
from time import sleep

def myProcess(name,nsec):
    print ("---- do somthing ----")
    sleep(nsec)

if  __name__ == '__main__' :
    t = multiprocessing.Process(target=myProcess, args=("Process-1", 3))
    t.start()
    t.join()
    print ("---- exit ----")

"""
위에 언급했다시피 파이썬에서 병렬적으로 계산하는 상황에서의 멀티쓰레드는 오히려 더 성능이 안좋아 집니다.
이때 멀티 프로세스를 활용하여 해결 할 수 있는데요. (이 이유로 다른 언어보다 프로세스를 적극 활용합니다.)자 겁내지 마세요. 멀티쓰레드와 아주 흡사하게 만들 수 있습니다. 
import Queue 모듈이 아니라 from multiprocessing import Queue 모듈을 사용해야 한다는 점! 잊지마세요.
"""

