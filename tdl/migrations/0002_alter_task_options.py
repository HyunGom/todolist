# Generated by Django 4.1.5 on 2023-02-02 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tdl", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["complete", "-created"]},
        ),
    ]
