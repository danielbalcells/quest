# Generated by Django 2.1.2 on 2018-10-25 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_basic-questionlink-model'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='questionlink',
            unique_together={('source', 'target')},
        ),
    ]
