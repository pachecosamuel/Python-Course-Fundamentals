class Person:
    def __init__(self, name, last_name, cpf):
        self.__name = name
        self.__last_name = last_name
        self.__cpf = cpf

    def get_name(self):
        return self.__name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_cpf(self):
        return self.__cpf
    
    def __str__(self):
        return f'{self.__name} {self.__last_name} {self.__cpf}'
    
class Client(Person):
    def __init__(self, name, last_name, cpf, income):
        super().__init__(name, last_name, cpf)
        self.__income = income

    def get_income(self):
        return self.__income

class Employee(Person):
    def __init__(self, name, last_name, cpf, enrollment):
        super().__init__(name, last_name, cpf)
        self.__enrollment = enrollment

    def get_enrollment(self):
        return self.__enrollment
    

client1 = Client('Bia', 'Shazan', 123456, 100000)
employee1 = Employee('Samuel', 'Pacheco', 654321, 220)

print(client1)
print(client1.get_income())
print("-------------------")

print(employee1)
print(employee1.get_enrollment())
    