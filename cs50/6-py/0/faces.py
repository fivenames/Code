def convert(sentence):

    result = sentence

    while ":)" in result or ":(" in result:
        result = result.replace(":)", "🙂")
        result = result.replace(":(", "🙁")

    return result

def main():

    sentence = input("Input: ")

    result = convert(sentence)

    print(f"Output: {result}")

main()
