"""Compound interest rate calculator"""

from decimal import Decimal

principal = Decimal(input('Enter the principal amount: ') or 1000)
rate = Decimal(input('Enter the savings rate (.05 for 5%): ') or 0.05)
years = int(input('Enter the number of years to save: ') or 5)
annual = Decimal(input('Enter annual addition to save: ') or 0)

for year in range(1, years + 1):
    amount = principal * (1 + rate) ** year
    if year > 1:
        amount += annual * (1 + rate) * ((1 + rate) ** year - 1) / rate
    print(f'{year:>2}{amount:>10.2f}')
