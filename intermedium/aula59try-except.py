try:
    pypro();
except NameError as name_error:
    print(f"Something went wrong: {name_error}");
finally:
    print(f"The life is going on")
