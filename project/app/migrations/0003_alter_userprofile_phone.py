# Generated by Django 5.2.3 on 2025-06-18 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_userprofile_email_alter_userprofile_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.BigIntegerField(verbose_name='phone'),
        ),
    ]
