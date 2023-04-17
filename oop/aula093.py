class Car:
    def __init__(self, tag, max_speed, actual_speed = 0):
        self.__tag = tag
        self.__max_speed = max_speed
        self.__actual_speed = actual_speed

    def get_tag(self):
        return self.__tag
    
    def get_maximum_speed(self):
        return self.__max_speed
    
    def set_maximum_speed(self, new_speed):
        self.__max_speed = new_speed
        print(f"The new maximum speed allowed is: {new_speed}")
    
    def drive(self, speed):
        print(f"I'm driving in {speed} mh/h")

    def __str__(self):
        return f"{self.__tag}, {self.__max_speed}, {self.__actual_speed}"
    
    def speed_up(self):
        if self.__actual_speed > self.__max_speed:
            return f"Maximum speed reached"
        else:
            self.__actual_speed += 10
            print(f"Actual speed = {self.__actual_speed} mh/h")
        
    def break_car(self):
        if self.__actual_speed < 10:
            return f"Minimum speed reached"
        else:
            self.__actual_speed -= 10
            print(f"Actual speed = {self.__actual_speed} mh/h")
        


kicks = Car("xyz-7762", 220)
print(kicks)

# Right principle of encapsulation
kicks.set_maximum_speed(200)
print(kicks)
