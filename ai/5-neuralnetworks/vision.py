'''
For image recognision, the input data can be the RGB values for each of the pixels. However, this input does not tell the structure and shape of the object in the image.
To better the efficiency of the DNN, a technique call Image Convolution can be used. It is the method of applying a filter that adds each pixel value of an image
to its neighbours, weighted according to a Kernal matrix. Recall from CS50 filter problem set, this technique can be used to find the egdes of the image.

Another possible problem might be the scale of the image is too large. A technique named Pooling can be used in this case. It involves reducing the size of an input by sampling
from regions in the input. A popular type of Pooling is the Max-Pooling, which carries out pooling by choosing the maximum value in each region. For eg. picking pixels with the 
highest RGB values of every 2 x 2 region.

A Convolutional Neural Network(CNN) is a ANN that uses convolution, usually for analysing images.
'''