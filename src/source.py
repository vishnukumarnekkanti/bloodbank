
class source(Object):
	def __init__(self, id, name, bloodtype, addr, contacts, dateOfProcurement, component, instr):
		self.Id = id
		self.Name = name
		self.bloodType = bloodtype
		self.Address = addr
		self.contact = contacts        #list
		self.DateOfProcurement = dateOfProcurement
		self.Donated = component
		self.Instructions = instr      #instructions to contact

		