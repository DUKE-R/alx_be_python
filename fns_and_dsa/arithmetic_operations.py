def perform_operation(num1: float, num2: float, operation: str) -> float or str:
    """
    Perform basic arithmetic operations: addition, subtraction, multiplication, or division.

    Parameters:
    - num1 (float): The first number.
    - num2 (float): The second number.
    - operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    - float: The result of the operation.
    - str: An error message for division by zero.
    """
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."

