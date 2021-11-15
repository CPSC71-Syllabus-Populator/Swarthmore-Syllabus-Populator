from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from bs4 import BeautifulSoup
import requests
import time


def verify_google_credentials(scope):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scope)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'api/credentials.json', scope)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)


def dateadd(indate, n):
    retdate = [indate[0], indate[1] + n]
    year = getsemester()[1]

    # january to february
    if (retdate[0] == 1) and (retdate[1] > 31):
        retdate[0] = 2
        retdate[1] = retdate[1] % 31
    # february to march (during non leap years)
    elif (year % 4 != 0) and (retdate[0] == 2) and (retdate[1] > 28):
        retdate[0] = 3
        retdate[1] = retdate[1] % 28
    # february to march (during leap years)
    elif (year % 4 == 0) and (retdate[0] == 2) and (retdate[1] > 29):
        retdate[0] = 3
        retdate[1] = retdate[1] % 29
    # march to april
    elif (retdate[0] == 3) and (retdate[1] > 31):
        retdate[0] = 4
        retdate[1] = retdate[1] % 31
    # april to may
    elif (retdate[0] == 4) and (retdate[1] > 30):
        retdate[0] = 5
        retdate[1] = retdate[1] % 30
    # may to june
    elif (retdate[0] == 5) and (retdate[1] > 31):
        retdate[0] = 6
        retdate[1] = retdate[1] % 31
    # june to july
    elif (retdate[0] == 6) and (retdate[1] > 30):
        retdate[0] = 7
        retdate[1] = retdate[1] % 30
    # july to august
    elif (retdate[0] == 7) and (retdate[1] > 31):
        retdate[0] = 8
        retdate[1] = retdate[1] % 31
    # august to september
    elif (retdate[0] == 8) and (retdate[1] > 31):
        retdate[0] = 9
        retdate[1] = retdate[1] % 31
    # september to october
    elif (retdate[0] == 9) and (retdate[1] > 30):
        retdate[0] = 10
        retdate[1] = retdate[1] % 30
    # october to november
    elif (retdate[0] == 10) and (retdate[1] > 31):
        retdate[0] = 11
        retdate[1] = retdate[1] % 31
    # november to december
    elif (retdate[0] == 11) and (retdate[1] > 30):
        retdate[0] = 12
        retdate[1] = retdate[1] % 30
    # december to january
    elif (retdate[0] == 12) and (retdate[1] > 31):
        retdate[0] = 1
        retdate[1] = retdate[1] % 31

    return retdate

# returns true if indate1 is before indate2 or if indate1 is indate2, returns
# false otherwise


def comparedays(indate1, indate2):
    # if indate1's month is before indate2's month
    if (indate1[0] < indate2[0]):
        return True
    # if indate1's month is the same as indate2's month
    elif (indate1[0] == indate2[0]):
        # if indate1's day is before or the same as indate2's day
        if (indate1[1] <= indate2[1]):
            return True
        else:
            return False
    else:
        return False


# returns "spring" when called during the first six months of the year, returns
# "fall" when called during the last six months of the year
def getsemester():
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

    return [semester, int(year)]

# returns the swarthmore semester schedule url


def constructurl():
    # get the semester
    urlsem = getsemester()
    # create the url string for the current relevant semester
    url = ("https://www.swarthmore.edu/academics/" + str(urlsem[1]) + "-" +
           urlsem[0] + "-semester")

    return url


# pull the tokenized text from the input url
def constructsoup(url):
    # store webpage text from input url in outtxt
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    outtxt = soup.get_text()

    # split outtxt by new line character and remove all empty strings
    outlst = outtxt.split("\n")
    cleanoutlst = []
    for i in range(len(outlst)):
        if (outlst[i] != ""):
            cleanoutlst.append(outlst[i])

    return cleanoutlst

# returns a list of the weekdays during week one
# works for fall and spring


def getfirstweek(souplst):
    # search for the "Classes begin." text
    for i in range(len(souplst)):
        if (souplst[i] == "Classes begin."):
            monday = souplst[i - 1]
            break

    # if monday is in August
    if (monday[0] == "A"):
        monday = [8, int(monday[-2:])]
    # if monday is in January (accounting for MLK Jr. day)
    else:
        monday = [1, int(monday[-2:]) - 1]

    # get dates for the first five weekdays in week one
    firstweek = [monday]
    for i in range(1, 5):
        tempday = dateadd(monday, i)
        firstweek.append(tempday)

    return firstweek

# returns a list of the weekdays during fall break
# only relevant for fall semesters


def getfallbreak(souplst):
    # search for the "Fall Break begins after last class." text
    for i in range(len(souplst)):
        if (souplst[i] == "Fall Break begins after last class."):
            prefriday = souplst[i - 1]
            break

    # store friday before fall break
    prefriday = [10, int(prefriday[-2:])]

    # store dates for weekdays of fall break
    fbweek = []
    for i in range(3, 8):
        fbtempday = [10, prefriday[1] + i]
        fbweek.append(fbtempday)

    return fbweek

# returns the two days of thanksgiving break
# only relevant for fall semesters


def getthanksgivingbreak(souplst):
    # search for the "Thanksgiving Break begins after last class." text
    for i in range(len(souplst)):
        if (souplst[i] == "Thanksgiving Break begins after last class."):
            prewednesday = souplst[i - 1]
            break

    # store wednesday before thanksgiving break
    prewednesday = [11, int(prewednesday[-2:])]

    # store dates for weekdays of thanksgiving break
    tbdays = []
    for i in range(1, 3):
        tbtempday = [11, prewednesday[1] + i]
        tbdays.append(tbtempday)

    return tbdays

# returns MLK Jr. day
# only relevant for spring semesters


def getmlkjrday(souplst):
    # search for the "Martin Luther King Jr." text
    for i in range(len(souplst)):
        if (souplst[i][:22] == "Martin Luther King Jr."):
            mlkjrday = souplst[i - 1]
            break

    # store date for MLK Jr. day
    mlkjrday = [1, int(mlkjrday[-2:])]

    return mlkjrday

# returns a list of the weekdays during spring break
# only relevant for spring semesters


def getspringbreak(souplst):
    # search for the "Spring Break begins after last class." text
    for i in range(len(souplst)):
        if (souplst[i] == "Spring Break begins after last class."):
            prefriday = souplst[i - 1]
            break

    # store friday before spring break
    prefriday = [3, int(prefriday[-1])]

    # store dates for weekdays of spring break
    sbweek = []
    for i in range(3, 8):
        sbtempday = [3, prefriday[1] + i]
        sbweek.append(sbtempday)

    return sbweek

# returns the last day of classes
# works for fall and spring


def getlastday(souplst):
    # search for the "Classes end. Lottery for spring housing." text
    for i in range(len(souplst)):
        if (souplst[i] == "Classes end. Lottery for spring housing."):
            lastday = souplst[i - 1]
            lastday = [12, int(lastday[-2:])]
            break
        # search for the "Classes and seminars end." text
        elif (souplst[i] == "Classes and seminars end."):
            lastday = souplst[i - 1]
            lastday = [4, int(lastday[-2:])]
            break

    return lastday


# returns a list of every weekday in the semester
# works for both fall and spring
def constructmondays(souplst):
    firstmonday = getfirstweek(souplst)[0]
    lastday = getlastday(souplst)

    retlst = [firstmonday]

    nextmonday = dateadd(firstmonday, 7)
    while (comparedays(nextmonday, lastday)):
        retlst.append(nextmonday)
        nextmonday = dateadd(retlst[-1], 7)

    # remove days off for fall semester
    if (firstmonday[0] == 8):
        retlst.remove(getfallbreak(souplst)[0])  # fall break
    # remove days off for spring semester
    else:
        retlst.remove(getmlkjrday(souplst))  # MLK Jr. day
        retlst.remove(getspringbreak(souplst)[0])  # spring break

    return retlst


def constructtuesdays(souplst):
    firsttuesday = getfirstweek(souplst)[1]
    lastday = getlastday(souplst)

    retlst = [firsttuesday]

    nexttuesday = dateadd(firsttuesday, 7)
    while (comparedays(nexttuesday, lastday)):
        retlst.append(nexttuesday)
        nexttuesday = dateadd(retlst[-1], 7)

    # remove days off for fall semester
    if (firsttuesday[0] == 8) or (firsttuesday[0] == 9):
        retlst.remove(getfallbreak(souplst)[1])  # fall break
    # remove days off for spring semester
    else:
        retlst.remove(getspringbreak(souplst)[1])  # spring break

    return retlst


def constructwednesdays(souplst):
    firstwednesday = getfirstweek(souplst)[2]
    lastday = getlastday(souplst)

    retlst = [firstwednesday]

    nextwednesday = dateadd(firstwednesday, 7)
    while (comparedays(nextwednesday, lastday)):
        retlst.append(nextwednesday)
        nextwednesday = dateadd(retlst[-1], 7)

    # remove days off for fall semester
    if (firstwednesday[0] == 8) or (firstwednesday[0] == 9):
        retlst.remove(getfallbreak(souplst)[2])  # fall break
    # remove days off for spring semester
    else:
        retlst.remove(getspringbreak(souplst)[2])  # spring break

    return retlst


def constructthursdays(souplst):
    firstthursday = getfirstweek(souplst)[3]
    lastday = getlastday(souplst)

    retlst = [firstthursday]

    nextthursday = dateadd(firstthursday, 7)
    while (comparedays(nextthursday, lastday)):
        retlst.append(nextthursday)
        nextthursday = dateadd(retlst[-1], 7)

    # remove days off for fall semester
    if (firstthursday[0] == 8) or (firstthursday[0] == 9):
        retlst.remove(getfallbreak(souplst)[3])  # fall break
        retlst.remove(getthanksgivingbreak(souplst)[0])  # thanksgiving break
    # remove days off for spring semester
    else:
        retlst.remove(getspringbreak(souplst)[3])  # spring break

    return retlst


def constructfridays(souplst):
    firstfriday = getfirstweek(souplst)[4]
    lastday = getlastday(souplst)

    retlst = [firstfriday]

    nextfriday = dateadd(firstfriday, 7)
    while (comparedays(nextfriday, lastday)):
        retlst.append(nextfriday)
        nextfriday = dateadd(retlst[-1], 7)

    # remove days off for fall semester
    if (firstfriday[0] == 8) or (firstfriday[0] == 9):
        retlst.remove(getfallbreak(souplst)[4])  # fall break
        retlst.remove(getthanksgivingbreak(souplst)[1])  # thanksgiving break
    # remove days off for spring semester
    else:
        retlst.remove(getspringbreak(souplst)[4])  # spring break

    return retlst
