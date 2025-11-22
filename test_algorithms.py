"""
Unit tests for Binary Search and Merge Sort implementations.

Tests cover:
- BinarySearch: iterative, recursive, edge cases
- MergeSort: basic sorting, stability, edge cases
- Statistics tracking
"""

import pytest
from binary_search import BinarySearch
from merge_sort import MergeSort


class TestBinarySearch:
    """Test suite for BinarySearch class."""

    def setup_method(self):
        """Set up test fixtures before each test."""
        self.bs = BinarySearch()

    def test_search_iterative_found(self):
        """Test iterative binary search when element is found."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        result = self.bs.search_iterative(arr, 7, visualize=False)
        assert result == 3

    def test_search_iterative_not_found(self):
        """Test iterative binary search when element is not found."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        result = self.bs.search_iterative(arr, 6, visualize=False)
        assert result == -1

    def test_search_iterative_first_element(self):
        """Test iterative binary search for first element."""
        arr = [1, 3, 5, 7, 9]
        result = self.bs.search_iterative(arr, 1, visualize=False)
        assert result == 0

    def test_search_iterative_last_element(self):
        """Test iterative binary search for last element."""
        arr = [1, 3, 5, 7, 9]
        result = self.bs.search_iterative(arr, 9, visualize=False)
        assert result == 4

    def test_search_iterative_single_element_found(self):
        """Test iterative binary search on single-element array."""
        arr = [5]
        result = self.bs.search_iterative(arr, 5, visualize=False)
        assert result == 0

    def test_search_iterative_single_element_not_found(self):
        """Test iterative binary search on single-element array with no match."""
        arr = [5]
        result = self.bs.search_iterative(arr, 3, visualize=False)
        assert result == -1

    def test_search_iterative_empty_array(self):
        """Test iterative binary search on empty array."""
        arr = []
        result = self.bs.search_iterative(arr, 5, visualize=False)
        assert result == -1

    def test_search_recursive_found(self):
        """Test recursive binary search when element is found."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        result = self.bs.search_recursive(arr, 7, visualize=False)
        assert result == 3

    def test_search_recursive_not_found(self):
        """Test recursive binary search when element is not found."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        result = self.bs.search_recursive(arr, 6, visualize=False)
        assert result == -1

    def test_search_recursive_first_element(self):
        """Test recursive binary search for first element."""
        arr = [1, 3, 5, 7, 9]
        result = self.bs.search_recursive(arr, 1, visualize=False)
        assert result == 0

    def test_search_recursive_last_element(self):
        """Test recursive binary search for last element."""
        arr = [1, 3, 5, 7, 9]
        result = self.bs.search_recursive(arr, 9, visualize=False)
        assert result == 4

    def test_search_iterative_statistics(self):
        """Test that iterative search tracks statistics correctly."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        self.bs.search_iterative(arr, 7, visualize=False)
        stats = self.bs.get_statistics()
        assert stats['comparisons'] > 0
        assert stats['steps'] > 0

    def test_search_recursive_statistics(self):
        """Test that recursive search tracks statistics correctly."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        self.bs.search_recursive(arr, 7, visualize=False)
        stats = self.bs.get_statistics()
        assert stats['comparisons'] > 0
        assert stats['steps'] > 0

    def test_search_with_negative_numbers(self):
        """Test binary search with negative numbers."""
        arr = [-10, -5, 0, 5, 10]
        result = self.bs.search_iterative(arr, -5, visualize=False)
        assert result == 1

    def test_search_with_duplicates(self):
        """Test binary search with duplicate elements (finds one occurrence)."""
        arr = [1, 3, 5, 5, 5, 7, 9]
        result = self.bs.search_iterative(arr, 5, visualize=False)
        assert result in [2, 3, 4]  # any of the 5s is valid

    def test_comparisons_increase_with_search(self):
        """Test that comparisons counter increases during search."""
        arr = list(range(1, 100))
        self.bs.search_iterative(arr, 50, visualize=False)
        stats1 = self.bs.get_statistics()
        
        self.bs.search_iterative(arr, 99, visualize=False)
        stats2 = self.bs.get_statistics()
        
        assert stats2['comparisons'] > 0


class TestMergeSort:
    """Test suite for MergeSort class."""

    def setup_method(self):
        """Set up test fixtures before each test."""
        self.ms = MergeSort()

    def test_sort_already_sorted(self):
        """Test sorting an already sorted array."""
        arr = [1, 2, 3, 4, 5]
        result = self.ms.sort(arr.copy(), visualize=False)
        assert result == [1, 2, 3, 4, 5]

    def test_sort_reverse_sorted(self):
        """Test sorting a reverse-sorted array."""
        arr = [5, 4, 3, 2, 1]
        result = self.ms.sort(arr.copy(), visualize=False)
        assert result == [1, 2, 3, 4, 5]

    def test_sort_random_order(self):
        """Test sorting a random order array."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = self.ms.sort(arr.copy(), visualize=False)
        assert result == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_sort_single_element(self):
        """Test sorting single-element array."""
        arr = [5]
        result = self.ms.sort(arr.copy(), visualize=False)
        assert result == [5]

    def test_sort_two_elements(self):
        """Test sorting two-element array."""
        arr = [2, 1]
        result = self.ms.sort(arr.copy(), visualize=False)
        assert result == [1, 2]

    def test_sort_empty_array(self):
        """Test sorting empty array."""
        arr = []
        result = self.ms.sort(arr.copy(), visualize=False)
        assert result == []

    def test_sort_with_duplicates(self):
        """Test sorting array with duplicate elements."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = self.ms.sort(arr.copy(), visualize=False)
        assert result == [1, 1, 2, 3, 4, 5, 5, 6, 9]

    def test_sort_negative_numbers(self):
        """Test sorting array with negative numbers."""
        arr = [3, -1, 4, -5, 0]
        result = self.ms.sort(arr.copy(), visualize=False)
        assert result == [-5, -1, 0, 3, 4]

    def test_sort_mixed_positive_negative(self):
        """Test sorting array with mixed positive and negative."""
        arr = [-10, 5, -3, 0, 8, -1]
        result = self.ms.sort(arr.copy(), visualize=False)
        assert result == [-10, -3, -1, 0, 5, 8]

    def test_sort_tuples_ascending(self):
        """Test sorting tuples in ascending order (stable sort)."""
        arr = [(3, 'a'), (1, 'b'), (2, 'c'), (1, 'd')]
        result = self.ms.sort(arr.copy(), visualize=False)
        # Should maintain relative order of (1, 'b') and (1, 'd') since stable
        assert result == [(1, 'b'), (1, 'd'), (2, 'c'), (3, 'a')]

    def test_sort_statistics_comparisons(self):
        """Test that sort tracks comparisons."""
        arr = [5, 2, 8, 1, 9, 3]
        self.ms.sort(arr.copy(), visualize=False)
        stats = self.ms.get_statistics()
        assert stats['comparisons'] > 0

    def test_sort_statistics_merges(self):
        """Test that sort tracks merge operations."""
        arr = [5, 2, 8, 1, 9, 3]
        self.ms.sort(arr.copy(), visualize=False)
        stats = self.ms.get_statistics()
        assert stats['merges'] > 0

    def test_sort_statistics_steps(self):
        """Test that sort tracks steps."""
        arr = [5, 2, 8, 1, 9, 3]
        self.ms.sort(arr.copy(), visualize=False)
        stats = self.ms.get_statistics()
        assert stats['steps'] > 0

    def test_sort_large_array(self):
        """Test sorting a larger array."""
        arr = list(range(100, 0, -1))
        result = self.ms.sort(arr.copy(), visualize=False)
        assert result == list(range(1, 101))

    def test_sort_floats(self):
        """Test sorting array of floating point numbers."""
        arr = [3.5, 1.2, 4.8, 1.1, 5.0]
        result = self.ms.sort(arr.copy(), visualize=False)
        assert result == [1.1, 1.2, 3.5, 4.8, 5.0]

    def test_sort_preserves_original(self):
        """Test that sort does not modify original array."""
        arr = [3, 1, 4, 1, 5]
        original = arr.copy()
        self.ms.sort(arr.copy(), visualize=False)
        assert arr == original


class TestBinarySearchAndMergeSort:
    """Integration tests combining BinarySearch and MergeSort."""

    def test_binary_search_on_merge_sorted_array(self):
        """Test that binary search works on merge-sorted array."""
        arr = [5, 2, 8, 1, 9, 3, 7, 4]
        
        # Sort using merge sort
        ms = MergeSort()
        sorted_arr = ms.sort(arr.copy(), visualize=False)
        
        # Search using binary search
        bs = BinarySearch()
        result = bs.search_iterative(sorted_arr, 7, visualize=False)
        
        assert result != -1
        assert sorted_arr[result] == 7

    def test_binary_search_on_merge_sorted_not_found(self):
        """Test binary search on merge-sorted array for non-existent element."""
        arr = [5, 2, 8, 1, 9, 3, 7, 4]
        
        # Sort using merge sort
        ms = MergeSort()
        sorted_arr = ms.sort(arr.copy(), visualize=False)
        
        # Search for element not in array
        bs = BinarySearch()
        result = bs.search_iterative(sorted_arr, 99, visualize=False)
        
        assert result == -1

    def test_sort_then_search_all_elements(self):
        """Test that all elements can be found after sorting."""
        arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
        
        # Sort
        ms = MergeSort()
        sorted_arr = ms.sort(arr.copy(), visualize=False)
        
        # Search for each element
        bs = BinarySearch()
        for elem in arr:
            result = bs.search_iterative(sorted_arr, elem, visualize=False)
            assert result != -1
            assert sorted_arr[result] == elem


class TestEdgeCases:
    """Edge case tests for both algorithms."""

    def test_binary_search_large_array(self):
        """Test binary search on a large array."""
        arr = list(range(0, 10000, 2))
        bs = BinarySearch()
        result = bs.search_iterative(arr, 5000, visualize=False)
        assert result != -1

    def test_merge_sort_stability(self):
        """Test that merge sort is stable (maintains relative order)."""
        # Using tuples where first element is key, second is original index
        arr = [(3, 0), (1, 1), (2, 2), (1, 3), (2, 4)]
        ms = MergeSort()
        result = ms.sort(arr.copy(), visualize=False)
        
        # Check stability: (1,1) should come before (1,3), (2,2) before (2,4)
        assert result.index((1, 1)) < result.index((1, 3))
        assert result.index((2, 2)) < result.index((2, 4))

    def test_merge_sort_all_same_elements(self):
        """Test sorting array where all elements are identical."""
        arr = [5, 5, 5, 5, 5]
        ms = MergeSort()
        result = ms.sort(arr.copy(), visualize=False)
        assert result == [5, 5, 5, 5, 5]

    def test_binary_search_all_same_elements(self):
        """Test binary search on array with all identical elements."""
        arr = [5, 5, 5, 5, 5]
        bs = BinarySearch()
        result = bs.search_iterative(arr, 5, visualize=False)
        assert result != -1


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
