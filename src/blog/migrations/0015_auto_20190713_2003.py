# Generated by Django 2.2 on 2019-07-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
