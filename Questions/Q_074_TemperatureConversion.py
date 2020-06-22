"""""""""
Write a Python function to convert temperatures from Fahrenheit to Celsius. 
More specifically, your function should be able to read an a list of unspecified length and 
print out the Celsius temperature for each item.

The formula to convert from Fahrenheit to Celsius is:
(Fahrenheit temperature - 32)*5 /9
"""

temp_convert_fn = lambda temp: (temp - 32) * 5 / 9

fahrenheit = [10, 20, 30, 40, 50, 60, 70, 80]

celcius = [temp_convert_fn(f) for f in fahrenheit]

print(celcius)
