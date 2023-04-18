class Person:
    def __init__(self, name, age, cpf):
        self.__name = name
        self.__age = age
        self.__cpf = cpf

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}, CPF: {self.__cpf}"
    
    def identification(self):
        return self.__cpf


class Customer(Person):
    def __init__(self, name, age, cpf, customer_code):
        super().__init__(name, age, cpf)
        self.__customer_code = customer_code

    def identification(self):
        return super().identification() 
    

class Employee(Person):
    def __init__(self, name, age, cpf, employee_code):
        super().__init__(name, age, cpf)
        self.__employee_code = employee_code

    def identification(self):
        return self.__employee_code
    

Customer1 = Customer("Client", 25, 2468, 10)

print(Customer1)
print(Customer1.identification())

print("----------------------")

Employee1 = Employee("Employee", 50, 1357, 20)

print(Employee1)
print(Employee1.identification())
