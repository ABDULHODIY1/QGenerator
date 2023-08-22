from django.db import models

class QRCode(models.Model):
    content = models.CharField(max_length=200)
