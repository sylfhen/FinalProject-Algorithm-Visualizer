"""
Real-world applications and demonstrations
"""

from binary_search import BinarySearch
from merge_sort import MergeSort
from visualizer import Visualizer
from settings import LINE_WIDTH
import random

class Applications:
    @staticmethod
    def number_guessing_game():
        """Launch the number guessing game"""
        bs = BinarySearch()
        bs.number_guessing_game(maximum=100)
    
    @staticmethod
    def array_search_demo():
        """Demonstrate searching in a sorted array"""
        print("\n" + "=" * 60)
        print("SEARCH IN SORTED ARRAY")
        print("=" * 60)
        
        # Create sorted array
        arr = sorted(random.sample(range(1, 100), 15))
        print(f"Sorted Array: {arr}")
        
        try:
            target = int(input("\nEnter a number to search for: "))
        except ValueError:
            print("Invalid input. Returning to menu.")
            return
        
        bs = BinarySearch()
        result = bs.search_iterative(arr, target, visualize=True)
        
        stats = bs.get_statistics()
        print(f"\nStatistics:")
        print(f"  Comparisons: {stats['comparisons']}")
        print(f"  Result: {'Found at index ' + str(result) if result != -1 else 'Not found'}")
    
    @staticmethod
    def sort_random_numbers():
        """Sort random numbers using merge sort"""
        print("\n" + "=" * 60)
        print("SORT RANDOM NUMBERS")
        print("=" * 60)
        
        try:
            size = int(input("How many numbers to sort? (5-20): "))
        except ValueError:
            print("Invalid input. Returning to menu.")
            return
        arr = [random.randint(1, 100) for _ in range(min(size, 20))]
        
        print(f"\nUnsorted: {arr}")
        
        ms = MergeSort()
        sorted_arr = ms.sort(arr, visualize=True)
        
        print(f"\nSorted: {sorted_arr}")
        
        stats = ms.get_statistics()
        print(f"\nStatistics:")
        print(f"  Comparisons: {stats['comparisons']}")
        print(f"  Merge operations: {stats['merges']}")
    
    # Implemented methods
    @staticmethod
    def student_search_demo():
        """Efficient student search demo with automatic or manual entry.

        The function minimizes copies, validates input, and uses
        `BinarySearch` on a list of IDs derived from the roster.
        """
        print("\n" + "=" * LINE_WIDTH)
        print("STUDENT SEARCH DEMO")
        print("=" * LINE_WIDTH)

        sample_names = [
            "Aisha", "Ben", "Carlos", "Divya", "Emma",
            "Farah", "George", "Hiro", "Ivy", "Jamal",
            "Keiko", "Liam"
        ]

        mode = input("Create students automatically or enter manually? (a/m) [a]: ").strip().lower()
        if mode not in ("a", "m", ""):
            mode = "a"

        # Roster size with sane defaults and bounds
        try:
            n = int(input("How many students to create (5-12)? [8]: ").strip() or 8)
        except ValueError:
            n = 8
        n = max(5, min(12, n))

        students = []

        if mode == "m":
            print("\nEnter student records manually. IDs must be unique integers.")
            used_ids = set()
            for i in range(n):
                while True:
                    raw_id = input(f"Student #{i+1} - ID: ").strip()
                    try:
                        sid = int(raw_id)
                    except ValueError:
                        print("  Invalid ID — must be an integer.")
                        continue
                    if sid in used_ids:
                        print("  ID already used — enter a unique ID.")
                        continue
                    name = input(f"Student #{i+1} - Name: ").strip()
                    if not name:
                        print("  Name cannot be empty.")
                        continue
                    used_ids.add(sid)
                    students.append({'id': sid, 'name': name})
                    break
        else:
            ids = random.sample(range(1000, 9999), n)
            # Choose distinct names where possible, otherwise cycle
            if len(sample_names) >= n:
                names = random.sample(sample_names, n)
            else:
                names = [sample_names[i % len(sample_names)] for i in range(n)]
            students = [{'id': sid, 'name': name} for sid, name in zip(ids, names)]

        # Sort by ID (in-place)
        students.sort(key=lambda s: s['id'])

        print("\nStudent Roster (sorted by ID):")
        for s in students:
            print(f"  ID: {s['id']}  Name: {s['name']}")

        try:
            target = int(input("\nEnter the student ID to search for: ").strip())
        except ValueError:
            print("Invalid ID. Returning to menu.")
            return

        visualize = input("Show step-by-step visualization? (y/N): ").strip().lower() == 'y'

        id_list = [s['id'] for s in students]
        bs = BinarySearch()
        idx = bs.search_iterative(id_list, target, visualize=visualize)
        stats = bs.get_statistics()

        print("\nSearch Result:")
        if idx != -1:
            s = students[idx]
            print(f"  ✅ Found: ID {s['id']} — {s['name']} (index {idx})")
        else:
            print("  ❌ Student ID not found in roster")

        print(f"\nStatistics: Comparisons={stats['comparisons']}  Steps={stats['steps']}")
    
    @staticmethod
    def sort_student_grades():
        """Sort student grades using MergeSort with clean data handling.

        Uses a list of (grade, name) tuples so MergeSort compares by grade
        naturally. Provides automatic entry and optional
        visualization. Keeps copies minimal and prints concise stats.
        """
        print("\n" + "=" * LINE_WIDTH)
        print("STUDENT GRADE SORTING")
        print("=" * LINE_WIDTH)

        sample_names = [
            "Aisha", "Ben", "Carlos", "Divya", "Emma",
            "Farah", "George", "Hiro", "Ivy", "Jamal",
            "Keiko", "Liam"
        ]

        mode = input("Create students automatically or enter manually? (a/m) [a]: ").strip().lower()
        if mode not in ("a", "m", ""):
            mode = "a"

        try:
            n = int(input("How many students to create (5-20)? [8]: ").strip() or 8)
        except ValueError:
            n = 8
        n = max(5, min(20, n))

        tuples = []  # store as (grade, name)

        if mode == "m":
            print("\nEnter student records manually. Grades should be 0-100.")
            used_names = set()
            for i in range(n):
                while True:
                    name = input(f"Student #{i+1} - Name: ").strip()
                    if not name:
                        print("  Name cannot be empty.")
                        continue
                    if name in used_names:
                        print("  Name already used; please enter a unique name.")
                        continue
                    grade_raw = input(f"Student #{i+1} - Grade (0-100): ").strip()
                    try:
                        grade = float(grade_raw)
                    except ValueError:
                        print("  Invalid grade. Enter a number between 0 and 100.")
                        continue
                    if not (0 <= grade <= 100):
                        print("  Grade out of range. Enter 0-100.")
                        continue
                    used_names.add(name)
                    tuples.append((grade, name))
                    break
        else:
            # automatic: sample distinct names when possible
            if len(sample_names) >= n:
                names = random.sample(sample_names, n)
            else:
                names = [sample_names[i % len(sample_names)] for i in range(n)]
            grades = [random.randint(0, 100) for _ in range(n)]
            tuples = [(g, name) for g, name in zip(grades, names)]

        print("\nUnsorted Student Grades:")
        for g, name in tuples:
            print(f"  {name:10s}  Grade: {g:6.2f}")

        order = input("Sort ascending or descending? (a/d) [d]: ").strip().lower()
        if order not in ("a", "d", ""):
            order = "d"

        visualize = input("Show merge-sort visualization? (y/N): ").strip().lower() == 'y'

        ms = MergeSort()
        sorted_tuples = ms.sort(tuples.copy(), visualize=visualize)
        if order != 'a':
            sorted_tuples = list(reversed(sorted_tuples))

        print("\nSorted Student Grades:")
        for g, name in sorted_tuples:
            print(f"  {name:10s}  Grade: {g:6.2f}")

        stats = ms.get_statistics()
        print(f"\nStatistics: Comparisons={stats.get('comparisons',0)}  Merges={stats.get('merges',0)} Steps={stats.get('steps',0)}")
    
    @staticmethod
    def visualize_merge_sort():
        """Visualize merge sort on a small array using `Visualizer` and `MergeSort`.

        Allows manual entry or random generation. Shows a simple bar chart
        before and after sorting and uses `MergeSort.sort(..., visualize=True)`
        to step through the algorithm when requested.
        """
        print("\n" + "=" * 60)
        print("MERGE SORT VISUALIZATION")
        print("=" * 60)

        try:
            n = int(input("How many elements to visualize (5-20)? [8]: ").strip() or 8)
        except ValueError:
            n = 8
        n = max(5, min(20, n))

        mode = input("Enter numbers manually or generate randomly? (m/r) [r]: ").strip().lower()
        arr = []
        if mode == 'm':
            print("Enter integer values (one per prompt):")
            for i in range(n):
                while True:
                    raw = input(f"Value #{i+1}: ").strip()
                    try:
                        val = int(raw)
                        arr.append(val)
                        break
                    except ValueError:
                        print("  Please enter an integer.")
        else:
            arr = [random.randint(1, 100) for _ in range(n)]

        print("\nInitial array:", arr)
        Visualizer.print_array_bar_chart(arr, title="Before: Array")

        ms = MergeSort()
        sorted_arr = ms.sort(arr.copy(), visualize=True)

        # Display final sorted array in yellow
        YELLOW = '\033[93m'
        RESET = '\033[0m'
        print(f"\n{YELLOW}Sorted array: {sorted_arr}{RESET}")
        Visualizer.print_array_bar_chart(sorted_arr, title="After: Sorted Array")

        stats = ms.get_statistics()
        print(f"\nStatistics: Comparisons={stats.get('comparisons',0)}  Merges={stats.get('merges',0)}")
    
    @staticmethod
    def sort_then_search_demo():
        """Demonstrate sorting an unsorted list with MergeSort then using
        BinarySearch to locate an element. Both steps offer optional
        visualization.
        """
        print("\n" + "=" * 60)
        print("COMBINED: SORT THEN SEARCH")
        print("=" * 60)

        try:
            n = int(input("How many elements? (5-50) [15]: ").strip() or 15)
        except ValueError:
            n = 15
        n = max(5, min(50, n))

        arr_mode = input("Enter array manually or generate randomly? (m/r) [r]: ").strip().lower()
        if arr_mode == 'm':
            arr = []
            print("Enter integer values:")
            for i in range(n):
                while True:
                    raw = input(f"Value #{i+1}: ").strip()
                    try:
                        arr.append(int(raw))
                        break
                    except ValueError:
                        print("  Please enter an integer.")
        else:
            arr = [random.randint(1, 1000) for _ in range(n)]

        print("\nUnsorted:\n", arr)

        vis_sort = input("Visualize merge sort? (y/N): ").strip().lower() == 'y'
        ms = MergeSort()
        sorted_arr = ms.sort(arr.copy(), visualize=vis_sort)

        print("\nSorted:\n", sorted_arr)

        try:
            target = int(input("\nEnter value to search for: ").strip())
        except ValueError:
            print("Invalid input. Returning to menu.")
            return

        vis_search = input("Visualize binary search? (y/N): ").strip().lower() == 'y'
        bs = BinarySearch()
        index = bs.search_iterative(sorted_arr, target, visualize=vis_search)

        if index != -1:
            print(f"\nFound {target} at index {index} in the sorted array")
        else:
            print(f"\n{target} not found in the array")

        s_stats = ms.get_statistics()
        b_stats = bs.get_statistics()
        print(f"\nMergeSort: comparisons={s_stats.get('comparisons',0)} merges={s_stats.get('merges',0)}")
        print(f"BinarySearch: comparisons={b_stats.get('comparisons',0)} steps={b_stats.get('steps',0)}")
    
    @staticmethod
    def performance_dashboard():
        """Run quick performance comparison (operation counts) for MergeSort
        and BinarySearch across increasing data sizes and display a table.
        Uses small number of trials to keep run-time reasonable.
        """
        print("\n" + "=" * 60)
        print("PERFORMANCE DASHBOARD")
        print("=" * 60)

        sizes = [100, 500, 1000, 2000]
        trials = 3
        bs_results = []
        ms_results = []

        for n in sizes:
            bs_ops = 0
            ms_ops = 0
            for _ in range(trials):
                arr = [random.randint(1, 1000000) for _ in range(n)]
                ms = MergeSort()
                sorted_arr = ms.sort(arr.copy(), visualize=False)
                ms_stats = ms.get_statistics()
                ms_ops += ms_stats.get('comparisons', 0)

                # pick target existing value to measure typical binary-search cost
                target = random.choice(sorted_arr)
                bs = BinarySearch()
                bs.search_iterative(sorted_arr, target, visualize=False)
                bs_stats = bs.get_statistics()
                bs_ops += bs_stats.get('comparisons', 0)

            ms_results.append(ms_ops // trials)
            bs_results.append(bs_ops // trials)

        Visualizer.print_comparison_table(sizes, bs_results, ms_results)
    
    @staticmethod
    def teach_binary_search():
        """Educational walkthrough for Binary Search: construct an array
        (manual or random), show complexity notes and run an optional
        step-by-step visualization.
        """
        print("\n" + "=" * 60)
        print("TEACH: BINARY SEARCH")
        print("=" * 60)

        Visualizer.print_algorithm_complexity()

        try:
            n = int(input("How many elements for demonstration (5-20)? [9]: ").strip() or 9)
        except ValueError:
            n = 9
        n = max(5, min(20, n))

        arr_mode = input("Enter array manually or generate randomly? (m/r) [r]: ").strip().lower()
        if arr_mode == 'm':
            arr = []
            print("Enter sorted values (increasing order):")
            for i in range(n):
                while True:
                    raw = input(f"Value #{i+1}: ").strip()
                    try:
                        arr.append(int(raw))
                        break
                    except ValueError:
                        print("  Please enter an integer.")
            arr.sort()
        else:
            arr = sorted(random.sample(range(1, 200), n))

        print("\nArray for demonstration:", arr)
        try:
            target = int(input("Enter target to search for: ").strip())
        except ValueError:
            print("Invalid input. Returning to menu.")
            return

        print("\nRunning step-by-step Binary Search...")
        bs = BinarySearch()
        bs.search_iterative(arr, target, visualize=True)
        stats = bs.get_statistics()
        print(f"\nCompleted: comparisons={stats.get('comparisons',0)} steps={stats.get('steps',0)}")
    
    @staticmethod
    def teach_merge_sort():
        """Educational walkthrough for Merge Sort: create an array and
        walk through the divide/merge steps using MergeSort's
        visualization helpers.
        """
        print("\n" + "=" * 60)
        print("TEACH: MERGE SORT")
        print("=" * 60)

        Visualizer.print_algorithm_complexity()

        try:
            n = int(input("How many elements for demonstration (5-20)? [9]: ").strip() or 9)
        except ValueError:
            n = 9
        n = max(5, min(20, n))

        arr_mode = input("Enter array manually or generate randomly? (m/r) [r]: ").strip().lower()
        if arr_mode == 'm':
            arr = []
            print("Enter integer values:")
            for i in range(n):
                while True:
                    raw = input(f"Value #{i+1}: ").strip()
                    try:
                        arr.append(int(raw))
                        break
                    except ValueError:
                        print("  Please enter an integer.")
        else:
            arr = [random.randint(1, 200) for _ in range(n)]

        print("\nArray for demonstration:", arr)
        ms = MergeSort()
        ms.sort(arr.copy(), visualize=True)
        stats = ms.get_statistics()
        print(f"\nCompleted: comparisons={stats.get('comparisons',0)} merges={stats.get('merges',0)} steps={stats.get('steps',0)}")
