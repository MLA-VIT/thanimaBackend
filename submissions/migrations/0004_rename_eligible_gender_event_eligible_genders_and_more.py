# Generated by Django 4.0.6 on 2022-09-19 18:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0003_alter_event_prize_1_alter_event_prize_2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='eligible_gender',
            new_name='eligible_genders',
        ),
        migrations.AlterField(
            model_name='event',
            name='accepted_formats',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('TIFF', 'TIFF'), ('JPEG', 'JPEG'), ('PNG', 'PNG'), ('JPG', 'JPG')], default=[], max_length=10), size=None),
        ),
    ]
