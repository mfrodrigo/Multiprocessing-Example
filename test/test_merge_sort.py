"""
Tests merge sort algorithm.
"""


import pytest
from sorting_method.merge_sort import merge_sort
from multiprocessing_sorting_method.multiprocessing_merge_sort import multiprocessing_merge_sort


class TestMergeSort:
    """
    Class to test merge sort method.
    """
    @pytest.fixture(scope="class")
    def value_list(self):
        """ Creates unsorted list to perform test. """
        return [12, 11, 13, 5, 6, 7]

    def test_merge_sort_6_element(self, value_list):
        """ Tests merge sort algorithm with 6 elements. """
        expected = [5, 6, 7, 11, 12, 13]
        merge_sort(value_list)
        assert expected == value_list

    def test_multiprocessing_merge_sort_6_element(self, value_list):
        """ Tests merge sort algorithm with 6 elements. """
        expected = [5, 6, 7, 11, 12, 13]
        counter_processing = 0
        multiprocessing_merge_sort(value_list, counter_processing)
        assert expected == value_list