# Generated by Django 2.2 on 2020-01-04 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
    ]
