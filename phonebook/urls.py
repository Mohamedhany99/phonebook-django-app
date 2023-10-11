from django.urls import path
from . import views

urlpatterns = [
    path("add_contact/", views.add_contact, name="add_contact"),
    path("contact_list/", views.contact_list, name="contact_list"),
    path(
        "contact_detail/<int:contact_id>/", views.contact_detail, name="contact_detail"
    ),
]
