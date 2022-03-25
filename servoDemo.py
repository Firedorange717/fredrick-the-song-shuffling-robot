#!/usr/bin/env python3

import time
from adafruit_crickit import crickit

angle = 0;

while True:
	crickit.servo_1.angle = angle
	crickit.servo_2.angle = angle
	angle += 1
	print(angle)
	
	if angle == 180:
		angle = 0
		crickit.servo_1.angle = 90
		crickit.servo_2.angle = 90
		time.sleep(3)
		