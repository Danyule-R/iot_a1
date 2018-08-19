#!/usr/bin/env python3
import sqlite3
from sense_hat import SenseHat
from datetime import datetime
import os
import json

PATH = "/home/pi/a1/"
DB_NAME = PATH+"weather_database/sensehat_log.db" 

conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

try:

    c.execute("SELECT id, time FROM data_entry")

    rows = c.fetchall()

    for row in rows:
        id = row[0]
        date = row[1]

        print(date)

        d = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        d_formatted = d.strftime('%H:%M:%S %d/%m/%Y')

        c.execute("UPDATE data_entry SET time=? WHERE id=?",(d_formatted,id))

        conn.commit()




except sqlite3.Error as e:
    print(e)


conn.close()