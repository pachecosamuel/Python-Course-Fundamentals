# Associating with a variable 
sum = lambda x, y, z: x + y + z
print(sum(2, 4, 6))

# Executing without a variable
print((lambda a,b,c: a * b * c)(1, 3, 5))

print("----------------------")

def greetings():
    title = "Mr(Ms.) "
    action = lambda name: title + name
    return action

another_way = greetings()
print(greetings())
print(another_way("Bia"))
print(greetings()("Samuel"))

