

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
            name='Patient',
            fields=[
                ('bloodGroup', models.CharField(blank=True, max_length=10)),
                ('allergies', models.CharField(default='none', max_length=500)),
                ('significantMedicalHistory', models.CharField(default='none', max_length=5000)),
                ('phoneNo', models.CharField(max_length=50)),
                ('emergencyContactName', models.CharField(max_length=50)),
                ('emergencyContactNo', models.CharField(max_length=50)),
                ('emergencyContactRelation', models.CharField(max_length=20)),
                ('rollNo', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('is_dependent', models.BooleanField(default=True)),
                ('dependentUser', models.CharField(blank=True, max_length=25)),
                ('dependentRelation', models.CharField(blank=True, max_length=50)),
                ('designation', models.CharField(blank=True, max_length=50)),
                ('department', models.CharField(blank=True, max_length=50)),
                ('ccUsername', models.CharField(blank=True, max_length=20)),
                ('program', models.CharField(blank=True, max_length=30)),
                ('hall', models.CharField(blank=True, max_length=50)),
                ('room', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('hometown', models.CharField(blank=True, max_length=30)),
                ('per_addr', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField(blank=True)),
                ('height', models.CharField(blank=True, max_length=20)),
                ('weight', models.CharField(blank=True, max_length=20)),
                ('is_student', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatmentFor', models.CharField(max_length=150)),
                ('remarks', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, upload_to='')),
                ('file_url', models.CharField(blank=True, max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.Patient')),
            ],
        ),
    ]
