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
durationInYears = int(relay.get(D.durationInYears))
autoRenew = bool(relay.get(D.autoRenew))

firstName = relay.get(D.firstName)
lastName = relay.get(D.lastName)
contactType = relay.get(D.contactType)
organizationName = relay.get(D.organizationName)
addressLine1 = relay.get(D.addressLine1)
addressLine2 = relay.get(D.addressLine2)
city = relay.get(D.city)
state = relay.get(D.state)
countryCode = relay.get(D.countryCode)
zipCode = relay.get(D.zipCode)
phoneNumber = relay.get(D.phoneNumber)
email = relay.get(D.email)
fax = relay.get(D.fax)

contact = {
  "FirstName": firstName,
  "LastName": lastName,
  "ContactType": contactType,
  "OrganizationName": organizationName,
  "AddressLine1": addressLine1,
  "AddressLine2": addressLine2,
  "City": city,
  "State": state,
  "CountryCode": countryCode,
  "ZipCode": zipCode,
  "PhoneNumber": phoneNumber,
  "Email": email,
  "Fax": fax
}

filtered = {k: v for k, v in contact.items() if v is not None}
contact.clear()
contact.update(filtered)

register_domain_dict = route53domains.register_domain(
    DomainName=domainName,
    DurationInYears=durationInYears,
    AutoRenew=autoRenew,
    AdminContact=contact,
    RegistrantContact=contact,
    TechContact=contact
  )



operationId = register_domain_dict['OperationId']

print('Operation ID {}'.format(operationId))

relay.outputs.set('operationId', operationId)