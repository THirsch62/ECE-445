from image_classification_model import *
import servo_controller_subsystem
from utils import *

model_name = "trained_model"
image_path = "image.jpg"

def main(train_model = True, evaluate_model = False):
    # Mainly used for testing and initial stages
    if train_model or evaluate_model:
        image_classification_model.load_training_data_into_memory()
        if train_model:
            model = image_classification_model.train_and_save_model(model_name)
        else:
            model = image_classification_model.load_model(model_name)
        image_classification_model.evaluate_model()
    
    # Repeat forever
    while True:
        # Wait until button is pressed
        while not button():
            pass

        # Take picture
        take_picture(image_path)
        # Normalize picture
        image = normalize_image(image_path)
        # Pass picture into predict function
        prediction = image_classification_model.predict(image)
        # Pass output of predict function into servo-controller subsystem
        servo_controller_subsystem.main(prediction)

if __name__ == "__main__":
    main(train_model = False, evaluate_model = True)
