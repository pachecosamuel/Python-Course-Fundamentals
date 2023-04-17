def square(value):
    return lambda : value * value

my_values = [square(value) for value in range(1, 6)]

print(my_values)
print("----------------------------")
print(my_values[0])
print("----------------------------")
print(my_values[0]())
print("----------------------------")

for element in my_values:
    print(element())