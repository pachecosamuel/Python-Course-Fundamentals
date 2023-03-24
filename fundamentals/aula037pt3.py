value = int(input("Type a number who you want to: "));
sum = 0;
qtd = 0;

while value != -1:
    sum += value;
    value = int(input("Type a number who you want to: "));
    qtd += 1;

print(f"The average is: {sum/qtd}");


# number = int(input("Type the table who you want to: "));
# i = 1;
#
# while (i <= 10):
#     print(f"The actual value between {i} * {number} is: {i * number}");
#     i += 1;

