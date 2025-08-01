# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global conversion factors"""
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FREEZING_POINT_OFFSET  # Explicitly declare we're using globals
    celsius = (fahrenheit - FREEZING_POINT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global conversion factors"""
    global CELSIUS_TO_FAHRENHEIT_FACTOR, FREEZING_POINT_OFFSET  # Explicitly declare we're using globals
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_OFFSET
    return fahrenheit

def test_conversions():
    """Test conversion functions with known values"""
    print("\nTesting conversions...")
    # Test freezing and boiling points
    assert abs(convert_to_celsius(32) - 0) < 0.001
    assert abs(convert_to_celsius(212) - 100) < 0.001
    assert abs(convert_to_fahrenheit(0) - 32) < 0.001
    assert abs(convert_to_fahrenheit(100) - 212) < 0.001
    print("All conversion tests passed!")

def get_temperature_input():
    """Get and validate user input"""
    while True:
        try:
            temp = float(input("Enter temperature to convert: "))
            scale = input("Is this in Celsius or Fahrenheit? (C/F): ").upper()
            if scale in ('C', 'F'):
                return temp, scale
            print("Error: Please enter either 'C' or 'F'")
        except ValueError:
            print("Error: Invalid temperature. Please enter a numeric value.")

def main():
    print("\nTemperature Conversion Tool")
    print("--------------------------")
    
    # Verify conversions work
    test_conversions()
    
    # Get user input
    temp, scale = get_temperature_input()
    
    # Perform and display conversion
    if scale == 'F':
        converted = convert_to_celsius(temp)
        print(f"\n{temp}°F = {converted:.2f}°C")
    else:
        converted = convert_to_fahrenheit(temp)
        print(f"\n{temp}°C = {converted:.2f}°F")

if __name__ == "__main__":
    main()