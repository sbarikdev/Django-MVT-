# Generated by Django 4.0.6 on 2022-07-16 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
