# Generated by Django 2.2 on 2019-07-12 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_blogpost_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='image',
        ),
    ]
