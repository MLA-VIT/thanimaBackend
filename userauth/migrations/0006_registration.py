# Generated by Django 4.0.6 on 2022-09-24 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0005_alter_user_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=128)),
                ('reg_no', models.CharField(max_length=10)),
                ('email', models.TextField()),
                ('mobile_no', models.CharField(max_length=15)),
                ('payment_done', models.BooleanField(default=True)),
            ],
        ),
    ]
