my_archive = open("cars.txt", "a")

text = input("Type a car who you like most: ")

my_archive.write(text)

my_archive.close()