# Generated by Django 3.0.5 on 2020-05-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20200518_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
