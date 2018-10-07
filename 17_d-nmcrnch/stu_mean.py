#Team wokeuplikethis* - Rubin P., Raymond W. 
#SoftDev1 pd7
#k17
#2018-10-05

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE = "database.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

# PARSE THROUGH CSV FILES AND CREATE A SQLITE-FRIENDLY LIST
def parse_csv(path_to_csv, header1, header2, header3):
    data = []

    with open(path_to_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            individual_rows = list((row[header1], row[header2], row[header3]))
            data.append(individual_rows)

    return data

# CREATE A DATABSE FROM THE LIST
#========peeps========
command = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)"
c.execute(command)

peeps = parse_csv('data/peeps.csv', 'name', 'age', 'id')
c.executemany('INSERT INTO peeps VALUES (?, ?, ?)', peeps)

#=====courses========
command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"
c.execute(command)

courses = parse_csv('data/courses.csv', 'code', 'mark', 'id')
c.executemany('INSERT INTO courses VALUES (?, ?, ?)', courses)
#======== end of creating database.db===========
db.commit() #save changes
db.close()  #close database

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

# CREATE A DICTIONARY BASED OFF databse.db FILE
#FORMAT: id : [name, grade0, grade1, grade2, ...]
def create_dict():
    DICT = {}
    LIST = []
    peeps = c.execute("SELECT * FROM peeps")
    for row in peeps:
        LIST.append(row[0])
        DICT[row[2]] = LIST
        LIST = []
    
    courses  = c.execute("SELECT * FROM courses")
    for row in courses:
        DICT[row[2]].append(row[1])

    return DICT 

# diagnostic print statements for the create_dict() method
'''
test = create_dict()
for key in test.keys():
    print(str(key) + ": " + str( test[key]))
'''

def calc_avg():
    DICT = create_dict()
    for key in DICT.keys():
        TOTAL  = 0
        SUM = 0
        for element in DICT[key]:
            if type(element) is int:
                TOTAL += 1
                SUM += element
        DICT[key].append(SUM / TOTAL)
    return DICT

#DIAGNOSTIC PRINT STATEMENT FOR THE calc_avg() METHOD
'''
test = calc_avg() 
for key in test.keys():
    print(str(key) + ": " + str( test[key]))
'''
db.commit() #save changes
db.close()  #close database


# CREATE A DATABSE FROM THE DICTIONARY
DB_FILE = "peeps_avg.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#======= creating the file and getting the averages
command = "CREATE TABLE peeps_avg (name TEXT, id INTEGER, avg INTEGER)"
c.execute(command)

#======================================

