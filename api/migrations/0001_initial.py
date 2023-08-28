# Generated by Django 4.1 on 2023-08-27 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.CharField(max_length=20, unique=True)),
                ('studentEmail', models.EmailField(max_length=254)),
                ('enrollmentDate', models.DateField()),
                ('classYear', models.PositiveIntegerField()),
                ('major', models.CharField(max_length=100)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('semester', models.CharField(max_length=20)),
                ('creditsCompleted', models.PositiveIntegerField()),
                ('creditsInProgress', models.PositiveIntegerField()),
                ('totalCredits', models.PositiveIntegerField()),
                ('graduationDate', models.DateField()),
                ('transcript', models.TextField()),
                ('contactEmail', models.EmailField(max_length=254)),
                ('contactPhone', models.CharField(max_length=20)),
                ('contactAddress', models.TextField()),
                ('guardianRelationship', models.CharField(max_length=50)),
                ('guardianName', models.CharField(max_length=100)),
                ('guardianAddress', models.TextField()),
                ('guardianContactNo', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('isHosteller', models.BooleanField(default=False)),
                ('hostelDetails', models.TextField()),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]