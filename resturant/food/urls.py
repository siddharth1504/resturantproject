
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('menu', views.menu, name='menu'),
    path('gallery', views.gallery, name='gallery'),
    path('contact-us', views.contact_us, name='contact-us'),
    path('about', views.about, name='about'),
    path('checkout', views.checkout, name='checkout'),
    path('billing-information', views.billingInfo, name='billing-info'),
]
