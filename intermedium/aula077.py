with open("cars.txt", "r", encoding="utf-8") as my_archive:
    for line in my_archive:
        print(line.strip())

print(my_archive.closed)