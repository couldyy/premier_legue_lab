# Generated by Django 4.1.2 on 2024-12-04 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_delete_pushdatarequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='likes',
        ),
    ]