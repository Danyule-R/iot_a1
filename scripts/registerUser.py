#!/usr/bin/env python3
import sqlite3

PATH = "/home/pi/a1/"
DB_NAME = PATH+"weather_database/sensehat_log.db" 

def addEntry(userName, macAddress):

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users(name, mac_address) VALUES(?,?)",(userName,macAddress))
        conn.commit()
        conn.close()
        print("New user added successfully.")
    except sqlite3.Error as e:
        print(e)
        conn.close()

addEntry("Daniel","50:01:D9:EE:FB:71")