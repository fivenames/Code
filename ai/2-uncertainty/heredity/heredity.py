import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene, if parent is unknown
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")

    # load_data() returns a dictionary of key "name" paird with a dictionary(contains name, mother, father and trait) as value.
    people = load_data(sys.argv[1])

    # Create a dictionary of key "name" paired with a ditionary(contains gene and trait probability distribution) as value
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        # loop over each person and initialised the probability distribution to 0
        for person in people
    }

    # Convert the dictionary returned by load_data() call into a set, Note: the set will contain only the key "name".
    names = set(people)

    # The powerset() returns a list of sets containing all possible combinations of elements from the set passed in. Ie. all subsets
    # Loop through all possible combinations of names.
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
            # Check if the current person have the trait but not in the current subset, or the person do not have the trait but is in the current subset.
            # There is an assumption here that the current subset is a set of people with the trait.
            people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue
        # Else, the current subset is a set of names of those with the traits

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    # Convert the set "s" into a list.
    s = list(s)
     
    return [
        # itertools.chain.from_iterable(iterable) is used to flatten a nested structure into a single-level structure
        set(s) for s in itertools.chain.from_iterable(
            # itertools.combinations(iterable, r) generates all possible combinations of r elements from the iterable. r ranges from 0 to the length of s
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]

# Joint probability = P(A ∧ B)
def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    no_gene = set(people) - one_gene - two_genes

    jp = 1
    temp = 0
    for person in people:
        gene_count = 1 if person in one_gene else (2 if person in two_genes else 0)
        has_trait = person in have_trait

        father = people[person]["father"]
        mother = people[person]["mother"]
        
        if not father or not mother:
            temp = PROBS["gene"][gene_count] * PROBS["trait"][gene_count][has_trait]
            jp = jp * temp
            continue

        if (father in one_gene and mother in no_gene) or (mother in one_gene and father in no_gene):
            if gene_count == 1:
                # The value 0.5 is not considered for mutation as it can happen both ways, the positive mutate into negative and vice versa
                temp = 0.5 * (1 - PROBS["mutation"]) + 0.5 * PROBS["mutation"]
            elif gene_count == 2:
                temp = 0.5 * PROBS["mutation"]
            else:
                temp = 0.5 * (1 - PROBS["mutation"])
            temp = temp * PROBS["trait"][gene_count][has_trait]
            jp = jp * temp
            continue

        if (father in two_genes and mother in no_gene) or (mother in two_genes and father in no_gene):
            if gene_count == 1:
                temp = (1 - PROBS["mutation"]) * (1 - PROBS["mutation"]) + PROBS["mutation"] * PROBS["mutation"]
            elif gene_count == 2:
                temp = (1 - PROBS["mutation"]) * PROBS["mutation"]
            else:
                temp = PROBS["mutation"] * (1 - PROBS["mutation"])
            temp = temp * PROBS["trait"][gene_count][has_trait]
            jp = jp * temp
            continue
        
        if (father in two_genes and mother in one_gene) or (mother in two_genes and father in one_gene):
            if gene_count == 1:
                temp = (1 - PROBS["mutation"]) * 0.5 + PROBS["mutation"] * 0.5
            elif gene_count == 2:
                temp = (1 - PROBS["mutation"]) * 0.5
            else:
                PROBS["mutation"] * 0.5
            temp = temp * PROBS["trait"][gene_count][has_trait]
            jp = jp * temp
            continue
        
        if father in no_gene and mother in no_gene:
            if gene_count == 1:
                temp = 2 * (PROBS["mutation"] * (1 - PROBS["mutation"]))
            elif gene_count == 2:
                temp = PROBS["mutation"] * PROBS["mutation"]
            else:
                temp = (1 - PROBS["mutation"]) * (1 - PROBS["mutation"])
            temp = temp * PROBS["trait"][gene_count][has_trait]
            jp = jp * temp
            continue

        if father in one_gene and mother in one_gene:
            if gene_count == 1:
                temp = 2 * (0.5 * 0.5)
            elif gene_count == 2:
                temp = 0.5 * 0.5
            else:
                temp = 0.5 * 0.5
            temp = temp * PROBS["trait"][gene_count][has_trait]
            jp = jp * temp
            continue
        
        if father in two_genes and mother in two_genes:
            if gene_count == 1:
                temp = 2 * ((1 - PROBS["mutation"]) * PROBS["mutation"])
            elif gene_count == 2:
                temp = (1 - PROBS["mutation"]) * (1 - PROBS["mutation"])
            else:
                temp = PROBS["mutation"] * PROBS["mutation"]
            temp = temp * PROBS["trait"][gene_count][has_trait]
            jp = jp * temp
            continue

    return jp


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        if person in have_trait:
            probabilities[person]["trait"][True] += p
        else:
            probabilities[person]["trait"][False] += p
        
        if person in one_gene:
            probabilities[person]["gene"][1] += p
        elif person in two_genes:
            probabilities[person]["gene"][2] += p
        else:
            probabilities[person]["gene"][0] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    sum = 0
    for person in probabilities:
        sum = probabilities[person]["trait"][True] + probabilities[person]["trait"][False]
        probabilities[person]["trait"][True] = probabilities[person]["trait"][True] / sum
        probabilities[person]["trait"][False] = probabilities[person]["trait"][False] / sum

        sum = probabilities[person]["gene"][0] + probabilities[person]["gene"][1] + probabilities[person]["gene"][2]
        probabilities[person]["gene"][0] = probabilities[person]["gene"][0] / sum
        probabilities[person]["gene"][1] = probabilities[person]["gene"][1] / sum
        probabilities[person]["gene"][2] = probabilities[person]["gene"][2] / sum


if __name__ == "__main__":
    main()
