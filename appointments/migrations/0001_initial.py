# Generated by Django 5.1.4 on 2024-12-28 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('dentist_name', models.CharField(max_length=100)),
                ('reason_for_visit', models.TextField()),
            ],
        ),
    ]
