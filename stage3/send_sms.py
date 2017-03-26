from twilio.rest import TwilioRestClient

account_sid = "AC063c058e6534fc5f165614c341ee1fa4" # Your Account SID from www.twilio.com/console
auth_token  = "bad196ae19e4e75069ffc5c2168aa251"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+19173927998",    # Replace with your phone number
    from_="+13475805926") # Replace with your Twilio number

print(message.sid)
