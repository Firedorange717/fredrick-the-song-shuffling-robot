#!/usr/bin/env python3

import time
from adafruit_crickit import crickit

angle = 0;

while True:
		crickit.servo_1.angle = 180
		crickit.servo_2.angle = 180
		crickit.servo_3.angle = 180
		time.sleep(3)
		crickit.servo_1.angle = 90
		crickit.servo_2.angle = 90
		crickit.servo_3.angle = 90
		time.sleep(3)
		crickit.servo_1.angle = 0
		crickit.servo_2.angle = 0
		crickit.servo_3.angle = 0
		time.sleep(3)
		