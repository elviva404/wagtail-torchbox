# Generated by Django 2.2.17 on 2021-02-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("work", "0021_update_streamblock_templates"),
    ]

    operations = [
        migrations.AddField(
            model_name="workpage",
            name="date",
            field=models.DateField(null=True, verbose_name="Post date"),
        ),
    ]
