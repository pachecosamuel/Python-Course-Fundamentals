def factorial(number):
    if number > 1:
        return number * factorial(number - 1)
    else:
        return 1
    
def pythonic_factorial(number):
    return (number * factorial(number -1)) if number > 1 else 1

print(factorial(5))

print(pythonic_factorial(6))