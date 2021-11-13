import pdfplumber
from api.Event import Event
import re


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
        r'\b(office hours|math clinic|class|meeting|meet|session)',
        re.IGNORECASE
    )

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

        event.set_weekday("")

        best_dist = float('inf')
        for match in matches:
            (ms, me) = match.span()
            if abs(s - me) > 550 or abs(e - ms) > 550:
                continue
            if (s - ms) < best_dist:
                event.set_weekday(text[ms:me])


def parse_text_for_events(text):
    events = set()
    parse_times(text, events)
    parse_titles(text, events)
    parse_weekdays(text, events)

    json_data = {'events': []}
    for i, event in enumerate(events):
        event.set_id(i)
        json_data['events'].append(event.serialize_to_JSON())

    return json_data
