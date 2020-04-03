from subscribers import models


def add_subscriber(recipient_id, page_id):
    models.Subscriber.objects.update_or_create(recipient_id=recipient_id, page_id=page_id)
