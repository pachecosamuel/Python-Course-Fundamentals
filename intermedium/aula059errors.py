def fruit(number):
    my_list = ['pineapple', 'pear', 'apple', 'strawberry'];
    if number > 3:
        raise IndexError("The value exceeds the elements list's number ");
    else:
        return my_list[number];

print(fruit(2))
print(fruit(5))