import argparse
import logging
import os

import boto3
from botocore.exceptions import ClientError

LOGGER = logging.getLogger('trellis')


class Uploader:

    def __init__(self, bucket, site, profile="default"):
        self.s3 = boto3.Session(profile_name=profile).client('s3')
        self.bucket = bucket
        self.site = site

    def upload(self, path, mime_type):
        LOGGER.info("Uploading {} as {}".format(path, mime_type))
        try:
            with open(os.path.join(self.site, path), 'rb') as fp:
                self.s3.upload_fileobj(fp, self.bucket, path, ExtraArgs={
                    'ContentType': mime_type})
        except ClientError as e:
            LOGGER.warn("Error writing {}: {}".format(path, e))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            description="Upload ontology files to S3")
    parser.add_argument("--site", default="_site", help="The site data")
    parser.add_argument("--bucket", required=True, help="The bucket name")
    parser.add_argument("--profile", default="default",
                        help="The credentials profile")

    args = parser.parse_args()

    LOGGER.setLevel(logging.INFO)
    LOGGER.addHandler(logging.StreamHandler())

    uploader = Uploader(bucket=args.bucket, site=args.site,
                        profile=args.profile)

    uploader.upload("index.html", "text/html; charset=utf-8")
    uploader.upload("about.html", "text/html; charset=utf-8")
    uploader.upload("download.html", "text/html; charset=utf-8")
    uploader.upload("404.html", "text/html; charset=utf-8")
    uploader.upload("feed.xml", "application/xml")

    uploader.upload("assets/main.css", "text/css")
    uploader.upload("assets/all.css", "text/css")
    uploader.upload("assets/minima-social-icons.svg", "image/svg+xml")
    uploader.upload("assets/trellis.css", "text/css")
    uploader.upload("assets/trellis.png", "image/png")
    uploader.upload("doap.ttl", "text/turtle; charset=utf-8")
    uploader.upload("webfonts/fa-brands-400.eot",
                    "application/vnd.ms-fontobject")
    uploader.upload("webfonts/fa-brands-400.svg", "application/svg+xml")
    uploader.upload("webfonts/fa-brands-400.ttf", "application/x-font-ttf")
    uploader.upload("webfonts/fa-brands-400.woff", "application/font-woff")
    uploader.upload("webfonts/fa-brands-400.woff2", "application/font-woff2")
    uploader.upload("webfonts/fa-regular-400.eot",
                    "application/vnd.ms-fontobject")
    uploader.upload("webfonts/fa-regular-400.svg", "application/svg+xml")
    uploader.upload("webfonts/fa-regular-400.ttf", "application/x-font-ttf")
    uploader.upload("webfonts/fa-regular-400.woff", "application/font-woff")
    uploader.upload("webfonts/fa-regular-400.woff2", "application/font-woff2")
    uploader.upload("webfonts/fa-solid-900.eot",
                    "application/vnd.ms-fontobject")
    uploader.upload("webfonts/fa-solid-900.svg", "application/svg+xml")
    uploader.upload("webfonts/fa-solid-900.ttf", "application/x-font-ttf")
    uploader.upload("webfonts/fa-solid-900.woff", "application/font-woff")
    uploader.upload("webfonts/fa-solid-900.woff2", "application/font-woff2")
