# Generated by Django 2.2.1 on 2019-05-07 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('uploaded_date', models.DateTimeField()),
                ('files', models.FileField(upload_to='uploaded_files/')),
            ],
        ),
    ]
