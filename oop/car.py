class Car:
    def __init__(self, make, model, year, kilometers):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__kilometers = kilometers

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year
    
    def get_kilometers(self):
        return self.__kilometers
    
    def set_kilometers(self, new_kilometers):
        self.__kilometers = new_kilometers
    
    def __str__(self):
        return f"{self.get_make()} {self.get_model()} {self.get_year()}"