# Get temperature in Fahrenheit from the user
fahrenheit = float(input("Enter the temperature in Fahrenheit (°F): "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5/9

# Convert Celsius to Kelvin
kelvin = celsius + 273.15

# Print the results
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C and {kelvin:.2f}K")
