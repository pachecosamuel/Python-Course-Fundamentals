import datetime as dt

today = dt.datetime.now()
birthday = dt.datetime(2023, 10, 14)

time_to_wait = birthday - today

print(repr(time_to_wait))
print(type(time_to_wait))
print(time_to_wait)