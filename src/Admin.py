class CompensationRequest(Request):
	"""Compensation Request flow"""
	def __init__(self, component, blood_type, units, compensation_type):
		super(CompensationRequest, self).__init__( component, blood_type, units, compensation_type)
		
	def flow():
		pass




class ReplacementRequest(CompensationRequest):
	"""Replacement Request flow"""
	def flow():
		pass
		

		