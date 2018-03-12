"""
Python 3.4부터 일반적인 비동기 프로그래밍을 위한 멋진 API를 제공하는
새로운 asyncio 모듈이 생겼습니다. 이제  asyncio 모듈과 함께 coroutines를 사용하여 비동기
작업을 쉽게 수행 할 수 있게 됬습니다. 다음은 공식 문서의 예입니다
다시 말씀드리지만 전체 시스템이 블러킹이 안되게 하는 방법으로
첫째, 멀티쓰레드를 통해 하나만 블럭되게 한다
2. 비동기 방식을 사용한다.  이렇게 2개로 크게 볼 수 있다고 말했죠?
asycnio 는 비동기 방식에 대한 이야기 입니다.
"""

import asyncio
import datetime
import random


@asyncio.coroutine
def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
    yield from asyncio.sleep(random.randint(0, 5))


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()
"""
코드를 살펴보면 이 함수(display_date) 는 주어진 시간(초) 후에 완료되는 코루틴 (coroutine)입니다. 식별자 수(num)와 이벤트 루프(loop)를 매개변수로 받아 현재 시간을 계속 출력하는 coroutine 인 display_date (num, loop) 을 만듭니다. 코루틴이기 때문에 외부로 부터 값을 받아드리는 성질이 있다는 것은 예상 할 수 있겠지요?  즉 다음 asyncio.sleep () 함수 호출의 결과를 기다리기 위해 키워드yield from 를 사용했습니다. 그래서 우리는 그것에 임의의 초를 보내고 asyncio.ensure_future()를 사용하여 기본 이벤트 루프에서 코루틴의 실행을 스케쥴합니다. 그런 다음 루프가 계속 실행되도록 요청 합니다.

출력을 보면 두 개의 coroutine이 동시에 실행되는데요. yield from 를 사용할 때, 이벤트 루프는 코루틴의 실행을 일시 중지하고 다른 루틴을 실행합니다. 따라서 두 개의 코루틴이 동시에 실행됩니다 (그러나 잊지 말아야 할 것은 이벤트 루프가 단일 스레드이기 때문에 병렬로 실행되지 않습니다).

 yield from 는for x in asyncio.sleep(random.randint(0, 5)): yield x 에 대한 멋진 syntactic sugar 입니다. 그것은 비동기 코드를 좀 더 간략히 만들어 주죠. 

"""