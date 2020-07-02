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
policy = relay.get(D.policy)

try:
  response = s3.put_bucket_policy(Bucket=bucketName,Policy=policy)

  print ("Added policy for bucket {}".format(bucketName))
except Exception as e: 
  print (e)