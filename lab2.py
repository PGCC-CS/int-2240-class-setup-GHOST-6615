# Lab 2
# Convert minutes into hours and minutes

# Ask user for input
minutes = int(input("Enter the number of minutes: "))

# Calculate hours and remaining minutes
hours = minutes // 60
remaining_minutes = minutes % 60

# Display result
print("That equals", hours, "hour(s) and", remaining_minutes, "minute(s).")