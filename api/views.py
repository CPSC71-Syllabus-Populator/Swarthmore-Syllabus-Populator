from flask import Blueprint, request
from werkzeug.utils import secure_filename
import pdfplumber
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

    content = ""
    with pdfplumber.open(rf"{destination}") as pdf:
        content = content.join([page.extract_text() for page in pdf.pages])

    return 'Parsed', 201


@main.route('/link_test', methods=['POST'])
def link_test():

    body = request.json['link']
    print(body)
    # # link = request.json
    # # print(link)
    # # my_json = request.get_json()
    # # link = my_json.get('link')
    print("Good function")

    return 'Linktest', 201
