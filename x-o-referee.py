def checkio(rows):
    cols = zip(*rows)
    diags = [(rows[0][0] + rows[1][1] + rows[2][2]),
             (rows[0][2] + rows[1][1] + rows[2][0]),
             '...'] # added dummy row for dimensional agreement in loop

    for i in range(len(rows)):
        # look for three in a row (not '.' though)
        r, c, d = set(rows[i]), set(cols[i]), set(diags[i])
        if (len(r) == 1) and ('.' not in r):
            return r.pop()
        if (len(c) == 1) and ('.' not in c):
            return c.pop()
        if (len(d) == 1) and ('.' not in d):
            return d.pop()
    return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

