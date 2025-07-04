import os

import cv2
import numpy as np
from matplotlib import pyplot as plt


def pure_colors():
    zeros = np.zeros((100, 100), np.uint8)
    ones = np.ones((100, 100), np.uint8)
    print(zeros)
    b_img = cv2.merge((zeros, zeros, 255 * ones))
    g_img = cv2.merge((zeros, 255 * ones, zeros))
    r_img = cv2.merge((255 * ones, zeros, zeros))

    black_img = cv2.merge((zeros, zeros, zeros))
    white_img = cv2.merge((255 * ones, 255 * ones, 255 * ones))

    plt.figure()
    plt.subplot(231), plt.imshow(b_img), plt.title('Blue channel')
    plt.subplot(232), plt.imshow(g_img), plt.title('Green channel')
    plt.subplot(233), plt.imshow(r_img), plt.title('Red channel')
    plt.subplot(234), plt.imshow(black_img), plt.title('Black channel')
    plt.subplot(235), plt.imshow(white_img), plt.title('White channel')

    plt.show()

def bgr_channel_grayscale():
    root = os.getcwd()
    img_path = os.path.join(root, 'img_5.png')
    img = cv2.imread(img_path)
    b, g, r = cv2.split(img)
    plt.figure()
    plt.subplot(221), plt.imshow(b, cmap='gray'), plt.title('Blue channel')
    plt.subplot(222), plt.imshow(g, cmap='gray'), plt.title('Green channel')
    plt.subplot(223), plt.imshow(r, cmap='gray'), plt.title('Red channel')
    plt.show()



if __name__ == '__main__':
    pure_colors()
    # bgr_channel_grayscale()
