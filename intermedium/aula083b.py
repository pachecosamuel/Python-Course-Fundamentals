import datetime as dt

today = dt.datetime.now()
rule = dt.timedelta(days=3, hours=2)

# Calculating the billet's date
billet = today + rule

print(today)
print(rule)
print(billet)
