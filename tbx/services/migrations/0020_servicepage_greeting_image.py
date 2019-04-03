# Generated by Django 2.1.5 on 2019-02-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0019_subservicepage_parent_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepage',
            name='greeting_image',
            field=models.CharField(blank=True, choices=[('woman-left', 'Woman (Left Aligned)'), ('man-left', 'Man (Left aligned)'), ('wagtail', 'Wagtail (Right aligned)')], default='woman-left', max_length=255, null=True),
        ),
    ]
