# Generated by Django 2.1.5 on 2019-02-13 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_culturepage_culturepagelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='personpage',
            name='short_intro',
            field=models.TextField(blank=True, null=True),
        ),
    ]
