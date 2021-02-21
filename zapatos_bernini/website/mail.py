from django.core.mail import send_mail
from app.settings import DEFAULT_FROM_EMAIL
import json


def send_order(to_email, data):
    json_data = json.dumps(data, indent=2, default=str)
    send_mail(
        subject='Pedidos',
        message=json_data,
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=[to_email],
    )
