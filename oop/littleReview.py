class Car:
    def __init__(self, tag, max_speed, actual_speed = 0):
        self.tag = tag
        self.max_speed = max_speed
        self.actual_speed = actual_speed

    def __str__(self):
        return f"{self.tag}, {self.max_speed}, {self.actual_speed}."
    
    def get_tag(self):
        return self.tag
    
    def drive(self, speed):
        print(f"I'm driving in {speed} miles per hour.")

    def car_max_speed(self):
        return self.max_speed
    
    def speed_up(self):
        if (self.actual_speed >= 180):
            print(f"Maximum speed has already reached")
        else:
            self.actual_speed += 10
            print(f"Actual speed is {self.actual_speed} miles per hour.")
    
    def break_car(self):
        if (self.actual_speed <= 0):
            print(f"You are at minimum speed possible.")
        else:
            self.actual_speed -= 10
            print(f"Actual speed is {self.actual_speed} miles per hour.")
    

kicks = Car("XYZ-1000", 220)

print(kicks.get_tag())
kicks.drive(80)
print(kicks.car_max_speed())

for _ in range(20):
    kicks.speed_up()

for _ in range(20):
    kicks.break_car()
        