# Generated by Django 2.2 on 2019-07-08 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190704_1939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-add_timestamp', '-edited_date']},
        ),
    ]
