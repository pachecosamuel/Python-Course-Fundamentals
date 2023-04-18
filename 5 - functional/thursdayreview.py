from functools import reduce

aleatory_numbers = (10, 5, 3, 25, 1.5, 11, -1.5)
names = ['John', 'Maria', 'Ralf', 'Maximiliano', 'Joane']

print(reduce(lambda x, y: x + y, aleatory_numbers))
print(reduce(lambda a, b: a + b, range(1, 50), 1000))
# print(min(names, key = lambda name: len(name)))
# print(max(names, key = lambda name: len(name)))

# print(min(aleatory_numbers))
# print(max(aleatory_numbers))

# print(sorted(aleatory_numbers))
# print(sorted(aleatory_numbers, reverse=True))