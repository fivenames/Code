'''
Artificial Neural Networks is a mathematical model for Machine Learning, ispired by biological neural networks. 
It can model a mathematical function from inputs to outputs based on the structure and parameters of the network. Learning of its parameters is based on data.
For eg. The activation function mentioned in machine learning: h(x) = w0 + w1x1 + w2x2 is a simple neural network. It contains two input nodes (x1 and x2) and one output node.

In more complex problems, training a neural network to learn the underlying mathematical function requires a technique called Gradient Descent. It is an optimisation algorithm 
used to minimise the loss during training. The loss function mentioned in machine learning, measures how poorly the hypothesis function performs. 
To apply Gradient Descent, differentiate the loss function. This will find the rate of change of the loss with respect to the network's weights. 
If the gradient is negative, it means that at the current weight assignment, the loss is decreasing with increasing weight, and vice versa.
Updating the weights in the opposite direction of the gradient helps achieve minimal loss. If the gradient is positive, the weight is decreased, 
and if the gradient is negative, the weight is increased:

Start with a random choice of weights
Loop:
    Calculate the gradient based on all data points, direction that will lead to decreasing loss
    Update weight according to the gradient

Stochastic Gradient Descent is an alternative approach that calculates the gradient using only one data point at a time, which saves computational resources. 
However, this may result in less accurate gradient estimates. To strike a balance between accuracy and efficiency, Mini-Batch Gradient Descent can be used. 
It calculates the gradient using a small batch of data points, providing a compromise between stochastic and full-batch gradient descent.


'''