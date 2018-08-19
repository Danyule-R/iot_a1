#!/usr/bin/env python3
import requests
import json
import os

ACCESS_TOKEN="o.6GhnVpyeC0rT5uUMweJy62R8wQoFd44k"

def send_notification_via_pushbullet(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {
        "type": "note", 
        "title": title, 
        "body": body, 
        "target_device_iden": "ujxOZ5FlrNssjAiVsKnSTs"
    }
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Access-Token': ACCESS_TOKEN, 
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        print(resp.status_code)
        raise Exception('Error sending pushbullet notification')
       
    else:
        print('complete sending')

#main function
def send(temp):
    ip_address = os.popen('hostname -I').read()
    send_notification_via_pushbullet(ip_address, "Hello Daniel! It is currently "+str(temp)+"c. Wear a sweater!")

