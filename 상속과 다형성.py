class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("멍멍!")

class Cat(Animal):
    def sound(self):
        print("야옹!")

dog = Dog()
dog.sound()  # 출력: 멍멍!

cat = Cat()
cat.sound()  # 출력: 야옹!
