import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
#data = open('test.txt', 'rb')
#s3.Bucket('sravantest123').put_object(Key='test.txt', Body=data)
