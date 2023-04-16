"""
Daily tides - downloads and emails the daily tide schedule

See also:
1. https://tidesandcurrents.noaa.gov/noaatidepredictions.html?id=8442645
"""

import urllib.request
from datetime import date, timedelta
import send_me_gmail as gmail

today = date.today()
bdate = today.strftime('%Y%m%d')
edate = (today + timedelta(days=6)).strftime('%Y%m%d')
url_tides_txt = ('https://tidesandcurrents.noaa.gov/cgi-bin/predictiondownload.cgi?'
                 '&stnid=8442645&threshold=&thresholdDirection='
                 f'&bdate={bdate}&edate={edate}'
                 '&units=standard&timezone=LST/LDT&datum=MLLW&interval=hilo'
                 '&clock=12hour&type=txt&annual=false')

with urllib.request.urlopen(url_tides_txt) as response:
   content = response.read().decode('utf-8')
   print(content)

today = today.strftime('%b %d %Y')
gmail.send(f'Daily Tide Schedule {today}', content)