'''
To ensure AI generates syntactically well formed sentences, Grammar rules can be applied. There are Grammar rules such as Formal Grammer and Context-Free Grammar(CFG). 
In CFG, the ouput words are called terminal symbols, and terminal symbols are associated with non-terminal symbols. For example: Consider "She saw the city." 
These words are terminal symbols, and are generated from non-terminal symbols. The non-terminal symbols can be N V D N, which stands for Noun, Verb, Derterminer and Noun respectively.

Terminal symbols are generated from non-terminal symbols using Re-Writing Rules, which takes a non-terminal symbol, rewriting it into another symbol. 
Non-terminal symbols like N is mapped to all possible nouns, and N can be mapped from another non-terminal symbols such as NP, which stands for noun phrase. 
Noun phrase are phrases that operates like a noun, for example: '... the car on the street ...'. The process of the rule might be: NP → N | D, N | ... → N | she, city, ... → she;
There are other non-terminal symbols such as VP(Verb Phrase) and S(Sentence). VP can consist of a verb or a verb and a NP, while S will consists of a NP and a VP.
The parse tree for this example might look like:
              S
        NP          VP
        N       V       NP
                      D    N
       she     saw   the  city
'''
'''
However, the sentences can be syntactically correct but not semantically correct. To ensure the AI generate meaningful sentences, the notion of n-gram has to be introduced.
N-gram is a contiguous sequence of n items from a sample of text. In which, the item can be characters and words, n can be any chosen number as well (unigram, bigram, trigram...).
Extracting n-gram from a text, the process is called Tokenisation, which refers to the task of splitting a sequence of characters into pieces(tokens). Tokens can be words or sentences. 
With a huge database of n-grams, and applying the Markov Model, this can be a simple approach to generating semantically correct sentences.
The database of n-grams will be useful in calculating the probability distribution for the subsequent word based on the previous n words, which is exactly how Markov Model needs.
'''



'''
In a Text Categorization problem, which categorises texts into different classes, there are many possible approaches. One approach is the Bag-of-Words Model,
this model represents text as an unordered collection of words. When a specific class contains texts with the specific word that the current text contains, the current text is
classified under that class. This approach tends to work quite well with classification such as good or bad sentiments/reviews.

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
'''