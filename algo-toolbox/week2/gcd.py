#python2

def gcd(a, b):

    while b != 0:
        mod = a % b
        a = b
        b = mod

    return a



if __name__ == '__main__':
    input = raw_input()
    a, b = map(int, input.split(" "))
    print gcd(a, b)