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
  region_name=relay.get(D.aws.region),
  aws_session_token=session_token
)

route53 = sess.client('route53')

hostedZoneId = relay.get(D.hostedZoneId)
changeBatch = relay.get(D.changeBatch)

response = route53.change_resource_record_sets(HostedZoneId=hostedZoneId,ChangeBatch=changeBatch)

print('Record set response {}'.format(response))