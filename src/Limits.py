class BloodBankLimits(object):
	"""Limits"""
	def __init__(self, component, blood_type):
		self.MAX_CAPACITY = 10000
		self.CRITICAL_LIMIT = self.MAX_CAPACITY/20
		self.component = component
		self.Type = blood_type


class LifeSpan(object):
	"""LifeSpan records of components"""
	def __init__(self):
		super(LifeSpan, self).__init__()
		self.Life = {}
		self.Life["wholeblood"] = 21
		self.Life["rbc"] = 42
		self.Life["frozenrbc"] = 3650

	def knownComponents(self):
		return self.Life.keys()

	def LifeSpanOf(self, component):
		if (self.knownComponents()).__contains__(component):
			return self.Life[component]
		else:
			raise ValueError("Unknown component type " + component + " known Components are " + str(self.knownComponents()))
		