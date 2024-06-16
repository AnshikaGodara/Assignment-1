def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# User input for the conversion
temp = float(input("Enter the temperature: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if unit == 'C':
    print(f"{temp} degrees Celsius is {celsius_to_fahrenheit(temp)} degrees Fahrenheit.")
elif unit == 'F':
    print(f"{temp} degrees Fahrenheit is {fahrenheit_to_celsius(temp)} degrees Celsius.")
else:
    print("Please enter a valid temperature unit (C or F).")