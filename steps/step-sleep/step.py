#!/usr/bin/env python
import time

from nebula_sdk import Interface, Dynamic as D

relay = Interface()

session_token = None
try:
  session_token = relay.get(D.aws.connection.sessionToken)
except:
  pass

sleepTime = relay.get(D.sleepTime)

time.sleep(sleepTime)