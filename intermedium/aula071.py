dict_numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

square = {key: value ** 2 for key, value in dict_numbers.items() if not(value%2)}

print(dict_numbers)
print(square)