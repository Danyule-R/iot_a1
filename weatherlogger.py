#!/usr/bin/env python3
import pushBulletNotify
import sqlite3
from sense_hat import SenseHat
from datetime import datetime
import os
import json

PATH = "/home/pi/a1/"
DB_NAME = PATH+"weather_database/sensehat_log.db" 

def get_sense_data():
	
	data = []
	sense = SenseHat()

	#get pi temp
	cpu_temp = os.popen("vcgencmd measure_temp").readline()
	cpu_temp = cpu_temp.replace("temp=","")
	cpu_temp = float(cpu_temp.replace("'C\n",""))

	calibrated_temp = round((cpu_temp-sense.get_temperature()),1)

	if(calibrated_temp<20):
		pushBulletNotify.send(calibrated_temp)
		
	data.append(calibrated_temp)
	data.append(round(sense.get_humidity(),1))
	data.append(round(sense.get_pressure(),1))

	return data


#add data entry to db
def insertIntoDatabase(sqlite_file,data):
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	temp = data[0]
	humid = data[1]
	press = data[2]
	time = str(datetime.now())

	
	try:
		c.execute("INSERT INTO data_entry(temp, humidity, pressure, time) VALUES(?,?,?,?)",(temp,humid,press,time))
		conn.commit()
		conn.close()
	except sqlite3.Error as e:
		print(e)
		conn.close()


#start program
def main():
	data = get_sense_data()
	if data is not None:
		print("Added entry")
		insertIntoDatabase(DB_NAME, data)

main()

