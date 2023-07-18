# Generated by Django 4.2.1 on 2023-07-17 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Batch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recid', models.CharField(blank=True, max_length=10, null=True)),
                ('deductionCode', models.CharField(blank=True, max_length=100, null=True)),
                ('reference', models.CharField(blank=True, max_length=100, null=True)),
                ('idNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('ecNumber', models.CharField(blank=True, max_length=9, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('startDate', models.CharField(blank=True, max_length=100, null=True)),
                ('endDate', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('bankAccount', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.CharField(blank=True, max_length=100, null=True)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='responses', to='Batch.batch')),
            ],
        ),
    ]