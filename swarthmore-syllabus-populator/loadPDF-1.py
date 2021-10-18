

#  take in a pdf file
# use  pdfplumber python module to parse the file

import pdfplumber
import re


# the difference between input() and sys.stdin.readline() is that the former doesn't
# read the escape char but we don't need it here 

#filename = input("please enter the file name: ")  # TODO uncomment

filename = '/Users/Arina/Desktop/Swarthmore-Syllabus-Populator/sample-syllabi/M34Fall_2019syll.pdf'
filename = '/Users/Arina/Desktop/Swarthmore-Syllabus-Populator/sample-syllabi/Popular Myths Syllabus.pdf'
filename = '/Users/Arina/Desktop/Swarthmore-Syllabus-Populator/sample-syllabi/MATH027.pdf'
""" 
with pdfplumber.open(filename) as pdf:   # open method returns a pdfplumber.PDF obj
    pages = pdf.pages   # list of pages 
        
    # sample routine 
    first_page = pages[0]
    first_page_text = first_page.extract_text().split('\n')
    print("ROWS:\n", first_page_text)

"""

# /Users/arina/Desktop/Swarthmore-Syllabus-Populator/swarthmore-syllabus-populator

syll = pdfplumber.open(filename)
# first_page = syll.pages[0]

# for line  7th line (ind 6) .replace('old parameter', 'new parameter')
# then split use .split() it will separate the text from the parameter we pass.
# value = text.split("\n")[6].replace("\t", "").split("R$")[1]

# extract all dates and days of the week
weekDays = set(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday", 
"Mon", "Tue","Wed","Thu","Thur","Fri","Sat","Sun", "MWF", "TTH"])

weekDaysArr = []

for ind, page in enumerate(syll.pages):
    text = page.extract_text()
    # Splitting characters in String by ',' OR '_', OR '-', OR ... etc
    res = re.split(', |_|-|\n| |%|. |\t', text)
    res =  list(filter(None, res))   #remove empty spaces from the list of words that were parced
    #print(res) print all words
    numsArr = []
    for el in res:
        if el.isdigit():
            numsArr.append(el)
        if el in weekDays:
            weekDaysArr.append(el)

        # check if the word is next to other 

    
    print("all nums extracted from page {} are: {}".format(ind, numsArr))
    print("all week days extracted from page {} are: {}".format(ind, weekDaysArr))
       


    # try to identify times by checking if a number is next to 


#value = text.split("\n")[6].replace("\t", "").split("R$")[1]
#print("text 1:", value)
#print("text 2:", )

# parce te tables separately 


