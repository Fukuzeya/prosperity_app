# Generated by Django 4.2.1 on 2023-07-17 18:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Batch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_id', models.CharField(blank=True, max_length=20, null=True)),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(choices=[('CANCELED', 'CANCELED'), ('DRAFT', 'DRAFT'), ('FAILED', 'FAILED'), ('PROCESSED', 'PROCESSED'), ('PROCESSING', 'PROCESSING'), ('SUCCESS', 'SUCCESS'), ('SENT', 'SENT'), ('SAVED', 'SAVED')], default='DRAFT', max_length=15)),
                ('request_type', models.CharField(choices=[('NEW', 'NEW'), ('CHANGE', 'CHANGE'), ('DELETE', 'DELETE')], default='NEW', max_length=20)),
                ('ec_number', models.CharField(max_length=8)),
                ('id_number', models.CharField(max_length=11)),
                ('transaction_refence', models.CharField(max_length=20)),
                ('deductions_start_date', models.DateField()),
                ('record_source', models.CharField(default='Bulk Upload', max_length=20)),
                ('deductions_end_date', models.DateField()),
                ('installment_amount', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch_records', to='Batch.batch')),
                ('deduction_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='deduction_code_records', to='Batch.deductioncode')),
            ],
            options={
                'ordering': ['-date_created'],
                'indexes': [models.Index(fields=['-date_created'], name='Record_reco_date_cr_7f03f8_idx')],
            },
        ),
    ]
