# Generated by Django 4.0.6 on 2022-09-23 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_alter_user_reg_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.CharField(max_length=14, null=True, unique=True),
        ),
    ]