import os

import utils
from flask import Flask

app = Flask(__name__)
app.config['S3_BUCKET'] = "ezai"
app.config['S3_KEY'] = os.environ["S3_KEY"]
app.config['S3_SECRET'] = os.environ["S3_SECRET"]

@app.route("/")
def welcome():
    return "<p>Welcome to EZ AI!</p>"

@app.route("/upload")
def upload():
    source_path = "tmp/dummy.keras"
    s3_destination_path = "models/01/dummy.keras"
    return utils.upload_to_s3(app, source_path, s3_destination_path)

@app.route("/get_image")
def get_image():
    s3_source_path = "datasets/test/daisy/10172379554_b296050f82_n.jpg"
    img = utils.fetch_image(app, s3_source_path)
    return "<p>Success!</p>"

@app.route("/list")
def list_out():
    res = utils.list_files_in_dataset(app, "test")
    return '\n'.join(res)
