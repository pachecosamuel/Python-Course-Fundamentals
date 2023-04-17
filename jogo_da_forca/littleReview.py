class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def greetings(self):
        return f"I'm {self.get_name()} animal"


class Terrestrial(Animal):
    def __init__(self, name, foot):
        super().__init__(name)
        self.__foot = foot

    def greetings(self):
        return f"I'm {self.get_name()} animal TERRESTRIAL"

    def walkings(self):
        return f"My kind of animal is terrestrial"


class Aquatic(Animal):
    def __init__(self, name):
        super().__init__(name)

    def greetings(self):
        return f"I'm {self.get_name()} animal AQUATIC"

    def swimming(self):
        return f"My kind of animal is aquatic"


class Penguim(Terrestrial, Aquatic):
    def __init__(self, name, foot):
        super().__init__(name, foot)


penguim1 = Penguim("Bob", "42")
print(penguim1.get_name())
print(penguim1.greetings())
print(penguim1.walkings())
print(penguim1.swimming())

print("-------------------------------------")

turtle1 = Terrestrial("Ninja", 4)
print(turtle1.get_name())
print(turtle1.greetings())
print(turtle1.walkings())

print("-------------------------------------")

dolphin1 = Aquatic("John")
print(dolphin1.get_name())
print(dolphin1.greetings())
print(dolphin1.swimming())

print("-------------------------------------")
