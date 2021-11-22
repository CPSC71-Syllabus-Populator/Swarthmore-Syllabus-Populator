import pdfplumber
from api.scraping import *


def get_syllabi_text(syllabi):
    pdf_text = ""

    with pdfplumber.open(syllabi) as pdf:
        for pdf_page in pdf.pages:
            page_text = pdf_page.extract_text()
            pdf_text += '\n' + page_text

    return pdf_text


def get_semester_dates():
    all_dates = {}

    semester, year = get_semester()
    swarthmore_cal_page_url = get_page_url(semester, year)
    soup_list = scrape_page_text(swarthmore_cal_page_url)

    blocked_dates = set()
    if semester == "fall":
        blocked_dates |= get_fall_break(soup_list, year)
        blocked_dates |= get_thanksgiving_break(soup_list, year)
    else:
        blocked_dates |= get_spring_break(soup_list, year)
        blocked_dates |= get_mlkjr_day(soup_list, year)

    first_week = get_first_week(soup_list, year)
    last_day = get_last_day(soup_list, year)
    all_dates[0] = construct_days(first_week[0], last_day, blocked_dates)
    all_dates[1] = construct_days(first_week[1], last_day, blocked_dates)
    all_dates[2] = construct_days(first_week[2], last_day, blocked_dates)
    all_dates[3] = construct_days(first_week[3], last_day, blocked_dates)
    all_dates[4] = construct_days(first_week[4], last_day, blocked_dates)

    return all_dates


def build_google_calendar_events_JSON(parsed_events, all_dates):
    events_to_publish = []
    for event in parsed_events:
        start_time = event['startTimestamp'][17:-4]
        end_time = event['endTimestamp'][17:-4]

        dates = []
        for weekday in event['weekday'].lower().split():
            if weekday in set(["mondays", "monday", "mon", "mwf"]):
                dates += all_dates[0]

            if weekday in set(["tuesdays", "tuesday", "tues"]):
                dates += all_dates[1]

            if weekday in set(["wednesdays", "wednesday", "wed", "mwf"]):
                dates += all_dates[2]

            if weekday in set(["thursdays", "thursday", "thurs"]):
                dates += all_dates[3]

            if weekday in set(["fridays", "friday", "fri", "mwf"]):
                dates += all_dates[4]

        for date in dates:
            formatted_date = date.strftime("%Y-%m-%d")
            start_timestamp = f"{formatted_date}T{start_time}"
            end_timestamp = f"{formatted_date}T{end_time}"

            cal_event = {
                'summary': event['summary'],
                'location': "",
                'description': "",
                'start': {'dateTime': start_timestamp, 'timeZone': "America/New_York"},
                'end': {'dateTime': end_timestamp, 'timeZone': "America/New_York"},
                'recurrence': [],
                'reminders': {}
            }

            events_to_publish.append(cal_event)

    return events_to_publish
