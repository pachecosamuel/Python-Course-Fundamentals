import os

my_new_path = os.path.join(os.getcwd(), "my_new_way")
# print(my_new_path)

# os.mkdir(my_new_path)
# os.chdir(my_new_path)

my_directories = os.listdir()

for i in range(len(my_directories)):
    print(my_directories[i])