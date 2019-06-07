import os
from twilio.rest import client
# import twilio
# import Client

account_sid = "AC26fe88618e0be12f63a17ed7c411bcc8"
auth_token = "52e414309956ce85112969bc34ebbf0a"

C = client.TwilioRestClient(account_sid,auth_token)
#c = cli(account_sid,auth_token)

call = C.calls.create(
    to = "+917503169933",
    from_="+13612453684",
    url="http://demo.twilio.com/docs/voice.xml"
    )

print(call.sid)
