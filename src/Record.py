from datetime import datetime
import Limits

class Record(object):
	"""Skeleton for Records"""
	def __init__(self, rec_id, component_name, blood_type):
		self.id = 0
		self.Name = component_name
		self.Type = blood_type
		

class ElementRecord(Record):
	"""Record for each blood unit"""
	def __init__(self, rec_id, component_name, blood_type, procurement_date):
		super(ElementRecord,self).__init__(rec_id, component_name, blood_type)
		self.DateOfProcurement = procurement_date
		self.LifeSpan = Limits.LifeSpan().LifeSpanOf(component_name)
		self.status = "GOOD"

	def getLifeLeft(self, current):
		x = abs((current - self.DateOfProcurement).days)
		return ((self.LifeSpan - x) if x<=self.LifeSpan else -1)

	def updateStatus(self, status):
		self.Status = status


class DayRecord(Record):
	"""day wise records to show socke at the end of the day"""
	def __init__(self, id, component_name, blood_type, date):
		super(DayRecord, self).__init__( rec_id, component_name, blood_type)
		self.date = date
		self.Requested = getTotalRequests()
		self.Supplied = getTotalSupplied()
		self.Replaced = getTotalReplacements()
		self.Expired = getExpired()
		self.Damaged = getDamaged()
		clean()                                    #removes all damages, supplied etc in db
		self.FinalStock = getFinalStock()


class ReplacementRecord(Record):
	"""Record for each blood unit"""
	def __init__(self, replacement_id, component_name, blood_type, units):
		super(ReplacementRecord,self).__init__(component_name, blood_type)
		self.ReplacerId = replcement_id
		self.units = units

