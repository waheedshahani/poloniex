from polowrapper import poloniex
import time
p=poloniex()
while (1==1):
	ticker=p.api_query('returnTicker','BTC_ETH')
	print "Ask:",ticker['BTC_STR']['lowestAsk'],"Bid:",ticker['BTC_STR']['highestBid'],"last:",ticker['BTC_STR']['last']
	time.sleep(5)
