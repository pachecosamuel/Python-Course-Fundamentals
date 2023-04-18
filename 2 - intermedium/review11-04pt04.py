import datetime as dt

today = dt.datetime.utcnow()
rule = dt.timedelta(days=3, hours=2, minutes=30)

billet = today + rule
print(today)
print(billet)