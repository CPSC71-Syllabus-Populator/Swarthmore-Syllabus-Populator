import re
from api.ParsedEvent import ParsedEvent
from datetime import datetime
import math


def parse_text_for_events(text):
    events = set()

    parse_times(text, events)
    parse_summaries(text, events)
    parse_weekdays(text, events)

    return events


def parse_times(text, events):
    times_indicies = set()

    pattern = re.compile(
        r'\d\d?:?(\d\d)?(am|pm)?(-|\sto\s)\d\d?:?(\d\d)?(am|pm)')

    matches = pattern.finditer(text)
    for i, match in enumerate(matches):
        span = match.span()
        if span not in times_indicies:
            times_indicies.add(span)
            # print(text[span[0]:span[1]], span)
            start_time, end_time = format_parsed_time(text[span[0]:span[1]])
            events.add(ParsedEvent(i, span, start_time, end_time))


def parse_summaries(text, events):
    pattern = re.compile(
        r'\b(math clinic|meeting|session|office hours)',
        re.IGNORECASE
    )
    matches = list(pattern.finditer(text))

    for event in events:
        s, e = event.pdf_location
        # print(text[s:e], (s, e))
        best_dist = float('inf')
        for match in matches:
            (ms, me) = match.span()
            match_dist = math.dist((s, e), (ms, me))
            # print("%-15s %-15s %-15.2f" % (text[ms:me], (ms, me), match_dist))
            if ms < s and match_dist < best_dist:
                best_dist = match_dist
                event.set_summary(text[ms:me])


def parse_weekdays(text, events):
    pattern = re.compile(
        r'(\b(Monday|Tuesday|Wednesday|Thursday|Friday)s?(\sand\s)?(Monday|Tuesday|Wednesday|Thursday|Friday)?s?|MWF)',
        re.IGNORECASE
    )
    matches = list(pattern.finditer(text))

    for event in events:
        (s, e) = event.pdf_location
        print(text[s:e], (s, e))

        best_dist = float('inf')
        for match in matches:
            (ms, me) = match.span()
            match_dist = math.dist((s, e), (ms, me))
            print("%-15s %-15s %-15.2f" % (text[ms:me], (ms, me), match_dist))
            if match_dist < best_dist:
                best_dist = match_dist
                event.set_weekday(text[ms:me])
        # print("\n")


def format_parsed_time(parsed_time):
    # s = parsed_time.lower()
    # if "-" in s:      # check if it's a times range
    #     s = s.split("-")
    # elif "to" in s:      # check if it's a times range
    #     s = s.split("to")
    # else:
    #     s = [s]
    # if len(s) == 2:
    #     if "am" not in s[0] and "pm" not in s[0]:
    #         if "am" in s[1]:
    #             s[0] += "am"
    #         if "pm" in s[1]:
    #             s[0] += "pm"

    # for ind, t in enumerate(s):
    #     # print("considering", t)
    #     if "pm" in t:
    #         t = t.replace("pm", " ")
    #         if ":" not in t:
    #             t += ":00"
    #         t = t.split(":")
    #         if t[0] != '12':
    #             t[0] = str(int(t[0])+12)
    #             s[ind] = (":").join(t)
    #         elif t[0] == '12':
    #             s[ind] = (":").join(t)

    #     elif "am" in t:
    #         t = t.replace("am", "")
    #         if ":" not in s:
    #             t = t + ":00"
    #             # print("here,", t)
    #         t = t.split(":")
    #         if t[0] != '12':
    #             s[ind] = (":").join(t)
    #         if t[0] == '12':
    #             t[0] = '00'
    #             s[ind] = (":").join(t)
    # # print("final result", s, s[0], s[1])

    # return "-".join(s)

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

    # Add the time of day to the start time if it does not contain it
    if time_of_day != "both" and time_of_day not in t[0]:
        t[0] += time_of_day

    # Convert the times to datetime objects based on whether they are in 24hr format
    t = [datetime.strptime(time, "%I:%M%p")
         if ':' in time else datetime.strptime(time, "%I%p") for time in t]

    return t
