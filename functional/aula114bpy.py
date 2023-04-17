from functools import reduce

my_list = [
    {'name': 'Alejandro', 'age': 15},
    {'name': 'Juan', 'age': 17},
    {'name': 'Maria', 'age': 20},
    {'name': 'Pedro', 'age': 21},
    {'name': 'Ana', 'age': 12},
    {'name': 'Carlos', 'age': 23},
    {'name': 'Ana', 'age': 24},
    {'name': 'Carlos', 'age': 15},
    {'name': 'Ana', 'age': 26},
]

only_ages = map(lambda x: x['age'], my_list)

only_small_ages = filter(lambda age: age < 18, only_ages)

average_age = reduce(lambda age, ages: ages + age, only_small_ages)

print(average_age)
