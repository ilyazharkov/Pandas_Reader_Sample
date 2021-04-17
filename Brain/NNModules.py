from keras import models
from keras import layers
from keras.utils import to_categorical
from keras.datasets import mnist
from enum import Enum
import zope.interface
from zope.interface import implementer


class ENNObjects(Enum):
    TextAnalyzer = 1
    ImageAnalyzer = 2
    PriceAnalyzer = 3


class INNNetwork(zope.interface.Interface):
    def GetData(self):
        pass

    def Teach(self):
        pass

    def Test(self):
        pass


@implementer(INNNetwork)
class ImageNetwork:

    def __init__(self):
        self.network = None
        self.train_images = []
        self.test_images = []
        self.train_labels = []
        self.test_labels = []

    def GetData(self):
        (self.train_images, self.train_labels), (self.test_images, self.test_labels) = mnist.load_data()
        self.train_images = self.train_images.reshape((60000, 28 * 28))
        self.train_images = self.train_images.astype('float32') / 255
        self.test_images = self.test_images.reshape((10000, 28 * 28))
        self.test_images = self.test_images.astype('float32') / 255
        self.train_labels = to_categorical(self.train_labels)
        self.test_labels = to_categorical(self.test_labels)

    def Teach(self):
        self.network = models.Sequential()
        self.network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
        self.network.add(layers.Dense(10, activation='softmax'))
        self.network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
        self.network.fit(self.train_images, self.train_labels, epochs=5, batch_size=128)
        self.network.compile()

    def Test(self):
        results = self.network.predict(self.test_images)
        return results
