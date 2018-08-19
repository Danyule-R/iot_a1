#!/usr/bin/env python3
import bluetooth
import os
import time
from sense_hat import SenseHat

PATH = "/home/pi/a1/"
DB_NAME = PATH+"weather_database/sensehat_log.db" 


# Main function
def main():
    # user_name = input("Enter your name: ")
    # device_name = input("Enter the name of your phone: ")
    while True:
        search("Daniel", "50:01:D9:EE:FB:71")
        time.sleep(30)


def getCurrentTemp():
    sense = SenseHat()
	cpu_temp = os.popen("vcgencmd measure_temp").readline()
	cpu_temp = cpu_temp.replace("temp=","")
	cpu_temp = float(cpu_temp.replace("'C\n",""))

	return round((cpu_temp-sense.get_temperature()),1)


# Search for device based on device's name
def search(user_name, mac_address):
    nearby_devices = bluetooth.discover_devices()

    for mac_address in nearby_devices:
        print(mac_address)
        # if device_name == bluetooth.lookup_name(mac_address, timeout=5):
        #     device_address = mac_address
        #     break
    if device_address is not None:
        print("Hi {}! Your phone ({}) has the MAC address: {}".format(user_name, device_name, device_address))
        temp = round(sense.get_temperature(), 1)
        sense.show_message("Hi {}! Current Temp is {}*c".format(user_name, temp), scroll_speed=0.05)
    else:
        print("Could not find target device nearby...")


#Execute program
main()


