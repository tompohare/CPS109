with open('tides.txt', mode='w') as tides:
    tides.write('12:02am 1.20 Low\n')
    tides.write('06:23am 9.60 High\n')
    tides.write('12:52pm 0.09 Low\n')
    tides.write('07:13pm 8.42 High\n')
    
with open('tides.txt', mode='r') as tides:
    print(f'{"Time":<10}{"Height":<10}{"Type":<6}')
    for record in tides:
        time, height, kind = record.split()
        print(f'{time:<10}{height:<10}{kind:<6}')