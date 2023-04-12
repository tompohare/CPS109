"""Meal tip and tax calculator

Massachusetts charges a sales tax on meals sold by restaurants or any part of
a store considered by Massachusetts law to be a restaurant.
The meals tax rate is 6.25%.
"""

from decimal import Decimal

meal = Decimal(input('Enter the meal amount: '))

print('Suggested Tip:',
    f"18%: (Tip ${meal * Decimal('.18')}  Total ${meal * Decimal('1.18')})",
    f"20%: (Tip ${meal * Decimal('.20')}  Total ${meal * Decimal('1.2')})",
    f"25%: (Tip ${meal * Decimal('.25')}  Total ${meal * Decimal('1.25')})",
    sep='\n')

tip = Decimal(input('Enter the tip percent (.2 for 20%): '))

meal_with_tax = meal * Decimal('1.0625')
meal_tip = meal * tip

print(f'Tip amount: ${meal_tip:.2f}',
    f'Meal + tax: ${meal_with_tax:.2f}',
    f'Total with tip: ${(meal_with_tax + meal_tip):.2f}',
    sep='\n')