from google.cloud import storage


def download_file_from_gcs(gcs_bucket_name, gcs_blob_object, local_model_path):
    # Initialise a client
    storage_client = storage.Client()
    # Create a bucket object for our bucket
    bucket = storage_client.get_bucket(gcs_bucket_name)
    # Create a blob object from the filepath
    blob = bucket.blob(gcs_blob_object)
    # Download the file to a destination
    blob.download_to_filename(local_model_path)