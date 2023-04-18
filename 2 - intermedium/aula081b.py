from io import StringIO

brands = ""
archive = StringIO(brands)

while True:
    brands = input("Type a brand: ")
    if brands == "sair":
        break
    else:
        archive.write(brands)
        archive.write("\n")

archive.seek(0)

with open("empty.txt", "a", encoding="utf-8") as my_brands:
    for b in archive.readlines():
        my_brands.write(b);
        print(b)

