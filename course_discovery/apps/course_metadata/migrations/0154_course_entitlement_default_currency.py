# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-06 21:09


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0153_auto_20190206_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseentitlement',
            name='currency',
            field=models.ForeignKey(default='USD', on_delete=django.db.models.deletion.CASCADE, to='core.Currency'),
        ),
    ]
