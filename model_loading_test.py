from keras.models import load_model
from keras.datasets import fashion_mnist
from keras.utils import to_categorical

model = load_model("trained_model")
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1)).astype('float32') / 255
test_labels = to_categorical(test_labels)

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=0)
print('Test accuracy:', test_acc)
