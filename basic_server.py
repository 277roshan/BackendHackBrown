import json
import sqlite3
from flask import Flask
app = Flask(__name__)

# {
#   "id": 38,
#   "email": "exampleuser@gmail.com",
#   "phone_number": "5555555555",
#   "first_name": "John",
#   "last_name": "Smith",
#   "address": "200 Meeting St",
#   "city": "Providence",
#   "state": "RI",
#   "zip_code": "02912",
#   "lat": 41.8290991,
#   "lng": -71.4017861,
#   "provider": "email",
#   "uid": "exampleuser@gmail.com",
#   "stripe_id": "cus_6R11Epn5AkhI9V",
#   "profile_photo": {
#     "url": null,`
#     "thumb": {
#       "url": null
#     }
#   },
#   "region_id": 1
# }

@app.route('/create_table')
def create_table():
	conn = sqlite3.connect('users.db')
	conn.execute('''CREATE TABLE USERS_INFO
       (EMAIL TEXT PRIMARY KEY     NOT NULL,
       	UID   TEXT,
       PHONE_NUMBER           TEXT    NOT NULL,
       FIRST_NAME            TEXT     NOT NULL,
       LAST_NAME        TEXT,
       ADDRESS         TEXT,
       CITY 			TEXT,
       STATE 			TEXT,
       ZIP_CODE			TEXT,
       LAT 				TEXT,
       LNG 				TEXT,
       PROFILE_PHOTO 	TEXT
       );''')
	print "Table users.db created successfully";
	conn.close()

	conn = sqlite3.connect('messages.db')
	conn.execute('''CREATE TABLE MESSAGES
       (MSGID TEXT PRIMARY KEY     NOT NULL,
       	MESSAGE   TEXT			NOT NULL,
       FIRST_NAME            TEXT     NOT NULL,
       LAST_NAME        TEXT,
       ADDRESS         TEXT,
       CITY 			TEXT,
       STATE 			TEXT,
       ZIP_CODE			TEXT,
       LAT 				TEXT,
       LNG 				TEXT,
       PROFILE_PHOTO 	TEXT
       );''')
	print "Table messages.db created successfully"
	conn.close()
	return json.dumps({'msg':'Successfully created'})

@app.route('/add_user')
def add_user():
      conn = sqlite3.connect('users.db')
      print "Opened database successfully"
      conn.execute("INSERT INTO USERS_INFO (EMAIL, UID, PHONE_NUMBER,FIRST_NAME, LAST_NAME, ADDRESS, CITY, STATE, ZIP_CODE, LAT, LNG, PROFILE_PHOTO) \
            VALUES ('test2@gmail.com', 'sdfsdfs', '2026583421','Paul', 'Lamela','211 Elm Street','Washington','DC', '20001','80','20','url.com' )")
      conn.commit()
      print "Records created successfully";
      conn.close()
      return json.dumps({'msg':'Successfully added records'})


@app.route('/get_user')
def get_all_user():
      conn = sqlite3.connect('users.db')
      print "Opened database successfully";
      cursor = conn.execute("SELECT EMAIL, FIRST_NAME, LAST_NAME from USERS_INFO")
      emails = []
      for row in cursor:
            emails.append(row[0])
      conn.close()
      return json.dumps({'msg':emails})


@app.route('/man')
def oi():
	print json.dumps({'username':'user','password':'sd'})
	return json.dumps({'username':'user','password':'sd'})

if __name__ == '__main__':
    app.run()