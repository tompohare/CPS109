'''
Bill James' Safe Lead Calculator
http://www.slate.com/id/2185975/

How to tell when a college basketball game is out of reach

1. Take the number of points one team is ahead.
2. Subtract three.
3. Add a half-point if the team that is ahead has the ball, and
   subtract a half-point if the other team has the ball.
   (Numbers less than zero become zero).
4. Square that.
5. If the result is greater than the number of seconds left in the game,
   the lead is safe.

December 27 2022
NY Nicks 9 point lead over Dallas Mavericks
26 seconds left
Mavs had the ball
https://www.nba.com/game/nyk-vs-dal-0022200512
'''

points_ahead = int(input('Enter the lead in points: '))
has_ball = input('Does the lead team have the ball (Yes or No): ')
seconds_remaining = int(input('Enter the number of seconds remaining: '))

lead_calculation = float(points_ahead - 3)

if has_ball == 'Yes':
    lead_calculation = lead_calculation + 0.5
else:
    lead_calculation = lead_calculation - 0.5

if lead_calculation < 0:
    lead_calculation = 0

safety_point_margin = lead_calculation

# Square that
lead_calculation = lead_calculation ** 2

if lead_calculation > seconds_remaining:
    print('Lead is safe.')
else:
    print('Lead is NOT safe.')

percent_safe = str(round(lead_calculation / seconds_remaining * 100)) + '%'
print(percent_safe, "percent safe,", safety_point_margin, "safety point margin")