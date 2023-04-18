import datetime as dt
from textblob import TextBlob

def retorna_data(today):
    mes = TextBlog(today.strftime('%B')).translate(from_lang='es', to='pt-br')
    return f"{today.day} de {mes} de {today.year}"

today = dt.datetime.now()
print(today)
format_today = today.strftime("%d/%B/%Y, %H:%M:%S")
print(format_today)