#!/usr/bin/env python                                  
#import pandas.io.data as web
import pandas as pd
import pandas_datareader.data as web
import datetime as dt


def get_px(stock, start, end): 
     return web.get_data_yahoo(stock, start, end)

current_low = 4
recent_up = 4
recent_low = 1

low_price_line = 2.5

start = dt.datetime(2016,1,2)

end= dt.date.today()
#- dt.timedelta(1)

infile = open("list.csv", "r")

names = infile.read().split("\n")
while '' in names:
    names.remove('')
print names

outfile = open("result.txt", "w")

dict1 = {}

for n in names:
	print "begin analyze: ", n
	try:
		px=pd.read_csv(n + ".csv")	
	except Exception:
		print "error 1: get data fail"
		continue
		
	if pd.to_numeric(px['Low'].iloc[-1]) < low_price_line:
		continue
		
#	print px
	if pd.to_numeric(px['MACD'].iloc[-1]) < 0:
#		print pd.to_numeric(px['MACD'].iloc[i] )  
		continue
#	print pd.to_numeric(px['MACD'].iloc[-1] ) 

	if pd.to_numeric(px['MACD'].iloc[-2]) > 0:
#		print pd.to_numeric(px['MACD'].iloc[i] )  
		continue
		
	i = -2 
	try:
		while pd.to_numeric(px['MACD'].iloc[i] )  <= 0.0 : 
			i = i - 1
	except Exception:
		print "error 2: out of bound fail"
		continue
	j = i
	a=px.iloc[j+1:-2]
#	print j
#	print a
	try:
		ai = a['Low'].idxmin()
	except Exception:
		print "error 3: get min fail"
		continue
#	print "former lowest price day:", ai
#	print px.iloc[0]

#	print ai,"  ", len(px.index)
#	if ai != len(px.index)-1:
#		continue
	
	if len(a.index) < current_low:
		continue
		
	while True: 
		if pd.to_numeric(px['MACD'].iloc[i] )  <= 0.0 :
			break
		i = i - 1
	k=i
#	print k
	if j - k < recent_up:
		continue
	
	while True: 
		try:
			if pd.to_numeric(px['MACD'].iloc[i] )  > 0.0:
				break
		except Exception:
			print "error 2: out of bound fail"
			break
		i = i - 1
		
	j = i+1
	c=px.iloc[j:k]
#	print j
#	print c
	try:
		ci = c['Low'].idxmin()
	except Exception:
		print "error 3: get min fail"
		continue
       		
	if len(c.index) < len(a.index):
		continue
		
#	print "former lowest price day:", ci
#	print c.ix[ci]

	if pd.to_numeric(c['Low'].ix[ci]) > pd.to_numeric(a['Low'].ix[ai]):
		if pd.to_numeric(c['MACD'].min()) < pd.to_numeric(a['MACD'].min()):
			if pd.to_numeric(c['MACD'].mean()) < pd.to_numeric(a['MACD'].mean()):
				print n, " is what we want."
				dict1.update({ n: ( pd.to_numeric(px['MACD'].iloc[-1]) )} )
				
#		else:
#			print n," is not what we want."
#	else:
#		print n," is not what we want."

#print dict1
dict2 = sorted(dict1.items(), key=lambda d: d[1], reverse=True)
outfile.write(str(dict2)) 
print(str(dict2))
outfile.close()
