# Generated by Django 4.0.6 on 2022-08-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pictures/profilepic.jpg', upload_to='profile_pictures'),
        ),
    ]
