# Generated by Django 2.1.5 on 2019-02-11 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0020_servicepage_greeting_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicepage',
            old_name='greeting_image',
            new_name='greeting_image_type',
        ),
    ]
