def verify_cousin_number(numero):
    count = 0;
    for i in range(1, numero + 1):
        if(numero % i == 0):
            count += 1;

    if count > 2:
        print(f"{numero} it's not a cousin number.")
    else:
        print(f"{numero} it's a cousin number.")

verify_cousin_number(14)

