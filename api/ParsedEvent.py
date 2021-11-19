class ParsedEvent:
    def __init__(self, id, pdf_location, start_time, end_time):
        self.id = id
        self.pdf_location = pdf_location
        self.start_time = start_time
        self.end_time = end_time
        self.checked = True
        self.parsed_weekday = None
        self.summary = None

    def __str__(self):
        output = ""
        output += f"Summary: {self.summary}\n"
        output += f"Location: {self.location}\n"
        output += f"Description: {self.description}"
        output += f"Parsed Time: {self.parsed_time}"
        output += f"Parsed Weekday: {self.parsed_weekday}"
        return output

    def set_weekday(self, parsed_weekday):
        self.parsed_weekday = parsed_weekday

    def set_summary(self, summary):
        self.summary = summary
