from flask import Blueprint, request, session
from werkzeug.utils import secure_filename
from api.parsing import parse_syllabi_events
from api.create_gcal_events import verify_google_credentials
from api.utils import build_google_calendar_events_JSON, get_semester_dates, get_syllabi_text
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
    file_name = secure_filename(file.filename)
    destination = "/".join([UPLOAD_FOLDER, file_name])
    file.save(destination)

    syllabi_text = get_syllabi_text(file)
    parsed_events = parse_syllabi_events(syllabi_text)
    session['parsed_events'] = parsed_events

    return 'Successfully parsed PDF', 201


@main.route('/parse_text', methods=['POST', 'GET'])
def parse_text():
    syllabi_text = request.form['text']
    parsed_events = parse_syllabi_events(syllabi_text)
    session['parsed_events'] = parsed_events

    return "Successfully parsed text", 201


@main.route('/get_events', methods=['GET'])
def get_events():
    return {'parsed_events': session['parsed_events']}, 201


@main.route('/post_events_to_calendar', methods=['POST'])
def post_events_to_calendar():
    selected_events = json.loads(request.form['selected_events'])

    all_dates = get_semester_dates()
    events_to_publish = build_google_calendar_events_JSON(
        selected_events, all_dates)

    gcal_service = verify_google_credentials(SCOPES)

    for event in events_to_publish:
        gcal_service.events().insert(
            calendarId='primary', body=event).execute()

    return "Successfully added to calendar", 201
