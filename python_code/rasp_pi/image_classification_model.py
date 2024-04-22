from keras.datasets import fashion_mnist
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.utils import to_categorical

from PIL import Image
from imutils import rotate

import numpy as np
import matplotlib.pyplot as plt
import picamera

def take_picture(file_path):
    with picamera.PiCamera() as camera:
        camera.capture(file_path)

# TODO
def normalize_image(image_path):
    image = Image.open(image_path)
    image = np.array(image)
    # isolate clothing item
    # resize image into 28x28
    return image

def rotate_image(image):
    output = []
    for i in range(len(image)):
        temp = []
        for j in range(len(image)):
            temp.append(image[j][i])
        output.append(temp)
    return output


class image_classification_model:
    working_set = (0, 1, 2)
        # Labels for fashion MNIST:
            # 0 T-shirt/top
            # 1 Trouser
            # 2 Pullover
            # 3 Dress
            # 4 Coat
            # 5 Sandal
            # 6 Shirt
            # 7 Sneaker
            # 8 Bag
            # 9 Ankle boot
    
    model = 0

    train_images, train_labels, test_images, test_labels = [], [], [], []

    def load_training_data_into_memory():
        # Load and preprocess the Fashion MNIST dataset
        (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

        # remove uneccessary training data
        remove_items = []
        for ind, train_label in enumerate(train_labels):
            if train_label not in image_classification_model.working_set:
                remove_items.insert(0, ind)
            elif train_label == 1:
                train_images[ind] = rotate(train_images[ind], angle=270)
        train_labels = np.delete(train_labels, remove_items, 0)
        train_images = np.delete(train_images, remove_items, 0)

        # remove unneccessary testing data
        remove_items = []
        for ind, test_label in enumerate(test_labels):
            if test_label not in image_classification_model.working_set:
                remove_items.insert(0, ind)
        test_labels = np.delete(test_labels, remove_items, 0)
        test_images = np.delete(test_images, remove_items, 0)
        
        print(set(train_labels), set(test_labels))

        # normalize data
        image_classification_model.train_images = train_images.reshape((train_images.shape[0], 28, 28, 1)).astype('float32') / 255
        image_classification_model.test_images = test_images.reshape((test_images.shape[0], 28, 28, 1)).astype('float32') / 255
        image_classification_model.train_labels = to_categorical(train_labels)
        image_classification_model.test_labels = to_categorical(test_labels)

    def train_and_save_model(model_name):
        # Define the CNN model
        model = Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            Flatten(),
            Dense(64, activation='relu'),
            Dense(3, activation='softmax')
        ])

        # Compile the model
        model.compile(optimizer='adam',
                    loss='categorical_crossentropy',
                    metrics=['accuracy'])

        # Train the model
        model.fit(image_classification_model.train_images, image_classification_model.train_labels, epochs=5, batch_size=64, verbose=1)

        # Save the model
        model.save(model_name)
        image_classification_model.model = model
        return model

    def evaluate_model():
        # Evaluate the model
        test_loss, test_acc = image_classification_model.model.evaluate(image_classification_model.test_images, image_classification_model.test_labels, verbose=0)
        print(test_loss, test_acc)

    def load_model(model_name):
        # Load the model
        model = load_model(model_name)
        image_classification_model.model = model
        return model
    
    def predict(image):
        convert = {
            0: "T-shirt/Top",
            1: "Trouser",
            2: "Pullover"
        }
        prediction = convert[image_classification_model.model.predict(image)]
        return prediction

