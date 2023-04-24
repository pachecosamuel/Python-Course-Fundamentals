from time import time

t_init = time()
g = sum((num for num in range(100000000)))
t_final = time()
tempo_gen = t_final - t_init

t_initial = time()
l = sum([num for num in range(100000000)])
time_final = time()
tempo_list = time_final - t_initial

print(f"Time with generator: {tempo_gen}")
print(f"Time with list: {tempo_list}")