def cousin_number(number):
    count = 0;
    for i in range(1, number+1):
        if number % i == 0:
            count += 1

    if count > 2:
        print(f"{number} It's not a cousin number");
    else:
        print(f"{number} It's a cousin number");

cousin_number(17)
