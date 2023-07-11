# 파일 쓰기
with open("file.txt", "w") as file:
    file.write("Hello, World!")

# 파일 읽기
with open("file.txt", "r") as file:
    contents = file.read()
    print(contents)  # 출력: Hello, World!
