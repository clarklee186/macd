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
		px = pd.DataFrame(get_px(n, start, end) )
	except Exception:
		print "error 1: get data fail"
		continue
	px.to_csv(n + "_raw.csv")
