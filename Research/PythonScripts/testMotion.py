#testMotion

from scipy.misc.pilutil import imread
from pylab import imshow, gray

# 'flatten' creates a 2D array from a JPEG.
mask = imread('mask.jpg', flatten=True)
# quickly view the image
gray()