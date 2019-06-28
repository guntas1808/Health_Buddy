# Generated by Django 2.2.2 on 2019-06-23 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seven', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodyvital',
            name='bloodPressure',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='bodyvital',
            name='height',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='bodyvital',
            name='prescription',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Doctor.Prescription'),
        ),
        migrations.AlterField(
            model_name='bodyvital',
            name='sugarLevel',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='bodyvital',
            name='weight',
            field=models.IntegerField(blank=True),
        ),
    ]
