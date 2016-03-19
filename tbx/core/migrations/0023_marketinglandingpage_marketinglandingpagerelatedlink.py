# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-19 08:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0022_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketingLandingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', models.TextField(blank=True)),
                ('hero_video_id', models.IntegerField(blank=True, help_text='Optional. The numeric ID of a Vimeo video to replace the background image.', null=True)),
                ('hero_video_poster_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='torchbox.TorchboxImage')),
            ],
            options={
                'verbose_name': 'MarketingLandingPage',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MarketingLandingPageRelatedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(blank=True, verbose_name='External link')),
                ('title', models.CharField(help_text='Link title', max_length=255)),
                ('link_document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_links', to='torchbox.MarketingLandingPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
