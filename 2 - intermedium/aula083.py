import datetime as dt

today = dt.datetime.now()
my_birthday = dt.datetime(2023, 10, 14, 0)

time_to_wait = my_birthday - today

print(type(time_to_wait))
print(repr(time_to_wait))
print(time_to_wait)