# Generated by Django 2.0.10 on 2019-04-04 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190210_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ValuesToLabels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable', models.IntegerField(default=1)),
                ('automatic', models.IntegerField()),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Label')),
                ('raw_data_source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.RawDataSource')),
            ],
        ),
        migrations.AddField(
            model_name='rawdatasource',
            name='labels',
            field=models.ManyToManyField(related_name='tags', through='core.ValuesToLabels', to='core.Label'),
        ),
        migrations.AddIndex(
            model_name='valuestolabels',
            index=models.Index(fields=['raw_data_source'], name='rds_vtl_idx'),
        ),
        migrations.AddIndex(
            model_name='valuestolabels',
            index=models.Index(fields=['label'], name='label_vtl_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='valuestolabels',
            unique_together={('raw_data_source', 'label')},
        ),
    ]
