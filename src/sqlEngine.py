"""database services"""
import random
from Record import *
from Admin import *


def getCurrentLevel(component, blood_type):
	#########################TODO : get count of records with status 1
	statusDict = {1:"Active",0:"used",-1:"expired"}
	return random.randint(1, 10000)

def saveER(er):
	################ save ER to db
	pass

def saveRR(rr):
	pass

def updateERStatus(er, status):
	pass

def saveDSR(dsr):
	pass

def RequestStatus(component, blood_type, units, status):
	statusDict = {1:"Active",0:"used",-1:"expired"}
	pass

def updateDailyRecord():
	pass