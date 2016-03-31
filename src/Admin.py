import Limits
import thread
from Request import *
from Record import *
from source import *
from datetime import date, timedelta
import random
import threading
import sqlEngine

currDate = 0
campLock = 0
campDay = date(2006, 1, 1)
lock = threading.Lock()

def getCurrDate():
	global currDate
	if currDate==0:
		currDate = date(2006, 1, 1)
	return currDate


def organizebloodCamp(component_name, blood_type): #blood camp for 3 days after 7 days from the present day
    rand = random.randint(2000, 3000)
    c = getCurrDate()
    print str(c),rand
    for x in xrange(rand):
        donation(0, component_name, blood_type, c)
    global campLock
    campLock = 0

def beginDay():
	if getCurrDate() == campDay:
		organizebloodCamp("rbc","A+")
	return getCurrDate()


def checkStockLevel(component, blood_type):
	limit = Limits.BloodBankLimits(component, blood_type)
	level = sqlEngine.getCurrentLevel(component, blood_type)                  #############DataBase - y
	global campLock
	global campDay
	if level < limit.MAX_CAPACITY/2 :#level < 4*limit.CRITICAL_LIMIT:
		if campLock == 0:   ############blood camp not scheduled
		    campLock=1
		    campDay = getCurrDate() + timedelta(days=5)
		    #organizeBloodCamp(getCurrDate(), component_name, blood_type)
		else:
			pass
	else:
		campLock = 0


def compensationRequest(component, blood_type, units):
	#create request
	req = Request(component, blood_type, units, 2)
	#serve request
	req.flow()
	#check stock level
	checkStockLevel(component, blood_type)

def ReplacementRequest(component, blood_type, units):
	#create replacer
	replacement = ReplacementRecord(0, component, blood_type, units, getCurrDate()+timedelta(days=7), 1)
	#replacementId = replacement.saveRR()                               ##########saves in db and returns replacement id
	#replacer = Replacer(0, "human", "addr", "125478963", getCurrDate() + timedelta(days=7) , replacementId, "instr")
	#---------------change------------------
	#saveReplacerData()
	#create request
	req = Request(component, blood_type, units, 2)
	#serve request
	req.flow()
	#check stock level
	checkStockLevel(component, blood_type)
	
def donation(rec_id, component_name, blood_type, procurement_date):
	er = ElementRecord(rec_id, component_name, blood_type, procurement_date, 1)
	er.save()

def endDay():
	global currDate
	with lock:
		sqlEngine.updateDailyRecord(getCurrDate())
		currDate = currDate + timedelta(days = 1)







#############################        input.py          ##################
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
	    inputData[int(k.strip())] = float(v.strip())
	f.close()
	component = "rbc"
	blood_type = "A+"
	for day in xrange(1,730):
		d = beginDay()
		choices_0 = [(0,90),(1,10)]
		requestNum = int((getRand(1,10))*inputData[day] + 2*((getRand(5,30))*inputData[day])*prob(choices_0))
		donationNum = int((getRand(0,50))*inputData[day])
		donationNum += sqlEngine.getReplacementNum()                 #####################db
		choices_1 = [(0,60),(1,40)]
		choices_2 = [(0,80),(1,20)]
		choices_3 = [(0,499),(1,1)]
		print "Transactions on ", str(currDate) , " = " , requestNum+donationNum
		for transaction in xrange(requestNum+donationNum):
			if (prob(choices_1) == 1) and donationNum>0:
				donation(0, component, blood_type, (getCurrDate()))
				donationNum-=1
			else:
				units = int((getRand(1,10))*inputData[day] + ((getRand(10,25))*inputData[day])*prob(choices_0) + 2*((getRand(20,50))*inputData[day])*prob(choices_3))
				if prob(choices_2):
					compensationRequest(component, blood_type, units)
				else:
					ReplacementRequest(component, blood_type, units)
				requestNum-=1
		endDay()