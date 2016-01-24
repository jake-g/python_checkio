def checkio(text):
    text = text.lower()
    count = {}
    for s in text:
      if count.has_key(s):
        count[s] += 1
      elif s.isalpha():
        count[s] = 1

    max = 0
    out = float("inf")
    for key in count:
        if (count[key] == max) and (ord(out) > ord(key)):
            out = str(key).lower()           
        if count[key] > max:
            max = count[key]
            out = str(key).lower()
    return out

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
