# Generated by Django 3.1.4 on 2020-12-17 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20201212_1227'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyuser',
            name='comapny_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='company_link',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.district'),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.division'),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='facebook_link',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='founded_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='full_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='linkdin_link',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='telephone',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='zip_code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
