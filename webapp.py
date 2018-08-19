#!/usr/bin/env python3
from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

app.database = "weather_database/sensehat_log.db"

@app.route('/')
def weatherdata():
    con = sql.connect("weather_database/sensehat_log.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute('SELECT * from data_entry')

    rows = cur.fetchall();
    
    return render_template("/index.html", rows = rows)

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
