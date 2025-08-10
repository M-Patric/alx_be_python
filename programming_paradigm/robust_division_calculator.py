def safe_divide(numerator, denominator):
    """
    Performs a safe division of numerator by denominator.

    Handles:
    - ZeroDivisionError (division by zero)
    - ValueError (non-numeric inputs)
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