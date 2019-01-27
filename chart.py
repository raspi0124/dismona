import requests,time
from datetime import datetime
import datetime as dt
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

def get_OHLC(before,after):
    url = 'https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc'
    query = {
        'periods':60,
        'before':before,
        'after':after,
    }
    res = requests.get(url,params=query).json()['result']['60']
    return res

unixTime = lambda y,m,d,h: int(time.mktime(datetime(y,m,d,h).timetuple()))

now = datetime.today()
y,m,d,h = now.year,now.month,now.day,now.hour
text = str(y) + '-' + str(m) + '-' + str(d) + ' ' + str(h) + ':00'

data = get_OHLC(unixTime(y,m,d,h),unixTime(y,m,d,h-1))

Time,Open,High,Low,Close = [],[],[],[],[]
for i in data:
    Time.append(i[0])
    Open.append(i[1])
    High.append(i[2])
    Low.append(i[3])
    Close.append(i[4])

pd.DataFrame({'time':Time, 'open':Open, 'high':High, 'low':Low, 'close':Close}).to_csv('price.csv')

Date = [datetime(y,m,d,h-1) + dt.timedelta(minutes=mi) for mi in range(60)]
ohlc = zip(mdates.date2num(Date),Open, High, Low, Close)
ax = plt.subplot()
ax.xaxis.set_major_locator(mdates.MinuteLocator([0,15,30,45]))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
candlestick_ohlc(ax, ohlc, width=(1/24/60)*0.7,colorup='g', colordown='r')
plt.title(text + '  BTC / JPY  by Cryptowatch API')

plt.savefig('price.png')
