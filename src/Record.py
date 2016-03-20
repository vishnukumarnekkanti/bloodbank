from datetime import datetime
import LifeSpan

class Record(object):
	"""Skeleton for Records"""
	def __init__(self, component_name, blood_type):
		self.id = 0
		self.Name = component_name
		self.Type = blood_type
		

class ElementRecord(Record):
	"""Record for each blood unit"""
	def __init__(self, component_name, blood_type, procurement_date):
		super(ElementRecord,self).__init__(component_name, blood_type)
		self.DateOfProcurement = procurement_date
		self.LifeSpan = LifeSpan.LifeSpanOf(component_name)

	def getLifeLeft(self, current):
		x = abs((current - self.DateOfProcurement).days)
		return ((self.LifeSpan - x) if x<=self.LifeSpan else -1)

class DayRecord(Record):
	"""day wise records to show socke at the end of the day"""
	def __init__(self, component_name, blood_type, requested, supplied, replaced, expired, damaged):
		super(DayRecord, self).__init__(component_name, blood_type)
		self.Requested = requested
		self.Supplied = supplied
		self.Replaced = replaced
		self.Expired = expired
		self.Damaged = damaged
		