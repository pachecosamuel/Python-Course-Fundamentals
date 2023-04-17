class Car:
    def __init__(self, tag):
        self.tag = tag

    def get_tag(self):
        return self.tag
    
    def drive(self, speed):
        print(f"I'm driving in {speed} mh/h")


kicks = Car("xyz-7762")
kicks.drive(100)
print(kicks.get_tag())
