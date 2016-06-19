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

subprocess.check_output("cp defaultCron todaysCron", shell = True)
cronCommand = """echo "%i %i * * * echo Sun is rising" >> todaysCron""" % (sunriseTime[1], sunriseTime[0])
print cronCommand 
subprocess.check_output(cronCommand, shell = True)

cronCommand = """echo "%i %i * * * echo Sun is setting" >> todaysCron""" % (sunsetTime[1], sunsetTime[0])
print cronCommand
subprocess.check_output(cronCommand, shell = True)

subprocess.check_output("crontab todaysCron", shell = True)
subprocess.check_output("rm todaysCron", shell = True)
