def checkio(psswd):
    # return True only if all of the following are True:
    # length of psswd is >= 10 chars
    # psswd is not all lowercase (conatins 1 or more uppercase)
    # psswd is not all uppercase (contains 1 or more lowercase)
    # psswd is not all alphanumeric (conatins 1 or more numbers)
    # psswd is not all numbers (conatins 1 or more alphanumerics)
    return ( (len(psswd) >= 10) and 
             (not psswd.islower()) and 
             (not psswd.isupper()) and 
             (not psswd.isalpha()) and
             (not psswd.isdigit()))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
