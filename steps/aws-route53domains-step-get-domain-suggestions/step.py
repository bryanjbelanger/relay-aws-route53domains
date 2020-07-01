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

domainName = relay.get(D.domainName)

domain_suggestions_dict = route53domains.get_domain_suggestions(DomainName=domainName,SuggestionCount=10,OnlyAvailable=True)

domain_suggestions_list = domain_suggestions_dict['SuggestionsList']

print("Domain suggestions:\n")

for suggestion in domain_suggestions_list:
  print(suggestion['DomainName'])

# relay.outputs.set('availability', availability)