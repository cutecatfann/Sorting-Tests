# Sorting-Tests: Insertion vs. Merge Sorting Algorithms

Dive into the performance comparison between the classic Insertion and Merge sorting algorithms. This project examines their behaviors on three distinct array types, then computes the degree of randomness in an array required for the Insertion sort to underperform against the Merge sort. For a comprehensive understanding, all results are visualized using Plotly.

## Features

- **Versatile Array Testing:** Experiments on:
  - Completely unsorted arrays.
  - Perfectly sorted arrays.
  - Arrays with varying degrees of randomness to pinpoint the threshold at which Insertion sort starts to lag.

- **Interactive Visualization:** Utilizes Plotly to graphically represent the comparative performance, offering clear insights into the efficiency of each algorithm.

## Prerequisites

- Python 3.x installed on your machine.
- Plotly library (`pip install plotly`).

## Getting Started

1. **Clone the Repository:**
   ```
   git clone https://github.com/cutecatfann/Sorting-Tests.git
   cd Sorting-Tests
   ```

2. **Run the Test:**
   ```
   python3 merge_sort.py
   ```

3. View the generated Plotly graphs for a visual representation of the sorting algorithms' performances across the different array types.

## Contributing

Feedback, improvements, and contributions are always welcomed. If you find something interesting or have suggestions, feel free to open a pull request or an issue.

## License

This project is open-source under MIT license.
