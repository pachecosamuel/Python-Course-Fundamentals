def cousin_number(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count > 2:
        print(f"{number} it's not a cousin number!")
    else:
        print(f"{number} it's a cousin number!")