from PIL import Image
import numpy as np
from keras.datasets import fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print(train_images)[0]

image = np.array(Image.open('output.jpg'))

print(image.size)
print(image[0][0])

