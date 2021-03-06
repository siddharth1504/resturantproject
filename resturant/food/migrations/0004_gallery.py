# Generated by Django 3.1 on 2020-08-20 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20200820_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_heading', models.CharField(max_length=200, null=True, verbose_name='Tag line in Image')),
                ('img', models.ImageField(default='default.jpg', upload_to='Gallery')),
                ('dishname', models.CharField(max_length=200, verbose_name='Dish Name for every picture')),
            ],
        ),
    ]
