#python2

def gcd(a, b):

    while b != 0:
        mod = a % b
        a = b
        b = mod

    return a


def lcm(a, b):
    return a / gcd(a, b) * b

if __name__ == '__main__':
    input = raw_input()
    a, b = map(int, input.split(" "))
    print lcm(a, b)