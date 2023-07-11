# 클래스 정의
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 클래스 인스턴스 생성
rect = Rectangle(5, 3)
print(rect.area())  # 출력: 15
