# import required libraries
import numpy as np
import cv2
import matplotlib.image as mping

from matplotlib import pyplot as plt

# read input image
img = mping.imread("Activity_1.1\Activity_1.1.3\girl.jpg") # Path Picture
img_g = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# convert to np.float32
z = np.float32(img_g).reshape((-1,2))
print(z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret,label,center=cv2.kmeans(z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img_g.shape))

plt.subplot(1,2,1);plt.imshow(img_g, cmap='gray');plt.title("Original")
plt.subplot(1,2,2);plt.imshow(res2, cmap='gray');plt.title("Reduce")
# display the image
plt.show()
