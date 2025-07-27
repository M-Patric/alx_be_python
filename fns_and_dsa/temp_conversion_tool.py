# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global conversion factor"""
    celsius = (fahrenheit - FREEZING_POINT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global conversion factor"""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_OFFSET
    return fahrenheit

def test_conversions():
    """Test cases for conversion functions"""
    print("\nRunning conversion tests...")
    # Test known values
    assert round(convert_to_celsius(32), 2) == 0.00      # Freezing point
    assert round(convert_to_celsius(212), 2) == 100.00    # Boiling point
    assert convert_to_fahrenheit(0) == 32                 # Freezing point
    assert convert_to_fahrenheit(100) == 212              # Boiling point
    print("All conversion tests passed!")

def get_user_input():
    """Handle user input with validation"""
    while True:
        try:
            temp_input = input("Enter the temperature to convert: ")
            temperature = float(temp_input)
            
            while True:
                unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
                if unit in ('C', 'F'):
                    return temperature, unit
                print("Error: Please enter either 'C' for Celsius or 'F' for Fahrenheit.")
        
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

def main():
    print("Temperature Conversion Tool")
    print("--------------------------")
    
    # Run test cases first
    test_conversions()
    
    # Get user input
    temperature, unit = get_user_input()
    
    # Perform conversion
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"\n{temperature}°F is {converted_temp:.2f}°C")
    else:
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"\n{temperature}°C is {converted_temp:.2f}°F")

if __name__ == "__main__":
    main()