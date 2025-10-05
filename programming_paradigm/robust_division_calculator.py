# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform division with robust error handling.
    
    Args:
        numerator: The numerator value (string or number).
        denominator: The denominator value (string or number).
    
    Returns:
        str: Result of division or an appropriate error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
