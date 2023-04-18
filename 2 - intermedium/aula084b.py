import datetime as dt

today = dt.datetime.now()
tomorrow = today + dt.timedelta(days=1)
midnight = dt.time()
task = dt.datetime.combine(tomorrow, midnight)

print(f"Today = {today}")
print(f"Task to be done = {task}")
print(type(task))
print(repr(task))