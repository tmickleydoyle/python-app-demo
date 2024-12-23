def main():
    from greetings import say_hello
    from operations import add_numbers

    print("Welcome to the Simple App")
    print("1. Say Hello")
    print("2. Add Numbers")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        say_hello()
    elif choice == '2':
        add_numbers()
    elif choice == '3':
        print("Goodbye!")
    else:
        print("Invalid option. Try again.")
        main()

if __name__ == "__main__":
    main()