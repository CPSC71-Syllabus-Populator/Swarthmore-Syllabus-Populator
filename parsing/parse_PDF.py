from ast import parse
import re
from datetime import *


class Event:
    def __init__(self, time, course_name):
        self.time = time
        self.course_name = course_name

    def __str__(self):
        return f"{self.time[0]}, {self.time[1]}"

    def set_title(self, title):
        self.title = title

    def set_cathegory(self, cathegory): # Available cathegories: 
        self.cathegory = cathegory      # "Office Hours", "Class Times", "Help Sessions"

    def set_weekday(self, weekday):
        self.weekday = weekday

    def cathegorize(self, matches_arr, cathegory):
        best_dist = float('inf')
        for match in matches_arr:
            (ms, me) = match.span()
            if (ms - me) < best_dist:
                self.set_title((ms, me))   # (ms, me) are the indices
                self.set_cathegory(cathegory)


def parse_course_name(text):
    # look for the first number in the doc
    # the word before that is likely the course title
    for ind, symbol in enumerate(text):
         if symbol.isdigit():
            s = ind
            ind += 1
            while ind < len(text) and text[ind].isdigit():
                ind += 1
            e = ind    # (s,e) is the first number
            break 
    return text[s-6:e]   # TODO: make it more generalizable? 
 




def parse_times(text, events):
    course_name = parse_course_name(text)
    times_indicies = set()
    pattern = re.compile(
        r'\d\d?:?(\d\d)?(am|pm)?(-|\sto\s)\d\d?:?(\d\d)?(am|pm)')

    matches = pattern.finditer(text)

    for match in matches:
        time_indicie = match.span()
        if time_indicie not in times_indicies:
            times_indicies.add(match.span())
            events.add(Event(time_indicie, course_name))


def convert_times(text, event):
    time = text[event.time[0]:event.time[1]]
    s = time.lower()
    if "-" in s:      # check if it's a times range
        s = s.split("-")
    elif "to" in s:      # check if it's a times range
        s = s.split("to")
    else:
        s = [s]
    if len(s)==2:
        if "am" not in s[0] and "pm" not in s[0]:
            if "am" in s[1]:
                s[0] += "am"
            if "pm" in s[1]:
                s[0] += "pm"
            
    for ind, t in enumerate(s):
        if "pm" in t:
            t=t.replace("pm"," ")
            if ":" not in t:
                t += ":00"
            t = t.split(":")

            if t[0] != '12':
                t[0]=str(int(t[0])+12)
                s[ind] = (":").join(t)
        elif "am" in t:
            t = t.replace("am", " ")
            if ":" not in s:
                t = t + ":00"
            t= t.split(":")
            if t[0] == '12':
                t[0]='00'
                s[ind] = (":").join(t)
    return "-".join(s)
            

def parse_cathegorize_titles(text, events):
    oh_pattern = re.compile(
        r'\b(office hours|oh|)', re.IGNORECASE)
    class_pattern =  re.compile(
        r'\b(class|meeting|lecture)', re.IGNORECASE)
    help_pattern =  re.compile(
        r'\b(clinic|help|session)', re.IGNORECASE)

    for event in events:
        s, e = event.time  # get the time associated with the event

        oh_matches = oh_pattern.finditer(text[0:e])
        class_matches = class_pattern.finditer(text[0:e])
        help_matches = help_pattern.finditer(text[0:e])
        
        event.cathegorize(oh_matches, "Office Hours")
        event.cathegorize(class_matches, "Class Times")
        event.cathegorize(help_matches, "Help Sessions")






def parse_weekdays(text, events):
    pattern = re.compile(
        r'\b(monday|mon|tuesday|tues|wednesday|wed|thursday|thurs|friday|fri)',
        re.IGNORECASE
    )
    for event in events:
        s, e = event.time
        matches = pattern.finditer(text)
        best_dist = float('inf')
        for match in matches:
            (ms, me) = match.span()
            if abs(s - me) > 550 or abs(e - ms) > 550:
                continue
            if (s - ms) < best_dist:
                event.set_weekday = text[ms:me]
        #print("\n")


def parse_text_for_events(text):
    events = set()
    parse_times(text, events)
    parse_cathegorize_titles(text, events)
    parse_weekdays(text, events)

    for event in events:
        title = event.title
        #print(text[title[0]:title[1]])
        #print(convert_times(text, event))  # this will print the time
        #print("")






"""
This function returns a list of event dictionaries, each containing
1) Event class (course meeting times, OH, help sessions)
3) Date of the event (if available)
4) Day of the week (if available)  -- LIST ONLY ONE DAY OF THE WEEK AT A TIME
5) Time of the event in a 24-hr format (if available)
"""
def get_events_dict_list(text):
    events = set()
    parse_times(text, events)
    parse_cathegorize_titles(text, events)
    parse_weekdays(text, events)

    event_dict_list = []  # a list of events (each event is a dictionary)

    for event in events:
        event_dict = {}
        event_dict["course name"] = event.course_name
        event_dict["event title"] = text[event.title[0]:event.title[1]]
        event_dict["time"] = convert_times(text, event)
        event_dict["day of the week"] = text[event.weekday[0]:event.weekday[1]]
        event_dict["cathegory"] = event.cathegory
        event_dict_list.append(event_dict)
    return event_dict_list







"""
This function returns a list of event objects, with the following fields:
"""
def get_events_list(text):
    events = set()
    parse_times(text, events)
    parse_cathegorize_titles(text, events)
    parse_weekdays(text, events)

    events_list = []  # a list of events (each event is a dictionary)

    for event in events:
        event.time = convert_times(text, event)
        events_list.append(event)
    return events_list






