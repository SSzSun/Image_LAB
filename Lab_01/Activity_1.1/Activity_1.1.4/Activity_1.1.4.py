# import Lib
import cv2
import numpy as np
import math
import matplotlib.image as mping

from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from mpl_toolkits.mplot3d import Axes3D

# import Picture
img = mping.imread("Activity_1.1\Activity_1.1.4\girl.jpg") # Path Picture

r = 225.0 / img.shape[0]
dim = (int(img.shape[1] * r), 250)
# perform the resizing
img_re = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# perform color to gray
img_gray = cv2.cvtColor(img_re, cv2.COLOR_RGB2GRAY)

# create the x and y coordinate arrays
x, y = np.mgrid[0:img_gray.shape[0], 0:img_gray.shape[1]]

# create the figure
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, img_gray ,rstride=1, cstride=1, cmap=plt.cm.gray, linewidth=0)
ax.set_zlim(0,256)
ax.zaxis.set_major_locator(mdates.AutoDateLocator())
ax.zaxis.set_major_formatter('{x:.02f}')

# Show Picture
plt.show()

