#!/usr/bin/env python3
import bluetooth
import os
import time
import sqlite3

from sense_hat import SenseHat

PATH = "/home/pi/a1/"
DB_NAME = PATH+"weather_database/sensehat_log.db" 
sense = SenseHat()

# Main function
def main():
    users = getRegisteredUsers()
    while True:
        search(users)
        time.sleep(30)


def getRegisteredUsers():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("SELECT name, mac_address, device_name FROM users")
        registeredUsers = c.fetchall()

        conn.commit()
        conn.close()

        return registeredUsers

    except sqlite3.Error as e:
        print(e)
        conn.close()    

        return None


#check whether found devices match any registered in database
def userMatch(mac_address, users):
    for user in users:
        mac_add = user[1]

        if(mac_address == mac_add):
            return user
        else:
            return None
            

#calibrate current temp
def getCurrentTemp():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    cpu_temp = cpu_temp.replace("temp=","")
    cpu_temp = float(cpu_temp.replace("'C\n",""))

    return round((cpu_temp-sense.get_temperature()),1)


# Search for device based on device's name
def search(users):
    nearby_devices = bluetooth.discover_devices()
    user = None
    for mac_address in nearby_devices:
        user = userMatch(mac_address,users)
        
        if(user is not None):
            break

    if user is not None:
        u_name = user[0]
        u_device_name = user[2]
        u_mac_address = user[1]

        print("Hi {}! Your phone ({}) has the MAC address: {}".format(u_name, u_device_name, u_mac_address))
        temp = getCurrentTemp()
        sense.show_message("Hi {}! Current Temp is {}*c".format(u_name, temp), scroll_speed=0.05)
    else:
        print("No registered devices nearby...")


#Execute program
main()


