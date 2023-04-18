class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def greetings(self):
        return f"I'm a {self.__name} animal"
    

class Terrestrial(Animal):
    def __init__(self, name):
        super().__init__(name)

    def greetings(self):
        return f"I'm a {self.get_name()} terrestrial"
    
    def walk(self):
        return f"I'm a {self.get_name()} and i'm walking right now"
    

class Aquatic(Animal):
    def __init__(self, name):
        super().__init__(name)

    def greetings(self):
        return f"I'm a {self.get_name()} aquatic"
    
    def swimming(self):
        return f"I'm a {self.get_name()} and i'm swimming right now"
    

class Penguim(Terrestrial, Aquatic):
    def __init__(self, name):
        super().__init__(name)


turtle = Terrestrial("Ninja")
print(turtle.greetings())
print(turtle.walk())

print("-------------------")

dolphin = Aquatic("Dubuzinho")
print(dolphin.greetings())
print(dolphin.swimming())

print("-------------------")

penguin = Penguim("Captain")

print(penguin.greetings())

print(penguin.swimming())

print(penguin.walk())
        
