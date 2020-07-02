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

bucketName = relay.get(D.bucketName)
targetBucket = relay.get(D.targetBucket)
targetPrefix = relay.get(D.targetPrefix)

get_response = s3.get_bucket_logging(Bucket=bucketName)

print ("Bucket get info 1 {}".format(get_response))

try:
  bucketLoggingStatus = {
    'LoggingEnabled': {
      'TargetBucket': targetBucket,
      'TargetPrefix': targetPrefix,
    }
  }

  response = s3.put_bucket_logging(Bucket=bucketName,BucketLoggingStatus=bucketLoggingStatus)

  print ("Connect log bucket for {}".format(bucketName))

  get_response = s3.get_bucket_logging(Bucket=bucketName)

  print ("Bucket get info 2 {}".format(get_response))
except Exception as e: 
  print (e)