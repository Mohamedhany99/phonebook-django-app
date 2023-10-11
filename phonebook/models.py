from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)


class PhoneNumber(models.Model):
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name="phone_numbers"
    )
    number = models.CharField(max_length=20)
