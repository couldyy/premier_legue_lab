# Generated by Django 4.1.2 on 2024-12-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comments_comm_to_repl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
