# Generated by Django 4.0.7 on 2023-05-04 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_profile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
