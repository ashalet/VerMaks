# Generated by Django 4.1.2 on 2022-10-30 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='image',
            field=models.ImageField(upload_to='images_works/'),
        ),
    ]
