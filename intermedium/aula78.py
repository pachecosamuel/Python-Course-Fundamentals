try:
    with open("fruits.txt", "a") as my_fruits:
        while True:
            fruit = input("Type a fruit: ")
            if fruit != "sair":
                my_fruits.write(fruit)
                my_fruits.write("\n")
            else:
                break
except:
    print("Something went wrong")
            