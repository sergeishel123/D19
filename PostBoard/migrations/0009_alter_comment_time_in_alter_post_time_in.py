# Generated by Django 4.1.4 on 2023-01-05 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostBoard', '0008_alter_comment_time_in_alter_post_time_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 5, 7, 21, 33, 927746)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 5, 7, 21, 33, 927746)),
        ),
    ]
