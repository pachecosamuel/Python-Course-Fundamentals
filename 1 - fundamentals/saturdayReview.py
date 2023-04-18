cities = [];

while True:
    city = input("Type a city's name: ");

    if(city == 'sair'):
        break;
    else:
        cities.append(city);

cities.sort();
for city in cities:
    print(city)