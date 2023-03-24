#1° ler número positivo, inteiro, maior que zero e verificar se é par ou ímpar
number = int(input("Type a integer, positive number greater than zero: "));
if (number % 2 == 0):
    print(number, "is even!\n")
else:
    print(number, "is odd!\n")


#2° ler altura e sexo da pessoa
    # fórmula para homem: (72.7 * h) - 58;
    # fórmula para mulher: (62.1 * h) - 44.7;
gender = input("Type your gender as 'M' for man and 'W' for woman: ");
height = float(input("Type your height"));

imcMan = (72.7 * height) - 58;
imcWoman = (62.1 * height) - 44.7;

if(gender == 'M'):
    print("Your IMC is: ", imcMan);
else:
    print("Your IMC is: ", imcWoman);
