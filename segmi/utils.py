import os
import numpy as np
import random
import tensorflow as tf
import matplotlib.pyplot as plt
from unet_model import unet3d


def set_seed(SEED):
    os.environ['PYTHONHASHSEED'] = str(SEED)
    np.random.seed(SEED)
    random.seed(SEED)
    tf.random.set_seed(SEED)


def load_volume(path):
    return np.load(path).astype("float32")


def load_model():
    return unet3d(128, 128, 128, 3, 4)


def predict(model, volume):
    prediction = model.predict(np.expand_dims(volume, axis=0))
    return prediction[0]


def rgb_output(output, path, slice_num=64):
    output_slice = np.argmax(output, axis=3)[:, :, slice_num]
    return output_slice


def plot_save_slice(input, output, path="test.png", slice_num=64, plot=True):
    plt.subplot(1, 2, 1)
    plt.imshow(input[:, :, slice_num, 0], cmap='gray', interpolation='none')
    plt.title("Original MRI")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(input[:, :, slice_num, 0], cmap='gray', interpolation='none')
    plt.imshow(output, cmap='jet', alpha=0.5, interpolation='none')
    plt.title("Segmented MRI")
    plt.axis("off")

    plt.savefig(path)
    if plot == True:
        plt.show()
