# Generated by Django 4.0.2 on 2022-02-28 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_filelinks_link_visit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filelinks',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 28, 9, 58, 54, 664058)),
        ),
        migrations.AlterField(
            model_name='filesmanagement',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 28, 9, 58, 54, 663908)),
        ),
    ]
