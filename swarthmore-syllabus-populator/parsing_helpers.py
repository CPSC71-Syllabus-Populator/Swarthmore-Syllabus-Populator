import re

def find_all(str, substr):
    start = 0
    while True:
        start = str.find(substr, start)
        if start == -1:
            return
        yield start
        start += len(substr) # use start += 1 to find overlapping matches

list(find_all('spam spam spam spam', 'spam')) # [0, 5, 10, 15]



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
            inds.append([s,e])
            #inds.append(s)
    return inds


def find_all_nums(main_str):
    l = len(main_str)
    ind_arr = [int(s) for s in range(len(main_str)) if main_str[s].isdigit()]
    new_ind_arr = []
    # combine the inds for numbers with more than one digit
    i=0
    for i in range(len(ind_arr)-1):
        s = ind_arr[i]
        e = ind_arr[i]

        print("s i", s)
        for j in range(i,len(ind_arr)-1):
            if j<len(ind_arr)-1 and ind_arr[j+1]-ind_arr[j]==1:
                e=ind_arr[j+1]+1
                j+=1
            else:
                pass
            i=j
        if s!=e:
            new_ind_arr.append([s,e])
    return new_ind_arr






def find_am_pm(main_str):
    inds = [m.start() for m in re.finditer("am", main_str)]
    inds += [m.start() for m in re.finditer("pm", main_str)]
    return inds



main_str, substr = 'Monday100iamsthpe800mefiramst200dayMond00ay11','Mon'
find_word_regex(main_str, substr)

# regex = re.compile(r'\b(' + '|'.join(pattern) + r')\b')

keywords = ["OH", "office", "hours", "meeting", "class", "sessions",
"sessions", "drop-in"]
print("am/pm", find_am_pm(main_str))

num_inds = find_all_nums(main_str)
for i in num_inds:
    print(main_str[i[0]:i[1]])