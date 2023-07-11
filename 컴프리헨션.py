# 리스트 컴프리헨션
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)  # 출력: [1, 4, 9, 16, 25]

# 딕셔너리 컴프리헨션
fruits = ["apple", "banana", "cherry"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(fruit_lengths)  # 출력: {'apple': 5, 'banana': 6, 'cherry': 6}
