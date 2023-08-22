'''
To ensure that AI generates grammatically correct sentences, we can apply grammar rules. These rules include Formal Grammar and Context-Free Grammar (CFG). 
In CFG, the words that the AI produces are referred to as terminal symbols. These terminal symbols are associated with non-terminal symbols. For instance, 
the sentence "She saw the city." The words "She," "saw," and "the city" are terminal symbols, and they are generated from non-terminal symbols like N, V, D, N, 
representing Noun, Verb, Determiner, and Noun, respectively.

To create terminal symbols from non-terminal symbols, Re-Writing Rules are used. These rules take a non-terminal symbol and rewrite it as another symbol. 
For example, a non-terminal symbol N can be mapped to all possible nouns. Additionally, N can be derived from other non-terminal symbols, such as NP (noun phrase). 
A noun phrase is a phrase that functions as a noun, like the phrase: "the car on the street" The process of the rule might be: NP → N | D, N | ... → N | she, city, ... → she.
There are other non-terminal symbols, such as VP (Verb Phrase) and S (Sentence). VP can consist of only a verb or a verb and an NP, while S consists of an NP and a VP.
The parse tree for this example might look like:
              S
        NP          VP
        N       V       NP
                      D    N
       she     saw   the  city
'''
'''
To ensure that AI generates not only syntactically correct but also semantically meaningful sentences, the concept of n-grams is introduced. 
An n-gram is a contiguous sequence of n items, which can be characters or words, extracted from a text sample. The value of n can be chosen as desired, 
resulting in different types of n-grams such as unigrams (single items), bigrams (two-item sequences), trigrams (three-item sequences), and so on.

The process of extracting n-grams from a text is known as Tokenization. Tokenization involves breaking down a sequence of characters into individual pieces or tokens, 
which can represent either words or sentences, depending on the granularity desired.
By building a substantial database of n-grams and employing the Markov Model, a straightforward approach to generating semantically correct sentences can be achieved. 
The Markov Model relies on the probability distribution of the subsequent word based on the previous n words.

When the AI generates a sentence, it can consult the database of n-grams to calculate the likelihood of a particular word following a specific sequence of n words. 
This probability information helps the AI to construct sentences that are not only grammatically coherent but also contextually appropriate, 
improving the overall semantic correctness of the generated text.
'''



'''
In Text Categorization problems, where texts are classified into different classes, the Bag-of-Words Model is a popular approach. 
This model represents text as an unordered collection of words. The classification process involves checking if a specific class contains texts with the same word as the current text. 
This approach is particularly effective for tasks like sentiment analysis, where texts are categorized as having positive or negative sentiments.

A popular approach using this model is the Naive Bayes approach, which is based on the Baye's rule. Recall Baye's Rule: P(A|B) = P(B|A) * [ P(A) / P(B) ], 
P(text is classA | text is "my grandson loved it.") = P(text|classA) * [ P(classA) / P(text) ] = k * P(classA) * P(text|classA) 
= k * P("my" ∧ "grandson" ∧ "loved" ∧ "it" | classA) * P(classA) = k * P("my" ∧ "grandson" ∧ "loved" ∧ "it" ∧ classA) ----- P(B|A) = P(B, A) / A; P(B|A) * P(A) = P(B, A)
To calculate the joint probability, P("my" ∧ "grandson" ∧ "loved" ∧ "it" ∧ classA); equivalent to a Baysian Network of a Node classA dependent on 4 Nodes of the respective words;
= P(classA)P("my"|classA)P("grandson"|"my" ∧ classA)P("loved"|"grandson" ∧ "my" ∧ classA)P("it"|"it" ∧ "grandson" ∧ "my" ∧ classA);

However, the listed joint probability is not something readily available, hence in the Naive Bayes approach, there is an assumption that words are independent of each other.
Therefore, the computed joint probability became P(classA) * P("my"|classA) * P("grandson"|classA) * P("loved"|classA) * P("it"|classA);
P(classA) = number of classA samples / Total; P("my"|classA) = number of class samples with "my" / Total; and so on...
Finally, the joint probability of the other classes are computed as well, ie: P(classB) * P("my"|classB) * P("grandson"|classB) * P("loved"|classB) * P("it"|classB); ...
All the joint probability is then normalised so that they sum up to 1.

A problem arises when a word in the current text has never appeared in the samples of a certain class. In such cases, the conditional probability P(word|class) becomes zero. 
This results in the joint probability becoming zero as well, effectively neglecting all other words in the sentence since anything multiplied by zero is zero. 
To overcome this challenge, one common approach is called the Addictive Smooothing, such that a value k is added to each of the value in the distribution to smooth the data. 
The Laplace Smoothing, in particular, adds 1 to each value in the distribution, sort of pretending that each value has appeared one more time than it actually had.
'''



'''
Word representation is a technique used to convert words into numerical values, making them suitable for computational processing. One common method is the One-Hot Representation, 
where each word is represented by a vector with a single "1" and the rest "0s". For instance, the sentence "He wrote a book." would be represented as 
[he: (1, 0, 0, 0), wrote: (0, 1, 0, 0), a: (0, 0, 0, 1), book: (0, 0, 0, 1)]. However, this approach has limitations, particularly when dealing with a large vocabulary. 
The vectors become very large and resource-intensive. Additionally, words with similar meanings are not effectively captured.

To address these issues, a distributed representation is preferred. Here, word meanings are distributed across multiple values. For instance, "He wrote a book." 
might be represented as [he: (-0.211, -0.311, 0.2, ...), wrote: (0.663, 0.99, -0.01, ...), ...]. The context surrounding each word influences its distribution, 
allowing words with similar contexts to have closer vectors in a multi-dimensional space. This relationship-based approach is well suited for capturing semantic meaning.

Word2Vec is a widely used model for creating such distributed representations. This model begins with words assigned random positions and then adjusts these positions during training. 
It learns from a large corpus of text to understand how words appear in various contexts. Words that appear in similar contexts are positioned closer together in the vector space. 
Word2Vec can also capture word relationships, exemplified by its ability to deduce that the displacement between "man" and "king" is similar to that between "woman" and "queen".
'''



'''
In Recurrent Neural Networks (RNNs), generating a sequence of text involves encoding inputs into a hidden state, which is then used to generate subsequent outputs. 
However, when dealing with large inputs, the hidden state can become overwhelmed with information, leading to inefficiency. 
To address this issue, a strategy is to encode each input word into a hidden state and utilize all these states when generating output.
In this approach, the weighting for each hidden state become important as some words are functional words such as "the", "or". 

The Attention mechanism provides a solution by calculating an attention score for each input word, assigning it importance. 
The network can then use these scores to determine the weight of each hidden state when generating output words. 
This allows the model to focus on relevant parts of the input sequence when producing each output word.
'''
'''
Traditional RNNs lack parallelism due to their dependency on previous hidden states for encoding and decoding. To overcome this limitation, the Transformer architecture was introduced. 
In Transformers, each input word is processed independently. In order to do that, the process involves passing each word through self-attention layers, 
which capture contextual information by considering other words in the sequence, and a positional encoding which maintains the word order is passed through the NN.
This parallel processing happens for each input word simultaneously.
For decoding or generating outputs, Transformers employ an additional attention layer that focuses on the encoded representations of the input words. 
This enables the model to use the relevant information from the input sequence when producing the output sequence.
'''