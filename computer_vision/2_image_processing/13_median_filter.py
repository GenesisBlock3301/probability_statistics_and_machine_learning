"""
Why need median filter?
1. Noise reduction
2. Edge preservation.
Find the median value of all kernel's/window value, then reduce noise overall situation.

"""
import os

import cv2
import numpy as np
from matplotlib import pyplot as plt


def median_filter(img_path):
    if img_path is None:
        raise Exception("Could not read image from image")

    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    noisy_img = img_rgb.copy()
    noise_probability = 0.05
    noise = np.random.rand(noisy_img.shape[0], noisy_img.shape[1])
    noisy_img[noise < noise_probability/2] = 0
    noisy_img[noise > 1 - noise_probability/2] = 255

    img_filter = cv2.medianBlur(noisy_img, 3)

    plt.figure()
    plt.subplot(2, 2, 1), plt.imshow(noisy_img), plt.title('Noisy Image')
    plt.subplot(2, 2, 2), plt.imshow(img_filter), plt.title('Filtered Image')

    plt.show()

if __name__ == '__main__':
    root = os.getcwd()
    img_path = os.path.join(root, 'noisy_image.png')
    median_filter(img_path)