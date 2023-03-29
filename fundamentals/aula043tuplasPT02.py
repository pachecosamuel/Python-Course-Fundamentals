list_ages = [];

while True:
    age = int(input("Type an age: "));

    if(age == -1):
        break;
    else:
        list_ages.append(age);

count_ages = len(list_ages)

tuple_ages = tuple(list_ages);
print(f"The amount of typed ages was {count_ages}\n"
      f"The average between the ages is {(sum(tuple_ages) / count_ages)}");