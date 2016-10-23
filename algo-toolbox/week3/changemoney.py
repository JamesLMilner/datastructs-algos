#python2

def changemoney(n):
    fives = 0
    ones = 0
    tens = int(n / 10)
    tens_leftover = n % 10

    if tens_leftover >= 5:
        fives = 1
        ones = tens_leftover - 5
    else:
        ones = tens_leftover

    return tens + fives + ones

if __name__ == "__main__":
    n = int(raw_input())
    print(changemoney(n))
