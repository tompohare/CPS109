"""BMI - Calculate Body Mass Index

Body Mass Index (BMI) is calculated from a person's weight and height.
BMI is a fairly reliable indicator of body fatness for most people.
The formula for BMI is:

    kilograms / meters ** 2

where weight is in kilograms and height is in meters.
If pounds and inches are used, a conversion factor of 703 is applied.

    (pounds / inches ** 2) * 703

See also: https://en.wikipedia.org/wiki/Body_mass_index
"""

pounds = float(input('What is your weight (pounds)? '))
inches = float(input('What is your height (inches)? '))

# Calculate bmi from pounds and inches
bmi = round((pounds / inches ** 2) * 703, 1)

bmi_categories_msg = '''
BMI Categories:
Underweight <= 18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater
'''

if bmi < 18.5:
    bmi_category = 'Underweight'
elif 18.5 <= bmi < 25:
    bmi_category = 'Normal weight'
elif 25 <= bmi < 30:
    bmi_category = 'Overweight'
else:
    bmi_category = 'Obesity'

print(bmi_categories_msg)
print('Your BMI is', bmi, 'which is categorized as', bmi_category)
