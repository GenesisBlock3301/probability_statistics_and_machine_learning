import os

import cv2
import numpy as np
from matplotlib import pyplot as plt


def convolution_2d():
    root = os.getcwd()
    img_path = os.path.join(root, 'img_5.png')
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    n = 100
    kernel = np.ones((n, n), np.float32)/(n*n)
    img_filter =cv2.filter2D(img_rgb, -1, kernel)
    # print(img_filter)

    plt.figure()
    plt.subplot(2, 2, 1), plt.imshow(img_rgb), plt.title('Original')
    plt.subplot(2, 2, 2), plt.imshow(img_filter), plt.title('Filtered')
    plt.show()


if __name__ == '__main__':
    convolution_2d()