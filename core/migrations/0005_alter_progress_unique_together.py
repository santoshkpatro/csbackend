# Generated by Django 4.0.1 on 2022-01-16 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_resource_is_free'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='progress',
            unique_together={('user', 'resource')},
        ),
    ]