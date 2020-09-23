import sys
#https://github.com/RobertSmith3248/Temperature-Converter.git

F=float(input("Please enter a temperature in Fahrenheit here: "))

Kelvin1=((F-32)*(5/9))+273
Kelvin=round(Kelvin1, 2)

print ("The temperature is", Kelvin, "K")
