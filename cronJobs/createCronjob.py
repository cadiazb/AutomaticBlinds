#!/usr/bin/env python

import subprocess
from getSunTimes import getSunriseTime, getSunsetTime

# crontab syntax
# Minute   Hour   Day of Month       Month          Day of Week        Command    
# (0-59)  (0-23)     (1-31)    (1-12 or Jan-Dec)  (0-6 or Sun-Sat)
#print "Sunrise is at [hh,mm]:", getSunriseTime()
#print "Sunset is at [hh,mm]:", getSunsetTime()

sunriseTime = getSunriseTime()
sunsetTime = getSunsetTime()

#cd to correct folder
scriptFolder = '/home/camilo/Github/AutomaticBlinds/cronJobs/'

#Create clean cron job file from default file
CMD = 'cp ' + scriptFolder + 'defaultCron ' + scriptFolder + 'todaysCron'
subprocess.check_output(CMD, shell = True)

#Add cron job to run this script first thing in the morning
CMD = 'echo "5 0 * * * python /home/camilo/Github/AutomaticBlinds/cronJobs/createCronjob.py" >> ' + scriptFolder + 'todaysCron'
subprocess.check_output(CMD, shell = True)

#Get sunrise time and add cron job
CMD = 'echo "%i %i * * * echo Sun is rising" >> ' % (sunriseTime[1], sunriseTime[0]) + scriptFolder + """todaysCron"""
subprocess.check_output(CMD, shell = True)

#Get sunset time and add cron job
CMD = 'echo "%i %i * * * echo Sun is setting" >> ' % (sunsetTime[1], sunsetTime[0]) + scriptFolder + """todaysCron"""
subprocess.check_output(CMD, shell = True)

#Create cron job from new file and delete temp file
subprocess.check_output("crontab " + scriptFolder + "todaysCron", shell = True)
subprocess.check_output("rm " + scriptFolder + "todaysCron", shell = True)
