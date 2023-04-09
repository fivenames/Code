import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

    lst = re.findall(r"\bum\b", s, re.I)

    return len(lst)


if __name__ == "__main__":
    main()