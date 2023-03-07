# Generated by Django 4.1.6 on 2023-03-07 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0006_electionlist_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electionlist',
            name='type',
        ),
        migrations.AddField(
            model_name='electionlist',
            name='electionid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='election_id', to='homeapp.electiontype'),
        ),
        migrations.AlterField(
            model_name='electiontype',
            name='type',
            field=models.CharField(choices=[('Loksabha', 'Loksabha'), ('Assembly', 'Assembly'), ('Panchayat', 'Panchayat')], max_length=255),
        ),
    ]
