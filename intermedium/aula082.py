import datetime as dt

my_birthday = input("Type your birth date dd/mm/aaaa : ")
birth_date_list = my_birthday.split("/")

birthday_converted = dt.date(
    int(birth_date_list[2]),
    int(birth_date_list[1]),
    int(birth_date_list[0]),
)

print(birthday_converted)
print(type(birthday_converted))