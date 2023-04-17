from car import Car

car1 = Car("BMW", "X1", 2022, 1000)

print(car1.get_make())

print(car1.get_model())

print(car1.get_year())

print(car1.get_kilometers())

print("-------------------------------")

car1.set_kilometers(500)

print(car1.get_kilometers())