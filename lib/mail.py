from dotenv import load_dotenv
import requests
import os
from datetime import datetime, timedelta
load_dotenv()

api_key = os.environ['DEV_KEY']
domain = os.environ['DOMAIN']
recipient_email = os.environ['EMAIL']

def send_simple_message():
    # Construct the sender email from the domain (Modify 'admin' as needed if you have a specific sender id set up in Mailgun)
    sender_email = f"admin@{domain}"
    time = datetime.now() + timedelta(minutes=20)
    delivery_time = f'{time.hour}:{time.minute}'
    # Make the API request to send an email
    response = requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={
            "from": sender_email,
            "to": recipient_email,
            "subject": "Delivery Confirmation",
            "text": f"Thanks for ordering! Your delivery will be with you at {delivery_time}"
        }
    )

    # Print response information to diagnose issues or confirm success
    if response.ok:
        print("Email successfully sent!")
    else:
        print("Failed to send email.")
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
    return response
	

send_simple_message()
print(f"https://api.mailgun.net/v3/{domain}/messages")