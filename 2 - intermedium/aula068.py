numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double_list = []
pythonic_list = []

# Traditional way
for i in range(len(numbers)):
    double_list.append(numbers[i] * 2)

# List comprehension
double_list = [(num / 1.5) for num in numbers if (num % 2)]
pythonic_list = [(n * 2) for n in numbers if (n % 2 == 0)]

print(double_list)
print(pythonic_list)
