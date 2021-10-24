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
def find_all_regex(main_str, substr):
    substr = substr.lower()
    main_str = main_str.lower()
    #regex = re.compile(r'\b(' + '|'.join(pattern) + r')\b')

    inds = [m.start() for m in re.finditer(substr, main_str)]

    print("here inds", inds)
    for ind in inds:
        print(main_str[ind:ind+len(substr)])


# this function
def find_all_regex2(main_str, patterns):
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
    return [int(s) for s in range(len(main_str)) if main_str[s].isdigit()]


def find_am_pm(main_str):
    inds = [m.start() for m in re.finditer("am", main_str)]
    inds += [m.start() for m in re.finditer("pm", main_str)]
    return inds



str, substr = 'MondayiamsthpmefiramstdayMonday','Mon'
find_all_regex(str, substr)

# regex = re.compile(r'\b(' + '|'.join(pattern) + r')\b')

keywords = ["OH", "office", "hours", "meeting", "class", "sessions",
"sessions", "drop-in"]
print("am/pm", find_am_pm(str))