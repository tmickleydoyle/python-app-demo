# Simple Python App

This is a simple Python application designed to showcase basic functionality such as user greetings and basic arithmetic operations. The app is divided into multiple files for modularity and maintainability.

## Features
- Greet the user with their name.
- Add two numbers provided by the user.
- Handle invalid inputs gracefully.

## File Structure
- `main.py`: The entry point of the application. Provides a menu for users to interact with the app.
- `greetings.py`: Contains the functionality to greet the user.
- `operations.py`: Includes arithmetic operations such as addition.
- `utils.py`: Provides utility functions (e.g., welcome messages).
- `errors.py`: Handles error messages and exceptions.

## How to Run
1. Ensure you have Python installed (version 3.6 or later).
2. Clone or download the repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Run the application using:
   ```bash
   python main.py
   ```

## Example Usage
### Greet the User
```
Welcome to the Simple App
1. Say Hello
2. Add Numbers
3. Exit
Choose an option: 1
Enter your name: John
Hello, John!
```

### Add Numbers
```
Welcome to the Simple App
1. Say Hello
2. Add Numbers
3. Exit
Choose an option: 2
Enter the first number: 5
Enter the second number: 10
The sum is: 15
```

### Handle Errors
```
Welcome to the Simple App
1. Say Hello
2. Add Numbers
3. Exit
Choose an option: 2
Enter the first number: five
Please enter valid numbers.
```