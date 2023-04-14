# Writing to a CSV File
import csv

with open('tides.csv', mode='w', newline='') as tides:
    writer = csv.writer(tides)
    writer.writerow(['12:02am', 1.20, 'Low'])
    writer.writerow(['06:23am', 9.60, 'High'])
    writer.writerow(['12:52pm', 0.09, 'Low'])
    writer.writerow(['07:13pm', 8.42, 'High'])

# Reading from a CSV File
with open('tides.csv', mode='r', newline='') as tides:
    print(f'{"Time":<10}{"Height":<10}{"Type":<6}')
    reader = csv.reader(tides)
    for record in reader:
        time, height, kind = record
        print(f'{time:<10}{height:<10}{kind:<6}')