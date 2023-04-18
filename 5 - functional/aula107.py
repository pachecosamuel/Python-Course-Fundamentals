def mulplicate(value):
    def calculate(value2):
        return value * value2
    return calculate

execution_one = mulplicate(10)
execution_two = mulplicate(20)

print(execution_one(10))
print(execution_two(20))

