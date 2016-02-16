def verify_anagrams(first_word, second_word):
    a = list(first_word.lower().replace(" ", ""))
    b = list(second_word.lower().replace(" ", ""))
    a.sort()
    b.sort()
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if a[i] != b[i]:
            return False
            
    return True


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams(u"a", u"z"), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams(u"Hello", u"Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

