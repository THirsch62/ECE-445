import RPi.GPIO as GPIO

BUTTON = 17

DIODE = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(DIODE, GPIO.OUT)

GPIO.output(DIODE, 0)

while True:
	button = GPIO.input(BUTTON)
	if button:
		GPIO.output(DIODE, 1)
	else:
		GPIO.output(DIODE, 0)

GPIO.cleanup()
