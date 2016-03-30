"""database services"""
import random
from Record import *
# from Admin import *
# from Admin import getCurrDate
from Input import *
import mysql.connector
from datetime import date, timedelta

cnx = mysql.connector.connect(user='root', password='spurthi12', database='BLOODBANK')
cursor = cnx.cursor()

def strTodate(s):
	s = s.split('-')
	return date(int(s[0]), int(s[1]), int(s[2]))

def getCurrentLevel(component, blood_type):
	#########################TODO : get count of records with status 1
	statusDict = {1:"Active",0:"used",-1:"expired"}
	cursor.execute("SELECT * FROM element_record")
	row = cursor.fetchone()
	count = 0
	while row is not None:
		#print(row)
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
		#print(row)
		if row[-1] == 1:
			count += 1
		row = cursor.fetchone()
	if count > units:
		u = units
		ans = []
		cursor.execute("SELECT * FROM element_record WHERE status = 1")
		row = cursor.fetchone()
		while row is not None:
			if u > 0:
				ans.append(row[0])
			u -= 1
			row = cursor.fetchone()

		for row in ans:
			cursor.execute("UPDATE element_record SET status='{0}' WHERE id = '{1}'".format(0, row))
		cnx.commit()
		return True
	else:
		return False

def saveER(er):
	################ save ER to db
	data_record = (str(er.DateOfProcurement), er.Name, er.Type, er.Status)
	#print data_record
	# add_record = ("INSERT INTO element_record "
	# 		"(procurement_date, component_name, blood_type, status) "
	# 		"VALUES (%s, %s, %s, %d)")
	add_record = "INSERT INTO element_record(procurement_date, component_name, blood_type, status) VALUES('{0}', '{1}', '{2}', '{3}');".format(str(er.DateOfProcurement), er.Name, er.Type, er.Status)
	cursor.execute(add_record)
	cnx.commit()

def saveRR(rr):
	data_record = (rr.Name, rr.Type, rr.units, str(rr.Deadline))
	add_record = ("INSERT INTO replacement_record "
			"(component_name, blood_type, units, deadline) "
			"VALUES (%s, %s, %d, %d)")
	cursor.execute(add_record, data_record)
	cnx.commit()

def updateERStatus(er, status):
	pass

def saveDSR(dsr):
	pass

def RequestStatus(component, blood_type, u, s):
	statusDict = {1:"success",0:"failure", 2:"notyetserved"}
	data_record = (component, blood_type, int(u), int(s))
	#print data_record
	#add_record = ("INSERT INTO request(component_name, blood_type, units, status) VALUES(%s, %s, %d, %d)")
	add_record = "INSERT INTO request(component_name, blood_type, units, status) VALUES('{0}', '{1}', '{2}', '{3}');".format(component, blood_type, u, s)
	cursor.execute(add_record)
	cnx.commit()

def updateDailyRecord(getCurrDate):
	cursor.execute("SELECT * FROM element_record")
	row = cursor.fetchone()
	supplied = 0
	failure = 0
	expired = 0
	donations = 0
	while row is not None:
		#print(row)
		if row[-1] == 1:
			supplied += 1
		elif row[1] == str(getCurrDate-timedelta(days=21)):
			expired += 1
		if strTodate(row[1]) == getCurrDate:
			donations += 1
		row = cursor.fetchone()
	
	cursor.execute("SELECT * FROM request")
	row = cursor.fetchone()
	while row is not None:
		#print(row)
		if row[-1] == 0:
			failure += row[-2]
		row = cursor.fetchone()
	
	cursor.execute("DELETE FROM element_record WHERE status = '{0}' OR procurement_date = '{1}';".format(0, str((getCurrDate-timedelta(days=21)))))
	cursor.execute("TRUNCATE TABLE request")
	cursor.execute("DELETE FROM replacement_record WHERE status = 0 OR deadline = '{0}';".format(str(getCurrDate)))
	cursor.execute("SELECT COUNT(*) AS C FROM element_record")
	stock = int((cursor.fetchone())[0])
	#data_record = ('rbc', 'A+', str(getCurrDate), (supplied+failure), supplied, donations, expired, stock)
	add_record = "INSERT INTO daily_record (component_name, blood_type, `date`, required, supplied, received, expired, final_stock) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}');".format('rbc', 'A+', str(getCurrDate), supplied+failure, supplied, donations, expired, stock)
	cursor.execute(add_record)
	cnx.commit()

def getReplacementNum():
	cursor.execute("SELECT COUNT(*) AS C FROM replacement_record")
	a = int((cursor.fetchone())[0])
	num = getRand(0, a)
	lst = random.sample(range(1, a), num)
	count = 1
	ans = []
	cursor.execute("SELECT * FROM replacement_record")
	row = cursor.fetchone()
	while row is not None:
		if count in lst:
			ans.append(row)
		count += 1
	replacements = 0
	for row in ans:
		key = row[0]
		cursor.execute("UPDATE replacement_record SET status=%s WHERE replacement_id = key " % (0))
		replacements += row[3]
	cnx.commit()
	return replacements