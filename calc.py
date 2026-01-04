"""A script that takes two numbers and an operator as input and prints the result."""

from __future__ import annotations

from typing import Dict, Callable

# I/O functions
def prompt(prompt_text: str) -> str:
    """Requests input based on prompt_text."""
    return input(prompt_text).strip()

def info(message: str) -> None:
    """Prints message."""
    print(message)

def warning(message: str) -> None:
    """Prints warning message."""
    print(f"Warning: {message}")

def error(message: str) -> None:
    """Prints error message."""
    print(f"Error: {message}")

# Operator functions
def add(num1: float, num2: float) -> float:
    """Adds input numbers and returns the result."""
    return num1 + num2

def subtract(num1: float, num2: float) -> float:
    """Subtracts the second input number from the first and returns the result."""
    return num1 - num2

def multiply(num1: float, num2: float) -> float:
    """Multiplies input numbers and returns the result."""
    return num1 * num2

def divide(num1: float, num2: float) -> float | None:
    """Divides first input number by the second and returns the result or returns None if second number is 0."""
    if num2 != 0:
        return num1 / num2
    return None

OperatorHandler = Callable[[float, float], float | None]

OPERATORS: Dict[str, OperatorHandler] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def main() -> None:
    info("Welcome to calc.py! Enter 'q' at any time to exit the program.")

    while True:
        print()

        num1: str = prompt("Enter first number: ")
        if num1.lower() == "q":
            info("Exiting program")
            break
        try:
            x: float = float(num1)
        except ValueError:
            error("Not a number")
            continue

        num2: str = prompt("Enter second number: ")
        if num2.lower() == "q":
            info("Exiting program")
            break
        try:
            y: float = float(num2)
        except ValueError:
            error("Not a number")
            continue

        operator_input: str = prompt("Enter operation (+, -, *, /): ")

        if operator_input == "q":
            info("Exiting program")
            break

        handler = OPERATORS.get(operator_input)
        if handler:
            result: float = handler(x, y)
            if result is not None:
                info(f"Result: {result}")
            else:
                error("Divide by zero")
        else:
            error(f"Unknown operator {operator_input}")

if __name__ == "__main__":
    main()
