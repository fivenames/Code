''' 
Conditional probability: P(A|B) = P(A ∧ B) / P(B), and since P(A ∧ B) = P(B ∧ A), hence P(B|A) = P(A ∧ B) / P(A). Re-arranging to derive Baye's rule:
P(A|B) = P(B|A) * ( P(A) / P(B) ); This can be used for eg. 80% of counterfeit bills has blurry text, calculate the probability of a bill with blurry text is a counterfeit bill.

Recall H2 Math probability Venn diagram: Negation( P(A) = 1 - P(¬A) ), Inclusion-Exclusion( P(A V B) = P(A) + P(B) - P(A ∧ B) ), and;
Marginalisation( P(A) = P(A ∧ B) + P(A ∧ ¬B) ) == Conditioning( P(A) = P(A|B)P(B) + P(A|¬B)P(¬B) )
'''

#