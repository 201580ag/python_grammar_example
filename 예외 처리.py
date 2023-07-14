try:
    print("정수 덧셈 계산기")
    a = int(input("첫 번째 숫자를 입력 해 주세요. : "))
    b = int(input("두 번째 숫자를 입력 해 주세요. : "))
except ValueError:
    print("정수만 입력 해 주세요.")
else:
    print(f"\n\n계산 결과 = {a+b}")
finally:
    print("-예외 처리 예제-")





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



try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Error:", str(e))
finally:
    print("Finally block")

# 여러 예외 처리
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid value")
