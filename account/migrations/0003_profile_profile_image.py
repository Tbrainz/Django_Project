# Generated by Django 4.1.6 on 2023-03-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_lga_of_origin_profile_scheme_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='', upload_to='profile_pics'),
        ),
    ]
