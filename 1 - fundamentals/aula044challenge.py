realstate = {};

while True:
    apto = int(input("Type the apartment's number: "));

    if apto == -1:
        break;

    owner = input("Type the name of the apartment's owner: ");

    realstate.update({apto: owner});

amount_apt = len(realstate)

sorted_real_state = dict(sorted(realstate.items()))

print(sorted_real_state)
print(amount_apt)

