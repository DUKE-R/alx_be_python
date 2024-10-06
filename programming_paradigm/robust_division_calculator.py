# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform division and handle errors like division by zero and non-numeric input."""
    try:
        num = float(numerator)
        denom = float(denominator)

        if denom == 0:
            return "Error: Cannot divide by zero."
        else:
            result = num / denom
            return f"The result of the division is {result:.2f}"

    except ValueError:
        return "Error: Please enter numeric values only."
