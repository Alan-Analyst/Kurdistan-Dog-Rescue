# Generated by Django 4.2.1 on 2023-06-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt_app', '0002_alter_dog_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='picture',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='dog_pictures/'),
        ),
    ]
