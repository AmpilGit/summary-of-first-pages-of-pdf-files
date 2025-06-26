import os
from pathlib import Path
import logging
from PyPDF2 import PdfReader, PdfWriter
import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.pdfbase.pdfmetrics import TTFont
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
def create_text_page(file_name):
    from PyPDF2 import PageObject
    from reportlab.pdfgen import canvas
    from io import BytesIO
    packet = BytesIO()
    can = canvas.Canvas(packet)
    can.setFont("Times-Bold", 10)
    can.drawString(50, 750, f"Source File: {file_name}") 
    can.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)
    return new_pdf.pages[0]
def extract_first_pages(input_folder, output_path):
    try:
        pdf_writer = PdfWriter()
        pdf_files = list(Path(input_folder).glob('*.pdf'))
        logger.info(f"Found {len(pdf_files)} PDF files in {input_folder}")
        
        if not pdf_files:
            logger.warning("No PDF files found in the input folder.")
            return
        for pdf_file in pdf_files:
            try:
                logger.info(f"Processing {pdf_file.name}")
                pdf_reader = PdfReader(pdf_file)
                if len(pdf_reader.pages) == 0:
                    logger.warning(f"No pages found in {pdf_file.name}. Skipping.")
                    continue
                first_page = pdf_reader.pages[0]
                fileName = create_text_page(pdf_file.name)
                
                pdf_writer.add_page(first_page)
                pdf_writer.add_page(fileName)
                logger.info(f"Extracted the first page from {pdf_file.name}")
            except Exception as e:
                logger.error(f"Error processing {pdf_file.name}: {str(e)}")
        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
        
        logger.info(f"All first pages saved to {output_path}")
        messagebox.showinfo("Success", f"All first pages saved to:\n{output_path}")
    except Exception as e:
        logger.error(f"Error during extraction: {str(e)}")
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
class PDFExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF First Page Extractor")
        self.root.geometry("500x300")
        
        # Variables
        self.input_folder = tk.StringVar()
        self.output_file = tk.StringVar()
        
        # Input folder selection
        tk.Label(root, text="Выберите папку с файлами pdf").pack(pady=10)
        tk.Entry(root, textvariable=self.input_folder, width=50, state="readonly").pack(pady=5)
        tk.Button(root, text="Выбрать папку", command=self.select_input_folder).pack(pady=5)
        
        # Output file selection
        tk.Label(root, text="Сохранить результат в файл").pack(pady=10)
        tk.Entry(root, textvariable=self.output_file, width=50, state="readonly").pack(pady=5)
        tk.Button(root, text="Исходный файл", command=self.select_output_file).pack(pady=5)
        
        # Extract button
        tk.Button(root, text="Собрать первые страницы", command=self.extract_pages).pack(pady=20)

    def select_input_folder(self):
        folder = filedialog.askdirectory(title="Select Folder with PDFs")
        if folder:
            self.input_folder.set(folder)

    def select_output_file(self):
        file = filedialog.asksaveasfilename(
            title="Save Resulting PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )
        if file:
            self.output_file.set(file)

    def extract_pages(self):
        input_folder = self.input_folder.get()
        output_path = self.output_file.get()
        
        if not input_folder:
            messagebox.showwarning("Input Error", "Please select a folder with PDFs.")
            return
        
        if not output_path:
            messagebox.showwarning("Output Error", "Please specify a file to save the result.")
            return
        
        extract_first_pages(input_folder, output_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFExtractorApp(root)
    root.mainloop()