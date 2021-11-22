import re
import math
from datetime import datetime


def parse_syllabi_events(text):
    events = []

    parse_syllabi_times(text, events)
    parse_event_categories(text, events)
    parse_event_weekdays(text, events)

    return events


def parse_syllabi_times(text, events):
    pattern = re.compile(
        r'\d\d?:?(\d\d)?(am|pm)?(-|\sto\s)\d\d?:?(\d\d)?(am|pm)')
    matches = pattern.finditer(text)

    for i, match in enumerate(matches):
        span = match.span()
        start_time, end_time = format_parsed_time(text[span[0]:span[1]])
        events.append({
            'id': i,
            'span': span,
            'checked': True,
            'displayTime': start_time.strftime("%I:%M%p") + "-" + end_time.strftime("%I:%M%p"),
            'summary': "",
            'description': "",
            'startTimestamp': start_time,
            'endTimestamp': end_time,
            'recurrence': [],
            'reminders': {}
        })


def parse_event_categories(text, events):
    pattern = re.compile(
        r'\b(math clinic|meeting|session|office hours)',
        re.IGNORECASE
    )
    matches = list(pattern.finditer(text))

    for event in events:
        s, e = event['span']
        best_dist = float('inf')

        for match in matches:
            (ms, me) = match.span()
            match_dist = math.dist((s, e), (ms, me))
            if ms < s and match_dist < best_dist:
                best_dist = match_dist
                event['summary'] = text[ms:me]


def parse_event_weekdays(text, events):
    pattern = re.compile(
        r'(\b(Monday|Tuesday|Wednesday|Thursday|Friday)s?(\sand\s)?(Monday|Tuesday|Wednesday|Thursday|Friday)?s?|MWF)',
        re.IGNORECASE
    )
    matches = list(pattern.finditer(text))

    for event in events:
        s, e = event['span']
        best_dist = float('inf')
        for match in matches:
            (ms, me) = match.span()
            match_dist = math.dist((s, e), (ms, me))
            if match_dist < best_dist:
                best_dist = match_dist
                event['weekday'] = text[ms:me]


def format_parsed_time(parsed_time):
    t = parsed_time.lower()

    # determine whether the time is am or pm
    time_of_day = "am"
    if "am" in t and "pm" in t:
        time_of_day = "both"
    elif "pm" in t:
        time_of_day = "pm"

    # split the time interval into its start and end time
    if "-" in t:
        t = t.split("-")
    elif "to" in t:
        t = t.split("to")
    else:
        t = [t]

    # Strip away white space from start and end time
    t = [text.strip() for text in t]

    end_time = datetime.strptime(
        t[1], "%I:%M%p") if ':' in t[1] else datetime.strptime(t[1], "%I%p")

    if time_of_day != "both" and time_of_day not in t[0]:
        start_time_1 = datetime.strptime(
            t[0] + "am", "%I:%M%p") if ':' in t[0] else datetime.strptime(t[0] + "am", "%I%p")

        start_time_2 = datetime.strptime(
            t[0] + "pm", "%I:%M%p") if ':' in t[0] else datetime.strptime(t[0] + "pm", "%I%p")

        start_time = start_time_2 if start_time_2 <= end_time else start_time_1
    else:
        start_time = datetime.strptime(
            t[0], "%I:%M%p") if ':' in t[0] else datetime.strptime(t[0], "%I%p")

    return (start_time, end_time)
