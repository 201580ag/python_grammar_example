# 예외 처리
try:
    x = 10 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

# 예외 발생
def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)  # 출력: 0으로 나눌 수 없습니다.
