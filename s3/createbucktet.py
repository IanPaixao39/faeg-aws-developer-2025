import boto3
# cliente em low level
s3api = boto3.client("s3", region_name="us-east-1")
bucket_name = "ianpaixao2002"

s3api.create_bucket(Bucket = bucket_name)
print("bucket criado com sucesso...")
