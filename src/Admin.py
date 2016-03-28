import Limits
from Request import Request
from source import *

def getCurrDate():
	pass
def checkStockLevel(component, blood_type):
	limit = Limits.BloodBankLimits(component, blood_type)
	level = getCurrentLevel(component, blood_type)                  #############DataBase
	if level > 2*limit.CRITICAL_LIMIT and level < 4*limit.CRITICAL_LIMIT:
		organizeBloodCamp()
	else:
		pass


def compensationRequest(component, blood_type, units):
	#create request
	req = new Request(component, blood_type, units, "compensation")
	#serve request
	req.flow()
	#check stock level
	checkStockLevel(component, blood_type)

def ReplacementRequest(component, blood_type, units):
	#create replacer
	replacement = 
	replacer = Replacer(0, "human", "addr", "125478963", currDate , replacement.Id, instr)
	#create request
	req = new Request(component, blood_type, units, "compensation")
	#serve request
	req.flow()
	#check stock level
	checkStockLevel(component, blood_type)
	