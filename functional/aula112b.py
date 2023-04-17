even_list = [2, -4, 6, -8, 10]
odd_list = [1, -3, 5, -7, 9, 11, 13, 15, 17]

cube = map(lambda x: pow(x, 3), even_list)
sum_ = map(lambda x, y: x + y, even_list, odd_list)

print(f"Cube -> {list(cube)}")
print("----------------------------------")
print(f"Sum -> {list(sum_)}")
