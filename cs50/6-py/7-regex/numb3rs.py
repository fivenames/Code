# Regular expressions use the backslash character ('\') to allow special characters to be used without invoking their special meaning.
# This collides with Python’s usage of the same character for the same purpose in string literals.
# For example, to match a literal backslash: the regular expression must be \\ and , and each backslash must be expressed as \\ inside a regular Python string literal.
# Hence, one might have to write '\\\\' as the pattern string. The solution is to use Python’s raw string notation for regular expression patterns

# Note: RegEx isn't part of Python, but instead a different programming language with its own parser and compiler.
# There are two parsers being employed here - first one is the Python parser, and it translates your string literal (or raw string literal) into a sequence of bytes.
# The second one is Python's regular expression parser, and it converts a sequence of bytes into a compiled regular expression.

# If you use a regular string and you pass in a pattern like "\t" to the RegEx parser, Python will translate that literal into a buffer with the tab byte in it (0x09).
# In contrast, if a pattern like r"\t" is passed to the RegEx parser, Python does not do any interpretation, and it creates a buffer with two bytes in it: '\', and 't'. (0x5c, 0x74).

# When calling a function from a module, the interpreter converts the arguments to their binary representation before passing them to the function.
# This is because the arguments need to be passed across the boundary between Python and the C code in the module, as modules are written in C.

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        return True

    return False

if __name__ == "__main__":
    main()