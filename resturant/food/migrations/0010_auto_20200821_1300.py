# Generated by Django 3.1 on 2020-08-21 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_contactdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdetails',
            name='phone',
            field=models.IntegerField(help_text='Enter Phone Number Like +91-##########', max_length=20, verbose_name='Phone number'),
        ),
    ]
