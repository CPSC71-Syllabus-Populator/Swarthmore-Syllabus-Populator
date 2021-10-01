

#  take in a pdf file
# use  pdfplumber python module to parse the file

import pdfplumber


# the difference between input() and sys.stdin.readline() is that the former doesn't
# read the escape char but we don't need it here 




#filename = input("please enter the file name: ")  # TODO uncomment

filename = '/Users/Arina/Documents/GitHub/Swarthmore-Syllabus-Populator/sample-syllabi/M34Fall_2019syll.pdf'

with pdfplumber.open(filename) as pdf:   # open method returns a pdfplumber.PDF obj
    pages = pdf.pages   # list of pages 
        
    # sample routine 
    first_page = pages[0]
    first_page_text = first_page.extract_text().split('\n')
    print("ROWS:\n", first_page_text)


#first_page= pages[0].extract_text()
#print("ALL:\n", first_page_rows)



# todo finish this 
#making the function
""" 
syll = pdfplumber.open(filename)
text = syll.pages[0]
value = text.split("\n")[6].replace("\t", "").split("R$")[1]
     value = float(value)
     sum += value
print("{} ----> {}".format(reports, value))

"""
# parce te tables separately 


