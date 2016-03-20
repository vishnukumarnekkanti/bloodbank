
class Person(object):
	"""Person"""
	def __init__(self, person_id, name, addr, contacts, instr):
		super(Person, self).__init__()
		self.Id = person_id
		self.Name = name
		self.Address = addr
		self.contact = contacts                             # list
		self.Instructions = instr                           # instructions to contact

class Source(Person):
	""" the donors """
	def __init__(self, person_id, name, bloodtype, addr, contacts, dateOfProcurement, component, compensation, availability, instr):
		super(Source, self).__init__(person_id, name, addr, contacts, instr)
		self.bloodType = bloodtype
		self.DateOfProcurement = dateOfProcurement
		self.Donated = component
		self.Compensation = compensation                    # 0 for donors
		self.availability = availability                    # 0 or 1 applicable only for donors
		
class Replacer(object):
	"""docstring for Replacer"""
	def __init__(self, person_id, name, addr, contacts, deadline, replacement_id, instr):
		super(Replacer, self).__init__(person_id, name, addr, contacts, instr)
		self.ReplacementRecordId = replacement_id
		self.Deadline = deadline
		