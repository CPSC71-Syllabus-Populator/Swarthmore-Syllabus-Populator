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
            print("found", main_str[s:e])
            inds.append([s,e])
    return inds




str, substr = 'MondayisthefirstdayMonday','Mon'
find_all_regex(str, substr)

# regex = re.compile(r'\b(' + '|'.join(pattern) + r')\b')

keywords = ["OH", "office", "hours", "meeting", "class", "sessions",
"sessions", "drop-in"]
