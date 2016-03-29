import Limits
import thread
from Request import Request
from Record import *
from source import *
from datetime import date, timedelta
import random
import threading
import sqlEngine
currDate = 0
campLock = 0
lock = threading.Lock()

def getCurrDate():
	global currDate
	if currDate==0:
		currDate = date(2006, 1, 1)
	return currDate


def beginDay():
	return getCurrDate()


def organizebloodCamp(presentDate,component_name, blood_type): #blood camp for 3 days after 7 days from the present day
    campday1 = presentDate + timedelta(days=7)
    campday2 = presentDate + timedelta(days=8)
    campday3 = presentDate + timedelta(days=9)
    while campday1!= getCurrDate():
    	pass
    with lock:
	    #rand number to decide on donations that day
	    rand = random.randint(500, 1000)
	    for x in xrange(rand):
	        donation(0, component_name, blood_type, campday1, 1)
    while campday2!= getCurrDate():
    	pass
    with lock:
	    #rand number to decide on donations that day
	    rand = random.randint(800, 1500)
	    for x in xrange(rand):
	        donation(0, component_name, blood_type, campday2, 1)
    while campday3!= getCurrDate():
    	pass
    with lock:
	    #rand number to decide on donations that day
	    rand = random.randint(1000, 2000)
	    for x in xrange(rand):
	    	donation(0, component_name, blood_type, campday2, 1)
    global campLock
    campLock = 0


def checkStockLevel(component, blood_type):
	limit = Limits.BloodBankLimits(component, blood_type)
	level = sqlEngine.getCurrentLevel(component, blood_type)                  #############DataBase
	global campLock
	if level > 2*limit.CRITICAL_LIMIT and level < 4*limit.CRITICAL_LIMIT:
		if campLock == 0:   ############blood camp not scheduled
		    campLock=1
		    thread.start_new_thread(organizeBloodCamp, getCurrDate(), component_name, blood_type,)
		else:
			pass
	else:
		campLock = 0


def compensationRequest(component, blood_type, units):
	#create request
	req = Request(component, blood_type, units)
	#serve request
	req.flow()
	#check stock level
	checkStockLevel(component, blood_type)

def ReplacementRequest(component, blood_type, units):
	#create replacer
	replacement = ReplacementRecord(0, component_name, blood_type, units, getCurrDate())
	#replacementId = replacement.saveRR()                               ##########saves in db and returns replacement id
	#replacer = Replacer(0, "human", "addr", "125478963", getCurrDate() + timedelta(days=7) , replacementId, "instr")
	saveReplacerData()
	#create request
	req = Request(component, blood_type, units)
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
		sqlEngine.updateDailyRecord()
		currDate = currDate + timedelta(days = 1)
