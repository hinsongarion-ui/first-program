# Get the length in feet from the user
feet = float(input("Enter the length in feet: "))

# Convert feet to other units
yards = feet / 3
miles = feet / 5280
inches = feet * 12
leagues = feet / 15840   # 1 league = 3 miles = 15840 feet
meters = feet * 0.3048   # 1 foot = 0.3048 meters

# Print the results
print(f"\n{feet} feet is equal to:")
print(f"{yards:.4f} yards")
print(f"{miles:.6f} miles")
print(f"{inches:.2f} inches")
print(f"{leagues:.6f} leagues")
print(f"{meters:.4f} meters")
