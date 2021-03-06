# Generated by Django 4.0.1 on 2022-03-18 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_age_profile_age_rename_degree_profile_degree_and_more'),
        ('segmi', '0004_alter_lab_report_doctor_alter_lab_report_lab_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab_report',
            name='doctor',
            field=models.ForeignKey(limit_choices_to={'category': 'Doctor'}, on_delete=django.db.models.deletion.CASCADE, related_name='Doctor', to='users.profile'),
        ),
        migrations.AlterField(
            model_name='lab_report',
            name='patient',
            field=models.ForeignKey(limit_choices_to={'category': 'Patient'}, on_delete=django.db.models.deletion.CASCADE, related_name='Patient', to='users.profile'),
        ),
    ]
