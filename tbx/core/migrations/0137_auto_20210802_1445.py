# Generated by Django 2.2.17 on 2021-08-02 13:45

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ("torchbox", "0136_auto_20210728_1356"),
    ]

    operations = [
        migrations.RemoveField(model_name="globalsettings", name="bristol_address",),
        migrations.RemoveField(
            model_name="globalsettings", name="bristol_address_title",
        ),
        migrations.RemoveField(model_name="globalsettings", name="cambridge_address",),
        migrations.RemoveField(
            model_name="globalsettings", name="cambridge_address_title",
        ),
        migrations.RemoveField(model_name="globalsettings", name="contact_person",),
        migrations.RemoveField(
            model_name="globalsettings", name="contact_widget_button_text",
        ),
        migrations.RemoveField(
            model_name="globalsettings", name="contact_widget_call_to_action",
        ),
        migrations.RemoveField(
            model_name="globalsettings", name="contact_widget_intro",
        ),
        migrations.RemoveField(model_name="globalsettings", name="oxford_address",),
        migrations.RemoveField(
            model_name="globalsettings", name="oxford_address_title",
        ),
        migrations.RemoveField(model_name="globalsettings", name="us_address",),
        migrations.RemoveField(model_name="globalsettings", name="us_address_title",),
        migrations.AddField(
            model_name="globalsettings",
            name="addresses",
            field=wagtail.core.fields.StreamField(
                [("address", wagtail.core.blocks.StructBlock([]))], blank=True
            ),
        ),
    ]
