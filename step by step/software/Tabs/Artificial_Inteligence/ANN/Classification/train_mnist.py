import numpy as np
import matplotlib.pyplot as plt
from lib.load_mnist import load_mnist
import keras

x_train, x_test, y_train, y_test = load_mnist('mnist_data/')




plt.imshow(x_train[12])
plt.show()
