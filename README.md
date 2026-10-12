# AWS Static Website Hosting Using Python & boto3

A professional static website hosting project that demonstrates how to deploy a website to **Amazon S3** using **Python and the AWS SDK for Python (boto3)**.

The deployment process is automated using a Python script that configures the S3 bucket, enables static website hosting, applies the required bucket policy, detects file content types, and uploads the website files.

---

## Project Overview

**Project Name:** Automated Static Website Hosting Using AWS SDK

**Cloud Platform:** Amazon Web Services (AWS)

**AWS Service:** Amazon S3

**Programming Language:** Python

**AWS SDK:** boto3

**AWS Region:** `ap-south-1`

This project is part of an AWS Capstone project and demonstrates practical cloud automation using Python.

---

## Architecture

```text
Developer
    |
    | Website Files
    v
Python Deployment Script
        |
        | boto3
        v
   Amazon S3 Bucket
        |
        | Static Website Hosting
        v
    Web Browser
```

---

## Technologies Used

### Amazon S3

Amazon S3 is used to:

* Store the HTML and CSS files
* Host the static website
* Provide public access to website content
* Serve the website through an S3 endpoint

### Python

Python is used to automate the deployment process instead of manually configuring the S3 bucket through the AWS Management Console.

### boto3

`boto3` is the AWS SDK for Python.

It is used to communicate with Amazon S3 and perform operations such as:

* Checking the bucket
* Configuring public access
* Applying the bucket policy
* Enabling website hosting
* Uploading files

### HTML & CSS

HTML provides the website structure while CSS provides the visual design and responsive layout.

---

## Project Structure

```text
aws-static-website-sdk/
│
├── deploy.py
├── requirements.txt
├── README.md
│
└── website/
    ├── index.html
    └── style.css
```

---

## How the Deployment Works

The deployment is performed automatically using `deploy.py`.

### Step 1 — Check S3 Bucket

The script connects to Amazon S3 and verifies that the configured bucket exists and is accessible.

```python
s3.head_bucket(Bucket=BUCKET_NAME)
```

---

### Step 2 — Configure Public Access

The script configures the S3 public access settings required for public website content.

---

### Step 3 — Apply Bucket Policy

A bucket policy is applied to allow public read access to objects stored in the website bucket.

The policy allows:

```text
s3:GetObject
```

for objects inside the configured bucket.

---

### Step 4 — Enable Static Website Hosting

Amazon S3 static website hosting is enabled with:

```text
index.html
```

as the default index document.

---

### Step 5 — Upload Website Files

The Python script scans the `website` directory and uploads the files to S3.

The script automatically detects the appropriate MIME type.

For example:

```text
index.html → text/html
style.css  → text/css
```

This ensures that the browser correctly interprets the uploaded files.

---

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

Navigate into the project:

```bash
cd aws-static-website-sdk
```

---

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## AWS Configuration

Before running the deployment script, configure AWS CLI credentials.

```bash
aws configure
```

Provide:

```text
AWS Access Key ID
AWS Secret Access Key
Default region name: ap-south-1
Default output format: json
```

The AWS credentials should never be stored inside the source code.

---

## Deploy the Website

Run:

```bash
python deploy.py
```

The script will:

```text
1. Check the S3 bucket
2. Configure public access
3. Apply the bucket policy
4. Enable static website hosting
5. Upload website files
6. Display deployment information
```

Example output:

```text
============================================================
AWS STATIC WEBSITE DEPLOYMENT
============================================================

Region      : ap-south-1
Bucket Name : aws-static-website-e1d75f1a66

[1/5] Checking S3 bucket...
Bucket exists and is accessible.

[2/5] Configuring bucket access...
Public access block configured.

[3/5] Applying bucket policy...
Bucket policy applied successfully.

[4/5] Enabling static website hosting...
Static website hosting enabled.

[5/5] Uploading website files...
Uploading: index.html
Content-Type: text/html
Uploading: style.css
Content-Type: text/css

Successfully uploaded 2 file(s).

============================================================
DEPLOYMENT SUCCESSFUL
============================================================
```

---

## Website

The deployed website is hosted on Amazon S3.

Example S3 object endpoint:

```text
https://aws-static-website-e1d75f1a66.s3.ap-south-1.amazonaws.com/index.html
```

Replace the bucket name with your own bucket if you deploy the project again.

---

## AWS Services Used

| Service                   | Purpose                        |
| ------------------------- | ------------------------------ |
| Amazon S3                 | Website storage and hosting    |
| AWS IAM                   | Authentication and permissions |
| AWS SDK for Python        | Programmatic AWS access        |
| Amazon S3 Website Hosting | Static website delivery        |

---

## Security Considerations

AWS credentials must **never** be committed to GitHub.

Do not upload files containing:

```text
AWS Access Key
AWS Secret Access Key
Passwords
API Keys
Tokens
.env files
```

Use AWS CLI configuration, IAM roles, environment variables, or another secure credential mechanism instead.

---

## Project Features

* Automated S3 deployment
* Python-based AWS automation
* boto3 integration
* Automatic MIME type detection
* S3 static website hosting
* Responsive HTML/CSS frontend
* Public website deployment
* Deployment status output
* Reusable deployment script

---

## Learning Outcomes

This project demonstrates practical knowledge of:

* Amazon S3
* Static website hosting
* AWS IAM permissions
* Python automation
* boto3
* AWS CLI
* Cloud deployment
* MIME types
* Infrastructure configuration through code

---

## Future Improvements

Possible improvements include:

* Amazon CloudFront for HTTPS and global content delivery
* Route 53 custom domain
* AWS Certificate Manager SSL certificate
* GitHub Actions CI/CD
* CloudFront caching
* S3 versioning
* CloudWatch monitoring
* Infrastructure as Code using Terraform or AWS CloudFormation

---

## Author

**AWS Capstone Project**

Built using:

```text
Amazon S3
Python
boto3
HTML
CSS
```

---

## License

This project is created for educational and AWS Capstone project purposes.
