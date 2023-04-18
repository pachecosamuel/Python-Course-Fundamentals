phrase = "I have an amazing spirits who accompany me"
numbers = [1, 2, 3, 4, 5, 6]

def my_loop(iterable_):
    it = iter(iterable_)
    while True:
        try:
            print(next(it), end=' ')
        except StopIteration:
            break

my_loop(phrase)
print("")
my_loop(numbers)