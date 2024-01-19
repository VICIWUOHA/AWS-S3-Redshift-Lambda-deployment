### S3 File Uploader
This script allows uploading files from a local directory to an Amazon S3 bucket.

Requirements
Python 3
Boto3 library for interacting with AWS services
AWS credentials configured with access key, secret key and region
Usage
Install boto3 library

        pip install boto3
Create a .env file and add your AWS credentials:


        AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
        AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY  
        AWS_DEFAULT_REGION=YOUR_REGION
Run the upload script:

        python s3-loader.py
Specify the local directory and S3 bucket name:

        upload_to_s3("data", "my-bucket")

How it works
The script imports boto3 and loads AWS credentials from the .env file. It initializes an S3 client and checks if the target bucket exists, creating it if needed. Then it iterates through files in the local directory and uploads each one to S3 with a "datafiles/" prefix path.

If you need more extensibilty of this for your use case. We can connect on Linkedin [@viciwuoha](https://linkedin.com/in/viciwuoha)