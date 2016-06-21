#!/usr/bin/env python

import subprocess
#from gpiozero import LED
from time import sleep

class stepperMotor:
	
	def __init__(self,enable, direction, step):
		#enablePin = LED(enable)
		#directionPin = LED(direction)
		#stepPin = LED(step)
		stepLocation = 0

		#enablePin.on() #Logic high disables motor
		#directionPin.on() #Default direction is forward
		#stepPin.off()

	def stepForward(self, steps, pause):
		with open('motorStepLocation','r') as motorLocation:
			for line in motorLocation:
				stepLocation = int(line.split(None, 1)[0])
		motorLocation.close()

		print stepLocation
		#stepPin.off()
		#enablePin.off() #Logic low enables motor
		#directionPin.on() #Choose forward direction

		for iStep in range (0, steps):
			#stepPin.on()
			#sleep(pause)
			#stepPin.off()
			#sleep(pause)
			stepLocation = stepLocation + 1

		#enablePin.on() #Logic high disables motor
		subprocess.check_output("mv motorStepLocation motorStepLocation.old", shell = True)
		subprocess.check_output("echo %i >> motorStepLocation" %stepLocation, shell = True)



if __name__ == "__main__":
	myMotor = stepperMotor(1,2,3)
	myMotor.stepForward(10,0.1)
