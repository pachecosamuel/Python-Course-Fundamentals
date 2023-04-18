# calcular a média entre 5 idades "automatizado"
totalSum = 0;

for a in range(1, 6):
    age = int(input(f"Type the {a}° age: "));
    totalSum += age;

    if(a == 5):
        print(f"The average between ages is {totalSum/a}\n");


for char in "phrase":
    print(char);