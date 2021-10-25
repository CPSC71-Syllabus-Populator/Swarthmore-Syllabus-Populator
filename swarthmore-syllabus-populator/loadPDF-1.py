

#  take in a pdf file
# use  pdfplumber python module to parse the file

import pdfplumber
import re
from itertools import product
import parsing_helpers as par

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

#cd /Users/arina/Desktop/Swarthmore-Syllabus-Populator/swarthmore-syllabus-populator

syll = pdfplumber.open(filename)

if filename.endswith('.pdf'):
    all_text = '' # new line
    with pdfplumber.open(filename) as pdf:
            # page = pdf.pages[0] - comment out or remove line
            # text = page.extract_text() - comment out or remove line
            for pdf_page in pdf.pages:
                single_page_text = pdf_page.extract_text()
                # separate each page's text with newline
                all_text = all_text + '\n' + single_page_text



keywords = ["OH", "office", "hours", "meeting", "class", "sessions",
"sessions", "drop-in"]

weekDays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday",
"mon", "tue","wed","thu","thur","fri","sat","sun", "mwt", "tth", "mondays","tuesdays","wednesdays","thursdays","fridays","saturdays","sundays"]

weekDaysArr = []
numsArr = []
foundKeywords = []

numIndsArr = []
keywordIndsArr = []
weekdayIndsArr = []

#    # Splitting characters in String by ',' OR '_', OR '-', OR ... etc
#res = re.split(', |_|-|\n| |%|. |\t', all_text)
res = re.split(' |\n', all_text)
res = list(filter(None, res))   #remove empty spaces from the list of words that were parced


for ind, el in enumerate(res):
    if el.isdigit():
        numsArr.append(el)
        numIndsArr.append(ind)
    elif el.lower() in weekDays:
        weekDaysArr.append(el)
        weekdayIndsArr.append(ind)
    elif el.lower() in keywords:
        foundKeywords.append(el)
        keywordIndsArr.append(ind)


print("{} nums extracted: {}".format(len(numsArr), numsArr))
print("{} weekdays extracted: {}".format(len(weekDaysArr), weekDaysArr))
print("{} keywords extracted: {}".format(len(keywordIndsArr), foundKeywords))


# ATTEMPT 2: extract the keywords and numbers are the located the closest to each other
# in the list of words
#print("the closest matching pairs are")
#pairs = sorted(product(numIndsArr, keywordIndsArr), key=lambda t: abs(t[0]-t[1]))
#for i in range(len(keywordIndsArr)):
#    currPair = pairs[i]
#    print(currPair, ":", res[currPair[0]], res[currPair[1]])


# ATTEMPT 3: extracting an words before and after
#for ind in numIndsArr:
#    print("num", res[ind], res[ind-10:ind+10])

# issues:
# PDFs are sometimes formated in 2 columns -- cannot read "across" the line

# ATTEMPT 5:
# new logic:  1) extract all numbers  2) search the substrings for keywords



# create a long string from the result
strRes = ''.join(map(str, res))
# par.find_all_regex(main_str=strRes, substr="class")  # this will return inds where the word "class" occurs
keyword_inds = par.find_all_regex(main_str=strRes, patterns=keywords)  # returns inds of all keywords
num_inds = par.find_all_nums(strRes)

for k in keyword_inds:  #attempting to match keywords and numbers
    print("keyword:", strRes[k[0]:k[1]])
    curr_num_inds = par.find_all_nums(strRes[k[1]:k[1]+100])
    curr_times_inds = par.find_am_pm(strRes[k[1]:k[1]+100])
    # adjust the inds
    curr_num_inds = [x+k[1] for x in curr_num_inds]
    curr_times_inds = [x+k[1] for x in curr_times_inds]
    for ind in curr_num_inds:
        print(strRes[ind])
    for ind in curr_times_inds:
        print(strRes[ind:ind+2])


