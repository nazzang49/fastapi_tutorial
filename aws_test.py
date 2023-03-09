import boto3

# print(boto3.resource("s3").Bucket("jyp-test").objects.all())

client = boto3.client("s3")

# response = client.get_object(
#     Bucket='jyp-test',
#     Key='test.txt',
# )

response = client.list_objects(
    Bucket='jyp-tutorial',
    # MaxKeys='2',
)

print(response)