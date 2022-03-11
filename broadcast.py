from array import array
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import cv2


def norm_square_list(vector):
    norm = 0
    for v in vector:
        norm += v * v

    return norm


def norm_square_list_comprehension(vector):
    return sum([v * v for v in vector])


def norm_square_array(vector):
    norm = 0
    for v in vector:
        norm += v * v
    return norm


def norm_square_numpy(vector):
    return np.sum(vector * vector)


def norm_square_numpy_dot(vector):
    return np.dot(vector, vector)


image1 = cv2.imread("files/dog-01.png")
image1 = cv2.resize(image1, (100, 100)).astype(np.int32)
image2 = cv2.imread("files/dog-02.png")
image2 = cv2.resize(image2, (100, 100)).astype(np.int32)


# Define the function that implements the loop version
def l2_loop(image1, image2):
    height, width, channels = image1.shape
    distance = 0

    for h in range(height):
        for w in range(width):
            for c in range(channels):
                distance += (image1[h][w][c] - image2[h][w][c]) ** 2


# Define the vectorised version
def l2_vectorise(image1, image2):
    return ((image1 - image2) ** 2).sum()


if __name__ == '__main__':
    l2_loop(image1, image2)
    l2_vectorise(image1, image2)