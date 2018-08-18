import sqlite3
app.database = "sensehat_log.db"

@app.route('weather_database/sensehat_log.db')
def weatherdata():
    g.db = connect.db()
    cur = g.db.execute('SELECT * from data_entry')
    Data = [dict(ID=row[0],
                    Temperature=column[1],
                    Humidity=column[2],
                    Pressure=column[3],
                    Time=column[4]) for column in cur.fetchall()]
    g.db.close()
    return render_template('index.html', Data=Data)