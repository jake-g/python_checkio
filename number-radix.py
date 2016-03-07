def checkio(str_n, base):
    dec = 0
    for i, c in enumerate(str_n[::-1]):
        if c.isalpha():
            c = ord(c) - 55
        if int(c) >= base:
            return -1
        dec += int(c) * base**i
    return dec

# Better Solution
# def checkio(str_number, radix):
#     try: return int(str_number, radix)
#     except ValueError: return -1


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"235", 8) == 157, "Hex"
    assert checkio(u"AF", 16) == 175, "Hex"
    assert checkio(u"101", 2) == 5, "Bin"
    assert checkio(u"101", 5) == 26, "5 base"
    assert checkio(u"Z", 36) == 35, "Z base"
    assert checkio(u"AB", 10) == -1, "B > A > 10"
