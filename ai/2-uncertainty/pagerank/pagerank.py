import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages

# corpus: {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {}}
def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    model = dict()

    n = len(corpus)
    for webpage in corpus.keys():
        # Equal chance of selection for all pages in the corpus for 1 - dampling_factor
        model[webpage] = (1 - damping_factor) / n

    # A set of links to other pages for the given webpage
    pagelinks = corpus[page]
    p = len(pagelinks)
    if p == 0:
        return model

    for link in pagelinks:
        # Equal chance of selection for all linked pages in the given page for damping_factor
        model[link] += damping_factor / p

    return model


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = dict()
    sample = random.choice(list(corpus.keys()))

    for _ in range(n):
        probability = transition_model(corpus, sample, damping_factor)
        sample = random.choices(list(probability.keys()), weights=list(probability.values()), k=1)[0]
        if sample in pagerank:
            pagerank[sample] += 1 / n
        else:
            pagerank[sample] = 1 / n
    
    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    iterate_PR = {}
    n = len(corpus)
    for page in corpus:
        iterate_PR[page] = 1 / n

    changes = 0.0011
    while changes >= 0.001:
        changes = 0

        previous_state = iterate_PR.copy()

        for curr_page in iterate_PR.keys():
            # If current page is linked by a page, append the page as parents
            parents = [page for page in corpus.keys() if curr_page in corpus[page]]
            first_part = ((1-damping_factor) / n)
            second_part = []

            if len(parents) != 0:
                # Calculate the second part of the equation by summing all the values
                for parent in parents:
                    num_links = len(corpus[parent])
                    val = iterate_PR[parent] / num_links
                    second_part.append(val)

            second_part = damping_factor * sum(second_part)
            iterate_PR[curr_page] = first_part + second_part

            changes = abs(iterate_PR[curr_page] - previous_state[curr_page])
    
    # Ensure that the sum will add up to 1 by dividing each value by the total sum.
    dictsum = sum(iterate_PR.values())
    iterate_PR = {key: value / dictsum for key, value in iterate_PR.items()}
    return iterate_PR

if __name__ == "__main__":
    main()
