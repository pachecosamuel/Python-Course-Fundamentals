text = "Hello, world!"

print(id(text))

text_upper = text

print(id(text_upper))

new_text_upper = text.upper()

print(id(new_text_upper))