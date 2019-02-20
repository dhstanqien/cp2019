# Fahrenheit to celsius converter

# Get input
fahrenheit = int(input("Enter temperature in Fahrenheit"))

# Compute celsius temperature
celsius = (5/9) * (fahrenheit - 32)

# Output result
print("{0:.1f}".format(celsius))
