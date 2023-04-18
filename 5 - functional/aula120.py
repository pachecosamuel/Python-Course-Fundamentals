list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
phrase = "I'm a rich man"

print(tuple(reversed(list_)))

var = [print(letter, end="") for letter in reversed(phrase)]

print(var)

# for letter in reversed(phrase):
#     print(letter, end="")