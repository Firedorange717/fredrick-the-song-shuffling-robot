#!/usr/bin/env python3
import gpiozero
import time
from adafruit_crickit import crickit

print("1 Servo demo!")

while True:
	print("Moving servo #1")
	crickit.servo_1.angle = 0      # right