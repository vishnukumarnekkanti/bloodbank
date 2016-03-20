
class Request(object):
	"""Skeleton class of all Requests"""
	def __init__(self, component, blood_type, units, compensation_type):
		super(Request, self).__init__()
		self.BloodComponent = component
		self.BloodType = blood_type
		self.Units = units
		self.CompensationMethod = compensation_type           # cash or replacement