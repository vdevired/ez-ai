import boto3

def upload_to_s3(app, source_path, s3_destination_path):
    """
    app: The flask app, has s3 config store in app.config
    source_path: relative to py file
    s3_destination_path: absolute path in s3 bucket
    """
    s3_client = boto3.client('s3', aws_access_key_id=app.config['S3_KEY'],
                             aws_secret_access_key=app.config['S3_SECRET'])

    try:
        with open(source_path, 'rb') as f:
            s3_client.upload_fileobj(f, app.config['S3_BUCKET'], s3_destination_path)
        return "Upload Succeeded"
    except (ClientError, FileNotFoundError) as e:
        print(e)
        return "Upload Failed"