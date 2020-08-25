# Generated by Django 3.1 on 2020-08-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_heading',
            field=models.CharField(max_length=200, null=True, verbose_name='Tag line in Image'),
        ),
        migrations.AddField(
            model_name='about',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='blog'),
        ),
    ]
