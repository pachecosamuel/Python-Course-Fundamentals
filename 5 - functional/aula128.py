def be_polite(func):
    def being():
        print("Hello ...")
        func()
        print("Goodbye, it was a pleasure to meet you ...")
    return being

def greetings():
    print("Welcome to this challenge!")


improved_greetings = be_polite(greetings)

improved_greetings()