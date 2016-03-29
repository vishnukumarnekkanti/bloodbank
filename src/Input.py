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
choices = [(0,99),(1,1)]

def prob():
    return weighted_choice(choices) 

f = open(filepath, 'r')
inputData = {}
for line in f:
    k, v = line.strip().split(',')
    inputData[k.strip()] = v.strip()

f.close()
for day in xrange(1,3651):
	beginDay()
	requestNum = (getRand(50,200))*inputData[day] + 3*((getRand(50,200))*inputData[day])*prob()