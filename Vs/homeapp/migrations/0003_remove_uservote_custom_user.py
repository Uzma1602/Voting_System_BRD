# Generated by Django 4.1.6 on 2023-03-01 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_alter_electionlist_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uservote',
            name='custom_user',
        ),
    ]
