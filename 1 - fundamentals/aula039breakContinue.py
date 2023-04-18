n = 0;

while True:
    n += 1;

    if(n > 10):
        break;
    elif(n % 2 == 0):
        print(f"Even value: {n}")
    else:
        continue;
