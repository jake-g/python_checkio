FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(n):
    s = ''
    nums = list(str(n))
    l = len(nums)
    while len(nums) > 0:
        if len(nums) == 3:
            s = s + '%s %s ' % (FIRST_TEN[int(nums[0])-1], HUNDRED)
            del nums[0] 
        elif len(nums) == 2 and nums[0] is '1':
            s = s + '%s ' % (SECOND_TEN[int(nums[1])])
            del nums[0]
            del nums[0]
        elif len(nums) == 2:
            if nums[0] is not '0':
                s = s+ '%s ' % (OTHER_TENS[int(nums[0])-2])
            del nums[0]
        elif len(nums) == 1:
            if nums[0] is not '0':
                s = s + '%s ' % (FIRST_TEN[int(nums[0])-1])
            del nums[0]

    print s
    return s.strip()

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
