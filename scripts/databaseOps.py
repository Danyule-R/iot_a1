#!/usr/bin/env python3

import sqlite3

sqlite_file = 'weather_database/sensehat_log.db'
table_name = 'data_entry'  # name of the table to be created
id_column = 'id' # name of the column
temp_column = 'temp'
humidity_column = 'humidity'
pressure_column = 'pressure'
time_column = 'time'
column_type_text = 'TEXT'
column_type_int = 'INTEGER'
column_type_dec = 'REAL'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
try:
    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn = table_name, nf = id_column, ft = column_type_int))

    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn = table_name, cn = temp_column, ct = column_type_dec))

    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn = table_name, cn = humidity_column, ct = column_type_dec))

    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn = table_name, cn = pressure_column, ct = column_type_dec))

    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn = table_name, cn = time_column, ct = column_type_text))

    conn.commit()
    print("Database created successfully...")

except sqlite3.OperationalError:
    print("Database not created - already exists")

conn.close()
