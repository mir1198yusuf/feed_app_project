# Generated by Django 2.2.11 on 2020-05-29 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20200529_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]