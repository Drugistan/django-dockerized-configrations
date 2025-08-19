import csv

from django.conf import settings

from django.core.mail import send_mail

from celery import shared_task

import os

@shared_task
def generate_user_credentials(order_id, username, email):
    file_path = os.path.join(settings.MEDIA_ROOT, f"order_credentials_{order_id}.csv")
    with open(file_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["order_id", "username", "email"])
        writer.writerow([order_id, username, email])
    return file_path
