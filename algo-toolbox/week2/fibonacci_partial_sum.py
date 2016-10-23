# Uses python2
import sys

def pisano(m):

    if m == 2:
        return 3

    n1 = 0
    n2 = 1

    length = 0 # length of pisano sequence
    mod1 = 0
    mod2 = 0
    sameSeq = True

    while sameSeq:
        length += 1
        res = n1 + n2
        n2 = n1
        n1 = res

        mod1 = res % m
        if mod1 == 0 and n1 != 0:
            if mod2 == 1 and n2 != 1:
                return length

        mod2 = mod1


def fib(n):

    if n == 0: return 0;
    if n == 1: return 1;

    nMinusTwo = 0
    nMinusOne = 1
    result = 0

    for i in range(2, n + 1):
        result = nMinusOne + nMinusTwo
        nMinusTwo = nMinusOne
        nMinusOne = result

    return result

def last(m,n):
    if n == 0: return 0
    if n == 1: return 1

    total = 0
    remainderSum = 0

    length = pisano(10) # this produces 60 so we can just assign that
    remainder = n % length

    # 100 - 200
    # 100
    # 60
    # 100 % 60 = 40
    # 60, 120, 180
    # 40,

    # 100 / 60

    # roundDown(100 / 60) = 1
    # 100 % 60 = 40
    # iterate 40, calculate 40 - 60

    # 120 - 180 - normal
    # 180 - 200 calculate 1 - 20

    lower = int(m / length) # 1
    lowerRemainder = m % length # 40

    lowerRemainderSum = 0

    for i in xrange(0, length + 1):

        if remainder != 0 and i <= remainder:
            remainderSum += fib(i) % 10

        if lowerRemainder != 0 and i >= lowerRemainder:
            lowerRemainderSum += fib(i) % 10

        total += fib(i) % 10

    return ((total * length) + remainderSum + lowerRemainderSum) % 10

def diff(m,n):
    if m == 0 and n == 0:
        return 0
    if m == 1 or m == 0:
        return last(m,n)

    return last(m,n)

if __name__ == '__main__':
    input = raw_input()
    m, n = map(int, input.split(" "))
    print diff(m, n)
