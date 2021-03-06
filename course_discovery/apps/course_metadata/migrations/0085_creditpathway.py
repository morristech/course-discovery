# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-06 14:21


import django_extensions.db.fields
import sortedm2m.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0084_auto_20180522_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditPathway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('org_name', models.CharField(max_length=255, verbose_name='Organization name')),
                ('email', models.EmailField(max_length=254)),
                ('programs', sortedm2m.fields.SortedManyToManyField(help_text=None, to='course_metadata.Program')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
                'ordering': ('-modified', '-created'),
            },
        ),
    ]
