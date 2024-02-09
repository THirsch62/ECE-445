import picamera

def take_picture(file_path):
    with picamera.PiCamera() as camera:
        camera.capture(file_path)
    

