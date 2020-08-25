from django.shortcuts import render, redirect
from .models import Menu, Category, About, Gallery, Headings, ContactDetails, Contact
from django.contrib import messages
from django.shortcuts import render

# Create your views here.


def home(request):
    displaynew = ContactDetails.objects.all()
    displays = Headings.objects.all()
    return render(request, 'food/home.html', {'displays': displays, 'displaynew': displaynew})


def menu(request):
    displaynew = ContactDetails.objects.all()
    displays = Headings.objects.all()
    products = Menu.objects.all()
    categories = Category.objects.all()

    data = {
        'categories': {
            category: Menu.objects.filter(category=category) for category in categories
        },
        'products': products,
        'displays': displays,
        'displaynew': displaynew
    }
    template = 'food/menu.html'
    return render(request, template, data)


def gallery(request):
    displaynew = ContactDetails.objects.all()
    displays = Headings.objects.all()
    display = Gallery.objects.all()

    return render(request, 'food/gallery.html', {'display': display, 'displays': displays, 'displaynew': displaynew})


def contact_us(request):
    displaynew = ContactDetails.objects.all()
    displays = Headings.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
        messages.success(request, f'Thanks for Submitting  your Feedback')
        return redirect('contact-us')
    else:

        return render(request, 'food/contact-us.html', {'displays': displays, 'displaynew': displaynew})


def about(request):
    displaynew = ContactDetails.objects.all()
    displays = Headings.objects.all()
    description = About.objects.all()
    return render(request, 'food/about.html', {'description': description, 'displays': displays, 'displaynew': displaynew})
