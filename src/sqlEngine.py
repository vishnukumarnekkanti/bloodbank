"""database services"""
import random
from Record import *
from Admin import *
import mysql.connector

cnx = mysql.connector.connect(user='root', password='spurthi12', database='BLOODBANK')
cursor = cnx.cursor()

def getCurrentLevel(component, blood_type):
	#########################TODO : get count of records with status 1
	statusDict = {1:"Active",0:"used",-1:"expired"}
	cursor.execute("SELECT * FROM element_record")
	row = cursor.fetchone()
	count = 0
	while row is not None:
		print(row)
		if row[-1] == 1:
			count += 1
		row = cursor.fetchone()

	# return random.randint(1, 10000)
	return count

def supply(component, blood_type, units):
	cursor.execute("SELECT * FROM element_record")
	row = cursor.fetchone()
	count = 0
	while row is not None:
		print(row)
		if row[-1] == 1:
			count += 1
		row = cursor.fetchone()
	if count > units:
		cursor.execute("UPDATE element_record SET status=%s WHERE status = 1 " % (0))
		return 1
	else:
		return -1

def saveER(er):
	################ save ER to db
	data_record = (er.DateOfProcurement, er.Name, er.Type, er.status)
	add_record = ("INSERT INTO element_record "
			"(procurement_date, component_name, blood_type, status) "
			"VALUES (%s, %s, %s, %d)")
	cursor.execute(add_record, data_record)
	cnx.commit()

def saveRR(rr):
	data_record = (rr.Name, rr.Type, rr.units, rr.Deadline)
	add_record = ("INSERT INTO replacement_record "
			"(component_name, blood_type, units, deadline) "
			"VALUES (%s, %s, %d, %d)")
	cursor.execute(add_record, data_record)
	cnx.commit()
	pass

def updateERStatus(er, status):
	pass

def saveDSR(dsr):
	pass

def RequestStatus(component, blood_type, u, s):
	statusDict = {1:"success",0:"failure", 2:"notyetserved"}
	cursor.execute("UPDATE request SET status=%d WHERE status = 2 AND units = u " % (s))

def updateDailyRecord():
	cursor.execute("SELECT * FROM element_record")
	row = cursor.fetchone()
	supplied = 0
	failure = 0
	expired = 0
	while row is not None:
		print(row)
		if row[-1] == 1:
			supplied += 1
		elif row[-1] == -1:
			expired += 1
		row = cursor.fetchone()
	cursor.execute("SELECT * FROM request")
	row = cursor.fetchone()
	while row is not None:
		print(row)
		if row[-1] == 0:
			failure += row[-2]
		row = cursor.fetchone()
	
	cursor.execute("DELETE FROM element_record WHERE status = 0")
	cursor.execute("DELETE FROM request WHERE status = 1")

def getReplacementNum():
	cursor.execute("SELECT * FROM element_record")
	row = cursor.fetchone()
	count = 0
	while row is not None:
		print(row)