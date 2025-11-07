# Generated manually to sync with existing database schema

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0002_job_additional_information_job_benefits_and_culture_and_more'),
    ]

    operations = [
        # These fields already exist in the database, so we're just telling Django about them
        migrations.AddField(
            model_name='job',
            name='application_deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='contact_email',
            field=models.EmailField(blank=True, default='hr@neeraali.com', max_length=254),
        ),
        migrations.AddField(
            model_name='job',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='remote_work_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='salary_range',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]