# Generated by Django 4.2.6 on 2023-10-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0009_alter_user_details_age_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_details",
            name="known_skills",
            field=models.ManyToManyField(
                help_text="Choose your skiils", to="info.skills"
            ),
        ),
    ]
