# 메타클래스 정의
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        # 클래스 생성 전에 실행됨
        print("Creating class:", name)
        return super().__new__(cls, name, bases, attrs)

# 메타클래스를 사용하여 클래스 생성
class MyClass(metaclass=MyMeta):
    def __init__(self, x):
        self.x = x

    def print_x(self):
        print(self.x)

obj = MyClass(10)  # 출력: Creating class: MyClass
obj.print_x()  # 출력: 10
