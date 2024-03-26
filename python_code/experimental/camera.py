import picamera

with picamera.PiCamera() as camera:
    camera.capture("output.jpg")

