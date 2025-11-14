import string

def file_reader(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        raise None

def clean(text):
    text = text.lower()
    for i in string.punctuation:
        text = text.replace(i, '')
    return text

def count_word(text):
    words = text.split()
    count_words = {}

    for word in words:
        if word not in count_words:
            count_words[word] = 1
        else:
            count_words[word] += 1
    return count_words


def print_words(counts):
    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_items:
        print(word, count)



def top(count_words, n=20):
    items = list(count_words.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for word, cnt in items[:n]:
        print(f"{word}: {cnt}")

def main():
    print("Word Count Program")

    small_text = file_reader("/Users/aidarmamaturaimov/Downloads/small.txt")
    if small_text:
        small_text = clean(small_text)
        small_counts = count_word(small_text)
        print("\nAll words from small.txt:")
        print_words(small_counts)

    alice_text = file_reader("/Users/aidarmamaturaimov/Downloads/alice.txt")
    if alice_text:
        alice_text = clean(alice_text)
        alice_counts = count_word(alice_text)
        print("\nTop 20 words from alice.txt:")
        top(alice_counts, n=20)


if __name__ == "__main__":
    main()

