class Book:
    def __init__(self, title, author, publishing_company, year, pages):
        self.__title = title
        self.__author = author
        self.__publishing_company = publishing_company
        self.__year = year
        self.__pages = pages

    def __repr__(self):
        return f'Title = {self.__title}'
    
    def __str__(self):
        return f'Author = {self.__author}'
    
    def __len__(self):
        return self.__pages
    
    def __add__(self, other):
        return self.__pages + other.__pages
    
    def __del__(self):
        print(f'Book {self.__title} was deleted')

book1 = Book('Pai rico Pai pobre', 'Kyozaki', 'USA', 2001, 300)

book2 = Book('Quem pensa enriquece', 'Napoleon Hill', 'USA', 1940, 250)

print(book2.__repr__())
print(book1)
print(len(book1))
print(len(book2))
print(book1 + book2)