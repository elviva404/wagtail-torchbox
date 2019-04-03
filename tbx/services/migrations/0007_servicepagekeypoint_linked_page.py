# Generated by Django 2.1.5 on 2019-02-05 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('services', '0006_new_servicepage_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepagekeypoint',
            name='linked_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]
