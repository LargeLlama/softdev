#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import os

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

data = []
individual_rows = []

with open('data/peeps.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		individual_rows.append(row['name'])
		individual_rows.append(row['age'])
		individual_rows.append(row['id'])
		data.append(individual_rows)
		individual_rows = []

command = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGERY PRIMARY KEY)"          #build SQL stmt, save as string
c.execute(command)    #run SQL statement
c.executemany('INSERT INTO peeps VALUES (?, ?, ?)', data)
#==========================================================

db.commit() #save changes
db.close()  #close database


