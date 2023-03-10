"""Convert Fahrenheit temperature to Celsius"""

fahrenheit = int(input('Fahrenheit temperature: '))

celsius = (fahrenheit - 32) * 5 / 9

print(f'The Celsius temperature for {fahrenheit} is {celsius}')