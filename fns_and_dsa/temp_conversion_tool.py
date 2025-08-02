# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global factor:
      C = (F - 32) * (5/9)
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global factor:
      F = C * (9/5) + 32
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    # Validate numeric input
    temp_str = input("Enter the temperature to convert: ").strip()
    try:
        temp_val = float(temp_str)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == "F":
        c = convert_to_celsius(temp_val)
        print(f"{temp_val}°F is {c}°C")
    elif unit == "C":
        f = convert_to_fahrenheit(temp_val)
        print(f"{temp_val}°C is {f}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
