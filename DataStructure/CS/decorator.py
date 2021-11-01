#데코레이더 사용 전
def hello():
    print('hello 함수 시작')
    print('hello')
    print('hello 함수 끝')

def world():
    print('world 함수 시작')
    print('world')
    print('world 함수 끝')

hello()
world()

'''
hello 함수 시작
hello
hello 함수 끝
world 함수 시작
world
world 함수 끝
'''

# 데코레이터 사용 후
def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():                           # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환

def hello():
    print('hello')

def world():
    print('world')

trace_hello = trace(hello)    # 데코레이터에 호출할 함수를 넣음
trace_hello()                 # 반환된 함수를 호출
trace_world = trace(world)    # 데코레이터에 호출할 함수를 넣음
trace_world()                 # 반환된 함수를 호출


# @ 사용하는 경우
def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환

@trace    # @데코레이터
def hello():
    print('hello')

@trace    # @데코레이터
def world():
    print('world')

hello()    # 함수를 그대로 호출
world()    # 함수를 그대로 호출