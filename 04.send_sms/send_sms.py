from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC4da8a8a44345d127d88c9efeefe4b2d1"
auth_token  = "7280a3754b4429f025e2e141c6cae5d9"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Yes!",
    to="+5511989757122",    # Replace with your phone number
    from_="++551132303803") # Replace with your Twilio number
print message.sid
