from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
	try:
		cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
	except mysql.connector.Error as err:
		print("Failed creating database: {}".format(err))
		exit(1)

DB_NAME = 'BLOODBANK'

TABLES = {}
TABLES['element_record'] = (
	"CREATE TABLE `element_record` ("
	"  `id` int NOT NULL AUTO_INCREMENT,"
	"  `procurement_date` varchar(15) NOT NULL,"
	"  `component_name` varchar(15) NOT NULL,"
	"  `blood_type` varchar(5) NOT NULL,"
	"  `status` int NOT NULL,"
	"  PRIMARY KEY (`id`)"
	") ENGINE=InnoDB")

TABLES['daily_record'] = (
	"CREATE TABLE `daily_record` ("
	"  `component_name` varchar(15) NOT NULL,"
	"  `blood_type` varchar(5) NOT NULL,"
	"  `date` varchar(15) NOT NULL,"
	"  `required` int NOT NULL,"
	"  `supplied` int NOT NULL,"
	"  `replaced` int NOT NULL,"
	"  `damage` int NOT NULL,"
	"  `expired` int NOT NULL,"
	"  `final_stock` int NOT NULL"
	") ENGINE=InnoDB")

TABLES['request'] = (
	"CREATE TABLE `request` ("
	"  `id` int NOT NULL AUTO_INCREMENT,"
	"  `component_name` varchar(15) NOT NULL,"
	"  `blood_type` varchar(5) NOT NULL,"
	"  `units` int NOT NULL,"
	"  `status` int NOT NULL,"
	"  KEY `id` (`id`)"
	") ENGINE=InnoDB")

TABLES['replacement_record'] = (
	"CREATE TABLE `replacement_record` ("
	"  `replacement_id` int NOT NULL,"
	"  `component_name` varchar(15) NOT NULL,"
	"  `blood_type` varchar(5) NOT NULL,"
	"  `units` int NOT NULL,"
	"  PRIMARY KEY (`replacement_id`)"
	") ENGINE=InnoDB")

TABLES['replacer'] = (
	"CREATE TABLE `replacer` ("
	"  `replacer_id` int NOT NULL,"
	"  `replacement_id` int NOT NULL,"
	"  `instructions` varchar(30) NOT NULL,"
	"  `name` varchar(15) NOT NULL,"
	"  `address` varchar(30) NOT NULL,"
	"  `contact` int NOT NULL,"
	"  `deadline` varchar(15) NOT NULL,"
	"  `status` int NOT NULL,"
	"  FOREIGN KEY (`replacement_id`)"
	"     REFERENCES `replacement_record` (`replacement_id`)"
	") ENGINE=InnoDB")

cnx = mysql.connector.connect(user='root',password='spurthi12')
cursor = cnx.cursor()

try:
	cnx.database = DB_NAME    
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_BAD_DB_ERROR:
		create_database(cursor)
		cnx.database = DB_NAME
	else:
		print(err)
		exit(1)

for name, ddl in TABLES.iteritems():
	try:
		print("Creating table {}: ".format(name), end='')
		cursor.execute(ddl)
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
			print("already exists.")
		else:
			print(err.msg)
	else:
		print("OK")

cursor.close()
cnx.close()
