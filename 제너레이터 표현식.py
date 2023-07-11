# 제너레이터 표현식
numbers = [1, 2, 3, 4, 5]
squared_numbers = (x ** 2 for x in numbers)

for num in squared_numbers:
    print(num)  # 출력: 1 4 9 16 25
