# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+14155551212",
    from_="+15017122661",
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)
