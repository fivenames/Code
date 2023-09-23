import csv
import sys


def main():

    if len(sys.argv) != 3:
        sys.exit("Invalid command-line arguments.")

    try:
        with open(sys.argv[1], 'r') as file1:
            reader = csv.reader(file1)

            data = []
            for line in reader:
                data.append(line)

            header = data[0]
            subseqs = header[1:]
            data = data[1:]
        with open(sys.argv[2], 'r') as file2:
            sequence = file2.read()
    except FileNotFoundError:
        sys.exit('File not found.')

    num_match = []
    for subseq in subseqs:
        longest = longest_match(sequence, subseq)
        num_match.append(longest)

    for each in data:
        to_match = each[1:]
        # The map() function applies a given function to each element of a list and returns a new list with the results.
        to_match = list(map(int, to_match))

        if to_match == num_match:
            print(f'{each[0]}')
            quit()

    print('No match')

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
