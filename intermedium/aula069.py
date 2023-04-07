numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
double_list = [x ** 2 for x in numbers if x % 2]
half_list = [(e / 2) for e in numbers if (e % 2 == 0)]

friends = ['ana', 'carol', 'john', 'sam', 'bee']

print(friends)
print([x.title() for x in friends])
print([f.upper() for f in friends])
print([s.split('a') for s in friends])


