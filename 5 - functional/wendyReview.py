def talking_loud(func):
    def to_upper(word):
        return func(word).upper()
    return to_upper

@talking_loud
def greetings(word):
    return f"Hello, {word}!"


print(greetings("Samuel"))

# def be_polite(func):
#     def being():
#         print("Hello, morning! ")
#         func()
#         print("Bye bye!")
#     return being


# @be_polite
# def greetings():
#     print("Welcome to this challenge!")

# be_polite(greetings())

# def music_notes():
#     yield 'Dó'
#     yield 'Ré'
#     yield 'Mi'
#     yield 'Fá'
#     yield 'Sol'
#     yield 'Lá'
#     yield 'Si'

# def music_notes_v1():
#     return 'Dó'
#     return 'Ré'
#     return 'Só'

# new_gen = music_notes()
# new_gen_v1 = music_notes_v1()

# [print(note) for note in new_gen]
# print("------")
# [print(note) for note in new_gen_v1]

# def to_count(max):
#     cont = 1

#     while cont <= max:
#         yield cont
#         cont += 1

#     print(type(cont))

# gen = to_count(10)

# print(type(gen))
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))


# phrase = "I have an amazing abbility playing Dota2"
# list_number = [1, 2, 3, 4, 5, 6, 7, 8]
# empty_list = []

# def transform_to_iter(data):
#     it = iter(data)
#     while True:
#         try:
#             print(next(it), end=" ")
#         except StopIteration:
#             break

# print(transform_to_iter(phrase))


# iter_name = iter(name)

# print(iter_name)

# print(next(iter_name))
# print(next(iter_name))
# print(next(iter_name))
# print(next(iter_name))
# print(next(iter_name))
# print(next(iter_name))
# print(next(iter_name))
# print(next(iter_name))
# print(next(iter_name))
# print(next(iter_name))


# str_ = "It's an example of a big phrase to us apply some native methods from python."

# [print(letter, end=" ") for letter in str_]


# num_list = [1, 2, -3, -4, 5, 0.5]
# name_tuple = ('João', 'Marcos', 'Judas')
# str_ = "Should I stay or should I go?"

# print(list(reversed(str_)))

# print(sorted(name_tuple))

# print(list(reversed(num_list)))

# print(tuple(reversed(name_tuple)))


# print(sum([1, 2]))

# print(len('Samuel'))

# print(abs(-10))

# print(round(3.5, 2))