# Generated by Django 4.0.4 on 2022-05-21 10:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_todo_user_alter_timingtodo_uid_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('183337af-55ef-4a44-8994-cfa6a65ed4ab'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('183337af-55ef-4a44-8994-cfa6a65ed4ab'), editable=False, primary_key=True, serialize=False),
        ),
    ]
