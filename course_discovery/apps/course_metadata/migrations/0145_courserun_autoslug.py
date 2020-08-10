# Generated by Django 1.11.15 on 2019-01-03 19:56


from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0144_person_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courserun',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, default='', editable=False, max_length=255, populate_from='title'),
            preserve_default=False,
        ),
    ]
