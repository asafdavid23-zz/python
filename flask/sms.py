from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC286ffbaf5068a338cc399fb457de49b0'
auth_token = '22d31dd47dda3a52aef00cf367dadc7f'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hi there!',
    from_='+972504205408',
    to='+972525119694'
)

print(message.sid)