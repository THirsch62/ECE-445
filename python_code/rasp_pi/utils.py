import RPi.GPIO as GPIO
import time

BUTTON = 17

SERVO1 = 2
SERVO2 = 3
SERVO3 = 4
SERVO4 = 14
SERVO5 = 15
SERVO6 = 18
DIODE  = 27

ROTATION = 7    # x18 degrees

panels = {}

def setup_board():
    GPIO.setmode(GPIO.BCM)

    # Inputs
    GPIO.setup(BUTTON, GPIO.IN)

    # Output
    GPIO.setup(SERVO1, GPIO.OUT)
    GPIO.setup(SERVO2, GPIO.OUT)
    GPIO.setup(SERVO3, GPIO.OUT)
    GPIO.setup(SERVO4, GPIO.OUT)
    GPIO.setup(SERVO5, GPIO.OUT)
    GPIO.setup(SERVO6, GPIO.OUT)
    GPIO.setup(DIODE, GPIO.OUT)

    # Initialize dictionary
    panels[1] = GPIO.PWM(SERVO1, 50)
    panels[2] = GPIO.PWM(SERVO2, 50)
    panels[3] = GPIO.PWM(SERVO3, 50)
    panels[4] = GPIO.PWM(SERVO4, 50)
    panels[5] = GPIO.PWM(SERVO5, 50)
    panels[6] = GPIO.PWM(SERVO6, 50)

    # Set servo positions
    panels[1].start(2)
    panels[2].start(2)
    panels[3].start(2)
    panels[4].start(2)
    panels[5].start(2)
    panels[6].start(2)

    # Set DIODE Low
    GPIO.output(DIODE, 0)

def turn_diode_on():
    GPIO.output(DIODE, 1)

def turn_diode_off():
    GPIO.output(DIODE, 0)


def button():
    return GPIO.input(BUTTON)

def fold(panel):
    panels[panel].ChangeDutyCycle(2 + ROTATION)
    time.sleep(2)
    panels[panel].ChangeDutyCycle(2)
    time.sleep(1)