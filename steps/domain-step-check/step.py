#!/usr/bin/env python
import re

from nebula_sdk import Interface, Dynamic as D

relay = Interface()

session_token = None
try:
  session_token = relay.get(D.aws.connection.sessionToken)
except:
  pass

domainName = relay.get(D.domainName)
if domainName and re.fullmatch("^((?!-)[A-Z0-9-]{1, 63}(?<!-)\\.)+[A-Z]{2, 6}$", domainName, re.IGNORECASE) is None:
    raise Exception("Invalid domainName")

durationInYears = relay.get(D.durationInYears)
if durationInYears and re.fullmatch("\\d+", durationInYears) is None:
    raise Exception("Invalid durationInYears")

autoRenew = relay.get(D.autoRenew)
if autoRenew and re.fullmatch("(True|False)", autoRenew) is None:
    raise Exception("Invalid autoRenew")

firstName = relay.get(D.firstName)
if firstName and re.fullmatch("\\w+", firstName) is None:
    raise Exception("Invalid firstName")

lastName = relay.get(D.lastName)
if lastName and re.fullmatch("\\w+", lastName) is None:
    raise Exception("Invalid lastName")

contactType = relay.get(D.contactType)
if contactType and re.fullmatch("\\w+", contactType) is None:
    raise Exception("Invalid contactType")

organizationName = relay.get(D.organizationName)
if organizationName and re.fullmatch("[\\s\\w]+", organizationName) is None:
    raise Exception("Invalid organizationName")

# addressLine1 = relay.get(D.addressLine1)
# if addressLine1 and re.fullmatch("[\\s\\w\\d]+", addressLine1) is None:
#     raise Exception("Invalid addressLine1")

# addressLine2 = relay.get(D.addressLine2)
# if addressLine2 and re.fullmatch("[\\s\\w\\d]+", addressLine2) is None:
#     raise Exception("Invalid addressLine2")

city = relay.get(D.city)
if city and re.fullmatch("[\\s\\w]+", city) is None:
    raise Exception("Invalid city")

state = relay.get(D.state)
if state and re.fullmatch("\\w+", state) is None:
    raise Exception("Invalid state")

countryCode = relay.get(D.countryCode)
if countryCode and re.fullmatch("\\w+", countryCode) is None:
    raise Exception("Invalid countryCode")

zipCode = relay.get(D.zipCode)
if zipCode and re.fullmatch("\\d{5}", zipCode) is None:
    raise Exception("Invalid zipCode")

phoneNumber = relay.get(D.phoneNumber)
if phoneNumber and re.fullmatch("\\+1\\.\\d{10}", phoneNumber) is None:
    raise Exception("Invalid phoneNumber")

email = relay.get(D.email)
if not email or re.fullmatch("^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}$", email, re.IGNORECASE) is None:
    raise Exception("Invalid email")

fax = relay.get(D.fax)
if fax and re.fullmatch("\\+1\\.\\d{10}", fax) is None:
    raise Exception("Invalid fax")


# print('Domain availability {}'.format(availability))

# relay.outputs.set('availability', availability)