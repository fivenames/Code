'''
Machine Learning(ML) - the computer learns patterns or relationships from the provided data without explicit instructions.
'''


'''
Supervised Learning - A type of ML which learns from a labeled dataset, contains input-output pairs, a model that can accurately map input data to corresponding output labels.

Classification - a type of supervised learning task where the computer learns a function to assign discrete categories to input data. For eg. classifying emails as spam or not spam.
One algorithm used for classification is nearest-neighbor classification. It assigns a class label to an input point based on the class of the nearest data point in the dataset. 
However, this approach has a limitation as it only considers the closest neighbor. To overcome the limitation, the k-nearest neighbor classification algorithm can be used. 
Instead of considering only the closest neighbor, it consider all k nearest data points. The algorithm chooses the most common class among those k nearest neighbors 
to determine the class label for the input point.

Classes or categories can often be separated by an imaginary boundary. This boundary divides the dataset, with most instances of Class X on one side and Class Y on the other.
To determine which side an input point falls into, a hypothesis function, denoted as h(), is defined. This function can be modeled as a linear equation of input variables, 
with coefficients known as weights, indicating their impact on the classification. The output of the hypothesis function, either positive or negative, 
determines the side of the boundary the input point belongs to. h(x1, x2), can be represented as h(x) = w0 + w1x1 + w2x2, where w0 accounts for the translation of the boundary. 
A weight vector, w, holds all the weights of the hypothesis function, while an input vector, x, contains the input data. The lengths of w and x are equal, and 
the hypothesis function can be expressed as the dot product of w and x, denoted as h(x) = w • x. Considering the dot product involves vectors, x is typically augmented 
with a value of 1 as the first element, accounting for the weight w0. Formally, the hypothesis function is written as h(x) = 1 if w • x >= 0, otherwise 0.
'''
'''
Perceptron Learning Rule - a learning rule is a method to update the weights based on individual data points (x, y), where x represents the input point and 
y is the corresponding output. The update rule for each weight is: w = w + k(y - h(x)) * x. Here, w is the original weight, and it is updated by adding a fraction, k, 
of the difference between the actual value, y, and the estimated value, h(x). If the actual value is higher, the weight is updated with a higher value, and vice versa.

One limitation of this method is that it provides a binary output, classifying instances as either Class X or Class Y. If an input point lies close to the boundary, 
the result does not indicate uncertainty. This type of boundary is known as a hard threshold. In contrast, a soft threshold outputs a real number between the two possible values, 
providing an indication of the confidence or certainty of the result.

In scenarios where there are multiple possible boundaries, especially if classes are concentrated and separated far apart, a Maximum Margin Separator can be used to determine 
the best-fit boundary. A Maximum Margin Separator is a boundary that maximises the distance between any of the data points. It aims to find the largest margin or gap between classes, 
which helps in achieving better generalisation to new data. Support Vector Machines (SVMs) are a popular algorithm used to implement the Maximum Margin Separator. 
SVMs determine the optimal boundary by identifying support vectors, which are data points located closest to the decision boundary. 
SVMs can utilise a kernel function to map the original input data into a higher-dimensional space through a process known as the kernel trick,
if the data points are not linearly separable(for eg. class Y surrounding class X as an outer circle)
'''


'''
Regression - a type of supervised learning task where the computer learns a function to map an input point to a continuous value. 
for eg. predicting the revenue of a company based on its advertising spent. This time, the hypothesis function produces a line that approximates the relationship between data points.
'''


'''
Evaluating hypothesis functions involves using a loss function, which measures how poorly the hypothesis function performs. The loss function quantifies the accumulated errors or 
inaccuracies in the predictions made by the hypothesis function. Evaluate the performance of different hypothesis functions by comparing their loss values.

One variant of the loss function is the L1 loss function. The L1 loss considers the difference between the actual value and the predicted value: 
L1(actual, predicted) = | actual - predicted |. This loss function is especially useful in regression as it captures the magnitude of the inaccuracies.
Another variant is the L2 loss function, which penalises inaccurate predictions heavily by taking the squared difference between the actual value and the predicted value: 
L2(actual, predicted) = (actual - predicted)^2.

Overfitting is a common problem that occurs when a model that fits too closely to a particular data set and therefore may fail to generalise to future data.
For eg. in classification problems, overfitting may manifest as irregular decision boundaries, while in regression problems, it can be seen as irregular lines or curves. 
Although an overfitting hypothesis may represent the training data well, it fails to generalise to new data effectively.

To address overfitting, regularisation techniques can be employed. One approach involves incorporating the complexity of the hypothesis into the loss function: 
loss(h) = L + k * complexity(h), where h represents the hypothesis function and k determines the weighting given to the complexity term.
Regularisation favors simpler and general hypotheses, by penalising complexity.

Another approach is the Holdout Cross-Validation method, which splits data into a training set and a testing set, such that learning happens on the training set and hypothesis
is evaluated on the testing set. This method helps assess the generalisation ability of the hypothesis. However, it does not fully utilise the data for training, which can limit 
the optimality of the hypothesis. To make more efficient use of the data, the k-fold Cross-Validation method can be employed.  the data is divided into k subsets or folds. 
The model is trained and evaluated k times, each time using a different fold as the testing set and the remaining folds as the training set. 
This results in k different hypotheses. The final evaluation can be done by averaging the results of all k hypotheses or selecting the best-performing hypothesis.
'''


'''
Reinforcement Learning - a type of ML that train an Agent to make a sequence of actions in an Environment based on a system of rewards or punishments(in a form of numerical values).
Agent - an AI programme, or a physical Robot(which often adopts this type of ML to learn how to perform a specific task.)
Environment - the context in which the Agent operates and provides feedback to the Agent in the form of reward/punishment. Agent's will try to maximise the cumulative reward over time.
The Agent is first being placed in an initial state within the Environment. The Agent selects an action to perform based on the current state. After taking the action, 
the Environment transitions to a new state, and the Agent receives a reward/punishment based on the outcome of its action.

Markov Decision Process(MDP) - a mathematical model for decision-making in the field of reinforcement learning. It represents a system of states, actions, and the associated rewards.
Recall a Markov Chain, a sequence of nodes representing states, and each node has a probability distribution that determines the likelihood of transitioning to subsequent states.
In an MDP, it extend on the Markov Chain concept to include actions and rewards. Each node or state in an MDP can lead to multiple chains of nodes, representing different possible 
actions the Agent can take. The arrows connecting the nodes represent these actions, and each action is associated with a probability distribution that determines the likelihood 
of transitioning to the subsequent states. In addition to that, MDP assigns a reward to every specific action taken by the Agent. The components of the MDP are: 
A set of States.
A set of Actions.
A transition model: P( newState | currState ∧ actionA ) - the probabilities of transitioning to a new state (newState) given the current state (currState) and the action (actionA) 
taken by the agent. It handles situations where the Environment is non-deterministic, meaning that the outcome state of an action is uncertain.
A Reward Function: R(currState, actionA, newState), returns the reward of the action (actionA) taken which resulted the transition to the state (newState).
'''
'''
Q-Learning is a method in Reinforcement Learning the agent learns a function, Q(s, a), that estimates the reward of taking an action, a, in a given state, s. 

Start by initialising Q(s, a) = 0 all possible states and actions
When Agent took an action and received a feedback:
    Estimates the value Q(s, a) based on current reward and expected future rewards that can be achieved. 
    
    Update Q(s, a) with the new estimate but taking into account of the old estimate, Q(s, a) = Q(s, a) + α(new estimate - old estimate).
    Here, α is the learning rate, which represents how much new information is valued over the old information. A value of α = 1 indicates that the new estimate completely replaces 
    the old estimate. old estimate == Q(s, a), and new estimate == currentReward + γ * future reward estimate, where γ is the discount factor, which represents how much future reward 
    is valued(works similar to α). future reward estmate == max( for all possible Q(s', a'), where s' and a' represent all the possible future actions and states )

A Greedy Decision-Making will always selecting the action with the highest Q-value for a given state. A possible downside of this approach is that the Agent will always pick the 
action that it knows is the best rewarding, hence it will not explore other possible paths of the state-action chain, which can be more efficient or rewarding.
ε-Greedy algorithm is a possible way to address the problem. The Agent, with a probability of 1 - ε, it will choose the known best move, while with a probability of ε,
it chooses a random move to favour exploration over exploitation. Over time, ε can be decreased to gradually reduce the exploration and focus more on exploiting the learned knowledge.

In scenarios where the number of states and actions is too large to learn the exact Q-value for each state-action pair, functional approximation techniques can be used.
It approximates the Q-value function, Q(s, a), by employing a function that combines various features instead of storing a exact value for every state-action pair. 
This allows for generalization of states based on similar features, where states with similar features can be approximated with the same Q-value. 
This approach is particularly useful in complex games like chess, where the number of possible states is immense.
'''


'''
Unsupervised Learning - Another type of Machines Learning, which learns patterns and structures from unlabeled datasets.

Clustering - a technique in unsupervised learning that aims to organize a set of objects into groups, or clusters, based on their inherent similarities. 
It is commonly used in various domains such as genetic research, image segmentation, market research, medical imaging, and social network analysis.
One commonly used clustering algorithm is k-Means Clustering. This algorithm iteratively defines clusters by their centers, assigns data points to the cluster with the closest center, 
and then updates the centers based on the assigned points. The process continues until a state of equilibrium is reached, where there is no further change in the assignment of points.
'''