import sys
from calculator import Calculator

def format_number(n):
    """Format number as int if it has no decimals; otherwise, keep as float."""
    return int(n) if n.is_integer() else n

def main():
    """Command-line calculator with exception handling."""
    if len(sys.argv) != 4:
        print("Usage: python main.py <num1> <num2> <operation>")
        sys.exit(1)

    num1, num2, operation = sys.argv[1], sys.argv[2], sys.argv[3]

    # Validate numbers
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid number input")
        sys.exit(0)

    # Perform calculation
    try:
        operations = {
            "add": Calculator.add,
            "subtract": Calculator.subtract,
            "multiply": Calculator.multiply,
            "divide": Calculator.divide,
        }
        if operation not in operations:
            print("Unknown operation")
            sys.exit(0)

        if operation == "divide" and num2 == 0:
            print("An error occurred: Cannot divide by zero")
            sys.exit(0)

        result = operations[operation](num1, num2)                      # Convert numbers & result to int if possible
        num1 = format_number(num1)
        num2 = format_number(num2)
        result = format_number(result)

        print(f"The result of {num1} {operation} {num2} is equal to {result}")

    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")
        sys.exit(0)


if __name__ == "__main__":
    main()
