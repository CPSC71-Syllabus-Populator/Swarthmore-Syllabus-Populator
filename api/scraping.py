import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta


def get_semester():
    """
    Returns:
        * "spring" when called during the first six months of the year
        * "fall" when called during the last six months of the year
    """
    # store the time at which the function is called
    local_time = time.ctime(time.time()).split(" ")

    # store the month when the function is called
    if (local_time[1] == "Jul"):
        semester = "fall"
    elif (local_time[1] == "Aug"):
        semester = "fall"
    elif (local_time[1] == "Sep"):
        semester = "fall"
    elif (local_time[1] == "Oct"):
        semester = "fall"
    elif (local_time[1] == "Nov"):
        semester = "fall"
    elif (local_time[1] == "Dec"):
        semester = "fall"
    else:
        semester = "spring"

    # store the year when the function is called
    year = local_time[-1]

    return (semester, year)


def get_page_url(semester, year):
    """
    Purpose: returns the swarthmore semester schedule url
    """
    # create the url string for the current relevant semester
    return ("https://www.swarthmore.edu/academics/" + year + "-" +
            semester + "-semester")


def scrape_page_text(url):
    """
    Purpose: pull the tokenized text from the input url
    """
    # store webpage text from input url in outtxt
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")

    # split outtxt by new line character and remove all empty strings
    page_text_items = soup.get_text().split("\n")

    return [text_item for text_item in page_text_items if text_item != ""]


def get_first_week(soup_lst, year):
    """
    Purpose:
        * returns a list of the weekdays during week one
        * works for fall and spring
    """
    first_week = {}

    # search for the "Classes begin." text
    for i in range(len(soup_lst)):
        if soup_lst[i] == "Classes begin.":
            first_day = datetime.strptime(
                soup_lst[i - 1] + " " + year, "%B %d %Y")
            first_week[first_day.weekday()] = first_day
            break

    next_day = first_day + timedelta(1)
    while next_day.weekday() != first_day.weekday():
        if next_day.weekday() != 5 and next_day.weekday() != 6:
            first_week[next_day.weekday()] = next_day
        next_day += timedelta(1)

    return first_week


def get_last_day(soup_lst, year):
    """
    Purpose:
        * returns the last day of classes
        * works for fall and spring
    """
    # search for the "Classes end. Lottery for spring housing." text
    for i in range(len(soup_lst)):
        if soup_lst[i] == "Classes end. Lottery for spring housing.":
            return datetime.strptime(
                soup_lst[i - 1] + " " + year, "%B %d %Y")
        # search for the "Classes and seminars end." text
        elif soup_lst[i] == "Classes and seminars end.":
            return datetime.strptime(
                soup_lst[i - 1] + " " + year, "%B %d %Y")


def get_fall_break(soup_lst, year):
    """
    Purpose:
       * returns a list of the weekdays during fall break
       * only relevant for fall semesters
    """
    fall_break_week = set()

    # search for the "Fall Break begins after last class." text
    for i in range(len(soup_lst)):
        if soup_lst[i] == "Fall Break begins after last class.":
            pre_friday = datetime.strptime(
                soup_lst[i - 1] + " " + year, "%B %d %Y")
            break

    next_day = pre_friday + timedelta(1)
    while next_day.weekday() != 4:
        if next_day.weekday() != 5 and next_day.weekday() != 6:
            fall_break_week.add(next_day)
        next_day += timedelta(1)

    fall_break_week.add(next_day)

    return fall_break_week


def get_spring_break(soup_lst, year):
    """
    Purpose:
        * returns a list of the weekdays during spring break
        * only relevant for spring semesters
    """
    spring_break_week = set()

    # search for the "Spring Break begins after last class." text
    for i in range(len(soup_lst)):
        if soup_lst[i] == "Spring Break begins after last class.":
            pre_friday = datetime.strptime(
                soup_lst[i - 1] + " " + year, "%B %d %Y")
            break

    next_day = pre_friday + timedelta(1)
    while next_day.weekday() != 4:
        if next_day.weekday() != 5 and next_day.weekday() != 6:
            spring_break_week.add(next_day)
        next_day += timedelta(1)

    spring_break_week.add(next_day)

    return spring_break_week


def get_thanksgiving_break(soup_lst, year):
    thanksgiving_break = set()

    # search for the "Thanksgiving Break begins after last class." text
    for i in range(len(soup_lst)):
        if soup_lst[i] == "Thanksgiving Break begins after last class.":
            pre_thanksgiving_day = datetime.strptime(
                soup_lst[i - 1] + " " + year, "%B %d %Y")
            break

    next_day = pre_thanksgiving_day + timedelta(1)
    while next_day.weekday() != 5:
        if next_day.weekday() != 5 and next_day.weekday() != 6:
            thanksgiving_break.add(next_day)
        next_day += timedelta(1)

    return thanksgiving_break


def get_mlkjr_day(soup_lst, year):
    """
    Purpose:
        * returns MLK Jr. day
        * only relevant for spring semesters
    """
    # search for the "Martin Luther King Jr." text
    for i in range(len(soup_lst)):
        if "Martin Luther Kind Jr." in soup_lst[i]:
            return datetime.strptime(
                soup_lst[i - 1] + " " + year, "%B %d %Y")


def construct_days(first_day, last_day,  blocked_days):
    all_days = []
    next_friday = first_day + timedelta(7)
    while next_friday <= last_day:
        if next_friday not in blocked_days:
            all_days.append(next_friday)
        next_friday += timedelta(7)

    return all_days
