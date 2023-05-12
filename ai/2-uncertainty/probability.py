''' 
Conditional probability: P(A|B) = P(A ∧ B) / P(B), and since P(A ∧ B) = P(B ∧ A), hence P(B|A) = P(A ∧ B) / P(A). Re-arranging to derive Baye's rule:
P(A|B) = P(B|A) * [ P(A) / P(B) ]; This can be used for eg. 80% of counterfeit bills has blurry text, calculate the probability of a bill with blurry text is a counterfeit bill.

Recall H2 Math probability Venn diagram: Negation[ P(A) = 1 - P(¬A) ], Inclusion-Exclusion[ P(A V B) = P(A) + P(B) - P(A ∧ B) ], and;
Marginalisation[ P(A) = P(A ∧ B) + P(A ∧ ¬B) ] == Conditioning[ P(A) = P(A|B)P(B) + P(A|¬B)P(¬B) ] (re-arranging). if B has more possibilities, sum all possible B probability.

Bayesian Network - data structure that represents the dependencies among random variable, it is implemented using a directed graph with each node representing a random variable
and has the probability distribution: P(X|parents(X)); To calculate the joint probability, P(grandparents ∧ parents ∧ X) == P(grandparent)P(parent|grandparent)P(X|parent)

Using Inference by Enumeration to find P(Query|Evidence) == k * P(Query ∧ Evidence), where k is a constant == 1/P(Evidence) and Evidence is already observed -> P(Evidence) known.
Using Marginalisation, P(Query|Evidence) = k * P(Query ∧ Evidence) = k * Σ[ P(Query ∧ Evidence ∧ hidden variables) ] for all possible values of hidden variables.
'''

'''
Sampling - select a large number of possible states based on the conditional probability in the network, and then use the samples to estimate the probability of the query.

Rejection Sampling is a way to carry out sampling, check the samples which the evidence is false and reject them, then count the number of samples that query is true,
this divided by the accepted sample will be an estimation for P(query|evidence). However, this method will be very inefficient when the acceptance rate is low.

Likelyhood weighting is another way to carry out sampling, sample the network with fixed evidence. The weight of the sample is calculated by multiplying the probabilities of
the evidence variables given the sample, it measures how well the sample matches the evidence. The final estimate for the probability of the query given the evidence is obtained
by summing up the weights of all the samples where the query is true, and then dividing this by the sum of the weights of all the generated samples.
'''



'''
Markov Model is used to model the behavior of a system that has each of its state changes depend only on the previous states(evidence).
If the evidence is too large with too many previous state, Markov Assumption can be used: the current state depends on only a finite fixed number of previous states.
A chain of random variables that are assumed under Markov assumption is called a Markov Chain, together with a transition model which defines the probability distribution
of the current state given the evidence, forms the model.

Hidden Markov Model(HMM) a type of Markov Model, for eg. voice recognision, the observation is the audio waveforms and the hidden state is the words spoken.
Each of the HMM's states produces an observable emission(observation), but its state are hidden and not directly observed. In addition to a transition model, it also consists of
a sensor model: the probability distribution of the observation given its current state. Essentially made up of two chains, a Markov chain and an emission chain.
Its observations are assumed under the Sensor Markov Assumption as well which assumes the observation depends only on the corresponding state.

Possible application of HMM:
Given the past observations, calculate the probability distribution for the current state(Filtering) or future state(Prediction) or past state(Smoothing).
Given the past observations, calculate the most likely sequence of states(Most Likely Explanation).
'''