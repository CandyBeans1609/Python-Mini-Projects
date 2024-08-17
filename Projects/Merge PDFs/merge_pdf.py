from PyPDF2 import PdfWriter
import os

# Specify the directory where your PDFs are located using a raw string or double backslashes
pdf_folder = r"C:\Users\Akanksha\Documents\GitHub\Python-Mini-Projects\Projects\Merge PDFs"

# Change the working directory to the folder containing the PDFs
os.chdir(pdf_folder)

# List all files in the specified directory
files = [file for file in os.listdir() if file.endswith(".pdf")]

# Initialize PdfWriter
merger = PdfWriter()

# Loop through each PDF file and append it to the merger
for pdf in files:
    merger.append(pdf)

# Write the merged PDF to the same folder
merged_pdf_path = os.path.join(pdf_folder, "merged-pdf.pdf")
merger.write(merged_pdf_path)
merger.close()

print(f"\nMerged PDF saved at: {merged_pdf_path}\n")
