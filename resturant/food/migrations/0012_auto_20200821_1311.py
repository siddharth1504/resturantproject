# Generated by Django 3.1 on 2020-08-21 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_auto_20200821_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdetails',
            name='address_main',
            field=models.CharField(help_text='Enter Address: House Name/No., Street Name, Locality', max_length=200, verbose_name='Address Main'),
        ),
        migrations.AlterField(
            model_name='contactdetails',
            name='address_sub',
            field=models.CharField(help_text='Enter Address: Area, City, State, Pincode', max_length=200, verbose_name='Address Sub'),
        ),
        migrations.AlterField(
            model_name='contactdetails',
            name='weekday_opening',
            field=models.CharField(help_text='Enter Weekday (Mon-Thurs) Opening Hours: 10:00 AM - 10:00 PM', max_length=200, verbose_name='Weekday Opening Hours'),
        ),
        migrations.AlterField(
            model_name='contactdetails',
            name='weekend_opening',
            field=models.CharField(help_text='Enter Weekend (Fri-Sun) Opening Hours: 10:00 AM - 10:00 PM', max_length=200, verbose_name='Weekend Opening Hours'),
        ),
        migrations.AlterField(
            model_name='headings',
            name='about_heading',
            field=models.CharField(blank=True, help_text='Enter the Tag line on the Image on About Page', max_length=200, null=True, verbose_name='Tag line in About Page'),
        ),
        migrations.AlterField(
            model_name='headings',
            name='cafe_name',
            field=models.CharField(blank=True, help_text='Enter Cafe Name to be Displayed on Main Page', max_length=200, null=True, verbose_name='This is name of the Cafe in Main Page'),
        ),
        migrations.AlterField(
            model_name='headings',
            name='cafe_name_subheading',
            field=models.CharField(blank=True, help_text='Enter Sub Heading to be displayed just Below Cafe Name: Resturant / Coffee/... (Give Spacing between / )', max_length=200, null=True, verbose_name='This is sub name of the Cafe in Main Page'),
        ),
        migrations.AlterField(
            model_name='headings',
            name='contact_heading',
            field=models.CharField(blank=True, help_text='Enter the Tag line on the Image on Contact US Page', max_length=200, null=True, verbose_name='Tag line in Contact Us Page'),
        ),
        migrations.AlterField(
            model_name='headings',
            name='gallery_heading',
            field=models.CharField(blank=True, help_text='Enter the Tag line on the Image on Gallery Page', max_length=200, null=True, verbose_name='Tag line in Gallery Page'),
        ),
        migrations.AlterField(
            model_name='headings',
            name='menu_heading',
            field=models.CharField(blank=True, help_text='Enter the Tag line on the Image on Menu Page', max_length=200, null=True, verbose_name='Tag line in Menu Page'),
        ),
    ]
