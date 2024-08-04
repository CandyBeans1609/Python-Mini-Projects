## Phone Number Finder

This guide demonstrates how to implement a script that searches for a telephone number formatted as `###-###-####` within multiple text files in various directories using Python. The script leverages the `os` module to traverse directories and the `re` module for regular expression matching.

<br>

<p align="center">
    <img src="https://github.com/user-attachments/assets/46bdf1b5-071b-4f11-803d-65c5d33bb43b">
</p>

<br>

## 🌟 Explanation

- **Phone Number Format**: The script searches for phone numbers formatted as `###-###-####`.
- **Directory Traversal**: Uses Python's `os` module to walk through directories and subdirectories.
- **Regular Expressions**: Utilizes the `re` module to define and search for the phone number pattern.
- **File Handling**: Reads the content of each text file to find matches.

<br>

## ⚙️ Prerequisites

- **Basic Python Knowledge**: Understanding of Python syntax, functions, and loops.
- **Familiarity with Regular Expressions**: Basic knowledge of how to use regular expressions in Python.
- **Understanding of File I/O**: Knowledge of how to open, read, and close files in Python.

<br>

## 🛠️ How to Run

1. **Ensure the directory structure**:
   - You should have a directory named `extracted_content` with subdirectories and text files.

2. **Run the script**:
    ```python
    python3 find_phone_num.py
    ```
 
<br>

## 📺 Output

![image](https://github.com/user-attachments/assets/df94bcdd-ca90-43cc-b8e2-ccbbd37cb55e)

<br>

## 📜 Conclusion

Using the `os` and `re` modules to implement a phone number search in Python provides a robust way to search through multiple files and directories. This approach is efficient for scanning large datasets and ensures that all files are checked without loading them entirely into memory.

<br>

## 👻 Author

[Akanksha Kanade](https://github.com/CandyBeans1609)
