# Generated by Django 4.2.6 on 2023-11-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0021_alter_vacant_position_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vacant_position",
            name="id",
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]