# Generated by Django 4.0.2 on 2022-02-27 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_filelinks_link_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesmanagement',
            name='file_visit',
            field=models.IntegerField(null=True),
        ),
    ]
