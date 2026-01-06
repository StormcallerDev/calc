"""A script that takes two numbers and an operator as input and prints the result of the operation."""

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
    """Adds both numbers and returns the result."""
    return num1 + num2

def subtract(num1: float, num2: float) -> float:
    """Subtracts the second number from the first and returns the result."""
    return num1 - num2

def multiply(num1: float, num2: float) -> float:
    """Multiplies both numbers and returns the result."""
    return num1 * num2

def divide(num1: float, num2: float) -> float | None:
    """Divides the first number by the second and returns the result or returns None if second number is 0."""
    if num2 == 0:
        return None
    return num1 / num2

def power(num1: float, num2: float) -> float:
    """Returns the result of the first number to the power of the second number."""
    return num1 ** num2

def modulo(num1: float, num2: float) -> float | None:
    """Divides the first number by the second and returns the remainder or returns None if second number is 0."""
    if num2 == 0:
        return None
    return num1 % num2

OperatorHandler = Callable[[float, float], float | None]

OPERATORS: Dict[str, OperatorHandler] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "%": modulo,
}

VALID_OPERATORS: str = ", ".join(OPERATORS.keys())

def get_number(prompt_text: str) -> float | None:
    """Requests a number as input and returns that number if it is a valid number."""
    while True:
        value: str = prompt(prompt_text)
        if value.lower() in {"q", "quit", "exit"}:
            return None
        if value == "":
            warning("Empty input, please try again.")
            continue
        try:
            return float(value)
        except ValueError:
            error("Invalid number, please try again.")

def get_operator() -> str | None:
    while True:
        op = prompt(f"Enter operation ({VALID_OPERATORS}): ")
        if op.lower() in {"q", "quit", "exit"}:
            return None
        if op in OPERATORS:
            return op
        error(f"Unknown operator '{op}'")

def main() -> None:
    info("Welcome to calc.py! Enter 'q', 'quit', or 'exit' at any time to quit the program.")

    while True:
        info("")
        x: float | None = get_number("Enter first number: ")
        if x is None:
            info("Exiting program")
            break

        y: float | None = get_number("Enter second number: ")
        if y is None:
            info("Exiting program")
            break

        op: str | None = get_operator()
        if op is None:
            info("Exiting program")
            break

        result: float | None = OPERATORS[op](x, y)
        if result is None:
            error("Divide by zero")
        else:
            info(f"Result: {result}")

if __name__ == "__main__":
    main()
