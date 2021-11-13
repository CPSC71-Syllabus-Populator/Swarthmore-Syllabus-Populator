class Event:
    def __init__(self, location, time):
        self.time = time
        self.location = location

    def __str__(self):
        output = ""
        output += f"Location: {self.location}\n"
        output += f"Title: {self.title}\n"
        output += f"Time: {self.time}"
        output += f"Weekday: {self.weekday}"
        return output

    def set_title(self, title):
        self.title = title

    def set_weekday(self, weekday):
        self.weekday = weekday

    def set_id(self, id):
        self.id = id

    def serialize_to_JSON(self):
        return {'id': self.id, 'title': self.title, 'time': self.time,
                'weekday': self.weekday}
