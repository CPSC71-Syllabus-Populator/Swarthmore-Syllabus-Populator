import re
from itertools import combinations, groupby, count
from operator import itemgetter


def find_all(str, substr):
    start = 0
    while True:
        start = str.find(substr, start)
        if start == -1:
            return
        yield start
        start += len(substr)  # use start += 1 to find overlapping matches

# an alternative implementation using Regex


def find_word_regex(main_str, substr):
    substr = substr.lower()
    main_str = main_str.lower()
    #regex = re.compile(r'\b(' + '|'.join(pattern) + r')\b')
    inds = [m.start() for m in re.finditer(substr, main_str)]
    return inds


# this function
def find_all_regex(main_str, patterns):
    main_str = main_str.lower()
    inds = []
    for pattern in patterns:
        if re.search(pattern, main_str):
            match = re.search(pattern, main_str)
            s = match.start()
            e = match.end()
            #print("found", main_str[s:e])
            inds.append([s, e])
    return inds


def find_all_nums(main_str):
    l = len(main_str)
    ind_arr = [int(s) for s in range(len(main_str)) if main_str[s].isdigit()]
    # combine the inds for numbers with more than one digit
    ind_arr = remove_consecutive(ind_arr)
    return ind_arr


def diff(lst):
    return map(lambda x, y: y-x, lst[:-1], lst[1:])


def remove_consecutive(lst):
    groups = groupby(lst, key=lambda item, c=count(): item - next(c))
    tmp = [list(g) for k, g in groups]
    return [[t[0], t[-1]+1] for t in tmp]


def find_am_pm(main_str):
    main_str = main_str.lower()
    inds = [m.start() for m in re.finditer("am", main_str)]
    inds += [m.start() for m in re.finditer("pm", main_str)]
    return inds


# TESTING
#main_str, substr = 'Monday100iamsthpe800mefiramst200dayMond00ay11','Mon'
#find_word_regex(main_str, substr)

# regex = re.compile(r'\b(' + '|'.join(pattern) + r')\b')
#keywords = ["OH", "office", "hours", "meeting", "class", "sessions", "sessions", "drop-in"]
#print("am/pm", find_am_pm(main_str))

#num_inds = find_all_nums(main_str)
# for i in num_inds:
#    print(main_str[i[0]:i[1]])
