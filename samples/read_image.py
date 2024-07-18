## This is course material for Introduction to Python Scientific Programming
## Example code: read_image.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Please do <pip3 install matplotlib> and <pip3 install pillow> first
from matplotlib import image
from matplotlib import pyplot
import os

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
data = image.imread(filename)

# Display image information
print('Image type is: ', type(data))
print('Image shape is: ', data.shape)

# Add some color boundaries to modify an image array
plot_data = data.copy()
for width in range(512):
    for height in range(10):


# Write the modified images
image.imsave(path+'/'+'lenna-mod.jpg', plot_data)

# use pyplot to plot the image
pyplot.imshow(plot_data)
pyplot.show()