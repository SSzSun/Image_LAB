# import required libraries
import cv2
import numpy as np
import math
import matplotlib.image as mping

from matplotlib import pyplot as plt

# read input image
img = mping.imread("Activity_1.1\Activity_1.1.2\girl.jpg") # Path Picture
X = np.array(img)
W = np.transpose(X)
Y = X.reshape((189600))
K = np.moveaxis(X,2,0)
# K = np.swapaxes(img,0,-2)

print("Initial Shape:",img.shape)
# print("New Shape transpose:",W.shape)
print("New Shape reshape:",Y.shape)
# print("New Shape moveaxis:",K.shape)

fig = plt.figure(figsize=(6,6))
plt.subplot(2,3,1);plt.imshow(img[:,:,0],cmap='gray');plt.title("R_original")
plt.subplot(2,3,2);plt.imshow(W[0,:,:],cmap='gray');plt.title("R_Transpose")
# plt.subplot(2,3,3);plt.imshow(Y[0,:,:],cmap='gray');plt.title("R_reshape")
# plt.subplot(2,3,4);plt.imshow(img[0,:,:],cmap='gray');plt.title("R_Manual swap")
# plt.subplot(2,3,5);plt.imshow(K[0,:,:],cmap='gray');plt.title("R_moveaxis")
# plt.subplot(2,3,6);plt.imshow(K[0,:,:],cmap='gray');plt.title("R_swapaxes")
# display the image
# plt.show()
