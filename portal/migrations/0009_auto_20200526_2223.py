# Generated by Django 3.0.5 on 2020-05-26 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20200526_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 26, 22, 23, 16, 379249)),
        ),
    ]
