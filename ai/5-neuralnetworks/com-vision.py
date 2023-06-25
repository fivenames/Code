'''
In image recognition tasks, using the raw RGB pixel values as input may not effectively capture the structure and shape of objects in the image. To improve the efficiency of DNNs 
for image analysis, a technique call Image Convolution can be used. It is the method of applying a filter that adds each pixel value of an image to its neighbours,
weighted according to a Kernal matrix. Recall from CS50 filter problem set, the filter weights are used to emphasise edges.
This process extracts relevant information and helps the network focus on important visual characteristics. 

Another possible problem faced during image analysis is the resolution of the image. Images with a high number of pixels will produce many input nodes, which will
increase computational resource consumption. A technique named Pooling can be used to reduce the resolution of the image. It involves reducing the size of an input by sampling
from regions in the input. A popular type of Pooling is the Max-Pooling, which carries out pooling by choosing the maximum value in each region. 
By dividing the input into regions, such as 2x2 windows, and selecting the maximum value within each region, this downsampling process 
reduces the spatial resolution of the input while retaining the most prominent information.

A Convolutional Neural Network(CNN) is a ANN that uses convolution, usually for analysing images.
'''