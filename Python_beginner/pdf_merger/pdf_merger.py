import PyPDF2
import os
import sys

def merge_pdfs(output_filename, pdf_files=None):
    merger = PyPDF2.PdfMerger()
    
    try:
        if pdf_files:  # If specific files were provided
            for pdf in pdf_files:
                if os.path.exists(pdf):
                    merger.append(pdf)
                else:
                    print(f"Warning: File '{pdf}' not found - skipping")
        else:  # Merge all PDFs in current directory
            for file in os.listdir(os.curdir):
                if file.endswith(".pdf"):
                    merger.append(file)
        
        if len(merger.pages) > 0:  # Only write if we found PDFs
            merger.write(output_filename)
            print(f"Successfully merged into {output_filename}")
        else:
            print("No PDF files found to merge")
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        merger.close()

if __name__ == "__main__":
    output_file = "combined.pdf"
    
    # If arguments were provided, use them as specific files to merge
    if len(sys.argv) > 1:
        merge_pdfs(output_file, sys.argv[1:])
    else:
        merge_pdfs(output_file)