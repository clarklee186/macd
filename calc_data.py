#!/usr/bin/env python
#import pandas.io.data as web
import pandas as pd
import pandas_datareader.data as web
import datetime as dt


def get_px(stock, start, end): 
     return web.get_data_yahoo(stock, start, end)

start = dt.datetime(2016,1,2)

end= dt.date.today()
#- dt.timedelta(1)

infile = open("list.csv", "r")

names = infile.read().split("\n")
#print names
while '' in names:
    names.remove('')
print names

for n in names:
	try:
		px = pd.read_csv(n +"_raw.csv" )
	except Exception:
		print "error 1: get data fail"
		continue
	px['26 ema'] = pd.ewma(px["Adj Close"], span=26)
	px['12 ema'] = pd.ewma(px["Adj Close"], span=12)
	px['MACD'] = (px['12 ema'] - px['26 ema'])
	px.to_csv(n + ".csv")
