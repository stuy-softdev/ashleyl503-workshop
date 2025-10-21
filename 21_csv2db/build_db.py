#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024
#time taken : 1 hr

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

c.execute("CREATE TABLE IF NOT EXISTS students(name TEXT, age INTEGER, id INTEGER, UNIQUE(id))")

with open('students.csv', newline='') as studentscsv:
    reader = csv.DictReader(studentscsv)
    for row in reader:
        c.execute("INSERT OR IGNORE INTO students VALUES (\"" + row['name'] + "\", " + row['age'] + ", " + row['id'] + ")")

c.execute("CREATE TABLE IF NOT EXISTS courses(code TEXT, mark INTEGER, id INTEGER, UNIQUE(id))")

with open('courses.csv', newline='') as coursescsv:
    reader = csv.DictReader(coursescsv)
    for row in reader:
        c.execute("INSERT OR IGNORE INTO courses VALUES (\"" + row['code'] + "\", " + row['mark'] + ", " + row['id'] + ")")

#==========================================================

db.commit() #save changes
db.close()  #close database