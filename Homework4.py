# Temperature Conversion Table
# Celsius to Fahrenheit

print("Celsius\tFahrenheit")

for c in range(10, 51, 5):
    f = ((9/5) * c) + 32
    print(c, "\t", f)