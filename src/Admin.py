import Limits
from Request import Request

def checkStockLevel(component, blood_type):
	limit = Limits.BloodBankLimits(component, blood_type)
	level = getCurrentLevel(component, blood_type)
	if level > 2*limit.CRITICAL_LIMIT and level < 4*limit.CRITICAL_LIMIT:
		getDonorHelp()
	elif level < 2*limit.CRITICAL_LIMIT:
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
		

		