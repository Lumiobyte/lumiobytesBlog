# Generated by Django 2.2 on 2019-07-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_blogpost_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]