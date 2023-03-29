navigators = "Vikings";
word_to_tuple = tuple(navigators);
print(word_to_tuple);

tuple_one = (1, 'a', "Samu", 20.53);
tuple_to_list = list(tuple_one)
print(tuple_to_list)

tupla_aninhada = (navigators, tuple_one)
print(tupla_aninhada)
print(tupla_aninhada[1][2])