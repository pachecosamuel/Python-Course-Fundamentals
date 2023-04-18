my_list = [
    {'name': 'Alejandro', 'age': 18},
    {'name': 'Juan', 'age': 19},
    {'name': 'Maria', 'age': 20},
    {'name': 'Pedro', 'age': 21}
]

sum_ = 0

only_names = lambda set_: set_.get('name')
only_names_v2 = map(lambda set_: set_['name'], my_list)

only_age = lambda set_: set_.get("age")
only_age_v2 = map(lambda set_: set_['age'], my_list)

print(list(map(only_names, my_list)))
print(list(only_names_v2))

print(list(map(only_age, my_list)))
print(list(only_age_v2))

print(sum(only_age_v2))