# Generated by Django 5.0.4 on 2024-05-20 10:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("userAPI", "0004_uploadedimage_result"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="uploadedimage",
            name="result",
        ),
    ]
