# Program to print the multiplication table for a given number

# Get input from the user
number = int(input("Enter a number: "))

# Print the multiplication table
print(f"\nMultiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
