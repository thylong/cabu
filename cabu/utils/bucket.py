# -*- coding: utf-8 -*-


from awsauth import S3Auth
import requests


class Bucket(object):
    """Convenient class to export datas to an Amazon S3 bucket.

    Args:
        bucket_name (str): The name of the bucket to export.
        access_key (str): The access_key of the owner of the bucket to export.
        secret_key (str): The secret_key of the owner of the bucket to export.
    """

    def __init__(self, bucket_name, access_key, secret_key):
        self.bucket = bucket_name
        self.access_key = access_key
        self.secret_key = secret_key

    def put(self, filename, data):
        """Put given datas in the file with the given filename in the S3 bucket.

        Args:
            filename (str): A string representing the name of the file to store.
            datas (str|object): The datas to export.
        Returns:
            response (object): The object returned by requests.
        """
        url = 'http://' + self.bucket + '.s3.amazonaws.com/' + filename
        return requests.put(url, data=data, auth=S3Auth(self.access_key, self.secret_key))

    def get(self, filename):
        """Get the file on the distant S3 bucket with the given filename.

        Args:
            filename (str): A string representing the name of the file to get.
        Returns:
            response (object): The object returned by requests.
        """
        url = 'http://' + self.bucket + '.s3.amazonaws.com/' + filename
        return requests.get(url, auth=S3Auth(self.access_key, self.secret_key))

    def delete(self, filename):
        """Delete the file on the distant S3 bucket with the given filename.

        Args:
            filename (str): A string representing the name of the file to delete.
        Returns:
            response (object): The object returned by requests.
        """
        url = 'http://' + self.bucket + '.s3.amazonaws.com/' + filename
        return requests.delete(url, auth=S3Auth(self.access_key, self.secret_key))
