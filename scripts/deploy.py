import argparse
import logging

import boto3
from botocore.exceptions import ClientError

LOGGER = logging.getLogger('trellis')


class Uploader:

    def __init__(self, bucket, profile="default"):
        self.s3 = boto3.Session(profile_name=profile).client('s3')
        self.bucket = bucket

    def upload(self, path, mime_type):
        LOGGER.info("Uploading {} as {}".format(path, mime_type))
        try:
            with open(path, 'rb') as fp:
                self.s3.upload_fileobj(fp, self.bucket, path, ExtraArgs={
                    'ContentType': mime_type})
        except ClientError as e:
            LOGGER.warn("Error writing {}: {}".format(path, e))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            description="Upload ontology files to S3")
    parser.add_argument("--bucket", required=True, help="The bucket name")
    parser.add_argument("--profile", default="default",
                        help="The credentials profile")

    args = parser.parse_args()

    LOGGER.setLevel(logging.INFO)
    LOGGER.addHandler(logging.StreamHandler())

    uploader = Uploader(bucket=args.bucket, profile=args.profile)

    uploader.upload("index.html", "text/html")
    uploader.upload("download.html", "text/html")
    uploader.upload("css/trellis.css", "text/css")
    uploader.upload("img/trellis.png", "image/png")
    uploader.upload("img/trellis_white.png", "image/png")
