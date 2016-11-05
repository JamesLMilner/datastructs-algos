# Uses python3
import sys

def get_majority_element(input_array, left, right):
    
    length = len(input_array)
    final_el = False

    if (len(input_array) % 2 == 1):
        final_el = input_array[-1]
        length = len(input_array)-1

    paired = []

    for i in range(0, length, 2):
        if input_array[i] == input_array[i+1] and input_array[i] not in paired:
            paired.append(input_array[i])

    half = int(len(input_array) / 2)
    if len(paired) > 0:
        for j in paired:

            if final_el == j and input_array.count(j) + 1 > half:
                return 1
            elif input_array.count(j) > half:
                return 1
    elif final_el and input_array.count(final_el) > half:
        return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *input_array = list(map(int, input.split()))
    print(get_majority_element(input_array, n, 1))

