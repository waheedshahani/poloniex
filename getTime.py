import time
#Return current unix time
def currenttime():
	return int(time.time())
#returns start and end unix time for peiod given.
def startendtime(minutes):
	end=currenttime()
	start=end-minutes*60
	return start,end
