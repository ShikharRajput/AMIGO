import os
from twilio.rest import client
# import twilio
# import Client

account_sid = "AC26fe88618e0be12f63a17ed7c411bcc8"
auth_token = "52e414309956ce85112969bc34ebbf0a"

Client = client.TwilioClient(account_sid,auth_token)
#c = cli(account_sid,auth_token)

call = Client.calls.create(
    to = "+918527249366",
    from_="+13612453684",
    url="http://demo.twilio.com/docs/voice.xml"
    )

print(call.sid)
