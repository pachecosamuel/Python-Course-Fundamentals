la = [1, 3, 5, 7]
lb = [2, 4, 6, 8]
lx = [0, 0.1, 0.2, 0.3]

r = map(lambda x, y, z: x * y + z, la, lb, lx)
print(list(r))