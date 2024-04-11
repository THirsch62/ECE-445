import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN)

while True:
	button = GPIO.input(2)
	if button:
		print("button is on")
	else:
		print("button is off")

GPIO.cleanup()
