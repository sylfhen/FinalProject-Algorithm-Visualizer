"""
Merge Sort Algorithm Implementation
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

import sys

from settings import LINE_WIDTH


class MergeSort:
    def __init__(self):
        self.comparisons = 0
        self.merges = 0
        self.steps = []
    
    def sort(self, arr, visualize=False):
        """
        Main merge sort function
        
        Args:
            arr: List to be sorted
            visualize: Boolean to enable visualization
        
        Returns:
            Sorted list
        """
        self.comparisons = 0
        self.merges = 0
        self.steps = []
        
        if len(arr) <= 1:
            return arr
        
        result = self._merge_sort_recursive(arr.copy(), 0, len(arr) - 1, visualize)
        return result
    
    def _merge_sort_recursive(self, arr, left, right, visualize):
        """
        Recursive merge sort helper
        
        Args:
            arr: Array to sort
            left: Left boundary
            right: Right boundary
            visualize: Visualization flag
        
        Returns:
            Sorted portion of array
        """
        if left >= right:
            return arr
        
        mid = (left + right) // 2
        
        if visualize:
            self._visualize_divide(arr, left, mid, right)
        
        # Divide
        self._merge_sort_recursive(arr, left, mid, visualize)
        self._merge_sort_recursive(arr, mid + 1, right, visualize)
        
        # Conquer (Merge)
        self._merge(arr, left, mid, right, visualize)
        
        return arr
    
    def _merge(self, arr, left, mid, right, visualize):
        """
        Merge two sorted subarrays
        
        Args:
            arr: Array containing subarrays
            left: Start of left subarray
            mid: End of left subarray
            right: End of right subarray
            visualize: Visualization flag
        """
        # Create temporary arrays
        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        # Merge process
        while i < len(left_part) and j < len(right_part):
            self.comparisons += 1

            if self._le(left_part[i], right_part[j]):
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1
        
        # Copy remaining elements
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
        
        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
        
        self.merges += 1
        
        if visualize:
            self._visualize_merge(arr, left, mid, right, left_part, right_part)
        
        self.steps.append({
            'left': left,
            'mid': mid,
            'right': right,
            'result': arr[left:right + 1].copy()
        })
    
    def _visualize_divide(self, arr, left, mid, right):
        """Visualize the divide step with colored output"""
        # ANSI color codes
        RED = '\033[91m'
        GREEN = '\033[92m'
        RESET = '\033[0m'
        
        print("\n" + "-" * LINE_WIDTH)
        print("DIVIDE STEP")
        
        # Show only the section being divided with colors
        section_display = []
        for i in range(left, right + 1):
            if i <= mid:
                section_display.append(f"{RED}{arr[i]}{RESET}")
            else:
                section_display.append(f"{GREEN}{arr[i]}{RESET}")
        
        print(f"Splitting: [{', '.join(section_display)}]")
        
        # Display left half on left side and right half on right side
        left_str = f"{RED}{arr[left:mid + 1]}{RESET}"
        right_str = f"{GREEN}{arr[mid + 1:right + 1]}{RESET}"
        
        # Calculate spacing to position halves on left and right
        max_half_width = LINE_WIDTH // 2 - 5
        print(f"{left_str:<{max_half_width}}{right_str:>{max_half_width}}")
        
        try:
            if sys.stdin.isatty():
                input("Press Enter to continue...")
        except Exception:
            pass
    
    def _visualize_merge(self, arr, left, mid, right, left_part, right_part):
        """Visualize the merge step with colored output"""
        # ANSI color codes
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RESET = '\033[0m'
        
        print("\n" + "-" * LINE_WIDTH)
        print("MERGE STEP")
        print(f"{RED}Left:  {left_part}{RESET}")
        print(f"{GREEN}Right: {right_part}{RESET}")
        
        # Show the merged result in yellow
        merged_result = arr[left:right + 1]
        print(f"{YELLOW}Merged: {merged_result}{RESET}")
        try:
            if sys.stdin.isatty():
                input("Press Enter to continue...")
        except Exception:
            pass

    def _le(self, a, b):
        """Less-or-equal comparator that falls back to __lt__ if __le__ is not defined.

        This preserves stability: when elements compare equal (neither a<b nor b<a)
        we treat a <= b as True so the left element stays before the right.
        """
        try:
            return a <= b
        except TypeError:
            # Try to use __lt__ if __le__ isn't available
            try:
                if a < b:
                    return True
            except Exception:
                pass
            try:
                if b < a:
                    return False
            except Exception:
                pass
            # Neither a < b nor b < a -> treat as equal (stable: left <= right)
            return True
    
    def get_statistics(self):
        """Return sorting statistics"""
        return {
            'comparisons': self.comparisons,
            'merges': self.merges,
            'steps': len(self.steps)
        }
