#!/usr/bin/env python3

import time
from adafruit_crickit import crickit

print("1 Servo demo!")
angle = 0;

while True:
	print("Moving servo #1")
	crickit.servo_1.angle = angle
	time.sleep(1)
	angle += 1
	
	if angle == 180:
		angle = 0
		time.sleep(1)