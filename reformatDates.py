#!/usr/bin/env python3
import pushBulletNotify
import sqlite3
from sense_hat import SenseHat
from datetime import datetime
import os
import json

PATH = "/home/pi/a1/"
DB_NAME = PATH+"weather_database/test.db" 

conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

try:

    c.execute("SELECT time FROM data_entry")

    rows = c.fetchall()

    for row in rows:
        
        row = str(row)
        print(row)
        entry = row.replace("('","")
        entry = entry.replace("',)","")
        c.execute("UPDATE users SET time=? WHERE time=?",(entry,str(d)))

        d = datetime.strptime(str(entry), '%Y-%m-%d %H:%M:%S.%f')

        print(d.strftime('%H:%M:%S %d/%m/%Y'))

        conn.close()

except sqlite3.Error as e:
    print(e)
    conn.close()