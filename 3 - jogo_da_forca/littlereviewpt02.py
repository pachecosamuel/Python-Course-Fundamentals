class Book:
    def __init__(self, title, author, year, pages):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__pages = pages

    def __repr__(self):
        return f"Repr Title = {self.__title}"
    
    def __str__(self):
        return f"Str Author = {self.__author}"
    
    def __len__(self):
        return self.__pages
    
    def __add__(self, other):
        return self.__pages + other.__pages
    
    def __del__(self):
        print(f"Book {self.__title} was deleted")

    
book1 = Book("Pai rico pai pobre", "R. Kyozaki", 1997, 300)
book2 = Book("Quem pensa enriquece", "Napoleon Hill", 1950, 250)
print(book1)
print(book1.__repr__())
print(book1.__str__())
print(len(book1))
print(book1 + book2)