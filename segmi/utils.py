import os
import numpy as np
import random
import tensorflow as tf
import matplotlib.pyplot as plt
from segmi.unet_model import unet3d


def set_seed(SEED):
    """ Set the seed for reproducibility.

    Args:
        SEED (int): The seed to use.
    """
    os.environ['PYTHONHASHSEED'] = str(SEED)
    np.random.seed(SEED)
    random.seed(SEED)
    tf.random.set_seed(SEED)


def load_volume(path):
    """ Load a volume from a numpy file.

    Args:
        path (str): The path to the numpy file.

    Returns:
        numpy.ndarray: Numpy array of the volume.
    """
    return np.load(path).astype("float32")


def load_model():
    """ Load the model.

    Returns:
        Tensorflow Model: The model.
    """
    return unet3d(128, 128, 128, 3, 4)


def predict(model, volume):
    """ Predict the volume.

    Args:
        model (Model): UNet3D model.
        volume (numpy.ndarray): The volume to predict.

    Returns:
        numpy.ndarray: The predicted volume of shape (128, 128, 128, 4).
    """
    prediction = model.predict(np.expand_dims(volume, axis=0))
    return prediction[0]


def argmax_output(output, slice_num=64):
    """ Convert the output to rgb.

    Args:
        output (numpy.ndarray): The output of shape (128, 128, 128, 4).
        slice_num (int, optional): slice to be cut from the volume . Defaults to 64.

    Returns:
        numpy.ndarray: Ouput of shape (128, 128) i.e. slice_num'th slice of argmax output.
    """
    output_slice = np.argmax(output, axis=3)[:, :, slice_num]
    return output_slice


def plot_save_slice(input, output_slice, path="test.png", slice_num=64, plot=True):
    """ Plot and save a slice of the volume.

    Args:
        input (numpy.ndarray): The input of shape (128, 128, 128, 4).
        output_slice (numpy.ndarray): The output_slice of shape (128, 128).
        path (str, optional): Path to save the figure. Defaults to "test.png".
        slice_num (int, optional): _description_. Defaults to 64.
        plot (bool, optional): Whether or not plot. Defaults to True.
    """
    plt.subplot(1, 2, 1)
    plt.imshow(input[:, :, slice_num, 0], cmap='gray', interpolation='none')
    plt.title("Original MRI")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(input[:, :, slice_num, 0], cmap='gray', interpolation='none')
    plt.imshow(output_slice, cmap='jet', alpha=0.5, interpolation='none')
    plt.title("Segmented MRI")
    plt.axis("off")

    plt.savefig(path)
    if plot == True:
        plt.show()
