# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-08 14:32


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0066_auto_20171107_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='key',
            field=models.CharField(help_text='Only ascii characters allowed (a-zA-Z0-9)', max_length=255),
        ),
    ]
