#!/usr/bin/env python
import boto3
from nebula_sdk import Interface, Dynamic as D

relay = Interface()

session_token = None
try:
  session_token = relay.get(D.aws.connection.sessionToken)
except:
  pass

sess = boto3.Session(
  aws_access_key_id=relay.get(D.aws.connection.accessKeyID),
  aws_secret_access_key=relay.get(D.aws.connection.secretAccessKey),
  aws_session_token=session_token
)

s3 = sess.client('s3')

# region = relay.get(D.aws.region)
bucketName = relay.get(D.bucketName)

redirectAllRequestsToHostName = relay.get(D.redirectAllRequestsToHostName)

print ("Redirect all requests value {}".format(redirectAllRequestsToHostName))

if redirectAllRequestsToHostName:
  try:
    # bucket_website = s3.BucketWebsite(bucketName)
    websiteConfiguration = {
      'RedirectAllRequestsTo' : { 'HostName': redirectAllRequestsToHostName}
    }

    response = s3.put_bucket_website(Bucket=bucketName,WebsiteConfiguration=websiteConfiguration)

    print ("Created redirect bucket website {} to {}".format(bucketName, redirectAllRequestsToHostName))
  except Exception as e: 
    print (e)
else:
  try:
    # bucket_website = s3.BucketWebsite(bucketName)
    websiteConfiguration = {
      'ErrorDocument' : { 'Key': 'error.html'},
      'IndexDocument' : { 'Suffix': 'index.html'}
    }

    response = s3.put_bucket_website(Bucket=bucketName,WebsiteConfiguration=websiteConfiguration)

    print ("Created bucket website {}".format(bucketName))
  except Exception as e: 
    print (e)
