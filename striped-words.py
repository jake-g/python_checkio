VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):
    v = list(VOWELS)
    c = list(CONSONANTS)
    count = 0

    words  = text.split()
    for w in words:
        w = w.upper()
        print w
        status = None   # 1 vowel 0 con
        # check each n char words
        for n in enumerate(w):
            is_word = False
            char = n[1]
            print char
            # Check first char
            if n[0] == 0:
                if n[1] in v:
                    status = 1
#                elif n[1] in c:
 #                   status = 0
                    
            # Check other chars       
            if (char in v and status == 0):
                is_word = True
            elif (char in c and status == 1):
                is_word = True
            else: 
                print 'break '
                break
            
        if is_word:
            count += 1
            print count
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
