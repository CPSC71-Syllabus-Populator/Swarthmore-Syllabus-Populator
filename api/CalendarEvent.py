class CalendarEvent():
    def __init__(self, parsedEvent, start_time, end_time):
        self.summary = parsedEvent["summary"]
        self.location = 'SCI 199'
        self.description = ""
        self.start = {'dateTime': start_time, "timeZone": "America/New_York"}
        self.end = {'dateTime': end_time, "timeZone": "America/New_York"}
        self.recurrence = []
        self.reminders = {}

    def __str__(self):
        output = ""
        output += f"start: {self.start['dateTime']}"
        return output
