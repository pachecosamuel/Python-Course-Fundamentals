number = int(input("Type the factorial number who you want to: "));
factorial = 1;

for fact in range(1, (number+1)):
    factorial = fact * factorial;

    if(fact == number):
        print(f"Your factorial! number is: {factorial}\n");



