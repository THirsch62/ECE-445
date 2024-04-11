import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

left = GPIO.PWM(2, 50)
right = GPIO.PWM(3, 50)


left.start(2)
right.start(12)

GPIO.output(4, 1)


ROTATION = 7

left.ChangeDutyCycle(2 + ROTATION)
time.sleep(2)
left.ChangeDutyCycle(2)


time.sleep(5)

GPIO.output(4, 0)

left.stop()
right.stop()
GPIO.cleanup()
