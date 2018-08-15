#!/usr/bin/env python3
from crontab import CronTab

cron = CronTab(user='pi')

for j in cron:
    print(j.is_enabled())
    print(j.is_valid())
