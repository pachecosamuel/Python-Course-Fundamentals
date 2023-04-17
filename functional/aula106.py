def double(value):
    return value * 2

def square(value):
    return value * value

def calculate(operation, iterator, function):
    print(f"Calculating {operation}...")
    for num in iterator:
        print(f"{num} -> {function(num)}")

calculate("Multiply", range(1,6), double)
calculate("Square", range(1,6), square)