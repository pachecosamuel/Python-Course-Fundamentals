# n1 = int(input("Type your first grade: "));
# n2 = int(input("Type your first grade: "));
#
#
# if(((n1+n2)/2) >= 7.0):
#         print("Parabéns você foi aprovado");
# elif(((n1+n2)/2) >= 5.0 and ((n1+n2)/2) <= 7.0):
#         print("Você está de recuperação");
# else:
#         print("Você está reprovado");

number = float(input("Type a number -> "));

if(number > 0.0):
    if(number % 2 == 0):
        print("Positivo e par!");
    else:
        print("Positivo e ímpar");
else:
    if (number % 2 == 0):
        print("Negativo e par!");
    else:
        print("Negativo e ímpar");

