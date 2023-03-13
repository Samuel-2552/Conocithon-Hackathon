import ipp

# Set up a connection to the printer
printer_uri = 'ipp://192.168.1.100/ipp/print'  # Replace with the URI of your printer
printer = ipp.Printer(printer_uri)

# Load the file to be printed
file_path = 'path/to/document.pdf'  # Replace with the path to your document file
with open(file_path, 'rb') as file:
    file_contents = file.read()

# Print the file
job_attributes = {'document-format': 'application/pdf'}
job_id = printer.printJob(file_contents, job_attributes)

print("Print job submitted successfully.")
