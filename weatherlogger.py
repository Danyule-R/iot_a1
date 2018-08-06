''' array to store each item for database '''

from sense_hat import SenseHat
from datetime import datetime
import sqlite3

timestamp = datetime.now()
delay = 1

sqlite_file = 'rpiWeatherTable.sqlite'
table_name = 'Weather Data'  # name of the table to be created
id_column = 'id_col' # name of the column
temp_column = 'temp_col'
humidity_column = 'hum_col'
time_column = 'time_col'
column_type_text = 'TEXT'
column_type_int = 'INTEGER'

sense = SenseHat()

def get_sense_data():
	sense_data = []

	sense_data.append(sense.get_temperature())
	sense_data.append(sense.get_pressure())
	sense_data.append(sense.get_humidity())

	sense_data.append(datetime.now())

	return sense_data

''' create/write to databse goes here '''

# def create_db(): not sure if a function is needed for this for now

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
	.format(tn = table_name, nf = id_column, ft = column_type_int))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
	.format(tn = table_name, cn = temp_col, ct = column_type_int))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
	.format(tn = table_name, cn = humidity_column, ct = column_type_int))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
	.format(tn = table_name, cn = time_column, ct = column_type_text))

conn.commit()
conn.close()

''' infinite loop until interval checker is implemented '''

while True:
	data = get_sense_data()
	dt = data[-1] - timestamp
	if dt.seconds > delay:
		''' write data to database using writenow(insertsomedatavariablehere) or similar '''
		timestamp = datetime.now()

