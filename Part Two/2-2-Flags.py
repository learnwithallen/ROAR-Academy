from matplotlib import image
from matplotlib import pyplot
import os

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
wales_flag = path + '/' + 'wales-flag-xs.jpg'
lenna = path + '/' + 'lenna.bmp'
bottom = image.imread(lenna)
top = image.imread(wales_flag)
# Display image information



# Add some color boundaries to modify an image array
edited = bottom.copy()
for width in range(top.shape[1]):
    for height in range(top.shape[0]):
        edited[height][512-250+width] = [
            (top[height][width][0]),
            (top[height][width][1]),
            (top[height][width][2]),
        ]
image.imsave(path+'/'+'lenna_with_dragon.jpg', edited)
pyplot.imshow(edited)
