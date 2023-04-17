my_list = [
    {'name': 'Alejandro', 'age': 15},
    {'name': 'Juan', 'age': 17},
    {'name': 'Maria', 'age': 20},
    {'name': 'Pedro', 'age': 21}
]

only_menores = filter(lambda set_: set_['age'] < 18, my_list)
print(list(only_menores))