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

try:
  response = s3.delete_public_access_block(Bucket=bucketName)

  print ("Dropped public block from bucket website {}".format(bucketName))
except Exception as e: 
  print (e)