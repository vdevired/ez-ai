import boto3
import io
import numpy as np
import numpy.typing as npt
from flask import Flask
from keras.preprocessing.image import img_to_array, load_img
from typing import List

RESIZE_IMAGE_HEIGHT = 300
RESIZE_IMAGE_WIDTH = 300


def upload_to_s3(app: Flask, source_path: str, s3_destination_path: str):
    """
    app: The flask app, has s3 config store in app.config
    source_path: relative to py file
    s3_destination_path: absolute path in s3 bucket
    """
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=app.config["S3_KEY"],
        aws_secret_access_key=app.config["S3_SECRET"],
    )

    try:
        with open(source_path, "rb") as f:
            s3_client.upload_fileobj(f, app.config["S3_BUCKET"], s3_destination_path)
        return "Upload Succeeded"
    except (ClientError, FileNotFoundError) as e:
        print(e)
        return "Upload Failed"


def list_files_in_dataset(app: Flask, dataset_id: int) -> List[str]:
    """
    app: The flask app, has s3 config store in app.config
    source_path: relative to py file
    dataset_id: The ID of the dataset

    returns list of strings of format 'label/filename'
    """
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=app.config["S3_KEY"],
        aws_secret_access_key=app.config["S3_SECRET"],
    )
    res = []

    prefix = f"datasets/{dataset_id}/"
    paginator = s3_client.get_paginator("list_objects")
    operation_parameters = {"Bucket": app.config["S3_BUCKET"], "Prefix": prefix}
    page_iterator = paginator.paginate(**operation_parameters)
    for page in page_iterator:
        for entry in page["Contents"]:
            res.append(entry["Key"].replace(prefix, ""))

    return res


def fetch_image(app: Flask, s3_source_path: str) -> npt.NDArray[np.float64]:
    """
    app: The flask app, has s3 config store in app.config
    source_path: relative to py file
    s3_source_path: The path of the image in s3
    """
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=app.config["S3_KEY"],
        aws_secret_access_key=app.config["S3_SECRET"],
    )

    response = s3_client.get_object(Bucket=app.config["S3_BUCKET"], Key=s3_source_path)
    img = load_img(
        io.BytesIO(response["Body"].read()),
        target_size=(RESIZE_IMAGE_HEIGHT, RESIZE_IMAGE_WIDTH),
    )
    # img.show()
    input_arr = img_to_array(img)
    return input_arr
