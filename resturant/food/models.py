from django.db import models
import uuid
from django.utils import timezone
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50, help_text='Enter the Category Name to be Displayed')

    def __str__(self):
        return self.category_name


class Menu(models.Model):
    dish_name = models.CharField(max_length=200, verbose_name='Name of Dish',
                                 help_text='Enter the Dish Name to be Displayed')
    Desc = models.TextField(verbose_name='Dish Description',
                            help_text='Enter the Description of the Dish Name')
    Amount = models.CharField(null=False, max_length=10, blank=False, verbose_name='Amount of Dish')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Dish Date Posted',
                                       help_text='Leave as it is')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1,
                                 help_text='Please select the Category in which Dish needs to be Shown')

    def __str__(self):
        return self.dish_name


class About(models.Model):
    heading_main = models.CharField(max_length=200, verbose_name='Main Heading',
                                    help_text='Enter the Main Heading to be displayed ')
    main_desc = models.TextField(verbose_name='Main Description',
                                 help_text='Enter the Main Description or the content')
    sub_heading = models.CharField(max_length=200, verbose_name='Sub Heading',
                                   help_text='Enter the Sub Heading if any and is Mandatory')
    sub_desc = models.TextField(verbose_name='Sub Description',
                                help_text='Enter the Sub Description if any and is Mandatory')
    img = models.ImageField(default='default.jpg', upload_to='blog',
                            help_text='Select the Image and is Mandatory')


class Gallery(models.Model):
    img = models.ImageField(default='default.jpg', upload_to='Gallery',
                            help_text='Select the Image to be Displayed')
    dishname = models.CharField(max_length=200, verbose_name='Dish Name for every picture',
                                help_text='Enter the Dish Name to be Displayed on Image')

    def __str__(self):
        return self.dishname


class Headings(models.Model):
    about_heading = models.CharField(null=True, blank=True, max_length=200, verbose_name='Tag line in About Page',
                                     help_text='Enter the Tag line on the Image on About Page')
    menu_heading = models.CharField(null=True, blank=True, max_length=200, verbose_name='Tag line in Menu Page',
                                    help_text='Enter the Tag line on the Image on Menu Page')
    gallery_heading = models.CharField(null=True, blank=True, max_length=200, verbose_name='Tag line in Gallery Page',
                                       help_text='Enter the Tag line on the Image on Gallery Page')
    contact_heading = models.CharField(null=True, blank=True, max_length=200,
                                       verbose_name='Tag line in Contact Us Page',
                                       help_text='Enter the Tag line on the Image on Contact US Page')
    cafe_name = models.CharField(null=True, blank=True, max_length=200,
                                 verbose_name='This is name of the Cafe in Main Page',
                                 help_text='Enter Cafe Name to be Displayed on Main Page')
    cafe_name_subheading = models.CharField(null=True, blank=True, max_length=200,
                                            verbose_name='This is sub name of the Cafe in Main Page',
                                            help_text='Enter Sub Heading to be displayed just Below Cafe Name: Resturant / Coffee/... (Give Spacing between / )')


class ContactDetails(models.Model):
    address_main = models.CharField(max_length=200, verbose_name='Address Main',
                                    help_text='Enter Address: House Name/No., Street Name, Locality')
    address_sub = models.CharField(max_length=200, verbose_name='Address Sub',
                                   help_text='Enter Address: Area, City, State, Pincode')
    weekday_opening = models.CharField(max_length=200, verbose_name='Weekday Opening Hours',
                                       help_text='Enter Weekday (Mon-Thurs) Opening Hours: 10:00 AM - 10:00 PM')
    weekend_opening = models.CharField(max_length=200, verbose_name='Weekend Opening Hours',
                                       help_text='Enter Weekend (Fri-Sun) Opening Hours: 10:00 AM - 10:00 PM')
    phone = models.CharField(max_length=15, verbose_name='Phone number',
                             help_text='Enter Phone Number Like +91-##########')
    email = models.CharField(max_length=200, verbose_name='Email')


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.name
