# temp_conversion_tool.py

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temp_input = input("Enter the temperature to convert: ")
    temp = float(temp_input)
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if unit.upper() == "F":
    result = convert_to_celsius(temp)
    print(f"{temp}°F is {result}°C")
elif unit.upper() == "C":
    result = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {result}°F")
else:
    raise ValueError("Invalid unit. Please enter C or F.")
