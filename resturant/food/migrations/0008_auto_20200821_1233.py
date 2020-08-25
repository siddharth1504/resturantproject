# Generated by Django 3.1 on 2020-08-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20200821_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='headings',
            name='cafe_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='This is name of the Cafe in Main Page'),
        ),
        migrations.AddField(
            model_name='headings',
            name='cafe_name_subheading',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='This is sub name of the Cafe in Main Page'),
        ),
        migrations.AddField(
            model_name='headings',
            name='contact_heading',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Tag line in Contact Us Page'),
        ),
    ]