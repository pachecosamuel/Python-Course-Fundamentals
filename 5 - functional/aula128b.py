def be_polite(func):
    def being():
        print("Hello ...")
        func()
        print("Goodbye, it was a pleasure to meet you ...")
    return being

@be_polite
def greetings():
    print("Welcome to this challenge!")

greetings()