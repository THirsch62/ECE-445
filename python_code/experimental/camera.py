import picamera

output_name = input("File name: ")
with picamera.PiCamera() as camera:
    camera.capture(output_name + ".jpg")

