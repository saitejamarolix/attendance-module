# Generated by Django 4.2.2 on 2023-06-07 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("attApp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="shift",
        ),
        migrations.DeleteModel(
            name="Shift",
        ),
    ]
