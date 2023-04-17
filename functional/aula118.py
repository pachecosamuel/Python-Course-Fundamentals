names = ['John', 'Maria', 'Ralf', 'Maximiliano', 'Joze']

print(min(names, key=lambda name: len(name)))
print(max(names, key=lambda name: len(name)))