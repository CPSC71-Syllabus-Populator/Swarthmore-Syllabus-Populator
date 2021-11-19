import pdfplumber
from api.scraping import *
from api.CalendarEvent import CalendarEvent
from datetime import datetime


def extract_syllabi_text(syllabi):
    pdf_text = ""

    with pdfplumber.open(syllabi) as pdf:
        for pdf_page in pdf.pages:
            page_text = pdf_page.extract_text()
            pdf_text += '\n' + page_text

    return pdf_text


def serialize_parsed_events_to_JSON(events):
    json_data = {'events': []}
    for event in events:
        # if event.parsed_weekday == None or event.summary == None:
        # continue
        json_event = {'id': event.id,
                      'checked': event.checked,
                      'summary': event.summary,
                      'weekday': event.parsed_weekday,
                      'startTimestamp': event.start_time,
                      'endTimestamp': event.end_time,
                      'displayTime': event.start_time.strftime("%I:%M%p") + "-"
                      + event.end_time.strftime("%I:%M%p"),
                      }
        json_data['events'].append(json_event)

    return json_data


def build_google_calendar_events_JSON(events):
    json_data = []
    url = constructurl()
    souplist = constructsoup(url)

    semester, year = getsemester()
    print(semester, year)

    for event in events:
        start_time = event['startTimestamp'][17:-4]
        end_time = event['endTimestamp'][17:-4]
        print(start_time)
        print(end_time)

        dates = []
        if event["weekday"] == "Mondays":
            dates = constructmondays(souplist)

        for date in dates:
            start_timestamp = f"{year}-{date[0]}-{date[1]}T{start_time}"
            end_timestamp = f"{year}-{date[0]}-{date[1]}T{end_time}"

            cal_event = {
                'summary': event["summary"],
                'location': "",
                'description': "",
                'start': {'dateTime': start_timestamp, "timeZone": "America/New_York"},
                'end': {'dateTime': end_timestamp, "timeZone": "America/New_York"},
                'recurrence': [],
                'reminders': {}
            }

            json_data.append(cal_event)

    return json_data
