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

#Create clean cron job file from default file
subprocess.check_output("cp defaultCron todaysCron", shell = True)

#Add cron job to run this script first thing in the morning
subprocess.check_output("""echo "5 0 * * * python /home/camilo/Github/AutomaticBlinds/cronJobs/createCronjob.py" >> todaysCron""", shell = True)

#Get sunrise time and add cron job
cronCommand = """echo "%i %i * * * echo Sun is rising" >> todaysCron""" % (sunriseTime[1], sunriseTime[0])
subprocess.check_output(cronCommand, shell = True)

#Get sunset time and add cron job
cronCommand = """echo "%i %i * * * echo Sun is setting" >> todaysCron""" % (sunsetTime[1], sunsetTime[0])
subprocess.check_output(cronCommand, shell = True)

#Create cron job from new file and delete temp file
subprocess.check_output("crontab todaysCron", shell = True)
subprocess.check_output("rm todaysCron", shell = True)
