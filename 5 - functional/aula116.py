list_ = [0, 1, 2, 3]
names_ = ["Samuel", "Sandra", "Silvia", "Saxão"]

filtered_list = filter(lambda name: name[0][0] == "S", names_)
comprehension_list = [not(name[0] == "S") for name in names_]

print(all(filtered_list))
print(all(comprehension_list))
print(all(list_))
print(any(list_))
