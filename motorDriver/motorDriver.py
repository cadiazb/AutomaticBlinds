#!/usr/bin/env python

import subprocess
from gpiozero import LED
from time import sleep

def stepperMotor(enable, direction, step):
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

		#stepPin.off()
		#enablePin.off() #Logic low enables motor
		#directionPin.on() #Choose forward direction

		for iStep in range (0 to steps):
			#stepPin.on()
			#sleep(pause)
			#stepPin.off()
			#sleep(pause)
			#stepLocation = stepLocation + 1

		#enablePin.on() #Logic high disables motor
