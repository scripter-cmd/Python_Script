import subprocess
import os
def compress_pdf(input_pdf_path, output_pdf_path, target_size_kb):
    gs_command = [
        "gs",
        "-sDEVICE=pdfwrite",  
        "-dCompatibilityLevel=1.4",     
        "-dPDFSETTINGS=/ebook",  
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_pdf_path}",
        input_pdf_path
    ]
    try:
        subprocess.run(gs_command, check=True)
        file_size_kb = os.path.getsize(output_pdf_path) / 1024
        if file_size_kb > target_size_kb:
            print(f"Warning: Output PDF size is {file_size_kb:.2f} KB, which exceeds the target size of {target_size_kb} KB.")
        else:
            print(f"Compression successful. PDF size:{file_size_kb:.2f} KB.")
    except subprocess.CalledProcessError as e:
        print(f"Error during PDF compression: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

input_pdf = input("Enter Path :")

#path mention here for linux
output_pdf = "/home/"+os.getlogin()+"/Downloads/export.pdf"

#Path mention here for windows

# output_pdf = "C:\Users\\"+os.getlogin()+"\Desktop"


target_size_kb = 500

compress_pdf(input_pdf, output_pdf, target_size_kb)
