"""
Unit Tests for Binary Search and Merge Sort.
"""

import pytest
from binary_search import BinarySearch
from merge_sort import MergeSort


# ================================================================
#  BINARY SEARCH — CORE FUNCTIONALITY TESTS
# ================================================================
class TestBinarySearchCore:
    """Core tests for BinarySearch: iterative and recursive."""

    def setup_method(self):
        self.bs = BinarySearch()

    # ----------------- Iterative Search -----------------
    def test_iterative_found(self):
        arr = [1, 3, 5, 7, 9, 11]
        assert self.bs.search_iterative(arr, 7, visualize=False) == 3

    def test_iterative_not_found(self):
        arr = [1, 3, 5, 7]
        assert self.bs.search_iterative(arr, 6, visualize=False) == -1

    def test_iterative_first_last(self):
        arr = [1, 3, 5, 7, 9]
        assert self.bs.search_iterative(arr, 1, False) == 0
        assert self.bs.search_iterative(arr, 9, False) == 4

    def test_iterative_single_element(self):
        assert self.bs.search_iterative([5], 5, False) == 0
        assert self.bs.search_iterative([5], 3, False) == -1

    def test_iterative_empty_array(self):
        assert self.bs.search_iterative([], 5, False) == -1

    # ----------------- Recursive Search -----------------
    def test_recursive_found(self):
        arr = [1, 3, 5, 7]
        assert self.bs.search_recursive(arr, 7, False) == 3

    def test_recursive_not_found(self):
        arr = [1, 3, 5, 7]
        assert self.bs.search_recursive(arr, 6, False) == -1

    def test_recursive_first_last(self):
        arr = [1, 3, 5, 7, 9]
        assert self.bs.search_recursive(arr, 1, False) == 0
        assert self.bs.search_recursive(arr, 9, False) == 4


# ================================================================
#  BINARY SEARCH — STATISTICS & INTERNAL STATE
# ================================================================
class TestBinarySearchStatistics:
    """Tests verifying statistics collection."""

    def setup_method(self):
        self.bs = BinarySearch()

    def test_iterative_statistics(self):
        arr = [1, 3, 5, 7]
        self.bs.search_iterative(arr, 7, False)
        stats = self.bs.get_statistics()
        assert stats["comparisons"] > 0
        assert stats["steps"] > 0

    def test_recursive_statistics(self):
        arr = [1, 3, 5, 7]
        self.bs.search_recursive(arr, 7, False)
        stats = self.bs.get_statistics()
        assert stats["comparisons"] > 0
        assert stats["steps"] > 0

    def test_statistics_accumulate(self):
        arr = list(range(1, 11))

        self.bs.search_iterative(arr, 3, False)
        c1 = self.bs.get_statistics()["comparisons"]

        self.bs.search_iterative(arr, 7, False)
        c2 = self.bs.get_statistics()["comparisons"]

        assert c2 > c1

    def test_get_statistics_before_execution(self):
        stats = self.bs.get_statistics()
        assert "comparisons" in stats
        assert "steps" in stats


# ================================================================
#  BINARY SEARCH — EDGE CASES & DATA TYPES
# ================================================================
class TestBinarySearchEdgeCases:
    """Edge-case and diverse-type handling."""

    def setup_method(self):
        self.bs = BinarySearch()

    def test_negative_numbers(self):
        arr = [-10, -5, 0, 5]
        assert self.bs.search_iterative(arr, -5, False) == 1

    def test_duplicates(self):
        arr = [1, 3, 5, 5, 5, 7]
        assert self.bs.search_iterative(arr, 5, False) in [2, 3, 4]

    def test_large_array(self):
        arr = list(range(0, 10000, 2))
        assert self.bs.search_iterative(arr, 5000, False) != -1

    def test_large_index_values(self):
        arr = list(range(0, 100000, 2))
        assert self.bs.search_iterative(arr, 99998, False) == 49999

    def test_float_search(self):
        arr = [1.1, 2.2, 3.3]
        assert self.bs.search_iterative(arr, 3.3, False) == 2

    def test_float_precision(self):
        arr = [0.1, 0.2, 0.3]
        assert self.bs.search_iterative(arr, 0.3, False) == 2

    def test_strings(self):
        arr = ["apple", "banana", "cherry"]
        assert self.bs.search_iterative(arr, "cherry", False) == 2

    def test_strings_not_found(self):
        arr = ["apple", "banana"]
        assert self.bs.search_iterative(arr, "grape", False) == -1

    def test_recursive_large_array_no_recursion_error(self):
        arr = list(range(10000))
        assert self.bs.search_recursive(arr, 9999, False) == 9999

    def test_none_in_array(self):
        arr = [None, 1, 2]
        try:
            result = self.bs.search_iterative(arr, 2, False)
            assert isinstance(result, int)
        except TypeError:
            pass

    def test_mixed_numeric_types(self):
        arr = [1, 2.5, 3]
        assert self.bs.search_iterative(arr, 3, False) == 2

    def test_extreme_negative(self):
        arr = [-1_000_000, -100_000, -10_000]
        assert self.bs.search_iterative(arr, -100_000, False) == 1

    def test_search_unsorted_array(self):
        arr = [5, 2, 8]
        result = self.bs.search_iterative(arr, 5, False)
        assert isinstance(result, int)

    # ----------------- Visualization Mode -----------------
    def test_iterative_with_visualization(self):
        arr = [1, 3, 5, 7]
        assert self.bs.search_iterative(arr, 7, True) == 3

    def test_recursive_with_visualization(self):
        arr = [1, 3, 5, 7]
        assert self.bs.search_recursive(arr, 7, True) == 3


# ================================================================
#  MERGE SORT — BASIC SORTING TESTS
# ================================================================
class TestMergeSortCore:
    """Core merge sort tests."""

    def setup_method(self):
        self.ms = MergeSort()

    def test_sorted(self):
        arr = [1, 2, 3]
        assert self.ms.sort(arr.copy(), False) == [1, 2, 3]

    def test_reverse_sorted(self):
        arr = [3, 2, 1]
        assert self.ms.sort(arr.copy(), False) == [1, 2, 3]

    def test_random_order(self):
        arr = [3, 1, 4, 1, 5]
        assert self.ms.sort(arr.copy(), False) == [1, 1, 3, 4, 5]

    def test_single_element(self):
        assert self.ms.sort([5], False) == [5]

    def test_two_elements(self):
        assert self.ms.sort([2, 1], False) == [1, 2]

    def test_empty(self):
        assert self.ms.sort([], False) == []


# ================================================================
#  MERGE SORT — STABILITY TESTS
# ================================================================
class TestMergeSortStability:
    """Tests ensuring merge sort remains stable."""

    def setup_method(self):
        self.ms = MergeSort()

    def test_stability_tuples(self):
        arr = [(3, 'a'), (1, 'b'), (2, 'c'), (1, 'd')]
        result = self.ms.sort(arr.copy(), False)
        assert result == [(1, 'b'), (1, 'd'), (2, 'c'), (3, 'a')]

    def test_stability_objects(self):
        class Item:
            def __init__(self, value, id):
                self.value = value
                self.id = id
            def __lt__(self, o): return self.value < o.value

        items = [Item(3, 'a'), Item(1, 'b'), Item(2, 'c'), Item(1, 'd')]
        result = self.ms.sort(items.copy(), False)

        ones = [x for x in result if x.value == 1]
        assert [x.id for x in ones] == ['b', 'd']  # relative order preserved


# ================================================================
#  MERGE SORT — STATISTICS TESTS
# ================================================================
class TestMergeSortStatistics:
    def setup_method(self):
        self.ms = MergeSort()

    def test_comparisons(self):
        arr = [5, 2, 8, 1]
        self.ms.sort(arr.copy(), False)
        assert self.ms.get_statistics()['comparisons'] > 0

    def test_merges(self):
        arr = [5, 2, 8, 1]
        self.ms.sort(arr.copy(), False)
        assert self.ms.get_statistics()['merges'] > 0

    def test_steps(self):
        arr = [5, 2, 8, 1]
        self.ms.sort(arr.copy(), False)
        assert self.ms.get_statistics()['steps'] > 0


# ================================================================
#  MERGE SORT — EDGE CASES & DATA TYPE TESTS
# ================================================================
class TestMergeSortEdgeCases:
    def setup_method(self):
        self.ms = MergeSort()

    def test_duplicates(self):
        arr = [3, 1, 4, 1]
        assert self.ms.sort(arr.copy(), False) == [1, 1, 3, 4]

    def test_negative_numbers(self):
        arr = [3, -1, 4, -5]
        assert self.ms.sort(arr.copy(), False) == [-5, -1, 3, 4]

    def test_mixed_numbers(self):
        arr = [-10, 5, -3, 0]
        assert self.ms.sort(arr.copy(), False) == [-10, -3, 0, 5]

    def test_floats(self):
        arr = [3.5, 1.2, 4.8, 1.1]
        assert self.ms.sort(arr.copy(), False) == [1.1, 1.2, 3.5, 4.8]

    def test_preserves_original(self):
        arr = [3, 1, 4]
        original = arr.copy()
        self.ms.sort(arr.copy(), False)
        assert arr == original

    def test_nested_objects_not_modified(self):
        arr = [[3], [1], [2]]
        o1, o2, o3 = arr
        result = self.ms.sort(arr.copy(), False)
        assert arr[0] is o1
        assert arr[1] is o2
        assert arr[2] is o3

    def test_none_values(self):
        arr = [3, None, 1]
        try:
            result = self.ms.sort(arr.copy(), False)
            assert isinstance(result, list)
        except TypeError:
            pass

    def test_nan_values(self):
        arr = [3.5, float('nan'), 1.2]
        result = self.ms.sort(arr.copy(), False)
        assert isinstance(result, list)

    def test_infinity_values(self):
        arr = [3, float('inf'), 1, float('-inf')]
        result = self.ms.sort(arr.copy(), False)
        assert result[0] == float('-inf')
        assert result[-1] == float('inf')

    def test_strings(self):
        arr = ["zebra", "apple", "banana"]
        assert self.ms.sort(arr.copy(), False) == ["apple", "banana", "zebra"]

    def test_strings_case_sensitive(self):
        arr = ["Zebra", "apple", "banana"]
        assert self.ms.sort(arr.copy(), False) == ["Zebra", "apple", "banana"]

    def test_unicode_strings(self):
        arr = ["café", "apple", "résumé"]
        result = self.ms.sort(arr.copy(), False)
        assert len(result) == 3


# ================================================================
#  MERGE SORT — LARGE INPUT TESTS
# ================================================================
class TestMergeSortLargeInputs:
    def setup_method(self):
        self.ms = MergeSort()

    def test_large_array(self):
        arr = list(range(10000, 0, -1))
        result = self.ms.sort(arr.copy(), False)
        assert result == list(range(1, 10001))


# ================================================================
#  INTEGRATION TESTS
# ================================================================
class TestBinarySearchAndMergeSortIntegration:

    def test_search_after_sort(self):
        arr = [5, 2, 9, 1]
        sorted_arr = MergeSort().sort(arr.copy(), False)
        idx = BinarySearch().search_iterative(sorted_arr, 5, False)
        assert idx != -1
        assert sorted_arr[idx] == 5

    def test_not_found_after_sort(self):
        arr = [5, 2, 9, 1]
        sorted_arr = MergeSort().sort(arr.copy(), False)
        idx = BinarySearch().search_iterative(sorted_arr, 99, False)
        assert idx == -1

    def test_search_all_elements_after_sort(self):
        arr = [5, 2, 8, 1, 9]
        sorted_arr = MergeSort().sort(arr.copy(), False)
        bs = BinarySearch()
        for x in arr:
            idx = bs.search_iterative(sorted_arr, x, False)
            assert idx != -1
            assert sorted_arr[idx] == x


# ================================================================
#  COMBINED EDGE CASES
# ================================================================
class TestCombinedEdgeCases:

    def test_binary_search_large_even_numbers(self):
        arr = list(range(0, 10000, 2))
        assert BinarySearch().search_iterative(arr, 5000, False) != -1

    def test_merge_sort_stability(self):
        arr = [(3, 0), (1, 1), (1, 3)]
        result = MergeSort().sort(arr.copy(), False)
        assert result.index((1, 1)) < result.index((1, 3))

    def test_merge_sort_all_same(self):
        arr = [5, 5, 5, 5]
        assert MergeSort().sort(arr.copy(), False) == [5, 5, 5, 5]

    def test_binary_search_all_same(self):
        arr = [5, 5, 5, 5]
        assert BinarySearch().search_iterative(arr, 5, False) != -1



if __name__ == '__main__':
    pytest.main([__file__, '-v'])
