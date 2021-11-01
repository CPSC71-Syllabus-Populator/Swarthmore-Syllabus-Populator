from ast import parse
import re
from datetime import *


class Event:
    def __init__(self, time):
        self.time = time

    def __str__(self):
        return f"{self.time[0]}, {self.time[1]}"

    def set_title(self, title):
        self.title = title

    def set_weekday(self, weekday):
        self.weekday = weekday


def parse_times(text, events):
    times_indicies = set()

    pattern = re.compile(
        r'\d\d?:?(\d\d)?(am|pm)?(-|\sto\s)\d\d?:?(\d\d)?(am|pm)')

    matches = pattern.finditer(text)

    for match in matches:
        time_indicie = match.span()
        if time_indicie not in times_indicies:
            times_indicies.add(match.span())
            events.add(Event(time_indicie))


def convert_times(event, text):
    time = text[event.time[0]:event.time[1]]
    s = time.lower()
    if "-" in s:      # check if it's a times range
        s = s.split("-")
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
            t= t.split(":")

            if t[0] != '12':
                t[0]=str(int(t[0])+12)
                s[ind] = (":").join(t)
        elif "am" in t:
            t = t.replace("am"," ")
            if ":" not in s:
                t = t + ":00"
            t= t.split(":")
            if t[0] == '12':
                t[0]='00'
                s[ind] = (":").join(t)
    print(s)
    return s
            
    




def parse_titles(text, events):
    pattern = re.compile(
        r'\b(office hours|math clinic|class|meeting|meet|session)', re.IGNORECASE)
    for event in events:
        s, e = event.time

        matches = pattern.finditer(text[0:e])

        best_dist = float('inf')
        for match in matches:
            (ms, me) = match.span()
            if (s - me) < best_dist:
                event.set_title((ms, me))
    



def parse_weekdays(text, events):
    pattern = re.compile(
        r'\b(monday|mon|tuesday|tues|wednesday|wed|thursday|thurs|friday|fri)',
        re.IGNORECASE
    )

    for event in events:
        s, e = event.time

        matches = pattern.finditer(text)

        best_dist = float('inf')
        print(event)
        for match in matches:
            (ms, me) = match.span()
            if abs(s - me) > 550 or abs(e - ms) > 550:
                continue
            print(match)
            if (s - ms) < best_dist:
                event.set_weekday((ms, me))
        print("\n\n")


def parse_text_for_events(text):
    events = set()
    parse_times(text, events)
   
    parse_titles(text, events)
    parse_weekdays(text, events)

    for event in events:
        title = event.title
        time = event.time
        wd = event.weekday

        print(text[title[0]:title[1]])
        print(time, text[time[0]:time[1]])
        print(text[wd[0]:wd[1]])
        print("")




"""
This function returns a list of event objects, each containing
1+++ COURSE NUMBER/NAME 
1) Event class (course meeting times, OH, help sessions)
2) Event location  (if available)
3) Date of the event (if available)
4) Day of the week (if available)  -- LIST ONLY ONE DAY OF THE WEEK AT A TIME
5) Time of the event in a 24-hr format (if available)
"""
def create_an_event_list(text):
    events = set()
    parse_times(text, events)
    parse_titles(text, events)
    parse_weekdays(text, events)

    events_list = []
    for event in events:
        #event_dict = {"course name": TODO}
        # TODO : CHENGE EVENT TITLE TO EVENT CLASS
        
        event_dict = {"course name": TODO}

        title = event.title
        time = event.time
        wd = event.weekday



