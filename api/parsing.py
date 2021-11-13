import pdfplumber
import json
import re


class Event:
    def __init__(self, location, time):
        self.time = time
        self.location = location

    def __str__(self):
        return f"{self.time[0]}, {self.time[1]}"

    def set_title(self, title):
        self.title = title

    def set_weekday(self, weekday):
        self.weekday = weekday

    def set_id(self, id):
        self.id = id

    def serialize_to_JSON(self):
        return {'id': self.id, 'title': self.title, 'time': self.time,
                'weekday': self.weekday}


def extract_syllabi_text(syllabi):
    pdf_text = ""

    with pdfplumber.open(syllabi) as pdf:
        for pdf_page in pdf.pages:
            page_text = pdf_page.extract_text()
            pdf_text += '\n' + page_text

    return pdf_text


def parse_times(text, events):
    times_indicies = set()

    pattern = re.compile(
        r'\d\d?:?(\d\d)?(am|pm)?(-|\sto\s)\d\d?:?(\d\d)?(am|pm)')

    matches = pattern.finditer(text)
    for match in matches:
        s, e = match.span()
        if (s, e) not in times_indicies:
            times_indicies.add((s, e))
            events.add(Event((s, e), text[s:e]))


def parse_titles(text, events):
    pattern = re.compile(
        r'\b(office hours|math clinic|class|meeting|meet|session)', re.IGNORECASE)

    for event in events:
        s, e = event.location

        matches = pattern.finditer(text[0:e])

        best_dist = float('inf')
        event.set_title("")
        for match in matches:
            (ms, me) = match.span()
            if (s - me) < best_dist:
                event.set_title(text[ms:me])


def parse_weekdays(text, events):
    pattern = re.compile(
        r'\b(monday|mon|tuesday|tues|wednesday|wed|thursday|thurs|friday|fri)',
        re.IGNORECASE
    )

    for event in events:
        s, e = event.location
        matches = pattern.finditer(text)
        # print(event) REMOVE

        event.set_weekday("")

        best_dist = float('inf')
        for match in matches:
            (ms, me) = match.span()
            if abs(s - me) > 550 or abs(e - ms) > 550:
                continue
            # print(match) REMOVE
            if (s - ms) < best_dist:
                event.set_weekday(text[ms:me])
        # print("\n\n") REMOVE


def parse_text_for_events(text):
    events = set()
    parse_times(text, events)
    parse_titles(text, events)
    parse_weekdays(text, events)

    data = {'events': []}
    for i, event in enumerate(events):
        event.set_id(i)
        data['events'].append(event.serialize_to_JSON())

    return data
