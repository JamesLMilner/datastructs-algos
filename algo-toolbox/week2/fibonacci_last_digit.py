# Uses python2

def get_fibonacci_last_digit(n):

    if n == 0: return 0
    if n == 1: return 1

    nMinusTwo = 0
    nMinusOne = 1
    result = 0
    sum = 0

    for i in xrange(2, n + 1):
        result = (nMinusOne + nMinusTwo) % 10
        nMinusTwo = nMinusOne
        nMinusOne = result

    return result

if __name__ == '__main__':
    n = int(input())
    print get_fibonacci_last_digit(n)
