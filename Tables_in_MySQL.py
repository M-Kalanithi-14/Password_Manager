try : import pymysql as cntr
except ImportError: import mysql.connector as cntr
from sys import platform

if platform == "linux":
    db = cntr.connect(host="localhost", user='JB', passwd='manager')
else:
    db = cntr.connect(host="localhost", user='root', passwd='manager')

cur = db.cursor()

cur.execute("create database if not exists pasman;")
cur.execute("use pasman")
cur.execute("""create table users(
            Name varchar(255),
            Email varchar(255),
            username varchar(255),
            password varchar(255));""")
cur.execute("""create table AccountDetails(
            user varchar(255) References users(username),
            url varchar(255),
            email varchar(255),
            username varchar(255),
            password varchar(255));""")

db.commit()

print("Databases and Tables created SUCCESSFULLY")
c = input("Press Any Key to Continue ------>")

cur.close()
db.close()

del cur, db, cntr, platform, c