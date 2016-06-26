#!/usr/bin/env python

import subprocess
from gpiozero import LED
from time import sleep

class stepperMotor:
	
	def __init__(self,enable, direction, step):
		self.enablePin = LED(enable)
		self.directionPin = LED(direction)
		self.stepPin = LED(step)
		self.stepLocation = 0

		self.enablePin.on() #Logic high disables motor
		self.directionPin.on() #Default direction is forward
		self.stepPin.off()

	def rotate(self, steps, pause):
		with open('motorStepLocation','r') as motorLocation:
			for line in motorLocation:
				self.stepLocation = int(line.split(None, 1)[0])
		motorLocation.close()

		print self.stepLocation
		self.stepPin.off()
		self.enablePin.off() #Logic low enables motor
		if (steps > 0):
			self.directionPin.on() #Choose forward direction
			tmpForward = 1
		else:
			self.directionPin.off() #Choose reverse direction
			tmpForward = -1

		for iStep in range (0, abs(steps)):
			self.stepPin.on()
			sleep(pause)
			self.stepPin.off()
			sleep(pause)
			self.stepLocation = self.stepLocation + tmpForward

		self.enablePin.on() #Logic high disables motor
		print self.stepLocation
		subprocess.check_output("mv motorStepLocation motorStepLocation.old", shell = True)
		subprocess.check_output("echo %i >> motorStepLocation" %self.stepLocation, shell = True)
	
	def gotToOrigin(self):
		with open('motorStepLocation','r') as motorLocation:
                        for line in motorLocation:
                                self.stepLocation = int(line.split(None, 1)[0])
                motorLocation.close()

		self.rotate(-self.stepLocation, 0.01)

	def getPosition(self):
                with open('motorStepLocation','r') as motorLocation:
                        for line in motorLocation:
                                self.stepLocation = int(line.split(None, 1)[0])
                motorLocation.close()

                print self.stepLocation
		return self.stepLocation

if __name__ == "__main__":
	myMotor = stepperMotor(25,23,24)
	#myMotor.rotate(-500,0.025)
	#print "Motor position is:"
	sleep(1)
	#myMotor.getPosition()
	#myMotor.gotToOrigin()
	myMotor.rotate(1000,0.04)
