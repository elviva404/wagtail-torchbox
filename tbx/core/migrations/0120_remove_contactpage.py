# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-22 15:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('torchbox', '0119_auto_20190123_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='landing_image',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='landing_page_button_link',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='main_image',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='contactformfield',
            name='page',
        ),
        migrations.RemoveField(
            model_name='contactlandingpagerelatedlinkbutton',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='contactlandingpagerelatedlinkbutton',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='contactlandingpagerelatedlinkbutton',
            name='page',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='ContactFormField',
        ),
        migrations.DeleteModel(
            name='ContactLandingPageRelatedLinkButton',
        ),
    ]
