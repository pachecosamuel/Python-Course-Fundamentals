from io import StringIO

fruits = ""
archive = StringIO(fruits)

while True:
    fruit = input("Type a fruit: ")
    if fruit == "sair":
        break
    else:
        archive.write(fruit)
        archive.write("\n")

archive.seek(0)

with open("empty.txt", "a", encoding="utf-8") as my_fruits:
    for line in archive.readlines():
        my_fruits.write(line)