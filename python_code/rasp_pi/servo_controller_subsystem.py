from gpiozero import Servo
from threading import Thread
import time

FOLD_ANGLE = 120

class Servo_Custom(Servo):
    # angle should be between -90 and 90
    def set_angle(self, angle):
        self.value = angle / 90
    
    def offset_angle(self, angle):
        self.value += angle / 90

# TODO
# Add servo pins
# dictionary with panels as keys and corresponding servos as values
panel_servos = {
    1: (Servo_Custom(), Servo_Custom()),
    2: (Servo_Custom(), Servo_Custom()),
    3: (Servo_Custom(), Servo_Custom()),
    4: (Servo_Custom(), Servo_Custom()),
    5: (Servo_Custom(), Servo_Custom()),
    6: (Servo_Custom(), Servo_Custom()),
}

# TODO
# dictionary with folding patterns
folding_pattern = {
    "T-shirt/Top": [[]],
    "Trouser": [[]],
    "Pullover": [[]]
}

def fold_panel(panel):
    left, right = panel_servos[panel]
    # fold panel up and wait for servo to rotate
    left.offset_angle(-120)
    right.offset_angle(120)
    time.sleep(0.5)
    # restore panel to original position and wait for servo to rotate
    left.offset_angle(120)
    right.offset_angle(-120)
    time.sleep(0.5)

# TODO
def main(clothing_item):
    for panels in folding_pattern[clothing_item]:
        threads = []
        for panel in panels:
            thread = Thread(target=fold_panel, args=[panel])
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()