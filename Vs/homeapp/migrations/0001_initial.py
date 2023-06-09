# Generated by Django 4.1.6 on 2023-03-09 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('can_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('des', models.TextField()),
                ('logo', models.ImageField(upload_to='candidate_logos/')),
            ],
        ),
        migrations.CreateModel(
            name='ElectionList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('state', models.CharField(default='Karnataka', max_length=255)),
                ('end_date', models.DateField()),
                ('district', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('candidate', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_id', to='homeapp.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='ElectionType',
            fields=[
                ('ele_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('Loksabha', 'Loksabha'), ('Assembly', 'Assembly'), ('Panchayat', 'Panchayat')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.candidate')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.electionlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='electionlist',
            name='election_type_fk',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='homeapp.electiontype'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='election_type_fk',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='homeapp.electiontype'),
        ),
    ]
