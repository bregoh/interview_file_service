# Generated by Django 4.0.2 on 2022-03-01 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_filesmanagement_file_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useragent',
            name='link_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='useragent', to='api.filelinks'),
        ),
    ]
