import json
import boto3
import pandas as pd
from io import StringIO


def lambda_handler(event, context):
    # Retrieve the bucket name and object key from the S3 event
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    file_key = event["Records"][0]["s3"]["object"]["key"]

    # Create an S3 client
    s3_client = boto3.client("s3")

    # Read the CSV file from S3 into a DataFrame using pandas
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        csv_content = response["Body"].read().decode("utf-8")
        df = pd.read_csv(StringIO(csv_content))
    except Exception as e:
        raise e

    # Check the length of the DataFrame and print it
    df_length = len(df)
    print(f"Length of the DataFrame: {df_length}")

    return {
        "statusCode": 200,
        "body": json.dumps(
            f"Processed `{file_key}` with DataFrame length: `{df_length}`"
        ),
    }
