# Generated by Django 4.1.7 on 2023-03-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0010_accountapikey_rate_limit_alter_accountapikey_account"),
    ]

    operations = [
        migrations.AlterField(
            model_name="community",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
