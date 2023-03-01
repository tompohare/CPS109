"""Calculate the area and circumference of a circle from its radius
Step 1: prompt for a radius
Step 2: apply the circumference formula
Step 3: apply the area formula
Step 4: print out the results
"""

import math

radius = int(input('Enter the radius of your circle: '))

circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print(f'The circumference is: {circumference}, and the area is: {area}')
