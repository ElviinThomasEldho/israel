# Generated by Django 4.1.7 on 2023-02-28 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_service_link_testimony_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='link',
        ),
        migrations.RemoveField(
            model_name='testimony',
            name='link',
        ),
    ]