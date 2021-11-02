from google.cloud import storage
from google.cloud.exceptions import NotFound


def create_bucket(bucket_name, project):
    storage_client = storage.Client(project=project)
    storage_client.create_bucket(bucket_or_name=bucket_name)

    print(f"Created bucket {bucket_name}.")


def delete_bucket(bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete()

    print(f"Deleted bucket {bucket_name}.")


def upload_file(bucket_name, source_file_name, destination_blob_name, project):
    storage_client = storage.Client(project=project)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"Uploaded file {source_file_name} to gs://{bucket_name}/{destination_blob_name}.")


def download_file(bucket_name, source_blob_name, destination_file_name, project):
    storage_client = storage.Client(project=project)
    bucket = storage_client.bucket(bucket_name)
    file = bucket.blob(source_blob_name)
    file.download_to_filename(destination_file_name)

    print(f"Downloaded file {source_blob_name} from bucket {bucket_name} to {destination_file_name}.")


def copy_file(bucket_name, file_name, destination_bucket_name, destination_file_name):
    storage_client = storage.Client()

    source_bucket = storage_client.bucket(bucket_name)
    source_file = source_bucket.blob(file_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    file_copy = source_bucket.copy_blob(
        source_file, destination_bucket, destination_file_name
    )

    print(f"Copied file {file_name} from {bucket_name} to {destination_file_name} in {destination_bucket_name}.")


def find_bucket(bucket_name):
    """Prints out a bucket's metadata."""

    storage_client = storage.Client()
    try:
        bucket = storage_client.get_bucket(bucket_name)
    except NotFound:
        print("Sorry, that bucket does not exist!")
        return None
    return bucket


def file_exists(bucket_name, file_name):
    """Lists all the blobs in the bucket."""

    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)

    # If there is a file in the list of files that matches the file_name we passed in, we have found the file.
    for blob in blobs:
        if blob.name == file_name:
            return True

    # File not found.
    return False


def delete_file(bucket_name, file_name):
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    file_name = bucket.blob(file_name)
    file_name.delete()


def list_buckets():
    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    return buckets

