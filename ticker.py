from polowrapper import poloniex
import time
import getTime as t
p=poloniex()
#ticker=p.api_query('returnTicker','BTC_ETH')
#for key,value in ticker.iteritems():
#	print key
[start,end]=t.startendtime(5)
candlestickinterval=300
#Dummy pair list. we'll grab all pairs from exchange once in production
pairlist={'BTC_XMR','BTC_SJCX','BTC_VIA'}
parameters={'starttime':str(start),'endtime':str(end),'candle':str(candlestickinterval),'pairlist':pairlist}
p.returnChartData(parameters)
