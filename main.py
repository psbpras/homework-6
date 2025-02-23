import sys
from calculator import Calculator

def main():
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        operation = sys.argv[3]

        operations = {
            "add": Calculator.add,
            "subtract": Calculator.subtract,
            "multiply": Calculator.multiply,
            "divide": Calculator.divide
        }

        if operation in operations:
            result = operations[operation](a, b)
            print(f"The result of {a} {operation} {b} is equal to {result}")
        else:
            print(f"Unknown operation: {operation}")
    except IndexError:
        print("Error: Please provide two numbers and an operation.")
    except ValueError as e:
        print(f"Invalid number input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
