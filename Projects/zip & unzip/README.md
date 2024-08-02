## Zip and Unzip Utility
A Python utility for creating a zip archive from a specified directory and extracting the contents of a zip archive to a specified directory.

<br>

<p align="center">
    <img src="https://ubiq.co/tech-blog/wp-content/uploads/2020/08/install-zip-unzip-627x410.png">
  
</p>

<br>

## 🌟 Explanation

### Zip Functionality

- **Initialization**:
  - `dir_to_zip = r"C:\Users\Akanksha\Documents\GitHub\Python-Mini-Projects\Projects\zip & unzip\input"` sets the path to the directory you want to zip.
  - `output = 'example'` sets the name of the output zip file.
- **Function `shutil.make_archive(output, 'zip', dir_to_zip)`**:
  - Creates a zip file named `example.zip` containing all files and directories within `dir_to_zip`.

### Unzip Functionality

- **Function `shutil.unpack_archive("example.zip", "final_unzip", "zip")`**:
  - Extracts the contents of `example.zip` into the directory `final_unzip`.

<br>

## ⚙️ Prerequisites

- **Basic Understanding of Python**: Knowledge of file handling and the `shutil` module.
- **Python Environment Setup**: A Python interpreter installed on your system to run the code.
- **Basic Input/Output Operations**: Understanding how to specify file and directory paths in Python.

<br>

## 🛠️ How to Run

### Zipping a Directory

<br>

```python
import shutil

dir_to_zip = r"C:\Users\Akanksha\Documents\GitHub\Python-Mini-Projects\Projects\zip & unzip\input"
output = 'example'
shutil.make_archive(output, 'zip', dir_to_zip)
```
```python
python3 zip.py
```

### Unzipping a File

<br>

```python
import shutil

shutil.unpack_archive("example.zip", "final_unzip", "zip")
```
```python
python3 unzip.py
```

<br>

## 📜 Conclusion

The Zip and Unzip utility provides a simple yet effective way to compress and decompress files and directories using Python's `shutil` module. This functionality is useful for various file management tasks, including backup creation and distribution of bundled files.

<br>

## 👻 Author
[Akanksha Kanade](https://github.com/CandyBeans1609)
