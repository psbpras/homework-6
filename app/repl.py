from app.calculator import Calculator
from app.plugin_loader import load_plugins

def repl():
    """Interactive command-line interface."""
    calculator = Calculator()
    plugins = load_plugins()

    print("Welcome to the interactive calculator! Type 'menu' to see commands or 'exit' to quit.")

    while True:
        user_input = input("Enter command: ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break

        if user_input == "menu":
            print("Available commands:", ", ".join(plugins.keys()))
            continue

        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input. Format: <command> <num1> <num2>")
            continue

        command_name, num1, num2 = parts[0], parts[1], parts[2]

        if command_name not in plugins:
            print("Unknown command. Type 'menu' for available commands.")
            continue

        try:
            num1, num2 = float(num1), float(num2)
            command = plugins[command_name](num1, num2)
            result = calculator.execute(command)
            print("Result:", result)
        except ValueError:
            print("Invalid number input. Please enter valid numbers.")
