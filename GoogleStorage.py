from google.cloud import storage
from google.cloud.exceptions import NotFound


def create_bucket(bucket_name, project):
    project = "michael-gilbert-dev"

    storage_client = storage.Client(project=project)
    storage_client.create_bucket(bucket_or_name=bucket_name)

    print(f"Created bucket {bucket_name}.")


def uploading_string(bucket_name, string, destination_blob_name):
    """Uploads a string to the bucket."""
    
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    
    data = string

    blob.upload_from_string(data, content_type='text/plain')

    print("Text uploaded to {}.".format(destination_blob_name))


def find_bucket(bucket_name):
    """Prints out a bucket's metadata."""

    storage_client = storage.Client()
    try:
        bucket = storage_client.get_bucket(bucket_name)
    except NotFound:
        print("Sorry, that bucket does not exist!")
        return None
    return bucket
