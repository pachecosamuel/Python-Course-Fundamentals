def counter(max):
    count = 0
    while count < max:
        yield count
        count += 1

gen = counter(10)

print(type(gen))
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))