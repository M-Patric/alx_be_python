# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
    - num1 (float): The first operand.
    - num2 (float): The second operand.
    - operation (str): One of 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
    - float: The result of the arithmetic operation.
    - str: An error message if division by zero is attempted or operation is invalid.
    """
    operation = operation.lower().strip()

    if operation == 'add':
        return num1 + num2

    elif operation == 'subtract':
        return num1 - num2

    elif operation == 'multiply':
        return num1 * num2

    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

    else:
        return "Error: Invalid operation"
