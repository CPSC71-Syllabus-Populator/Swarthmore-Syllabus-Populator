from flask import Blueprint, request, session
from werkzeug.utils import secure_filename
from api.parsing import *
import os

UPLOAD_FOLDER = "./".join(["./uploads"])

main = Blueprint('main', __name__)


@main.route('/parse_pdf', methods=['POST'])
def parse_pdf():
    # if not os.path.isdir(UPLOAD_FOLDER):
    #     os.mkdir(UPLOAD_FOLDER)

    # file = request.files['file']
    # fileName = secure_filename(file.filename)
    # destination = "/".join([UPLOAD_FOLDER, fileName])
    # file.save(destination)

    return 'Parsed', 201


@main.route('/parse_text', methods=['POST', 'GET'])
def parse_text():
    text = request.form['text']
    session['content'] = text
    # print(text)  # remove this

    parse_text_for_events(text)

    return text, 201


@main.route('/get_events', methods=['GET'])
def get_events():
    if request.method == 'GET':
        return session['content'], 201

    return 'Invalid request', 401


@main.route('/send_link', methods=['POST'])
def send_link():
    link = request.form['link']
    print(link)

    return 'Link received', 201
