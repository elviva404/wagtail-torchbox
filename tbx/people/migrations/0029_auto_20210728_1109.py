# Generated by Django 2.2.17 on 2021-07-28 10:09

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0028_auto_20210604_1234"),
    ]

    operations = [
        migrations.AlterField(
            model_name="culturepage",
            name="instagram_posts",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "post",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "link",
                                    wagtail.core.blocks.URLBlock(
                                        help_text="Link to a specific post here or leave blank for it to link to https://www.instagram.com/torchboxltd/",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
