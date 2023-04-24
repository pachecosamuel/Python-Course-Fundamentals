def talking_loud(func):
    def to_upper(word):
        return func(word).upper()
    return to_upper

@talking_loud
def greetings(word):
    return f"Hello {word}"

print(greetings("Samuel"))