# Grayscale image = 0.299R + 0.587G + 0.114B
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


def grayscale_image():
    root = os.getcwd()
    img = cv2.imread(os.path.join(root, 'img_5.png'))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plt.figure()
    plt.subplot(2, 2, 1), plt.imshow(img), plt.title('original')
    plt.subplot(2, 2, 2), plt.imshow(img_gray), plt.title('grayscale')
    plt.show()




if __name__ == '__main__':
    grayscale_image()
