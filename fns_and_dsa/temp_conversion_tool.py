# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    # Prompt user for temperature input
    temp_input = input("Enter the temperature to convert: ")
    try:
        temp_value = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
    
    # Prompt user for unit (Celsius or Fahrenheit)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == 'F':
        converted_temp = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {converted_temp}°C")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted_temp}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()