'''
Propositional symbols - symbols representing a sentence that can be either true or false, ie: P, Q, ...
Logical connectors - the logic connecting different propositional symbols together, ie: ¬ NEGATION(not), ∧ AND(all true), 
V OR(one in which is true; not exclusive 'or', can be more than one is true), → IMPLICATION(if true then true), ↔ BICONDITIONAL(if true and only if true)

Model - assignment of a boolean value to every propositional symbol, there will be models(2^n) for each possible permutations. Eg, model_1: P = false, Q = true, ...
Knowledge base - a set of sentences that is already known to be true.
Entailment - if a entails b, in every model in which sentence a is true, sentence b is also true.

Inference rules - a way to convert logical connectors into other logical connectors, ie: 
Modus Ponens[ (a → b, a) = b ], Resolution[ (a V b, ¬a) = b,     (a V b, ¬a V c) = b V c ], 
AND Elimination( a ∧ b = a, b ), Double Negation Elimination( ¬(¬a) = a ), IMPLICATION Elimination( a → b = ¬a V b ), BICONDITIONAL Elimination[ a ↔ b = (a → b) ∧ (b → a) ], 
De Morgan's Law[ ¬(a ∧ b) = ¬a V ¬b,     ¬(a V b) = ¬a ∧ ¬b ], Distributive Law[ a ∧ (b V c) = (a ∧ b) V (a ∧ c),     a V (b ∧ c) = (a V b) ∧ (a V c) ]

Literal - symbols with only itself or with NOT connector, eg. p, ¬p
Disjunction - symbols connected with only OR, eg. p V q
Conjunction - symbols connected with only AND, eg. p ∧ q
Clause - a disjunction of literals, eg. p V q V ¬r
Conjunctive Normal Form - a conjunction of clause, eg. (a V b V c) ∧ (d V ¬e) ∧ (f V g)
'''

# To solve a logic problem(checking if KB entails query):
# Using model checking algorithm;
    # Enumerate all possible model
    # If in every model that KB is true(when the knowledge input is true, in another word: what is already known is set to true), query is also true, then KB entails query

# Using throrem proving algorithm;
    # initial state: KB
    # action: inference rules
    # transition model: new KB after action
    # goal test: check if current KB matches query
    # path cost function: number of steps in proving

# Using inference by resolution;
    # Determine if KB ∧ ¬query(if KB is true and query is false) is a contradiction to KB entails query(if KB is true, query is true)
        # Convert KB ∧ ¬query into conjunctive normal form
            # Elimination of BICONDITIONAL and IMPLICATION, move NEGATION inwards using De Morgan's Law, use distributive law to distribute OR whenever possible
        # Loop to check if resolution rule can be used to produce a new clause
            # If empty clause if produced[ (p, ¬p) = () ] (equivalent to false), there is an contradiction
                # return KB entails query
            # Add new clause
        # Otherwise if no more new clause can be added and there is no contradiction, return no entailment


'''
First-Order Logic is a different approach from the propositional logic;
it uses two symbol: Constant Symbol and Predicate Symbol, such that predicate symbol holds a different boolean value for each of the constant symbol.
Eg. Predicate1(Constant1) = true, Predicate1(Constant2) = false, ie: Person(Harry) = Harry is a person, Person(Gryffindor) = Gryffindor is not a person...

Quantifiers: 
∀ Universal Quantification - for all constant symbols that is true for a predicate symbol, the specified sentence is true, 
eg. ∀x. BelongsTo(x, Gryffindors) → ¬BelongsTo(x, Hufflepuff) = Anyone belongs to Gryffindor, does not belong to Hufflepuff
∃ Existential Quantification - there exists at least one value of a constant symbol that is true for a predicate symbol, the specified sentence is true, 
eg. ∃x. House(x) ∧ BelongsTo(Harry, x) = Harry belongs to one of the houses.
Combining these two idea; ∀x.Person(x) → [∃y. House(y) ∧ BelongsTo(x, y)] = for every person, there exists at least one house in which the person belongs to; ie: everyone has a house.
'''
