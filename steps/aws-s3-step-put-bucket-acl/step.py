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

currentACL = s3.get_bucket_acl(Bucket=bucketName)

print ("Current ACL {}".format(currentACL))

acl = relay.get(D.acl)
grantFullControl = relay.get(D.grantFullControl)
grantRead = relay.get(D.grantRead)
grantReadACP = relay.get(D.grantReadACP)
grantWrite = relay.get(D.grantWrite)
grantWriteACP = relay.get(D.grantWriteACP)

# accessControlPolicyGrants = (D.accessControlPolicyGrants + relay.get(D.accessControlPolicyGrants)).uniq  { |h| h[:key] } if D.accessControlPolicyGrants else currentACL['AccessControlPolicyGrants']['Grants']
accessControlPolicyOwner = relay.get(D.accessControlPolicyOwner) if relay.get(D.accessControlPolicyOwner) else currentACL['Owner']

print ("New owner {}".format(accessControlPolicyOwner))

if D.accessControlPolicyGrants:

  print ("New grants {}".format(relay.get(D.accessControlPolicyGrants)))
  grantSet = relay.get(D.accessControlPolicyGrants)

  for newGrant in currentACL['Grants']:
    grantSet.append(newGrant)

  accessControlPolicyGrants = grantSet
else:
  accessControlPolicyGrants = currentACL['Grants']

try:
  print ("Full grants {}".format(accessControlPolicyGrants))
  print ("Full owner {}".format(accessControlPolicyOwner))

  response = s3.put_bucket_acl(
    ACL=acl,
    AccessControlPolicy={
      'Grants': accessControlPolicyGrants,
      'Owner': accessControlPolicyOwner
    },
    Bucket=bucketName,
    GrantFullControl=grantFullControl,
    GrantRead=grantRead,
    GrantReadACP=grantReadACP,
    GrantWrite=grantWrite,
    GrantWriteACP=grantWriteACP
  )

  print ("Connect log bucket for {}".format(bucketName))
except Exception as e: 
  print (e)