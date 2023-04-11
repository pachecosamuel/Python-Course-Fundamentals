import os

print(os.getcwd())
my_path = os.path.join(os.getcwd(), '\\teste')
print(my_path)




---------------------------------------------------------------
from io import StringIO

starter = ""
archive = StringIO(starter)

while True:
    brand = input("Type a brand: ")
    if brand == 'sair':
        break
    else:
        archive.write(brand)
        archive.write("\n")

archive.seek(0)

with open("empty.txt", "a", encoding="utf-8") as my_brands:
    for i in archive.readlines():
        my_brands.write(i)
        print(i)