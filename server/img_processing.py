import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./floor_plan/test_img.png', 0)
# plt.imshow(img, cmap = 'gray')
# plt.show()
img[img == 255] = 1
plt.imshow(img, cmap = 'gray')
plt.show()


