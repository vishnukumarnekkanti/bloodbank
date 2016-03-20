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
		if self.knownComponents.__contains__(component):
			return self.Life[component]
		else:
			raise ValueError("Unknown component type " + component + " known Components are " + str(self.knownComponents()))
		