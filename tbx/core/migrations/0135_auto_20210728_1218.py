# Generated by Django 2.2.17 on 2021-07-28 11:18

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0134_remove_googleadgrantspage_and_related_models'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globalsettings',
            name='bristol_address_link',
        ),
        migrations.RemoveField(
            model_name='globalsettings',
            name='bristol_address_svg',
        ),
        migrations.RemoveField(
            model_name='globalsettings',
            name='cambridge_address_link',
        ),
        migrations.RemoveField(
            model_name='globalsettings',
            name='cambridge_address_svg',
        ),
        migrations.RemoveField(
            model_name='globalsettings',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='globalsettings',
            name='contact_telephone',
        ),
        migrations.RemoveField(
            model_name='globalsettings',
            name='contact_twitter',
        ),
        migrations.RemoveField(
            model_name='globalsettings',
            name='email_newsletter_teaser',
        ),
        migrations.RemoveField(
            model_name='globalsettings',
            name='oxford_address_link',
        ),
        migrations.RemoveField(
            model_name='globalsettings',
            name='oxford_address_svg',
        ),
        migrations.RemoveField(
            model_name='globalsettings',
            name='us_address_link',
        ),
        migrations.RemoveField(
            model_name='globalsettings',
            name='us_address_svg',
        ),
        migrations.AlterField(
            model_name='globalsettings',
            name='bristol_address',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Full address'),
        ),
        migrations.AlterField(
            model_name='globalsettings',
            name='bristol_address_title',
            field=models.CharField(blank=True, help_text='Full address', max_length=255),
        ),
        migrations.AlterField(
            model_name='globalsettings',
            name='oxford_address',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Full address'),
        ),
        migrations.AlterField(
            model_name='globalsettings',
            name='oxford_address_title',
            field=models.CharField(blank=True, help_text='Full address', max_length=255),
        ),
        migrations.AlterField(
            model_name='globalsettings',
            name='us_address',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Full address'),
        ),
        migrations.AlterField(
            model_name='globalsettings',
            name='us_address_title',
            field=models.CharField(blank=True, help_text='Full address', max_length=255),
        ),
    ]
