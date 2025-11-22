"""
Merge Sort Algorithm Implementation
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

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
            
            if left_part[i] <= right_part[j]:
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
        """Visualize the divide step"""
        print("\n" + "-" * LINE_WIDTH)
        print("DIVIDE STEP")
        print(f"Splitting: {arr[left:right + 1]}")
        print(f"Left half:  {arr[left:mid + 1]}")
        print(f"Right half: {arr[mid + 1:right + 1]}")
        input("Press Enter to continue...")
    
    def _visualize_merge(self, arr, left, mid, right, left_part, right_part):
        """Visualize the merge step"""
        print("\n" + "-" * LINE_WIDTH)
        print("MERGE STEP")
        print(f"Merging: {left_part} + {right_part}")
        print(f"Result:  {arr[left:right + 1]}")
        input("Press Enter to continue...")
    
    def get_statistics(self):
        """Return sorting statistics"""
        return {
            'comparisons': self.comparisons,
            'merges': self.merges,
            'steps': len(self.steps)
        }
