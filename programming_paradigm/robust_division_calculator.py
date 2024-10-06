def safe_divide(numerator, denominator):
    try:
        division_result = float(numerator) / float(denominator)
        result = f"The result of the division is {division_result}"
        return result
    except ZeroDivisionError as e:
        result = "Error: Cannot divide by zero."
        return result
    except ValueError as e:
        result = "Error: Please enter numeric values only."
        return result
