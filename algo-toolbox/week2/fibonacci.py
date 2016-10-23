# Uses python2

def fib(n):

    if n == 0: return 0
    if n == 1: return 1

    nMinusTwo = 0
    nMinusOne = 1
    result = 0

    for i in range(2, n + 1):
        result = nMinusOne + nMinusTwo
        nMinusTwo = nMinusOne
        nMinusOne = result

    return result

n = int(input())
print(fib(n))
