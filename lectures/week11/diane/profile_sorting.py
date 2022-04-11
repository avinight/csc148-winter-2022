"""Timing experiments for various sorting algorithms

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This file contains code to compare the run-time performance of various
sorting algorithms.
"""

import random
from typing import Any, Callable, List
import timeit

import matplotlib.pyplot as plt

from sorting import mergesort, quicksort, insertion_sort
# from in_place_quicksort import in_place_quicksort
from timsort import timsort2


SIZES = [2000 * i for i in range(1, 8)]  # [1000, 2000, 3000, 4000, 8000]
NUM_TRIALS = 3
SHUFFLE = True


def profile_alg(sizes: List[int], alg: Callable[[List], Any],
                shuffle: bool = True) -> List[float]:
    """Return a list of times for the algorithm."""
    times = []
    for size in sizes:
        for _ in range(NUM_TRIALS):
            lst = list(range(size))
            if shuffle:
                random.shuffle(lst)

            time = min(timeit.repeat('lst1 = lst[:]; alg(lst1)',
                                     repeat=10, number=1, globals=locals()))
            times.append(time)
    return times


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(20000)

    times = {
        'mergesort': profile_alg(SIZES, mergesort, shuffle=SHUFFLE),
        'quicksort': profile_alg(SIZES, quicksort, shuffle=SHUFFLE),
        # 'in_place_quicksort': profile_alg(SIZES, in_place_quicksort, shuffle=SHUFFLE),
        # 'insertion sort': profile_alg(SIZES, insertion_sort, shuffle=SHUFFLE)
        # 'timsort': profile_alg(SIZES, timsort2, shuffle=SHUFFLE),
        # 'list.sort': profile_alg(SIZES, list.sort, shuffle=SHUFFLE)
    }

    max_time = max(sum(times.values(), []))

    all_sizes = [x for x in SIZES for _ in range(NUM_TRIALS)]
    plt.plot(all_sizes, times['mergesort'], 'ro', label='mergesort')
    plt.plot(all_sizes, times['quicksort'], 'bo', label='quicksort')
    # plt.plot(all_sizes, times['in_place_quicksort'], 'co', label='in_place_quicksort')
    # plt.plot(all_sizes, times['timsort'], 'mo', label='timsort')
    # plt.plot(all_sizes, times['insertion sort'], 'go', label='insertion sort')
    # plt.plot(all_sizes, times['list.sort'], 'y*', label='list.sort', markersize=16)

    plt.axis([0, max(SIZES) * 1.05, 0, 1.05 * max_time])
    plt.legend()
    plt.show()
