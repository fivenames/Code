import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"(?:https?://)?(?:www\.)?youtube.com/embed/([a-zA-Z0-9]+)", s):
        url = matches.group(1)
        return f"https://youtu.be/{url}"

    return False

if __name__ == "__main__":
    main()