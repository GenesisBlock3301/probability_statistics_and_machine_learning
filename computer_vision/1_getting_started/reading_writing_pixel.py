import os

import cv2
import matplotlib.pyplot as plt


def read_write_pixel():
    root = os.getcwd()
    image_path = os.path.join(root, 'img_5.png')
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # print(img_rgb.shape)
    img_rgb[100:120, 350:370] = (255, 0, 0)

    plt.figure()
    plt.imshow(img_rgb)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    read_write_pixel()

