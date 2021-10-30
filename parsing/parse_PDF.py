from ast import parse
import re


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
