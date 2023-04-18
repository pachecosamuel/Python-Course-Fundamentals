from passlib.hash import pbkdf2_sha256 as my_cryp


class User:
    def __init__(self, name, last_name, email, password):
        self.__name = name
        self.__last_name = last_name
        self.__email = email
        self.__password = my_cryp.hash(password, rounds=1000, salt_size=10)

    def __str__(self):
        return f"{self.__name} {self.__last_name}, {self.__email}, {self.__password}"


    def verify_password(self, password):
        if my_cryp.verify(password, self.__password):
            return True
        return False


user1 = User('Samuel', 'Pacheco', 'samu@g.com', "123456sa@")
print(user1)
print(user1.verify_password("123456sa@"))
