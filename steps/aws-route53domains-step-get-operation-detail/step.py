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

route53domains = sess.client('route53domains')

operationId = relay.get(D.operationId)

operation_detail_dict = route53domains.get_operation_detail(OperationId=operationId)

operation_detail_status = operation_detail_dict['Status']

print('Domain status: {}'.format(operation_detail_status))

relay.outputs.set('operation_detail_status', operation_detail_status)