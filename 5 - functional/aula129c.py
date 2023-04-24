def verify_first_paremeter(value):
    def intern(func):
        def original(*args, **kwargs):
            if args and args[0] != value:
                return f"Incorret value, the first argument needs to be {value}"
            return func(*args, **kwargs)
        return original
    return intern

@verify_first_paremeter("samu@g.com.br")
def verify_login(user, password):
    return f"User -> {user} and password -> {password}"

print(verify_login("samu@g.com", "123"))