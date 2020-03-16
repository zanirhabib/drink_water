from twilio.rest import Client
from config import *

# Your Account SID from twilio.com/console
account_sid = sid
# Your Auth Token from twilio.com/console
auth_token  = token

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=to_number, 
    from_=from_number,
    body="Zanir texted you from his phone")

print(message.sid)
