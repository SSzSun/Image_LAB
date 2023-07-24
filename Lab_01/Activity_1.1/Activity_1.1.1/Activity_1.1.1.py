# import Lib
import cv2
import numpy as np
import math
import matplotlib.image as mping

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# import Picture
img = mping.imread("Activity_1.1\Activity_1.1.1\\fish.jpg") # Path Picture
# print(repr(img)) # Print Arry Picture
# print(img.shape)

# Convert Color
BGR = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
xB = BGR[:,:,0]
xG = BGR[:,:,1]
xR = BGR[:,:,2]

yR = img[:,:,0]
yG = img[:,:,1]
yB = img[:,:,2]

# Config Show Picture
# Line 1
plt.subplot(2,4,1);plt.imshow(BGR);plt.title("BGR")
plt.subplot(2,4,2);plt.imshow(xB, cmap='gray');plt.title("B")
plt.subplot(2,4,3);plt.imshow(xG, cmap='gray');plt.title("G")
plt.subplot(2,4,4);plt.imshow(xR, cmap='gray');plt.title("R")

# Line 2
plt.subplot(2,4,5);plt.imshow(img);plt.title("RGB")
plt.subplot(2,4,6);plt.imshow(yR, cmap='gray');plt.title("R")
plt.subplot(2,4,7);plt.imshow(yG, cmap='gray');plt.title("G")
plt.subplot(2,4,8);plt.imshow(yB, cmap='gray');plt.title("B")

# Show Picture
plt.show()