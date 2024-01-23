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

@app.route("/get_images")
def get_image():
    images, labels = utils.get_images_and_labels_from_s3(app, 1)
    print(len(images))
    print(len(labels))

    print(images[0])
    print(labels[0])

    return "<p>Success!</p>"