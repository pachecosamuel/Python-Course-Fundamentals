# try:
#     with open("empty.txt", "a", encoding="utf-8") as archive:
#         while True:
#             fruit = input("Type a fruit:")
#             if fruit == "sair":
#                 break
#             else:
#                 archive.write(fruit)
#                 archive.write("\n")

# except:
#     print("Something went wrong")


with open("empty.txt", "r", encoding="utf-8") as my_archive:
    for i in my_archive.readlines():
        print(i)