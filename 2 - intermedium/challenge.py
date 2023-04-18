people = []
sum_age = 0
sum_height = 0
# objeto -> person = [nome, idade, altura, peso]
# people.append(person) bidimensionalidade

while True:
    try:
        last_name = input("Type the name: ")

        if last_name == '':
            break
        else:
            age = int(input("Type the age: "))
            height = int(input("Type the height in centimeters: "))
            weight = float(input("Type the person's weight: "))

            sum_age += age
            sum_height += height

            person = [last_name, age, height, weight]
            people.append(person)
    except:
        print("You typed something wrong, pls try again.")


people.sort()

for i in people:
    print(f"Name = {i}")

print(f"Age average: {sum_age/len(people)}")
print(f"Height average: {sum_height/len(people)}")