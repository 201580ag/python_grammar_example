# 딕셔너리 생성
person = {"name": "John", "age": 25, "city": "New York"}

# 딕셔너리 값 조회
print(person["name"])  # 출력: John

# 딕셔너리 값 변경
person["age"] = 30

# 딕셔너리 순회
for key, value in person.items():
    print(key, value)
