# Generated by Django 4.1.6 on 2023-03-01 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0005_remove_electionlist_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='electionlist',
            name='state',
            field=models.CharField(default='Karnataka', max_length=255),
        ),
    ]