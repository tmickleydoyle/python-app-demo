def add_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The sum is: {num1 + num2}")
    except ValueError:
        from errors import handle_error
        handle_error()