from django.db import models

class Shipment(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_phone = models.CharField(max_length=20)
    sender_address = models.TextField()
    receiver_name = models.CharField(max_length=100)
    receiver_phone = models.CharField(max_length=20)
    receiver_address = models.TextField()
    package_size = models.CharField(max_length=20, choices=[
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ])
    tracking_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.tracking_id
