# Generated by Django 4.1.2 on 2024-12-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comments_like_count_remove_comments_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Last Name'),
        ),
    ]
