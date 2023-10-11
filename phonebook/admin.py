from django.contrib import admin
from phonebook.models import Contact, PhoneNumber

# Register your models here.
admin.site.register(Contact)
admin.site.register(PhoneNumber)
