"""Meal tip and tax calculator

Massachusetts charges a sales tax on meals sold by restaurants or any part of
a store considered by Massachusetts law to be a restaurant.
The meals tax rate is 6.25%.
"""
from decimal import Decimal

def tip_amount(meal, percent):
    """Calculate tip amount of meal.
    Pecent is a string for Decimal input value."""
    return round(meal * Decimal(percent), 2)

def meal_with_tip(meal, percent):
    """Calculate meal price with tip"""
    return round(meal * Decimal('1' + percent), 2)

def meal_with_tax(meal, tax_rate):
    """Calculate meal price with tax"""
    return round(meal * Decimal('1' + tax_rate), 2)


meal = Decimal(input('Enter the meal amount: '))

print('Suggested Tip:',
    f"18%: (Tip ${tip_amount(meal, '.18')}  Total ${meal_with_tip(meal, '.18')})",
    f"20%: (Tip ${tip_amount(meal, '.20')}  Total ${meal_with_tip(meal, '.20')})",
    f"25%: (Tip ${tip_amount(meal, '.25')}  Total ${meal_with_tip(meal, '.25')})",
    sep='\n')

tip = Decimal(input('Enter the tip percent (.2 for 20%): '))

meal_tip = tip_amount(meal, tip)
meal_with_tax = meal_with_tax(meal, '.0625') # 6.25% MA meal tax rate

print(f'Tip amount: ${meal_tip}',
    f'Meal + tax: ${meal_with_tax}',
    f'Total with tip: ${(meal_with_tax + meal_tip)}',
    sep='\n')