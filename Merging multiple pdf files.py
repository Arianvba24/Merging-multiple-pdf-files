from PyPDF2 import PdfMerger
l1 =["certificado.pdf","pruebas_1.pdf"]
x = r"C:\Users\Cash\Downloads"
merger = PdfMerger()
for i in l1:
    
    merger.append(f"{x}\\{i}")
    
merger.write(r"C:\Users\Cash\Downloads\output.pdf")
merger.close()
