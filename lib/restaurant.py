from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from twilio.rest import Client

load_dotenv()

email_api_key = os.environ['DEV_KEY']
domain = os.environ['DOMAIN']
recipient_email = os.environ['EMAIL']
account_sid = os.environ['SID']
auth_token = os.environ['AUTH_TOKEN']
client = Client(account_sid, auth_token)

class Restaurant():
    def __init__(self):
        self.order = []
        self.menu = []
    
    def add_menu_item(self, food):
        self.menu.append(food)
    
    def display_menu(self):
        menu = ''
        item_count = 1
        for item in self.menu:
            menu += f'{item_count}. {item.name} £{item.price:.2f} '
            item_count += 1
        print(menu)
        return menu
    
    def add_to_order(self, num):
        self.order.append(self.menu[num -1])
    
    def display_order(self):
        order = ''
        item_count = 1

        for item in self.order:
            order += f'{item_count}. {item.name} £{item.price:.2f} '
            item_count += 1
        print(order)
        return order
    
    def complete_order(self):
        receipt = ''
        total = 0
        item_count = 1

        for item in self.order:
            receipt += f'{item_count}. {item.name} £{item.price:.2f} '
            total += item.price
            item_count += 1
        receipt += f'Total: £{total:.2f}'
        print(receipt)
        return receipt
    
    def send_confirmation_email(self, requestor):
        sender_email = f"admin@{domain}"
        time = datetime.now() + timedelta(minutes=20)
        delivery_time = f'{time.hour}:{time.minute}'
        # Make the API request to send an email
        response = requestor.post(
            f"https://api.mailgun.net/v3/{domain}/messages",
            auth=("api", email_api_key),
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
    
    def send_confirmation_text(self, client):
        time = datetime.now() + timedelta(minutes=20)
        delivery_time = f'{time.hour}:{time.minute}'
        message = client.messages.create(
        from_='+447429634908',
        body=f'Thanks for ordering! Your delivery will be with you at {delivery_time}',
        to='+447568144268'
        )

        print(message.sid)
        return message