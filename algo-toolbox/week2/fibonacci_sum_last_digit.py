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

def last(n):
    if n == 0: return 0
    if n == 1: return 1

    sum = 0
    remainderSum = 0
    length = pisano(10) # this produces 60 so we can just assign that
    remainder = n % length

    for x in range(0, length + 1):
        if remainder != 0 and x <= remainder:
            remainderSum += fib(x) % 10

        sum += fib(x) % 10

    return ((sum * length) + remainderSum) % 10

if __name__ == '__main__':
    input = raw_input()
    n = int(input)
    print(last(n))
