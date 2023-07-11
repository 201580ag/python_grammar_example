# 데코레이터 정의
def uppercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()
    return wrapper

# 데코레이터 사용
@uppercase_decorator
def say_hello():
    return "hello"

print(say_hello())  # 출력: HELLO
