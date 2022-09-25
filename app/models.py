from django.db import models

# Create your models here.
class Details(models.Model):
    Firstname = models.CharField(max_length=26)
    Lastname = models.CharField(max_length=26)
    Emails = models.EmailField(max_length=30)
    Contacts = models.BigIntegerField()