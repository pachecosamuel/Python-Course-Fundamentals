from sys import getsizeof
gen = (i ** 2 for i in range(10000) if i % 2 == 0)
lc = [i ** 2 for i in range(10000) if i % 2 == 0]

print(f"Gen = {getsizeof(gen)}")
print(f"LC = {getsizeof(lc)}")