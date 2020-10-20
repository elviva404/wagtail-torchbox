# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-20 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [("wagtailcore", "0040_page_draft_title")]

    operations = [
        migrations.CreateModel(
            name="NavigationSettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "primary_navigation",
                    wagtail.core.fields.StreamField(
                        (
                            (
                                "link",
                                wagtail.core.blocks.StructBlock(
                                    (
                                        (
                                            "page",
                                            wagtail.core.blocks.PageChooserBlock(),
                                        ),
                                        (
                                            "title",
                                            wagtail.core.blocks.CharBlock(
                                                help_text="Leave blank to use the page's own title",
                                                required=False,
                                            ),
                                        ),
                                    )
                                ),
                            ),
                        ),
                        blank=True,
                        help_text="Main site navigation",
                    ),
                ),
                (
                    "secondary_navigation",
                    wagtail.core.fields.StreamField(
                        (
                            (
                                "link",
                                wagtail.core.blocks.StructBlock(
                                    (
                                        (
                                            "page",
                                            wagtail.core.blocks.PageChooserBlock(),
                                        ),
                                        (
                                            "title",
                                            wagtail.core.blocks.CharBlock(
                                                help_text="Leave blank to use the page's own title",
                                                required=False,
                                            ),
                                        ),
                                    )
                                ),
                            ),
                        ),
                        blank=True,
                        help_text="Alternative navigation",
                    ),
                ),
                (
                    "footer_navigation",
                    wagtail.core.fields.StreamField(
                        (
                            (
                                "column",
                                wagtail.core.blocks.StructBlock(
                                    (
                                        (
                                            "heading",
                                            wagtail.core.blocks.CharBlock(
                                                required=False,
                                                help_text="Leave blank if no header required.",
                                            ),
                                        ),
                                        (
                                            "links",
                                            wagtail.core.blocks.ListBlock(
                                                wagtail.core.blocks.StructBlock(
                                                    (
                                                        (
                                                            "page",
                                                            wagtail.core.blocks.PageChooserBlock(),
                                                        ),
                                                        (
                                                            "title",
                                                            wagtail.core.blocks.CharBlock(
                                                                help_text="Leave blank to use the page's own title",
                                                                required=False,
                                                            ),
                                                        ),
                                                    )
                                                )
                                            ),
                                        ),
                                    )
                                ),
                            ),
                        ),
                        blank=True,
                        help_text="Multiple columns of footer links with optional header.",
                    ),
                ),
                (
                    "footer_links",
                    wagtail.core.fields.StreamField(
                        (
                            (
                                "link",
                                wagtail.core.blocks.StructBlock(
                                    (
                                        (
                                            "page",
                                            wagtail.core.blocks.PageChooserBlock(),
                                        ),
                                        (
                                            "title",
                                            wagtail.core.blocks.CharBlock(
                                                help_text="Leave blank to use the page's own title",
                                                required=False,
                                            ),
                                        ),
                                    )
                                ),
                            ),
                        ),
                        blank=True,
                        help_text="Single list of elements at the base of the page.",
                    ),
                ),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.Site",
                    ),
                ),
            ],
            options={"abstract": False},
        )
    ]
