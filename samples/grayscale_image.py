## This is course material for Introduction to Python Scientific Programming
## Example code: grayscale_image.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Please do <pip3 install matplotlib> and <pip3 install pillow> first
from matplotlib import image
from matplotlib import pyplot
import numpy as np
import os

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
data = image.imread(filename)

# Display image information
print('Image type is: ', type(data))
print('Image shape is: ', data.shape)

# Add some color boundaries to modify an image array
plot_data = np.ndarray([512,512])
for width in range(512):
    for height in range(512):
        # Convert (R, G, B) to Grayscale per pixel
        R = data[height,width,0]    # data[height, width, :] = [R, G, B]
        G = data[height,width,1]
        B = data[height,width,2]
        plot_data[height][width] = int(0.3*R + 0.59*G + 0.11*B)

# use pyplot to plot the image
pyplot.imshow(plot_data, cmap = 'gray', vmin = 0, vmax = 255)
pyplot.show()