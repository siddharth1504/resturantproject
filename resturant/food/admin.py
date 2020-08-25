from django.contrib import admin
from .models import Menu, Category, About, Gallery, Headings, ContactDetails, Contact

# Register your models here.


class MenuDetails(admin.ModelAdmin):
    list_filter = ['category']
    list_display = ('dish_name', 'Desc', 'Amount', 'category')


class ContactDetailsDetails(admin.ModelAdmin):
    list_display = ('name', 'email', 'desc')


admin.site.register(Menu, MenuDetails)
admin.site.register(Category)
admin.site.register(About)
admin.site.register(Gallery)
admin.site.register(Headings)
admin.site.register(ContactDetails)
admin.site.register(Contact, ContactDetailsDetails)