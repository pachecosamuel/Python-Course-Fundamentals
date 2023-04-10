matrix = [[1,2,3], [4,5,6], [7,8,9]]

for line in matrix:
    for element in line:
        print(element)

[print(values) for values in matrix]

[[print(element) for element in line] for line in matrix]