class Car:
    def __init__(self, tag, max_speed):
        self.tag = tag
        self.max_speed = max_speed

    def get_tag(self):
        return self.tag
    
    def drive(self, speed):
        print(f"I'm driving in {speed} mh/h")

    def maximum_speed(self):
        print(f"Maximum speed is {self.max_speed} mh/h")

    def __str__(self):
        return f"{self.tag}, {self.max_speed}"


kicks = Car("xyz-7762", 220)
print(kicks)
print(kicks.__repr__())
print(kicks.__str__())


# print(kicks.get_tag())
# kicks.drive(100)
# kicks.maximum_speed()

