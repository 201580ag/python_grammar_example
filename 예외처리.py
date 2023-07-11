try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Error:", str(e))  # 출력: Error: division by zero
