from datetime import datetime
import Limits
import sqlEngine

class Record(object):
	"""Skeleton for Records"""
	def __init__(self, rec_id, component_name, blood_type):
		self.id = rec_id
		self.Name = component_name
		self.Type = blood_type
		

class ElementRecord(Record):
	"""Record for each blood unit"""
	def __init__(self, rec_id, component_name, blood_type, procurement_date, status):
		super(ElementRecord,self).__init__(rec_id, component_name, blood_type)
		self.DateOfProcurement = procurement_date
		self.LifeSpan = Limits.LifeSpan().LifeSpanOf(component_name)
		self.Status = status

	def getLifeLeft(self, current):
		x = abs((current - self.DateOfProcurement).days)
		return ((self.LifeSpan - x) if x<=self.LifeSpan else -1)

	def updateStatus(self, status):
		self.Status = status
		sqlEngine.updateElementRecordStatus(self)       #######sqlEngine

	def save(self):
		sqlEngine.saveER()


class DayRecord(Record):
	"""day wise records to show socke at the end of the day"""
	def __init__(self, id, component_name, blood_type, date):
		super(DayRecord, self).__init__( rec_id, component_name, blood_type)
		self.date = date
		self.Requested = sqlEngine.getTotalRequests()
		self.Supplied = sqlEngine.getTotalSupplied()
		self.Replaced = sqlEngine.getTotalReplacements()
		self.Expired = sqlEngine.getExpired()
		self.Damaged = sqlEngine.getDamaged()
		sqlEngine.clean()                                    #removes all damages, supplied etc in db
		self.FinalStock = sqlEngine.getFinalStock()

	def save(self):
		sqlEngine.saveDailyStats(self)                     #########sqlEngine


class ReplacementRecord(Record):
	"""Record for each blood unit"""
	def __init__(self, replacement_id, component_name, blood_type, units):
		super(ReplacementRecord,self).__init__(replacement_id, component_name, blood_type)
		self.units = units

	def save(self):
		return sqlEngine.saveRR() #returns replacementId

