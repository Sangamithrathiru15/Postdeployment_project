# Generated by Django 2.1.7 on 2019-05-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pilot', '0003_auto_20190509_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedata',
            name='RHEL_version',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='filedata',
            name='store_name',
            field=models.CharField(max_length=50),
        ),
    ]