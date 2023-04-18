class Mamifero:
    def __init__(self, fur, boobs, age):
        self.__fur = fur
        self.__boobs = boobs
        self.__age = age

    def comunicate(self):
        pass

class Dog(Mamifero):
    def __init__(self, fur, boobs, age, tail):
        Mamifero.__init__(fur, boobs, age)
        self.__tail = tail
    
    def bark(self):
        print("Woof!")

class Cat(Mamifero):
    def __init__(self, fur, boobs, age, tail):
        super().__init__(fur, boobs, age)
        self.__tail = tail

    def meow(self):
        print("Meow!")