import boto3
import mimetypes
import os
import json
from botocore.exceptions import ClientError


# ============================================================
# CONFIGURATION
# ============================================================

REGION = "ap-south-1"

# Existing bucket created during the previous run
BUCKET_NAME = "aws-static-website-e1d75f1a66"

# Website files are stored in this folder
WEBSITE_DIR = "website"


# ============================================================
# AWS CONNECTION
# ============================================================

s3 = boto3.client(
    "s3",
    region_name=REGION
)


# ============================================================
# START
# ============================================================

print("=" * 60)
print("AWS STATIC WEBSITE DEPLOYMENT")
print("=" * 60)

print(f"Region      : {REGION}")
print(f"Bucket Name : {BUCKET_NAME}")
print()


# ============================================================
# 1. CHECK BUCKET
# ============================================================

print("[1/5] Checking S3 bucket...")

try:
    s3.head_bucket(
        Bucket=BUCKET_NAME
    )

    print("Bucket exists and is accessible.")

except ClientError as e:
    print("ERROR: Unable to access the S3 bucket.")
    print(e)
    raise


# ============================================================
# 2. CONFIGURE PUBLIC ACCESS
# ============================================================

print("\n[2/5] Configuring bucket access...")

try:
    s3.put_public_access_block(
        Bucket=BUCKET_NAME,
        PublicAccessBlockConfiguration={
            "BlockPublicAcls": False,
            "IgnorePublicAcls": False,
            "BlockPublicPolicy": False,
            "RestrictPublicBuckets": False
        }
    )

    print("Public access block configured.")

except ClientError as e:
    print("ERROR: Could not configure public access.")
    print(e)
    raise


# ============================================================
# 3. APPLY BUCKET POLICY
# ============================================================

print("\n[3/5] Applying bucket policy...")

bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{BUCKET_NAME}/*"
        }
    ]
}

# Convert Python dictionary to valid JSON
bucket_policy_json = json.dumps(bucket_policy)

try:
    s3.put_bucket_policy(
        Bucket=BUCKET_NAME,
        Policy=bucket_policy_json
    )

    print("Bucket policy applied successfully.")

except ClientError as e:
    print("ERROR: Could not apply bucket policy.")
    print(e)
    raise


# ============================================================
# 4. ENABLE STATIC WEBSITE HOSTING
# ============================================================

print("\n[4/5] Enabling static website hosting...")

try:
    s3.put_bucket_website(
        Bucket=BUCKET_NAME,
        WebsiteConfiguration={
            "IndexDocument": {
                "Suffix": "index.html"
            }
        }
    )

    print("Static website hosting enabled.")

except ClientError as e:
    print("ERROR: Could not enable static website hosting.")
    print(e)
    raise


# ============================================================
# 5. UPLOAD WEBSITE FILES
# ============================================================

print("\n[5/5] Uploading website files...")

# Check website folder
if not os.path.exists(WEBSITE_DIR):
    print(f"ERROR: Website folder '{WEBSITE_DIR}' was not found.")
    raise SystemExit(1)


uploaded_files = 0

for root, directories, files in os.walk(WEBSITE_DIR):

    for filename in files:

        # Full local file path
        local_path = os.path.join(
            root,
            filename
        )

        # Path relative to website folder
        relative_path = os.path.relpath(
            local_path,
            WEBSITE_DIR
        )

        # Convert Windows \ to S3 /
        s3_key = relative_path.replace("\\", "/")

        # Detect Content-Type
        content_type, _ = mimetypes.guess_type(
            local_path
        )

        if content_type is None:
            content_type = "application/octet-stream"

        print(f"Uploading: {s3_key}")
        print(f"Content-Type: {content_type}")

        try:

            s3.upload_file(
                local_path,
                BUCKET_NAME,
                s3_key,
                ExtraArgs={
                    "ContentType": content_type
                }
            )

            uploaded_files += 1

        except ClientError as e:
            print(f"ERROR uploading {s3_key}")
            print(e)
            raise


print()
print(f"Successfully uploaded {uploaded_files} file(s).")


# ============================================================
# WEBSITE URL
# ============================================================

website_url = (
    f"http://{BUCKET_NAME}.s3-website-{REGION}.amazonaws.com"
)


# ============================================================
# DEPLOYMENT COMPLETE
# ============================================================

print()
print("=" * 60)
print("DEPLOYMENT SUCCESSFUL")
print("=" * 60)

print(f"Bucket : {BUCKET_NAME}")
print(f"Region : {REGION}")
print(f"Files  : {uploaded_files}")
print()
print("Website URL:")
print(website_url)

print("=" * 60)