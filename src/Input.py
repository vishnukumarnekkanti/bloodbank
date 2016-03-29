"""generates input to the bloodbank"""
from Admin import *
import random
"""Daily cycle"""
#loop1
#start day 
#get number of requests, donations

#####2loops
#decide on request or donation
###########
#end day
def getRand(a,b):
	return random.randint(a,b)

weighted_choice = lambda s : random.choice(sum(([v]*wt for v,wt in s),[]))

#choices = [(0,99),(1,1)]

def prob(choices):
    return weighted_choice(choices) 
if __name__ == '__main__':
	f = open("input.txt", 'r')
	inputData = {}
	for line in f:
	    k, v = line.strip().split(',')
	    inputData[k.strip()] = v.strip()

	f.close()
	component = "rbc"
	blood_type = "A+"
	for day in xrange(1,3651):
		beginDay()
		choices_0 = [(0,99),(1,1)]
		requestNum = int((getRand(50,100))*inputData[day] + 3*((getRand(50,100))*inputData[day])*prob(choices_0))
		donationNum = int((getRand(10,50))*inputData[day])
		donationNum += sqlEngine.getReplacementNum()                 #####################db
		choices_1 = [(0,60),(1,40)]
		choices_2 = [(0,80),(1,20)]
		for transaction in xrange(requestNum+donationNum):
			if (prob(choices_1) == 1) and donationNum>0:
				donation(0, component_name, blood_type, (getCurrDate()))
				donationNum-=1
			else:
				units = int((getRand(1,20))*inputData[day] + 3*((getRand(10,20))*inputData[day])*prob(choices_0))
				if prob(choices_2):
					compensationRequest(component, blood_type, units)
				else:
					ReplacementRequest(component, blood_type, units)
				requestNum-=1
		endDay()