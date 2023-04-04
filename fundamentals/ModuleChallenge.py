# receive (nome, idd, calçado) de 5 pessoas
# ordenar por ordem alfabética e printar
# média da idd
# número médio do calçado
people = [];
sum_age = 0;
sum_shoes_number = 0;

for p in range (1,6):
    print(f'Person {p}: ');
    name = input("Type the name: ");
    age = int(input("Type the age: "));
    shoesNumber = int(input("Type the shoe number: "));
    print('-------------------------------------------------');
    sum_age += age;
    sum_shoes_number += shoesNumber;
    person = [name, age, shoesNumber];
    people.append(person);

ordered_people = sorted(people);

for i in range(0, 5):
    print(f'Name: {ordered_people[i][0]}\n'
          f'Age: {ordered_people[i][1]}\n'
          f'Shoes Number: {ordered_people[i][2]}');

    if i == 4:
        print(f'------------------------------------\n'
              f'Age average: {sum_age / 5}\n'
              f'Shoes number average: {shoesNumber / 5}');