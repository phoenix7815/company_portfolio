# Generated by Django 4.2.6 on 2023-10-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0004_user_details_email_user_details_phone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_details",
            name="phone",
            field=models.BigIntegerField(null=True),
        ),
    ]