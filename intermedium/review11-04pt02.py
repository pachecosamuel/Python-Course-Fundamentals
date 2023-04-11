import datetime as dt

user_input_birth = input("Type your birthdate dd/mm/aaaa: ")
transform_to_date = user_input_birth.split("/")

final_date = dt.date(
    int(transform_to_date[2]),
    int(transform_to_date[1]),
    int(transform_to_date[0]),
)

print(user_input_birth)
print("--------------------")
print(final_date)


