import boto3
s3api= boto3.client("s3",region_name="us-east-1")
bucket_name = "ianpaixao2002"

file_name = "./s3/index.html"
object_name = "index.html"

s3api.upload_file(file_name, bucket_name, object_name)
print("arquivo enviado com sucesso para o s3")