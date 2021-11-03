import os
import pdfplumber
from parse_PDF import parse_text_for_events, create_an_event_list
import time
start_time = time.time()

def get_syllabi_directory_path():
    # change current directory to the parent
    os.chdir("../")

    return os.path.join(os.getcwd(), "sample-syllabi")


def select_syllabi_file(files):
    choice = ""

    while (not choice.isdigit() or int(choice) < 0 or int(choice) >
           len(files)):
        os.system('clear')
        print("Select a file from sample-syllabi/: ")

        for i, file in enumerate(files):
            print(f"{i} - {file:<45}")

        choice = input("\nSelect a file: ")

    os.system("clear")

    return files[int(choice)]


def extract_syllabi_text(syllabi):
    all_text = ""
    with pdfplumber.open(syllabi) as pdf:
        # page = pdf.pages[0] - comment out or remove line
        # text = page.extract_text() - comment out or remove line
        for pdf_page in pdf.pages:
            single_page_text = pdf_page.extract_text()
            all_text = all_text + '\n' + single_page_text

    return all_text



def main():
    syllabiPath = get_syllabi_directory_path()
    syllabiFiles = os.listdir(syllabiPath)
    syllabi = select_syllabi_file(syllabiFiles)
    text = extract_syllabi_text(os.path.join(syllabiPath, syllabi))
    parse_text_for_events(text)
    create_an_event_list(text)
    print("The dictionary of the events extracted from the file:", create_an_event_list(text))



main()
#print("--- %s seconds ---" % (time.time() - start_time))


# keywords = ["OH", "office", "hour", "meeting", "class", "sessions", "drop-in"]


# weekDays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",
#             "mon", "tue", "wed", "thu", "thur", "fri", "sat", "sun", "mwt", "tth"]

# weekDaysArr = []
# numsArr = []
# foundKeywords = []

# numIndsArr = []
# keywordIndsArr = []
# weekdayIndsArr = []

# # Splitting characters in String by ',' OR '_', OR '-', OR ... etc
# res = re.split(' |\n', all_text)
# # remove empty spaces from the list of words that were parced
# res = list(filter(None, res))

# """
# for ind, el in enumerate(res):
#     if el.isdigit():
#         numsArr.append(el)
#         numIndsArr.append(ind)
#     elif el.lower() in weekDays:
#         weekDaysArr.append(el)
#         weekdayIndsArr.append(ind)
#     elif el.lower() in keywords:
#         foundKeywords.append(el)
#         keywordIndsArr.append(ind)


# print("{} nums extracted: {}".format(len(numsArr), numsArr))
# print("{} weekdays extracted: {}".format(len(weekDaysArr), weekDaysArr))
# print("{} keywords extracted: {}".format(len(keywordIndsArr), foundKeywords))

# """

# # ATTEMPT 2: extract the keywords and numbers are the located the closest to each other
# # in the list of words
# #print("the closest matching pairs are")
# #pairs = sorted(product(numIndsArr, keywordIndsArr), key=lambda t: abs(t[0]-t[1]))
# # for i in range(len(keywordIndsArr)):
# #    currPair = pairs[i]
# #    print(currPair, ":", res[currPair[0]], res[currPair[1]])


# # ATTEMPT 3: extracting an words before and after
# # for ind in numIndsArr:
# #    print("num", res[ind], res[ind-10:ind+10])

# # issues:
# # PDFs are sometimes formated in 2 columns -- cannot read "across" the line

# # ATTEMPT 5:
# # new logic:  1) extract all numbers  2) search the substrings for keywords


# # create a long string from the result
# strRes = ''.join(map(str, res))
# # par.find_all_regex(main_str=strRes, substr="class")  # this will return inds where the word "class" occurs
# keyword_inds = par.find_all_regex(
#     main_str=strRes, patterns=keywords)  # returns inds of all keywords
# num_inds = par.find_all_nums(strRes)

# for k in keyword_inds:  # attempting to match keywords and numbers
#     # k==index of the last letter of the keyword
#     print("keyword:", strRes[k[0]:k[1]])
#     curr_num_inds = par.find_all_nums(strRes[k[1]:k[1]+150])
#     curr_times_inds = par.find_am_pm(strRes[k[1]:k[1]+150])
#     curr_weekday_inds = par.find_all_regex(
#         main_str=strRes[k[1]:k[1]+150], patterns=weekDays)
#     # adjust the inds
#     curr_num_inds_s = [x[0]+k[1] for x in curr_num_inds]
#     curr_num_inds_e = [x[1]+k[1] for x in curr_num_inds]
#     curr_times_inds = [x+k[1] for x in curr_times_inds]
#     curr_weekday_inds = [[x[0]+k[1], x[1]+k[1]] for x in curr_weekday_inds]

#     print("matching dates/times")
#     for s, e in zip(curr_num_inds_s, curr_num_inds_e):
#         print(strRes[s:e])
#     for ind in set(curr_times_inds):
#         print(strRes[ind:ind+2])
#     for ind in curr_weekday_inds:
#         print(strRes[ind[0]:ind[1]])


# # def is_a_time():
#     # if there is a am/pm keyword after the number
