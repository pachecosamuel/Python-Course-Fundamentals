from random import (
    random,
    uniform,
    randint,
    choice,
    shuffle
)

number_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 11]
car_list = ["Masseratti", "Ferrari", "Horus", "BMW"]

print(f"Random = {random()}")
print(f"Uniform = {uniform(2, 10)}")
print(f"Randint = {randint(2, 200)}")
print(f"Choice = {choice(car_list)}")
