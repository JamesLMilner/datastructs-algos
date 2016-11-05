# Uses python3
import sys
import random

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    lt = l
    gt = r
    i = lt

    while i <= gt:
        partition_item = a[lt]

        if a[i] < partition_item:

            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1

        elif a[i] > partition_item:
            a[gt], a[i] = a[i], a[gt]
            gt -= 1

        elif a[i] == partition_item:
            i += 1

    randomized_quick_sort(a, l, lt - 1);
    randomized_quick_sort(a, gt + 1, r);

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
