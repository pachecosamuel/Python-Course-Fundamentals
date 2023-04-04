words = [];
my_list = [];

while True:
    word = input("type a word: ");
    if word == '':
        break;
    else:
        words.append(word);

for word in words:
    my_list.append(list(set(word)))

for item in my_list:
    print(item)
