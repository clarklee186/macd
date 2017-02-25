#!/usr/bin/env python
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
from sys import argv

infile = open("list.txt", "r")

start = dt.datetime(2016,1,2)

end= dt.date.today()

all_stock_IDs = infile.read().split("\n")

for each_ID in all_stock_IDs:
	try:
		each_stock = web.DataReader(each_ID,'yahoo',start,end)
		print each_ID 
		print each_stock.ix['2017-02-21']
		print each_stock
		print each_stock['Adj Close']
		print each_stock['2016-02-17']
		outfilename = each_ID + "_history_price"
		outfile = open(outfilename, "w")
		outfile.write(str(each_stock))
		outfile.close()
	except Exception:
		print each_ID + "fail!!!"
infile.close()


