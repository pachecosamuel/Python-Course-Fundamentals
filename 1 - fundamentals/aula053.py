def potencia(number, exponent=2):
    """This function receive two numbers, the first one is the base and
    the second will be the exponent. pow(2, 3) -> 2³ = 8;"""
    return pow(number, exponent)

# Parâmetros nomeados
print(potencia(exponent=3, number=5));
print(potencia(3, 4))
print(potencia(5))
print(help(potencia))

