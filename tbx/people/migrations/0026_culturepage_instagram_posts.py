# Generated by Django 2.2.17 on 2021-05-21 21:22

from django.db import migrations
import tbx.people.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0025_auto_20210505_1057"),
    ]

    operations = [
        migrations.AddField(
            model_name="culturepage",
            name="instagram_posts",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "posts",
                        wagtail.core.blocks.StreamBlock(
                            [("post", tbx.people.blocks.InstagramEmbedBlock())],
                            icon="fa-instagram",
                            max_num=8,
                            min_num=8,
                            required=False,
                            template="patterns/molecules/instagram-gallery/instagram-gallery.html",
                        ),
                    )
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
