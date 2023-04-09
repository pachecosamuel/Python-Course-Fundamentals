my_archive = open("cars.txt", "r", encoding="utf-8")

print(type(my_archive))

my_text = my_archive.read()

print(my_text)

my_archive.close()