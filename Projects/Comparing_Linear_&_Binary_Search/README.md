## Comparison of Linear and Binary Search Algorithms

This Python script demonstrates the implementation and timing comparison of linear and binary search algorithms. It generates a list of random integers, ensures a specific key is present in the list, and then measures the time taken by each search algorithm to find the key.

<br>

<p align="center">
    <img src="https://github.com/user-attachments/assets/6c5346fe-d4c4-40e1-93b8-714893b14579"]
    

</p>

<br>

## 🌟 Explanation

1. **Linear Search Function (`linear_search`)**:
   - Iterates through the list `lst` to find the `key`.
   - Returns the index of the key if found, otherwise returns `-1`.

2. **Binary Search Function (`binary_search`)**:
   - Uses a divide-and-conquer approach on a sorted list.
   - Recursively divides the list into halves to find the `key`.
   - Returns the index if the key is found, or `-1` if not.

3. **Main Execution**:
   - Generates a list of 10,000 unique random integers and sorts it.
   - Measures the time taken for each search method to find all elements in the list.
   - Outputs the total time taken by linear and binary searches.


4. **Timing Comparison:**
   - The script measures the time taken by both linear and binary search algorithms to find the key in the list and prints the time taken for each search.

<br>

## ⚙️ Prerequisites

- **Basic Python Knowledge**:
  - Understanding of functions, loops, and basic data structures (lists).
- **Basic Knowledge of Search Algorithms**:
  - Familiarity with the concepts of linear and binary search.
- **Python Environment**:
  - Python 3.x installed on your machine.


<br>

## 🛠️ How to Run

```python3
  python3 compare.py
```


<br>

## 📺 Output

![image](https://github.com/user-attachments/assets/c138149c-4010-4f1a-b45d-f72157de825b)
)


<br>

## 📜 Conclusion

The script demonstrates that binary search is significantly faster than linear search for large, sorted datasets. While linear search has a time complexity of O(n), binary search operates with a time complexity of O(log n), making it more efficient for larger lists. This performance difference is particularly evident when the size of the dataset increases, showcasing the importance of choosing the right algorithm for efficient data retrieval.
<br>

## 👻 Author

[Akanksha Kanade](https://github.com/CandyBeans1609)




