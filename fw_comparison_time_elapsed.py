import sys
import time

import Floyd_warshall_imperative_solution
import Floyd_warshall_recursive_solution


def compare_performance():


    NO_PATH = sys.maxsize
    GRAPH = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0],
    ]

    started_at = time.time()
    for _ in range(2**12):
        Floyd_warshall_imperative_solution.floyd(GRAPH)
    elapsed_imperative = time.time() - started_at

    # above function measure the time elapsed for imperative solution
    # to complete the test

    started_at = time.time()
    for _ in range(2**12):
        Floyd_warshall_recursive_solution.fw_recursive(GRAPH)
    elapsed_recursive = time.time() - started_at

    # above function measure the time elapsed for recursive solution
    # to complete the test

    return (elapsed_imperative, elapsed_recursive)

# the purpose of the above function is to compare the performance 
# of both the imperative and recursive functions using time elapsed
# ideally the function that takes less time will pass the test


if __name__ == '__main__':
    elapsed_imperative, elapsed_recursive = compare_performance()
    print('imperative: {}s'.format(round(elapsed_imperative, 4)))
    print('recursive: {}s'.format(round(elapsed_recursive, 4)))

    # above function formats the time to 4 decimal points