# Generated by Django 3.2.6 on 2021-09-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210906_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/name.png', null=True, upload_to=''),
        ),
    ]
