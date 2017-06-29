# Sending an SMS using the Twilio API
from twilio.rest import Client
import json

import urllib3
urllib3.disable_warnings()

with open("twilio_auth.json", "r") as data_file:
  data = json.load(data_file)

# Find your Account Sid and Token at twilio.com/console
ACCOUNT_SID = data["sid"]
AUTH_TOKEN = data["token"]

# Create a client to talk to the Twilio REST API
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Send the message
client.messages.create(
  to=data["to"],
  from_=data["from"],
  body="Tomorrow's forecast in Financial District, San Francisco is Clear.",
)
