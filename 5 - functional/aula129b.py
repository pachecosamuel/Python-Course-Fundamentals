def talk_loud(func):
    def to_upper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return to_upper

@talk_loud
def order(*args):
    return f"I wanna a ice cream of {args[0]} and {args[1]}"

@talk_loud
def greetings(word):
    return f"Hello {word}"

print(order("Chocolate", "Strawberry"))
print(greetings("Samuel"))
