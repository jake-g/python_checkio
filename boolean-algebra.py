OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    ind = OPERATION_NAMES.index(operation)
    if ind == 0: return x & y
    if ind == 1: return x | y
    if ind == 2: return not(x) or y
    if ind == 3: return x ^ y
    if ind == 4: return x == y

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"
