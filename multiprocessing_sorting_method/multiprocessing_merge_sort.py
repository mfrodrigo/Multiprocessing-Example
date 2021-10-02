"""
Python program for implementation of MergeSort
"""
import multiprocessing


def multiprocessing_merge_sort(unsorted_list, counter_processing):
    """
    Recursive method to sort list. This method has pass-by-reference argument,
    so it doesn't need to return the sorted list in the end.
    Args:
        unsorted_list: (list) list with unsorted elements
        counter_processing: (int)
    """
    print(counter_processing)
    if len(unsorted_list) > 1:

        middle_list = len(unsorted_list) // 2
        left_list = unsorted_list[:middle_list]
        right_list = unsorted_list[middle_list:]
        if not counter_processing >= multiprocessing.cpu_count():
            counter_processing += 2
            processing_1 = multiprocessing.Process(target=multiprocessing_merge_sort, args=(left_list,
                                                                                            counter_processing))
            processing_2 = multiprocessing.Process(target=multiprocessing_merge_sort, args=(right_list,
                                                                                            counter_processing))
            processing_1.start()
            processing_2.start()
            processing_1.join()
            processing_2.join()
        else:
            multiprocessing_merge_sort(left_list, counter_processing)
            multiprocessing_merge_sort(right_list, counter_processing)

        i = j = k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                unsorted_list[k] = left_list[i]
                i += 1
            else:
                unsorted_list[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            unsorted_list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            unsorted_list[k] = right_list[j]
            j += 1
            k += 1
