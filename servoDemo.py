#!/usr/bin/env python3

import time
from adafruit_crickit import crickit

print("1 Servo demo!")
angle = 0;

while True:
	crickit.servo_1.angle = angle
	time.sleep(.001)
	angle += 1
	print(angle)
	
	if angle == 180:
		angle = 0
		time.sleep(.001)
		crickit.servo_1.angle = 90
		time.sleep(3)
		