import os
# print(os.getcwd())
# print(os.name)

my_path = (os.path.join(os.getcwd(), "my_folder"))
# print(my_path)

# os.mkdir(my_path)
os.chdir("..")
# print(os.getcwd())

print(os.listdir())
dir_list = os.listdir()

for i in range(len(dir_list)):
    print(dir_list[i])

