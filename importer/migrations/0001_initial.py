# Generated by Django 2.0.1 on 2018-03-09 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawDataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=255)),
                ('movement_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('date_value', models.DateField(null=True)),
                ('details', models.TextField(null=True)),
                ('value', models.FloatField()),
            ],
            options={
                'ordering': ('-date', '-date_value'),
            },
        ),
        migrations.CreateModel(
            name='StatusReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('file_name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('o', 'Ok'), ('w', 'Warnings'), ('e', 'Error')], max_length=1)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StatusReportRow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=255)),
                ('movement_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('date_value', models.DateField(null=True)),
                ('details', models.TextField(null=True)),
                ('value', models.FloatField()),
                ('message', models.TextField()),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='importer.StatusReport')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='rawdatasource',
            index=models.Index(fields=['kind', 'movement_name', 'date', 'value'], name='importer_ra_kind_7ecd55_idx'),
        ),
    ]
