from flask import Blueprint, request, session
from werkzeug.utils import secure_filename
from api.parsing import parse_text_for_events
from api.create_gcal_events import verify_google_credentials
from api.utils import build_google_calendar_events_JSON, extract_syllabi_text, serialize_parsed_events_to_JSON
import json
import os

UPLOAD_FOLDER = "./".join(["./uploads"])
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

main = Blueprint('main', __name__)


@main.route('/parse_pdf', methods=['POST'])
def parse_pdf():
    if not os.path.isdir(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)

    file = request.files['file']
    fileName = secure_filename(file.filename)
    destination = "/".join([UPLOAD_FOLDER, fileName])
    file.save(destination)

    syllabi_text = extract_syllabi_text(file)
    parsed_events = parse_text_for_events(syllabi_text)
    json_data = serialize_parsed_events_to_JSON(parsed_events)
    session['json_data'] = json_data

    return 'Successfully parsed PDF', 201


@main.route('/parse_text', methods=['POST', 'GET'])
def parse_text():
    syllabi_text = request.form['text']
    parsed_events = parse_text_for_events(syllabi_text)
    json_data = serialize_parsed_events_to_JSON(parsed_events)
    session['json_data'] = json_data

    return "Successfully parsed text", 201


@main.route('/get_events', methods=['GET'])
def get_events():
    for i in range(1000):
        for j in range(100000):
            ...
    return session['json_data'], 201


@main.route('/post_events_to_calendar', methods=['POST'])
def post_events_to_calendar():
    events = request.form["json_events"]
    json_events = json.loads(events)

    json_data = build_google_calendar_events_JSON(json_events)

    gcal_service = verify_google_credentials(SCOPES)

    print(json_data[0])

    for json_event in json_data:
        event = gcal_service.events().insert(
            calendarId='primary', body=json_event).execute()

    return "posted", 201
