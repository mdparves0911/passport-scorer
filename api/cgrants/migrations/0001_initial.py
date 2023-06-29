# Generated by Django 4.2.2 on 2023-06-29 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contribution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "data",
                    models.JSONField(
                        default=dict,
                        help_text="Original contribution data in JSON format",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Grant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "hidden",
                    models.BooleanField(
                        db_index=True,
                        default=False,
                        help_text="Hide the grant from the /grants page?",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        db_index=True,
                        default=True,
                        help_text="Whether or not the Grant is active.",
                    ),
                ),
                (
                    "is_clr_eligible",
                    models.BooleanField(
                        default=True, help_text="Is grant eligible for CLR"
                    ),
                ),
                (
                    "data",
                    models.JSONField(
                        default=dict, help_text="Original grant data in JSON format"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GrantCLR",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("main", "Main Round"),
                            ("ecosystem", "Ecosystem Round"),
                            ("cause", "Cause Round"),
                        ],
                        default="main",
                        help_text="Grant CLR Type",
                        max_length=25,
                    ),
                ),
                (
                    "data",
                    models.JSONField(
                        default=dict,
                        help_text="Original contribution data in JSON format",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "handle",
                    models.CharField(db_index=True, max_length=255, unique=True),
                ),
                (
                    "data",
                    models.JSONField(
                        default=dict, help_text="Original profile data in JSON format"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "data",
                    models.JSONField(
                        default=dict,
                        help_text="Original subscription data in JSON format",
                    ),
                ),
                (
                    "contributor_profile",
                    models.ForeignKey(
                        help_text="The Subscription contributor's Profile.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="grant_contributor",
                        to="cgrants.profile",
                    ),
                ),
                (
                    "grant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cgrants.grant"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SquelchProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(default=True, help_text="Is squelch applied?"),
                ),
                (
                    "data",
                    models.JSONField(
                        default=dict,
                        help_text="Original contribution data in JSON format",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="squelches",
                        to="cgrants.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GrantContributionIndex",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "round_num",
                    models.IntegerField(
                        blank=True,
                        help_text="The round number a user contributed to",
                        null=True,
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        db_index=True,
                        decimal_places=18,
                        default=0,
                        help_text="The amount contributed",
                        max_digits=64,
                    ),
                ),
                (
                    "contribution",
                    models.ForeignKey(
                        blank=True,
                        help_text="Contribution",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cgrants.contribution",
                    ),
                ),
                (
                    "grant",
                    models.ForeignKey(
                        help_text="The grant a user contributed to",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cgrants.grant",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        help_text="Contributor",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cgrants.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GrantCLRCalculation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        db_index=True, default=False, help_text="Is this calc active?"
                    ),
                ),
                (
                    "latest",
                    models.BooleanField(
                        db_index=True,
                        default=False,
                        help_text="Is this calc the latest?",
                    ),
                ),
                (
                    "data",
                    models.JSONField(
                        default=dict,
                        help_text="Original contribution data in JSON format",
                    ),
                ),
                (
                    "grant",
                    models.ForeignKey(
                        help_text="The grant",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="clr_calculations",
                        to="cgrants.grant",
                    ),
                ),
                (
                    "grantclr",
                    models.ForeignKey(
                        help_text="The grant CLR Round",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="clr_calculations",
                        to="cgrants.grantclr",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="grant",
            name="admin_profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cgrants.profile"
            ),
        ),
        migrations.AddField(
            model_name="contribution",
            name="subscription",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cgrants.subscription"
            ),
        ),
    ]
