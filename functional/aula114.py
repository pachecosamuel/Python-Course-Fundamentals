from functools import reduce

one = reduce(lambda x, y: x + y, range(1, 10))
two = reduce(lambda x, y: x + y, range(1, 10), 1000)

print(one)
print(two)