# Generated by Django 4.0.4 on 2022-05-21 08:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('b28c3261-cc1d-4360-9a7d-a08d182aa440'), editable=False, primary_key=True, serialize=False),
        ),
    ]
