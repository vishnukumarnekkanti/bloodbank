
class ParentRequest(object):
	"""Skeleton class of all Requests"""
	def __init__(self, component, blood_type, units, compensation_type):
		super(Request, self).__init__()
		self.BloodComponent = component
		self.BloodType = blood_type
		self.Units = units
		self.CompensationMethod = compensation_type           # cash or replacement

class Request(ParentRequest):
	"""Compensation Request flow"""
	def __init__(self, component, blood_type, units, compensation_type):
		super(CompensationRequest, self).__init__( component, blood_type, units, compensation_type)
		
	def flow():
		"""receive compensation, supply, check inventory status"""
		component = self.BloodComponent
		blood_type = self.BloodType
		units = self.Units 
		if stockLevel(component, blood_type, units) :                 #############DataBase
			supply(component, blood_type, units)                 #############DataBase
			RequestStatus(component, blood_type, units, 1)                 #############DataBase
		else:
			RequestStatus(component, blood_type, units, 0)                 #############DataBase
