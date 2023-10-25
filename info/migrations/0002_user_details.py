# Generated by Django 4.2.6 on 2023-10-24 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="user_details",
            fields=[
                (
                    "username",
                    models.CharField(
                        default="", max_length=100, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(help_text="Enter your name", max_length=100)),
                ("age", models.IntegerField(help_text="Enter your age")),
                (
                    "known_skills",
                    models.ManyToManyField(
                        help_text="Choose your skiils", to="info.skills"
                    ),
                ),
                ("role", models.ManyToManyField(to="info.position")),
            ],
        ),
    ]