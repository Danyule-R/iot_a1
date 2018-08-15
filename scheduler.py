#!/usr/bin/env python3
from crontab import CronTab

cron = CronTab(user='pi')
cron.remove_all()


job = cron.new(command='/home/pi/a1/weatherlogger.py')

job.minute.every(1)
cron.write()
