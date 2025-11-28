"""
Discrete Structures Final Project
Interactive Algorithm Learning Platform
Author: Sylfhen McLeod
Date: November 2025

This program demonstrates Binary Search and Merge Sort algorithms
through interactive visualizations and practical applications.
"""

from binary_search import BinarySearch
from merge_sort import MergeSort
from visualizer import Visualizer
from applications import Applications
from settings import LINE_WIDTH

def print_header():
    """Display program header"""
    print("=" * LINE_WIDTH)
    print(" " * 15 + "ALGORITHM VISUALIZATION SUITE")
    print(" " * 10 + "Binary Search & Merge Sort Demonstration")
    print("=" * 70)
    print()

def main_menu():
    """Display main menu and handle user selection"""
    while True:
        print("\n" + "=" * LINE_WIDTH)
        print("MAIN MENU")
        print("=" * LINE_WIDTH)
        print("1. Binary Search Demonstrations")
        print("2. Merge Sort Demonstrations")
        print("3. Combined Application: Search in Sorted Data")
        print("4. Algorithm Performance Comparison")
        print("5. Educational Mode (Step-by-Step)")
        print("6. GUI Visualizations (Matplotlib)")
        print("7. Exit")
        print("=" * LINE_WIDTH)
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            binary_search_menu()
        elif choice == '2':
            merge_sort_menu()
        elif choice == '3':
            combined_application()
        elif choice == '4':
            performance_comparison()
        elif choice == '5':
            educational_mode()
        elif choice == '6':
            gui_menu()
        elif choice == '7':
            print("\nThank you for using the Algorithm Visualization Suite!")
            print("Keep practicing divide and conquer! 🚀\n")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")

def binary_search_menu():
    """Submenu for binary search demonstrations"""
    print("\n" + "-" * LINE_WIDTH)
    print("BINARY SEARCH DEMONSTRATIONS")
    print("-" * LINE_WIDTH)
    print("1. Classic Number Guessing Game")
    print("2. Search in Sorted Array")
    print("3. Find Student by ID")
    print("4. Back to Main Menu")
    print("-" * LINE_WIDTH)
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == '1':
        Applications.number_guessing_game()
    elif choice == '2':
        Applications.array_search_demo()
    elif choice == '3':
        Applications.student_search_demo()
    elif choice == '4':
        return
    else:
        print("\n❌ Invalid choice.")

def merge_sort_menu():
    """Submenu for merge sort demonstrations"""
    print("\n" + "-" * LINE_WIDTH)
    print("MERGE SORT DEMONSTRATIONS")
    print("-" * LINE_WIDTH)
    print("1. Sort Random Numbers")
    print("2. Sort Student Grades")
    print("3. Visualize Sorting Process")
    print("4. Back to Main Menu")
    print("-" * LINE_WIDTH)
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == '1':
        Applications.sort_random_numbers()
    elif choice == '2':
        Applications.sort_student_grades()
    elif choice == '3':
        Applications.visualize_merge_sort()
    elif choice == '4':
        return
    else:
        print("\n❌ Invalid choice.")

def combined_application():
    """Demonstrate using merge sort then binary search"""
    print("\n" + "-" * LINE_WIDTH)
    print("COMBINED APPLICATION: Sort then Search")
    print("-" * LINE_WIDTH)
    print("This demonstrates the power of combining algorithms:")
    print("1. First, we'll use Merge Sort to organize unsorted data")
    print("2. Then, we'll use Binary Search for efficient lookup")
    print("-" * LINE_WIDTH)
    
    Applications.sort_then_search_demo()

def performance_comparison():
    """Compare algorithm performance"""
    print("\n" + "-" * LINE_WIDTH)
    print("ALGORITHM PERFORMANCE COMPARISON")
    print("-" * LINE_WIDTH)
    Applications.performance_dashboard()

def educational_mode():
    """Step-by-step educational walkthrough"""
    print("\n" + "-" * LINE_WIDTH)
    print("EDUCATIONAL MODE")
    print("-" * LINE_WIDTH)
    print("1. Learn Binary Search (Step-by-Step)")
    print("2. Learn Merge Sort (Step-by-Step)")
    print("3. Back to Main Menu")
    print("-" * LINE_WIDTH)
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == '1':
        Applications.teach_binary_search()
    elif choice == '2':
        Applications.teach_merge_sort()
    elif choice == '3':
        return
    else:
        print("\n❌ Invalid choice.")

def gui_menu():
    """Submenu for GUI visualizations"""
    print("\n" + "-" * LINE_WIDTH)
    print("GUI VISUALIZATIONS (MATPLOTLIB)")
    print("-" * LINE_WIDTH)
    print("1. Animated Merge Sort")
    print("2. Binary Search Steps")
    print("3. Algorithm Complexity Comparison")
    print("4. Performance Benchmark")
    print("5. Back to Main Menu")
    print("-" * LINE_WIDTH)
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == '1':
        Applications.gui_merge_sort_animation()
    elif choice == '2':
        Applications.gui_binary_search_visualization()
    elif choice == '3':
        Applications.gui_complexity_comparison()
    elif choice == '4':
        Applications.gui_performance_benchmark()
    elif choice == '5':
        return
    else:
        print("\n❌ Invalid choice.")

if __name__ == "__main__":
    print_header()
    print("Welcome to the Algorithm Visualization Suite!")
    print("This program will help you understand Binary Search and Merge Sort")
    print("through interactive demonstrations and visualizations.\n")
    
    input("Press Enter to continue...")
    main_menu()
