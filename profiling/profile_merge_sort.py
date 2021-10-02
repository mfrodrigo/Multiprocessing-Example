"""
Profiles merge_sort and multiprocessing_merge_sort
"""

import numpy as np
from sorting_method.merge_sort import merge_sort
from multiprocessing_sorting_method.multiprocessing_merge_sort import multiprocessing_merge_sort

if __name__ == "__main__":
    example = list(np.random.randint(0, 1000, 10000000))
    example2 = example.copy()
    merge_sort(example)
    multiprocessing_merge_sort(example2, 0)

