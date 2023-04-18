def divide_number(number, divisor):
    try:
        return number / divisor;
    except ZeroDivisionError as zero:
        print(f"You are trying to divide by zero: {zero}")
    except TypeError as type_error:
        print(f"You are trying to divide by something that isn't a number {type_error}")
    except:
        print("Something went wrong!")
    finally:
        print("Acabou!")

print(divide_number(10, 5))