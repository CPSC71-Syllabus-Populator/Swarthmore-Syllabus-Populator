from flask import Blueprint, request, session
from werkzeug.utils import secure_filename
from api.parsing import *
import os

UPLOAD_FOLDER = "./".join(["./uploads"])

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
    json_data = parse_text_for_events(syllabi_text)
    session['json_data'] = json_data

    return 'Successfully parsed PDF', 201


@main.route('/parse_text', methods=['POST', 'GET'])
def parse_text():
    syllabi_text = request.form['text']
    json_data = parse_text_for_events(syllabi_text)
    session['json_data'] = json_data

    return "Successfully parsed text", 201


@main.route('/get_events', methods=['GET'])
def get_events():
    return session['json_data'], 201


@main.route('/post_events_to_calendar', methods=['POST'])
def post_events_to_calendar():
    events = request.form["json_events"]

    return "posted", 201
