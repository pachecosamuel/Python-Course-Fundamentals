products = [('cook_top', 2000), ("tv", 3000)]

print(list(map(lambda x: (x[0], x[1] * 1.05), products)))