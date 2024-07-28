
### Title:
Comparing Linear and Binary Search Algorithms in Python

### Description:
This Python script demonstrates the implementation and timing comparison of linear and binary search algorithms. It generates a list of random integers, ensures a specific key is present in the list, and then measures the time taken by each search algorithm to find the key.

### Explanation:
1. **Functions:**
   - `linear_search(lst, key)`: Iterates through the list to find the key. Returns `True` if found, otherwise `False`.
   - `binary_search(lst, key, low, high)`: Recursively searches for the key in a sorted list using the binary search algorithm. Returns the index of the key if found, otherwise `False`.

2. **Generating Random List:**
   - A list of 100 random integers between -200 and 200 is generated and then sorted.

3. **Key Handling:**
   - The script checks if the key (`key = 16`) is in the list. If not, it adds the key to the list and re-sorts it.

4. **Timing Comparison:**
   - The script measures the time taken by both linear and binary search algorithms to find the key in the list and prints the time taken for each search.

### Prerequisites:
- **Basic Python Knowledge**:
  - Understanding of functions, loops, and basic data structures (lists).
- **Basic Knowledge of Search Algorithms**:
  - Familiarity with the concepts of linear and binary search.
- **Python Environment**:
  - Python 3.x installed on your machine.

### Conclusion:
The script demonstrates the efficiency differences between linear and binary search algorithms. While linear search scans each element until it finds the key or reaches the end of the list, binary search significantly reduces the number of comparisons by dividing the list in half with each step. The timing results highlight the advantage of using binary search with sorted data, as it generally performs faster than linear search, especially for larger datasets. This example illustrates the importance of choosing the appropriate algorithm based on the data structure and problem requirements.
