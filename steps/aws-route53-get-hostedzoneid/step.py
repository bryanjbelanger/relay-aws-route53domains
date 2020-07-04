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

dnsName = relay.get(D.dnsName)

host_zones_response = route53.list_hosted_zones_by_name(DNSName=dnsName)

hostedZoneId = host_zones_response['HostedZones'][0]['Id']

# hostedZoneIdSubstring = hostedZoneId.split('/')[2]

print('HostedZoneId: {}'.format(hostedZoneId))

relay.outputs.set('hostedZoneId', hostedZoneId)