
##request should have status

class ParentRequest(object):
	"""Skeleton class of all Requests"""
	def __init__(self, component, blood_type, units, status):
		super(Request, self).__init__()
		self.BloodComponent = component
		self.BloodType = blood_type
		self.Units = units
		self.status = status

class Request(ParentRequest):
	"""Request flow"""
	def __init__(self, component, blood_type, units, status):
		super(CompensationRequest, self).__init__( component, blood_type, units, status)
		
	def flow(self):
		"""receive compensation, supply, check inventory status"""
		component = self.BloodComponent
		blood_type = self.BloodType
		units = self.Units 
		if sqlEngine.supply(component, blood_type, units):                 #############DataBase - y
			sqlEngine.RequestStatus(component, blood_type, units, 1)                 #############DataBase - y
		else:
			sqlEngine.RequestStatus(component, blood_type, units, 0)