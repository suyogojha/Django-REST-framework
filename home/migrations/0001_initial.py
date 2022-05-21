# Generated by Django 4.0.4 on 2022-05-21 07:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('ab5e04db-dcee-445d-b072-20993105da41'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('todo_title', models.CharField(max_length=100)),
                ('todo_description', models.TextField()),
                ('id_done', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
