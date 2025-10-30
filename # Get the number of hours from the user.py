# Get the number of hours from the user
hours = float(input("Enter the number of hours: "))

# Convert hours to minutes and seconds
minutes = hours * 60
seconds = hours * 3600

# Print the results
print(f"{hours} hours is equal to {minutes:.2f} minutes or {seconds:.2f} seconds.")
