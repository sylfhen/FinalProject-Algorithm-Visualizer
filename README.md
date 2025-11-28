# Algorithm Visualization Suite

This project demonstrates Binary Search and Merge Sort with interactive
CLI visualizations, GUI animations, and practical application demos.

## Files

- `main.py` — Program entry point and menus
- `binary_search.py` — Binary Search implementation
- `merge_sort.py` — Merge Sort implementation
- `visualizer.py` — CLI visualization utilities
- `gui_visualizer.py` — Matplotlib GUI visualizations
- `applications.py` — Demos, use-cases, and GUI integration
- `test_algorithms.py` — Unit tests (pytest)

## Features

### CLI Visualizations
- Step-by-step algorithm walkthroughs with color-coded output
- Interactive number guessing game (Binary Search)
- Student search and grade sorting demos
- Performance statistics and comparisons

### GUI Visualizations (Matplotlib)
- **Animated Merge Sort**: Watch bars being sorted in real-time with color-coded phases
- **Binary Search Steps**: Visual representation of search range narrowing
- **Complexity Comparison**: Graph comparing O(log n), O(n), O(n log n), O(n²)
- **Performance Benchmark**: Real performance graphs for different input sizes

## Usage

Run the main program:
```bash
python3 main.py
```

From the main menu:
- Options 1-5: CLI demonstrations
- Option 6: GUI visualizations (requires matplotlib)
- Option 7: Exit

## Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

Required packages:
- matplotlib (for GUI visualizations)
- numpy (for performance analysis)
- pytest (for running tests)

## Testing

Run all tests:
```bash
pytest test_algorithms.py -v
```

## Notes

- CLI visualizations use blocking `input()` calls for educational step-through
- GUI visualizations open matplotlib windows (close window to continue)
- All tests pass with proper handling of interactive and non-interactive modes
