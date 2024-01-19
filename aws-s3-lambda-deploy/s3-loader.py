# use this script to upload data to s3
import os
import boto3
from dotenv import load_dotenv

# get access credentials from env
load_dotenv(override=True)

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")


# Connect to S3 and initialize
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
    region_name=AWS_DEFAULT_REGION,
)
print("==> Successfully Connected To AWS S3 Environment.")


def _check_and_create_bucket(bucket_name):
    # Check if the bucket exists
    bucket_exists = False
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        bucket_exists = True
        print(f"==> Bucket {bucket_name} already exists.. proceeding to upload.")
    except:
        print(f"==> Bucket {bucket_name} does not exist.. proceeding to create.")
        pass

    # Create bucket if it doesn't exist
    if not bucket_exists:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"==> Created bucket: {bucket_name}")
        bucket_exists = True

    return bucket_exists


def upload_to_s3(directory_path, bucket_name):
    # Check if the bucket exists
    bucket_exists = _check_and_create_bucket(bucket_name)

    if not bucket_exists:
        print(
            f"**** Bucket {bucket_name} does not exist. Please create the bucket manually first."
        )
        return

    # Iterate through each file in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if the file is a regular file
        if os.path.isfile(file_path):
            s3_key = "datafiles/"
            # Upload file to S3
            s3_client.upload_file(file_path, bucket_name, s3_key + filename)
            print(
                f"==> Uploaded {filename} to {'s3://'+bucket_name+'/'+s3_key+filename}"
            )


if __name__ == "__main__":
    upload_to_s3("data", "demo-lambda-bucket-vic")
