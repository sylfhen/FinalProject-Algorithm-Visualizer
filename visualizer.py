"""
Visualization utilities for algorithm demonstrations
"""

import time
import math
from settings import LINE_WIDTH

class Visualizer:
    @staticmethod
    def print_array_bar_chart(arr, highlight_indices=None, title="Array Visualization"):
        """
        Create a simple bar chart visualization of an array
        
        Args:
            arr: List of numbers to visualize
            highlight_indices: List of indices to highlight
            title: Chart title
        """
        if not arr:
            return
        
        print("\n" + "=" * LINE_WIDTH)
        print(title)
        print("=" * LINE_WIDTH)
        
        max_val = max(arr)
        height = 10
        
        for level in range(height, 0, -1):
            line = ""
            for i, val in enumerate(arr):
                threshold = (level / height) * max_val
                if val >= threshold:
                    if highlight_indices and i in highlight_indices:
                        line += " ■ "
                    else:
                        line += " █ "
                else:
                    line += "   "
            print(line)
        
        # Print values
        print("─" * (len(arr) * 3))
        values_line = ""
        for val in arr:
            values_line += f"{val:2d} "
        print(values_line)
        print("=" * LINE_WIDTH)
    
    @staticmethod
    def print_algorithm_complexity():
        """Display time complexity information"""
        print("\n" + "=" * LINE_WIDTH)
        print(" " * 20 + "ALGORITHM COMPLEXITY")
        print("=" * LINE_WIDTH)
        print("\nBINARY SEARCH:")
        print("  Time Complexity:  O(log n)")
        print("  Space Complexity: O(1) - iterative, O(log n) - recursive")
        print("  Best Case:        O(1) - element at middle")
        print("  Worst Case:       O(log n) - element not found")
        print("  Requirement:      Array must be sorted!")
        
        print("\nMERGE SORT:")
        print("  Time Complexity:  O(n log n)")
        print("  Space Complexity: O(n)")
        print("  Best Case:        O(n log n)")
        print("  Worst Case:       O(n log n)")
        print("  Stability:        Stable sort (preserves order of equal elements)")
        print("=" * LINE_WIDTH)
    
    @staticmethod
    def print_comparison_table(data_sizes, binary_search_times, merge_sort_times):
        """
        Print a comparison table of algorithm performance
        
        Args:
            data_sizes: List of data sizes tested
            binary_search_times: List of binary search operation counts
            merge_sort_times: List of merge sort operation counts
        """
        print("\n" + "=" * LINE_WIDTH)
        print(" " * 20 + "PERFORMANCE COMPARISON")
        print("=" * LINE_WIDTH)
        print(f"{'Data Size':<15} {'Binary Search':<20} {'Merge Sort':<20}")
        print(f"{'(n)':<15} {'Operations':<20} {'Operations':<20}")
        print("-" * LINE_WIDTH)
        
        for i in range(len(data_sizes)):
            print(f"{data_sizes[i]:<15} {binary_search_times[i]:<20} {merge_sort_times[i]:<20}")
        
        print("=" * LINE_WIDTH)
        print("Note: Binary Search requires sorted data (use Merge Sort first!)")
        print("=" * LINE_WIDTH)
