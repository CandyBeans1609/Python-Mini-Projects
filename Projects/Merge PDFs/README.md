# PDF Merger Script

This guide demonstrates how to implement a script that merges multiple PDF files into a single PDF file. The script uses the `PyPDF2` library for manipulating PDF files and the `os` library for handling file paths and directories.

<br>

<p align="center">
    <img src="https://blog.aspose.com/pdf/merge-pdf-files-in-python/images/Merge-PDF-Files-into-Single-PDF.jpg">
</p>

<br>

## 🌟 Explanation

- **PDF Merging**: The script combines multiple PDF files into a single PDF document.
- **Directory Handling**: Sets the working directory to the folder containing the PDFs and processes files in that directory.
- **File Processing**: Uses `PyPDF2` to append each PDF to the final merged document.
- **Output**: Saves the merged PDF in the same directory.

<br>

## ⚙️ Prerequisites

- **Basic Python Knowledge**: Understanding of Python syntax, functions, and file handling.
- **Familiarity with PDF Files**: Basic knowledge of PDF file structure and manipulation.
- **Required Libraries**: `PyPDF2` library for working with PDF files.

<br>

## 🛠️ How to Run

1. **Ensure the script is saved as** `merge_pdf.py`:
    - Copy the provided script code and save it as `merge_pdf.py`.

2. **Install the required library**:
    ```bash
    pip install PyPDF2
    ```

   This will install:

   - `PyPDF2`: a library for manipulating PDF files.

3. **Run the script**:
    ```bash
    python merge_pdf.py
    ```

<br>

The script will merge all PDF files in the specified directory and save the result as `merged-pdf.pdf` in the same directory.

<br>

## 📺 Output

### Before Merging (before running the script)
![image](https://github.com/user-attachments/assets/eddc358d-4c61-4326-accb-0f2356e74f99)

<br>

### After Merging (after running the script)

![image](https://github.com/user-attachments/assets/e1b5ec2a-848e-46d6-a10c-7af6a19e3c03)

![image](https://github.com/user-attachments/assets/b8660cbe-06f3-4a6a-943e-0dc3b6dc275f)


<br>


## 📜 Conclusion

This script efficiently merges multiple PDF files into a single document using `PyPDF2`. It demonstrates fundamental techniques for file handling and PDF manipulation.

<br>

## 👻 Author

[Akanksha Kanade](https://github.com/CandyBeans1609)



