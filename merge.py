from PyPDF2 import PdfFileMerger, PdfFileReader

# Create PdfFileMerger object
mergedObject = PdfFileMerger()

# Loop through all pdf files in the range 1-x (Edit the range with the amount of PDFs you have).
for fileNumber in range(1, 14):
    # Edit the file names depending on how your file sequence is named.  Ex: Chapter 1.pdf, Chapter 2.pdf, etc.
    mergedObject.append(PdfFileReader('Chapter ' + str(fileNumber) + '.pdf', 'rb'))

# Output the files into a merged file.
mergedObject.write("Book.pdf")
