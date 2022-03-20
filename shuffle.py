import time
from adafruit_crickit import crickit
from adafruit_motor import stepper

print("Bi-Polar or Uni-Polar Stepper motor demo!")

# make stepper motor a variable to make code shorter to type!
stepper_motor = crickit.stepper_motor

while True:
    print("Double step")
    for i in range(20000):
        stepper_motor.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
    for i in range(20000):
        stepper_motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)