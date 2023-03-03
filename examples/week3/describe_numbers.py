"""Describe the characteristics of three numbers"""

number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))

numbers = [number1, number2, number3]

print()
print('The minimum is:', min(numbers))
print('The maximum is:', max(numbers))

print('The total is:', sum(numbers))
print('The average is:', sum(numbers) / len(numbers))