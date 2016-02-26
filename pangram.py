def check_pangram(text):
    alpha = set()
    for c in text:
        if c.isalpha():
            alpha.add(c.lower())
    return True if len(alpha) >= 26 else False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    assert not check_pangram("Six big devils from Japan quickly forgot how to walt.")