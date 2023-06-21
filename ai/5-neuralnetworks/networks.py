'''
Artificial Neural Networks(ANN) is a mathematical model for Machine Learning, ispired by biological neural networks. 
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


'''
ANN can have multiple output nodes, each with a different set of weights and is connected to all the input nodes. These weights, combined with an activation function, can be used to 
determine the probabilities associated with each output node. This enables ANN to handle multi-class classification problems, going beyond just binary classification.

In reinforcement learning, ANN can be utilised by mapping the input nodes to the current state information, and the output nodes to the available actions the agent can take.

ANN is a versatile structure applicable to various learning problems. Gradient Descent can be employed to optimize the mathematical function represented by an ANN. 
When dealing with ANN that has multiple output nodes, each output node can be treated as a separate ANN, and the Gradient Descent process can be applied to each output node, 
similar to how it is done for an ANN with a single output node.
'''


'''
Multilayer Neural Network (MLNN) is an ANN with an input layer, an ouput layer and at least one hidden layer in between.
This architecture allows for the modeling of non-linear mathematical functions. In contrast, a neural network without hidden layers can only represent linear functions 
because the inputs are combined linearly (e.g., w0 + w1x1 + w2x2 + ...). However, real-world problems often require the modeling of non-linear relationships.

By passing the inputs through multiple hidden layers, each layer calculates its own output based on its input and passes it to the next layer. 
This ability to learn hierarchical representations is particularly valuable in classification problems. Each hidden node can learn to identify specific patterns or features, 
and subsequent layers or the output layer can combine these learned features to produce a more accurate decision boundary or classification.

Notice that the hidden intermediate layers the values in the hidden layers do not have a direct interpretation or use for calculating the error or loss. 
Backpropagation starts from the output layer and propagates the error backwards through the network, attributing the contribution of each node in the previous layer 
based on their assigned weights. This process allows the network to adjust the weights iteratively to minimize the overall error and improve the model's performance.

To run Gradient Descent with Backpropagation:
    Start with random choice of weights
    Loop:
        Calculate the loss for the output
        For each hidden layer from output layer backwards:
            Propagate the error back one layer
            Update the weights

Deep Learning refers to the use of Deep Neural Networks, which are ANN with multiple layers of hidden nodes, to solve predictions, and backpropagation is crucial in training DNNs.
'''


'''
To prevent Overfitting in DNN training, a technique call Dropout can be used. It temporarily remove units(selected as random) from a ANN to prevent over-reliance on certain units.
Essentially, during each iteration of the training algorithm, a percentage of randomly selected nodes from across the whole ANN is neglected,
simulating the nodes not receiving any inputs and producing any outputs. Dropout introduces a form of regularisation during training, it encourages the network to become more robust 
and prevents over-reliance on individual units or co-adaptation among units, and therefore generalise new datasets more accurately.
'''