# Generated by Django 4.0.2 on 2022-02-28 10:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_filelinks_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filelinks',
            name='created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='filesmanagement',
            name='created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
