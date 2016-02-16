
def fib():
 global a,b
 while True:
  a,b = b, a+b
  yield a
f=fibI()
f.next()
f.next()
f.next()
f.next()

def checkio(op):
    
    cur = fib()
    while cur <= op:
        f.next
    if cur == op:
        return 1000 - op
    else
    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"