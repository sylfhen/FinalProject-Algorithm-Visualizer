"""
GUI Visualizer using Matplotlib
Provides graphical visualizations for algorithms
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
import numpy as np
from typing import List, Tuple


class GUIVisualizer:
    """Graphical visualization using matplotlib"""
    
    @staticmethod
    def visualize_merge_sort_animated(arr: List[int]):
        """
        Animated visualization of merge sort algorithm
        Shows bars being sorted with color coding for different phases
        """
        # Create a copy to track states
        states = []
        colors = []
        
        def capture_state(arr_copy, left, right, highlight_type='normal'):
            """Capture current array state and color coding"""
            state = arr_copy.copy()
            color = ['lightblue'] * len(arr_copy)
            
            # Color the section being processed
            for i in range(left, right + 1):
                if highlight_type == 'divide':
                    color[i] = 'orange'
                elif highlight_type == 'merge':
                    color[i] = 'lightgreen'
                elif highlight_type == 'sorted':
                    color[i] = 'green'
            
            states.append(state)
            colors.append(color)
        
        def merge_sort_visual(arr, left, right):
            """Merge sort with state capturing"""
            if left >= right:
                return
            
            mid = (left + right) // 2
            
            # Capture divide state
            capture_state(arr, left, right, 'divide')
            
            # Recursively sort
            merge_sort_visual(arr, left, mid)
            merge_sort_visual(arr, mid + 1, right)
            
            # Merge
            merge_visual(arr, left, mid, right)
        
        def merge_visual(arr, left, mid, right):
            """Merge with visualization"""
            left_part = arr[left:mid + 1]
            right_part = arr[mid + 1:right + 1]
            
            i = j = 0
            k = left
            
            while i < len(left_part) and j < len(right_part):
                if left_part[i] <= right_part[j]:
                    arr[k] = left_part[i]
                    i += 1
                else:
                    arr[k] = right_part[j]
                    j += 1
                k += 1
                capture_state(arr, left, right, 'merge')
            
            while i < len(left_part):
                arr[k] = left_part[i]
                i += 1
                k += 1
                capture_state(arr, left, right, 'merge')
            
            while j < len(right_part):
                arr[k] = right_part[j]
                j += 1
                k += 1
                capture_state(arr, left, right, 'merge')
            
            # Mark as sorted
            capture_state(arr, left, right, 'sorted')
        
        # Initial state
        arr_copy = arr.copy()
        capture_state(arr_copy, 0, len(arr_copy) - 1, 'normal')
        
        # Run merge sort with visualization
        merge_sort_visual(arr_copy, 0, len(arr_copy) - 1)
        
        # Final sorted state
        capture_state(arr_copy, 0, len(arr_copy) - 1, 'sorted')
        
        # Create animation
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, len(arr))
        ax.set_ylim(0, max(arr) * 1.1)
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        ax.set_title('Merge Sort Visualization')
        
        bars = ax.bar(range(len(arr)), arr, color='lightblue')
        
        def update(frame):
            """Update function for animation"""
            state = states[frame]
            color = colors[frame]
            
            for bar, height, c in zip(bars, state, color):
                bar.set_height(height)
                bar.set_color(c)
            
            ax.set_title(f'Merge Sort - Step {frame + 1}/{len(states)}')
            return bars
        
        anim = animation.FuncAnimation(
            fig, update, frames=len(states),
            interval=500, repeat=True, blit=False
        )
        
        plt.tight_layout()
        plt.show()
        
        return arr_copy
    
    @staticmethod
    def visualize_binary_search_steps(arr: List[int], target: int):
        """
        Visualize binary search steps graphically
        Shows search range narrowing with each step
        """
        left, right = 0, len(arr) - 1
        steps = []
        
        # Capture all search steps
        while left <= right:
            mid = (left + right) // 2
            steps.append({
                'left': left,
                'mid': mid,
                'right': right,
                'found': arr[mid] == target
            })
            
            if arr[mid] == target:
                break
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # Create visualization
        fig, axes = plt.subplots(len(steps), 1, figsize=(10, 3 * len(steps)))
        if len(steps) == 1:
            axes = [axes]
        
        fig.suptitle(f'Binary Search for {target}', fontsize=16, fontweight='bold')
        
        for idx, (ax, step) in enumerate(zip(axes, steps)):
            colors = ['lightgray'] * len(arr)
            
            # Color code the search range
            for i in range(step['left'], step['right'] + 1):
                colors[i] = 'lightblue'
            
            # Highlight mid point
            if step['found']:
                colors[step['mid']] = 'green'
            else:
                colors[step['mid']] = 'orange'
            
            bars = ax.bar(range(len(arr)), arr, color=colors, edgecolor='black')
            
            # Add value labels on bars
            for i, (bar, val) in enumerate(zip(bars, arr)):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{val}', ha='center', va='bottom', fontsize=9)
            
            ax.set_xlim(-0.5, len(arr) - 0.5)
            ax.set_ylim(0, max(arr) * 1.2)
            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            
            status = 'FOUND!' if step['found'] else f"Searching... (mid={arr[step['mid']]})"
            ax.set_title(f"Step {idx + 1}: Range [{step['left']}...{step['right']}] - {status}")
            
            # Add arrow pointing to mid
            ax.annotate('', xy=(step['mid'], arr[step['mid']] * 1.1),
                       xytext=(step['mid'], arr[step['mid']] * 1.15),
                       arrowprops=dict(arrowstyle='->', color='red', lw=2))
        
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def plot_performance_comparison(sizes: List[int], 
                                    binary_times: List[float],
                                    merge_times: List[float]):
        """
        Plot performance comparison between algorithms
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        
        # Binary Search performance
        ax1.plot(sizes, binary_times, 'o-', color='blue', linewidth=2, 
                markersize=8, label='Binary Search')
        ax1.set_xlabel('Array Size', fontsize=12)
        ax1.set_ylabel('Time (seconds)', fontsize=12)
        ax1.set_title('Binary Search Performance', fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # Theoretical O(log n) curve
        theoretical = [np.log2(s) * binary_times[0] / np.log2(sizes[0]) for s in sizes]
        ax1.plot(sizes, theoretical, '--', color='red', alpha=0.5, label='O(log n)')
        ax1.legend()
        
        # Merge Sort performance
        ax2.plot(sizes, merge_times, 's-', color='green', linewidth=2,
                markersize=8, label='Merge Sort')
        ax2.set_xlabel('Array Size', fontsize=12)
        ax2.set_ylabel('Time (seconds)', fontsize=12)
        ax2.set_title('Merge Sort Performance', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        # Theoretical O(n log n) curve
        theoretical = [s * np.log2(s) * merge_times[0] / 
                      (sizes[0] * np.log2(sizes[0])) for s in sizes]
        ax2.plot(sizes, theoretical, '--', color='orange', alpha=0.5, label='O(n log n)')
        ax2.legend()
        
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def visualize_complexity_comparison():
        """
        Visualize time complexity comparison of different algorithms
        """
        n = np.linspace(1, 100, 100)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot different complexities
        ax.plot(n, np.log2(n), label='O(log n) - Binary Search', linewidth=2)
        ax.plot(n, n, label='O(n) - Linear Search', linewidth=2)
        ax.plot(n, n * np.log2(n), label='O(n log n) - Merge Sort', linewidth=2)
        ax.plot(n, n**2, label='O(n²) - Bubble Sort', linewidth=2)
        
        ax.set_xlabel('Input Size (n)', fontsize=12)
        ax.set_ylabel('Operations', fontsize=12)
        ax.set_title('Algorithm Time Complexity Comparison', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 1000)
        
        plt.tight_layout()
        plt.show()
