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