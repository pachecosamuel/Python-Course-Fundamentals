def potenciation(number, exponent=2):
    """This function will elevate a number to a specified exponent.
    number = 2, exponent = 3 -> 2³ = 8"""
    return pow(number, exponent);

def show_numbers(*args):
    return args;

def make_sum(*args):
    return sum(args);

def favorite_food(a, b, *args, c = 3, **kwargs):
    for i in kwargs:
        print(f"{i} likes {kwargs[i]}")


favorite_food(1, 2, ferrari=1000000, uno=20000, ecosport=50000)
print(show_numbers(1, 3, 5, 7, 9));
print(make_sum(1, 3, 5, 7, 9));
print(potenciation(exponent=2, number=5));
print(help(potenciation))

