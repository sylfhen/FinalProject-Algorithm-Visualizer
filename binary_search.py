"""
Binary Search Algorithm Implementation
Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive
"""

import sys

from settings import LINE_WIDTH


class BinarySearch:
    def __init__(self):
        self.comparisons = 0
        self.steps = []
    
    def search_iterative(self, arr, target, visualize=False):
        """
        Iterative binary search implementation
        
        Args:
            arr: Sorted list of elements
            target: Element to search for
            visualize: Boolean to enable step-by-step visualization
        
        Returns:
            Index of target if found, -1 otherwise
        """
        self.comparisons = 0
        self.steps = []
        
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            self.comparisons += 1
            
            if visualize:
                self._visualize_step(arr, left, mid, right, target)
            
            self.steps.append({
                'left': left,
                'mid': mid,
                'right': right,
                'mid_value': arr[mid],
                'target': target
            })
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    def search_recursive(self, arr, target, left=0, right=None, visualize=False):
        """
        Recursive binary search implementation
        
        Args:
            arr: Sorted list of elements
            target: Element to search for
            left: Left boundary index
            right: Right boundary index
            visualize: Boolean to enable visualization
        
        Returns:
            Index of target if found, -1 otherwise
        """
        if right is None:
            right = len(arr) - 1
            self.comparisons = 0
            self.steps = []
        
        if left > right:
            return -1
        
        mid = (left + right) // 2
        self.comparisons += 1
        
        if visualize:
            self._visualize_step(arr, left, mid, right, target)
        
        self.steps.append({
            'left': left,
            'mid': mid,
            'right': right,
            'mid_value': arr[mid],
            'target': target
        })
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return self.search_recursive(arr, target, mid + 1, right, visualize)
        else:
            return self.search_recursive(arr, target, left, mid - 1, visualize)
    
    def _visualize_step(self, arr, left, mid, right, target):
        """Helper method to visualize current search step"""
        print("\n" + "-" * LINE_WIDTH)
        print(f"Searching for: {target}")
        print(f"Search Range: [{left}...{right}]")
        print(f"Middle Index: {mid}, Middle Value: {arr[mid]}")
        
        # Visual representation
        visual = []
        for i in range(len(arr)):
            if i < left or i > right:
                visual.append("  _  ")
            elif i == mid:
                visual.append(f"[{arr[i]:2d}]")
            else:
                visual.append(f" {arr[i]:2d} ")
        
        print("Array: " + "".join(visual))
        
        if arr[mid] == target:
            print(f"✓ Found! Target {target} is at index {mid}")
        elif arr[mid] < target:
            print(f"→ {arr[mid]} < {target}, search right half")
        else:
            print(f"← {arr[mid]} > {target}, search left half")

        # Only pause for input when running interactively (tty).
        try:
            if sys.stdin.isatty():
                input("Press Enter to continue...")
        except Exception:
            # In non-interactive environments (pytest capture) skip waiting.
            pass
    
    def get_statistics(self):
        """Return search statistics"""
        return {
            'comparisons': self.comparisons,
            'steps': len(self.steps)
        }
    
    def number_guessing_game(self, maximum=100):
        """
        Interactive number guessing game using binary search
        """
        print("\n" + "=" * LINE_WIDTH)
        print(" " * 15 + "NUMBER GUESSING GAME")
        print("=" * LINE_WIDTH)
        print(f"Think of a number between 1 and {maximum}...")
        print("I'll try to guess it using Binary Search!")
        print("=" * 60)
        
        minimum = 1
        attempts = 0
        
        while True:
            guess = (maximum + minimum) // 2
            attempts += 1
            
            print(f"\nAttempt #{attempts}")
            print(f"Current range: [{minimum}, {maximum}]")
            print(f"My guess is: {guess}")
            print("-" * LINE_WIDTH)
            
            response = input("Is it (c)orrect, (h)igher, or (l)ower? ").strip().lower()
            
            if response == 'c':
                print("\n" + "=" * LINE_WIDTH)
                print(f"🎉 SUCCESS! I found your number: {guess}")
                print(f"It took me {attempts} attempts")
                print(f"Binary Search is efficient! 💪")
                print("=" * LINE_WIDTH)
                break
            elif response == 'h':
                minimum = guess + 1
                print(f"→ Eliminating numbers ≤ {guess}")
            elif response == 'l':
                maximum = guess - 1
                print(f"← Eliminating numbers ≥ {guess}")
            else:
                print("❌ Invalid input. Please enter 'c', 'h', or 'l'")
                attempts -= 1
            
            if minimum > maximum:
                print("\n❌ Something went wrong! Are you sure you didn't change your number?")
                break
