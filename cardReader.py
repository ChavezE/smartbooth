#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import time

reader = SimpleMFRC522.SimpleMFRC522()

def scanForRDIF():
	try:
		_, RFID = reader.read()

	finally:
		GPIO.cleanup()
		
		return RFID

