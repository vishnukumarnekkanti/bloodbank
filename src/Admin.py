class CompensationRequest(Request):
	"""Compensation Request flow"""
	def __init__(self, component, blood_type, units, compensation_type):
		super(CompensationRequest, self).__init__( component, blood_type, units, compensation_type)
		flow()
		
	def flow():
		"""receive compensation, supply, check inventory status"""
		pass




class ReplacementRequest(CompensationRequest):
	"""Replacement Request flow"""
	def flow():
		"""record replacer details, replacement details, supply, check inventory status, check for replacement"""
		pass
		

		