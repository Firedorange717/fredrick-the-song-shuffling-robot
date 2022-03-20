# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Drive NeoPixels on the NeoPixels Block on Crickit FeatherWing
import time
from rainbowio import colorwheel
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel

num_pixels = 60  # Number of pixels driven from Crickit NeoPixel terminal

# The following line sets up a NeoPixel strip on Seesaw pin 20 for Feather
pixels = NeoPixel(crickit.seesaw, 20, num_pixels,pixel_order=RGBW)

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

RED = (255, 0, 0,0)
YELLOW = (255, 150, 0,0)
GREEN = (0, 255, 0,0)
CYAN = (0, 255, 255,0)
BLUE = (0, 0, 255,0)
PURPLE = (180, 0, 255,0)

while True:
    print("fill")
    pixels.fill(RED)
    pixels.show()
    # Increase or decrease to change the speed of the solid color change.
    time.sleep(1)
    pixels.fill(GREEN)
    pixels.show()
    time.sleep(1)
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(1)

    print("chase")
    color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    color_chase(YELLOW, 0.1)
    color_chase(GREEN, 0.1)
    color_chase(CYAN, 0.1)
    color_chase(BLUE, 0.1)
    color_chase(PURPLE, 0.1)

    print("rainbow")
    rainbow_cycle(0)  # Increase the number to slow down the rainbow

