# Generated by Django 5.1.2 on 2024-10-28 17:17

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_post',
            name='author',
            field=models.CharField(default='0', max_length=50, verbose_name=django.contrib.auth.models.User),
        ),
    ]
