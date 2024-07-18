import PyPDF2
import os
import string
import time

start_time = time.time()

# Open PDF file
path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, 'Sense_and_sensibility.pdf')
file_handle = open(file_path, 'rb')
pdfReader = PyPDF2.PdfReader(file_handle)

frequency_table = {}

# Iterating thru pages
for page_num in range(len(pdfReader.pages)):
    page_object = pdfReader.pages[page_num]
    page_text = page_object.extract_text()
    words = page_text.split("\n")
    for extracted_string in words:
        # Clean the selected word
        list_of_string = extracted_string.split()
        for chars in list_of_string:
            if chars.isdigit():
                pass
            if chars.isalpha(): 
                if chars in frequency_table:
                    frequency_table[chars] += 1
                else:
                    frequency_table[chars] = 1
            else:
                chars = chars[:-1]
                if chars in frequency_table:
                    frequency_table[chars] += 1
                else:
                    frequency_table[chars] = 1
end_time = time.time()
file_handle.close()

total_distinct_words = len(frequency_table)
print("Total number of unique words: " + str(total_distinct_words))
print ("time taken: " + str(end_time-start_time))