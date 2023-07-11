# 람다 함수
add = lambda x, y: x + y
result = add(3, 4)
print(result)  # 출력: 7

# 맵
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # 출력: [1, 4, 9, 16, 25]

# 필터
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 출력: [2, 4]

# 리듀스
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 출력: 120
