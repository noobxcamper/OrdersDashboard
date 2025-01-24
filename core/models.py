from django.db import models
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    status = models.CharField(max_length=10, default="open")
    responder = models.CharField(max_length=100, default='')
    submission_id = models.CharField(max_length=100, default='')
    submission_date = models.DateField(default=timezone.now().date())
    department = models.CharField(max_length=50, default='')
    items = models.CharField(max_length=50, default='')
    price = models.FloatField(default=0.0)
    variation = models.CharField(max_length=200, default='No variation provided')
    notes = models.CharField(max_length=200, default='No notes provided')
    quantity = models.IntegerField(default=0)
    ship_to = models.CharField(max_length=100, default='')
    shipping_address = models.CharField(max_length=100, blank=True, default='No shipping address provided')
    hyperlink = models.CharField(max_length=500, default='')
    tracking_url = models.CharField(max_length=500, default='No tracking url provided')
    private_notes = models.CharField(max_length=5000, default='')