#!/usr/bin/env python

import sys
import subprocess, math

def getSunriseTime():
	sunwait_resp = subprocess.check_output("/home/camilo/Github/AutomaticBlinds/sunwait-20041208/sunwait -v sun up 00:00:00 37.8657N, 122.2863W", shell = True)
	index = sunwait_resp.index('Up')
	sunriseTime =  math.modf(float(sunwait_resp[(index+3):(index+9)]))
	sunriseTime = [int(sunriseTime[1]), int(sunriseTime[0]*60)]
	return sunriseTime

def getSunsetTime():
        sunwait_resp = subprocess.check_output("/home/camilo/Github/AutomaticBlinds/sunwait-20041208/sunwait -v sun down 00:00:00 37.8657N, 122.2863W", shell = True)
        index = sunwait_resp.index('Down')
        sunsetTime =  math.modf(float(sunwait_resp[(index+5):(index+11)]))
        sunsetTime = [int(sunsetTime[1]), int(sunsetTime[0]*60)]
        return sunsetTime
