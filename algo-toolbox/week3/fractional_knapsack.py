# Uses python3
import sys

def get_optimal_value(n, capacity, weights, values):

    total = len(weights)
    ratios = []

    for i in range(0, total):
        ratio = float(values[i] / weights[i])
        ratios.append(ratio)

    # Sort Descending
    sorted_ratios = ratios[:]
    sorted_ratios.sort()
    sorted_ratios.reverse()

    total_value = 0
    index = 0
    available_capacity = capacity

    while available_capacity > 0:

        if index < n:

            pos = ratios.index(sorted_ratios[index])

            if weights[pos] <= available_capacity: # 30 / 200 = 0.15

                total_value += values[pos]
                index += 1
                available_capacity = available_capacity - weights[pos]

            else:
                available_weight = (weights[pos] / available_capacity) * available_capacity # i.e. 50 / 60 = 0.81 * 50 = 41.6
                total_value += (values[pos] / available_weight) * available_capacity
                break

        else:
            break


    return total_value

#Example
#3 50 60 20 100 50 120 30


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n, capacity, weights, values)
    print("{:.10f}".format(opt_value))
