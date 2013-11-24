from django.db import models

class FileData(models.Model):
    """
    This Model contains all fields required on the file upload
    """
    purchaser_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.FloatField()
    purchase_count = models.IntegerField()
    merchant_address = models.CharField(max_length=200)
    merchant_name = models.CharField(max_length=200)