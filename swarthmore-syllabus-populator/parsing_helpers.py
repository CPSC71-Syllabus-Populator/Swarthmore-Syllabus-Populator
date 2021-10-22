import re

def find_all(str, substr):
    start = 0
    while True:
        start = str.find(substr, start)
        if start == -1: return
        yield start
        start += len(substr) # use start += 1 to find overlapping matches

list(find_all('spam spam spam spam', 'spam')) # [0, 5, 10, 15]



# alternative solution
def find_all_regex(str, substr):
    substr = substr.lower()
    str = str.lower()
    inds = [m.start() for m in re.finditer(substr, str)]
    for ind in inds:
        print(str[ind:ind+len(substr)])

str, substr = 'MondayisthefirstdayMonday','Mon'
find_all_regex(str, substr)

