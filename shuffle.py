import time
from adafruit_crickit import crickit
from adafruit_motor import stepper

print("Bi-Polar or Uni-Polar Stepper motor demo!")

# make stepper motor a variable to make code shorter to type!
stepper_motor = crickit.stepper_motor
# increase to slow down, decrease to speed up!
INTERSTEP_DELAY = 0.0001

while True:
    print("Double step")
    for i in range(40000):
        stepper_motor.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)