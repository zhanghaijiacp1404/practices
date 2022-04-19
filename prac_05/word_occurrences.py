"""
Based on user input string, count each character's occurrence
and display it
"""


def main():
    """Start program"""
    user_string = input("Text: ")
    words = user_string.split(sep=" ")
    word_to_count = {}
    for word in words:
        word_to_count[word] = 0
    for word in words:
        if word_to_count.get(word) is not None:
            word_to_count[word] += 1

    words = list(word_to_count.keys())
    words.sort()
    max_length = max(len(word) for word in words)
    for word in words:
        print(f"{str(word):{max_length}}: {word_to_count[word]}")


if __name__ == "__main__":
    main()
