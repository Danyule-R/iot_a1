#!/usr/bin/env python3
from sense_hat import SenseHat
from datetime import datetime
import json

timestamp = datetime.now()
delay = 1


sense = SenseHat()

def get_sense_data():
	data = {}

	data['entry'] = []

	data['entry'].append({
		'temp' : str(round(sense.get_temperature())),
		'pressure' : str(round(sense.get_pressure())),
		'humidity' : str(round(sense.get_humidity())),
		'time' : str(datetime.now())
	})

	return data


''' infinite loop until interval checker is implemented '''
dataFile = open("datalog.json","w")
data = get_sense_data()
json.dump(data, dataFile)


dataFile.close()

# while True:

# 	data = get_sense_data()
# 	dt = data[-1] - timestamp
# 	if dt.seconds > delay:
# 		''' write data to database using writenow(insertsomedatavariablehere) or similar '''
# 		timestamp = datetime.now()

