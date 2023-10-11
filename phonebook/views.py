from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Contact, PhoneNumber


def home(request):
    return render(request, "index.html")


# Create your views here.
def add_contact(request):
    if request.method == "POST":
        try:
            name = request.POST["name"]
            phone_numbers = request.POST.getlist("phone_numbers")
            print(phone_numbers)
            contact = Contact.objects.get(name=name)
            for number in phone_numbers:
                phone_number = PhoneNumber.objects.create(
                    contact=contact, number=number
                )
        except Contact.DoesNotExist:
            contact = Contact.objects.create(name=name)
            for number in phone_numbers:
                phone_number = PhoneNumber.objects.create(
                    contact=contact, number=number
                )
    return render(request, "add_contact.html")


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contact_list.html", {"contacts": contacts})


def contact_detail(request, contact_id):
    ph_number = get_list_or_404(PhoneNumber, contact=contact_id)
    return render(request, "contact_detail.html", {"phone_number": ph_number})
